import os
import datetime
import requests
from pathlib import Path
from dotenv import load_dotenv
from msal import PublicClientApplication, SerializableTokenCache
import msal
import mimetypes
import pytz
from dateutil import parser

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG (onedrive.py): Loading env from {env_path}")

# ▼ Azureアプリ登録時の情報（環境変数から取得）
CLIENT_ID = os.getenv("ONEDRIVE_CLIENT_ID")
TENANT_ID = os.getenv("MICROSOFT_TENANT_ID")

# 環境変数のチェック
if not CLIENT_ID or not TENANT_ID:
    print("エラー: 環境変数が設定されていません")
    print("env.localファイルにMICROSOFT_CLIENT_IDとMICROSOFT_TENANT_IDを設定してください")
    exit(1)

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = [
    'Files.Read.All',
    'Sites.Read.All',
    'User.Read'
]

# ▼ トークンキャッシュ設定（ファイルに保存）
TOKEN_CACHE_FILE = "token_cache_onedrive.bin"
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

def get_access_token():
    # グローバルなcacheを使う
    global cache
    app = msal.PublicClientApplication(
        client_id=CLIENT_ID,
        authority=AUTHORITY,
        token_cache=cache
    )
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    else:
        result = None
    if not result or 'access_token' not in result:
        # ここで初回のみインタラクティブ認証
        flow = app.initiate_device_flow(scopes=SCOPES)
        if "user_code" not in flow:
            print("デバイスコード認証に失敗しました:", flow)
            return None
        print(flow["message"])
        result = app.acquire_token_by_device_flow(flow)
        # 認証成功時はキャッシュを保存
        with open(TOKEN_CACHE_FILE, "w") as f:
            f.write(cache.serialize())
    return result["access_token"] if result and "access_token" in result else None

DELTA_LINK_FILE = "onedrive_delta_link.txt"

def load_delta_link():
    if os.path.exists(DELTA_LINK_FILE):
        with open(DELTA_LINK_FILE, "r") as f:
            return f.read().strip()
    return None

def save_delta_link(link):
    with open(DELTA_LINK_FILE, "w") as f:
        f.write(link)

def get_yesterday_created_files(target_date=None):
    """
    OneDriveの昨日作成・編集・移動・保存などの操作履歴を取得し、
    ファイル名・操作時間・ファイル拡張子などを返す（JST基準で昨日を判定）
    2回目以降はdeltaLinkを使って差分のみ取得し高速化
    """
    access_token = get_access_token()
    if not access_token:
        return []

    headers = {"Authorization": f"Bearer {access_token}"}
    # 指定日がある場合はキャッシュを使用しない
    if target_date:
        url = "https://graph.microsoft.com/v1.0/me/drive/root/delta"
    else:
        delta_link = load_delta_link()
        url = delta_link if delta_link else "https://graph.microsoft.com/v1.0/me/drive/root/delta"
    files = []
    JST = pytz.timezone('Asia/Tokyo')
    if target_date:
        # 文字列の場合はdatetimeに変換
        if isinstance(target_date, str):
            target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()
        target_jst = target_date
    else:
        now_jst = datetime.datetime.now(JST)
        target_jst = (now_jst - datetime.timedelta(days=1)).date()

    exclude_folders = [
        'Mac for Business-backup',
        'S_画面収録',
        'Scanner'
    ]

    while url:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("OneDrive APIエラー:", res.text)
            break
        data = res.json()
        for item in data.get("value", []):
            # ファイルのみ対象
            if "file" not in item:
                continue
            # 除外フォルダ配下のファイルはスキップ
            parent_path = item.get('parentReference', {}).get('path', '')
            if any(f"/{folder}" in parent_path for folder in exclude_folders):
                continue
            # 操作日時（最終更新日時・作成日時・移動日時など）
            created = item.get("createdDateTime", "")
            modified = item.get("lastModifiedDateTime", "")
            # UTC→JST変換
            def utc_to_jst_date(dtstr):
                if not dtstr:
                    return None
                dt_utc = parser.isoparse(dtstr)
                dt_jst = dt_utc.astimezone(JST)
                return dt_jst.date()
            created_jst = utc_to_jst_date(created)
            modified_jst = utc_to_jst_date(modified)
            # JST基準で昨日作成・編集・移動・保存されたもののみ
            if created_jst == target_jst or modified_jst == target_jst:
                files.append({
                    "name": item.get("name", ""),
                    "operation_time": modified or created,
                    "extension": item.get("file", {}).get("mimeType", ""),
                    "id": item.get("id", ""),
                    "webUrl": item.get("webUrl", ""),
                })
        # deltaLinkの保存（指定日がない場合のみ）
        if "@odata.deltaLink" in data and not target_date:
            save_delta_link(data["@odata.deltaLink"])
        url = data.get("@odata.nextLink", None)

    return files

def get_file_content(file_id):
    """
    OneDriveのファイルIDからファイルの内容（テキスト）を取得する
    """
    access_token = get_access_token()
    if not access_token:
        return None
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://graph.microsoft.com/v1.0/me/drive/items/{file_id}/content"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            # テキストとしてデコード（バイナリの場合はdecodeエラーになる可能性あり）
            return res.text
        else:
            print(f"ファイル内容取得失敗: {res.status_code} {res.text}")
            return None
    except Exception as e:
        print(f"ファイル内容取得時に例外: {e}")
        return None

def get_file_content_and_type(file_id, file_name):
    """
    ファイルIDとファイル名から内容とMIMEタイプを返す。
    動画ファイルの場合はNone, Noneを返す。
    """
    mime, _ = mimetypes.guess_type(file_name)
    if mime is None:
        mime = "application/octet-stream"
    # 動画ファイルは除外
    if mime.startswith("video/"):
        return None, None
    access_token = get_access_token()
    if not access_token:
        return None, None
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://graph.microsoft.com/v1.0/me/drive/items/{file_id}/content"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            if mime.startswith("text/"):
                return res.text, mime
            else:
                return res.content, mime  # 画像・音声はバイナリで返す
        else:
            print(f"ファイル内容取得失敗: {res.status_code} {res.text}")
            return None, None
    except Exception as e:
        print(f"ファイル内容取得時に例外: {e}")
        return None, None