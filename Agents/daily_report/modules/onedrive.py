import os
import datetime
import requests
from pathlib import Path
from dotenv import load_dotenv

# .env.local から環境変数を読み込む
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID")
TENANT_ID = os.getenv("MICROSOFT_TENANT_ID")
SECRET_ID = os.getenv("MICROSOFT_SECRET_ID")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]

import msal

def get_access_token():
    app = msal.ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=SECRET_ID,
        authority=AUTHORITY
    )
    result = app.acquire_token_silent(SCOPES, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=SCOPES)
    if "access_token" not in result:
        print("OneDrive用トークン取得失敗:", result)
        return None
    return result["access_token"]

def get_yesterday_created_files():
    """
    OneDriveの昨日作成・編集・移動・保存などの操作履歴を取得し、
    ファイル名・操作時間・ファイル拡張子などを返す
    """
    access_token = get_access_token()
    if not access_token:
        return []

    headers = {"Authorization": f"Bearer {access_token}"}
    # OneDriveのroot配下の全ファイル・フォルダを取得
    url = "https://graph.microsoft.com/v1.0/me/drive/root/delta"
    files = []
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    next_link = url

    # delta APIで全履歴を取得（ページング対応）
    while next_link:
        res = requests.get(next_link, headers=headers)
        if res.status_code != 200:
            print("OneDrive APIエラー:", res.text)
            break
        data = res.json()
        for item in data.get("value", []):
            # ファイルのみ対象
            if "file" not in item:
                continue
            # 操作日時（最終更新日時・作成日時・移動日時など）
            created = item.get("createdDateTime", "")
            modified = item.get("lastModifiedDateTime", "")
            # ISO8601→date
            created_date = created[:10] if created else ""
            modified_date = modified[:10] if modified else ""
            # 昨日作成・編集・移動・保存されたもののみ
            if created_date == yesterday.isoformat() or modified_date == yesterday.isoformat():
                files.append({
                    "name": item.get("name", ""),
                    "operation_time": modified or created,
                    "extension": item.get("file", {}).get("mimeType", ""),
                    "id": item.get("id", ""),
                    "webUrl": item.get("webUrl", ""),
                })
        # 次ページがあれば
        next_link = data.get("@odata.nextLink", None)

    return files