import requests
import datetime
import os
from msal import PublicClientApplication, SerializableTokenCache

# ▼ Azureアプリ登録時の情報（必要に応じて書き換えてください）
CLIENT_ID = 'a9741f3f-0d88-415a-bf33-fcfae84d8d7e'
TENANT_ID = '5483b7b9-ff5a-4b52-9169-f8884e38833a'
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
def get_yesterday_messages():
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    url = 'https://graph.microsoft.com/v1.0/me/chats'
    res = requests.get(url, headers=headers)
    chats = res.json().get('value', [])

    messages = []
    for chat in chats:
        chat_id = chat['id']
        msg_url = f'https://graph.microsoft.com/v1.0/me/chats/{chat_id}/messages'
        msg_res = requests.get(msg_url, headers=headers).json()

        for msg in msg_res.get("value", []):
            created = msg.get('createdDateTime', '')[:10]
            if created == yesterday:
                sender = msg.get('from', {}).get('user', {}).get('displayName', '不明')
                content = msg.get('body', {}).get('content', '').strip()
                messages.append(f"[{sender}] {content}")

    return messages