import os
import datetime
import requests
from pathlib import Path
from dotenv import load_dotenv
from msal import PublicClientApplication, SerializableTokenCache
from dateutil import parser
import pytz

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG (teams.py): Loading env from {env_path}")

# ▼ Azureアプリ登録時の情報（環境変数から取得）
CLIENT_ID = os.getenv('MICROSOFT_CLIENT_ID')
TENANT_ID = os.getenv('MICROSOFT_TENANT_ID')

# 環境変数のチェック
if not CLIENT_ID or not TENANT_ID:
    print("エラー: 環境変数が設定されていません")
    print("env.localファイルにMICROSOFT_CLIENT_IDとMICROSOFT_TENANT_IDを設定してください")
    exit(1)

AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPES = [
    'Channel.ReadBasic.All',
    'ChannelMessage.Read.All',
    'Chat.Read',
    'User.Read',
    'User.ReadBasic.All'
]

# ▼ トークンキャッシュ設定（ファイルに保存）
TOKEN_CACHE_FILE = "token_cache.bin"
cache = SerializableTokenCache()
if os.path.exists(TOKEN_CACHE_FILE):
    with open(TOKEN_CACHE_FILE, "r") as f:
        cache.deserialize(f.read())

app = PublicClientApplication(
    client_id=CLIENT_ID,
    authority=AUTHORITY,
    token_cache=cache
)

accounts = app.get_accounts()
result = None

if accounts:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])

if not result:
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        print("デバイスコード認証に失敗しました:", flow)
        exit(1)
    print(flow["message"])  # 認証コードとURLを表示
    result = app.acquire_token_by_device_flow(flow)

if "access_token" not in result:
    print("トークン取得失敗:", result)
    exit(1)

# ▼ 成功時、キャッシュを保存
with open(TOKEN_CACHE_FILE, "w") as f:
    f.write(cache.serialize())

access_token = result["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}

# ▼ 本日分のチャットメッセージを取得する関数
def get_yesterday_messages(target_date=None):
    JST = pytz.timezone('Asia/Tokyo')
    if target_date:
        # 文字列の場合はdatetimeに変換
        if isinstance(target_date, str):
            target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()
        target_jst = target_date
    else:
        now_jst = datetime.datetime.now(JST)
        target_jst = (now_jst - datetime.timedelta(days=1)).date()
    url = 'https://graph.microsoft.com/v1.0/me/chats'
    res = requests.get(url, headers=headers)
    chats = res.json().get('value', [])

    messages = []
    for chat in chats:
        chat_id = chat['id']
        msg_url = f'https://graph.microsoft.com/v1.0/me/chats/{chat_id}/messages'
        msg_res = requests.get(msg_url, headers=headers).json()

        for msg in msg_res.get("value", []):
            created_utc = msg.get('createdDateTime', '')
            if not created_utc:
                continue
            try:
                dt_utc = parser.isoparse(created_utc)
                dt_jst = dt_utc.astimezone(JST)
                created_jst_date = dt_jst.date()
            except Exception:
                continue
            if created_jst_date == target_jst:
                # senderの安全な取得
                sender = '不明'
                from_info = msg.get('from')
                if from_info and isinstance(from_info, dict):
                    user_info = from_info.get('user')
                    if user_info and isinstance(user_info, dict):
                        sender = user_info.get('displayName', '不明')
                content = msg.get('body', {}).get('content', '').strip()
                messages.append(f"[{sender}] {content}")
    return messages

def get_yesterday_channel_messages(target_date=None):
    """
    自分が所属する全チームの全チャンネルの投稿（会話）から、昨日(JST)分のみを抽出して返す
    """
    JST = pytz.timezone('Asia/Tokyo')
    if target_date:
        # 文字列の場合はdatetimeに変換
        if isinstance(target_date, str):
            target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()
        target_jst = target_date
    else:
        now_jst = datetime.datetime.now(JST)
        target_jst = (now_jst - datetime.timedelta(days=1)).date()
    messages = []
    # 1. 所属チーム一覧取得
    teams_url = 'https://graph.microsoft.com/v1.0/me/joinedTeams'
    teams_res = requests.get(teams_url, headers=headers)
    if teams_res.status_code != 200:
        print('チーム一覧取得失敗:', teams_res.text)
        return messages
    teams_data = teams_res.json().get('value', [])
    for team in teams_data:
        team_id = team.get('id')
        team_name = team.get('displayName', '不明なチーム')
        # 2. チャンネル一覧取得
        channels_url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels'
        channels_res = requests.get(channels_url, headers=headers)
        if channels_res.status_code != 200:
            print(f'チャンネル一覧取得失敗({team_name}):', channels_res.text)
            continue
        channels_data = channels_res.json().get('value', [])
        for channel in channels_data:
            channel_id = channel.get('id')
            channel_name = channel.get('displayName', '不明なチャンネル')
            # 3. チャンネル投稿（会話）取得
            posts_url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages'
            posts_res = requests.get(posts_url, headers=headers)
            if posts_res.status_code != 200:
                print(f'チャンネル投稿取得失敗({team_name}/{channel_name}):', posts_res.text)
                continue
            posts_data = posts_res.json().get('value', [])
            for post in posts_data:
                created_utc = post.get('createdDateTime', '')
                if not created_utc:
                    continue
                try:
                    dt_utc = parser.isoparse(created_utc)
                    dt_jst = dt_utc.astimezone(JST)
                    created_jst_date = dt_jst.date()
                except Exception:
                    continue
                if created_jst_date == target_jst:
                    # senderの安全な取得
                    sender = '不明'
                    from_info = post.get('from')
                    if from_info and isinstance(from_info, dict):
                        user_info = from_info.get('user')
                        if user_info and isinstance(user_info, dict):
                            sender = user_info.get('displayName', '不明')
                    content = post.get('body', {}).get('content', '').strip()
                    messages.append(f"[{team_name}/{channel_name}][{sender}] {content}")
    return messages