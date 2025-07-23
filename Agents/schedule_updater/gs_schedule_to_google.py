import csv
import os
from pathlib import Path
from datetime import datetime, timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv
from dateutil.parser import parse
import glob

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)

# GoogleカレンダーAPIの認証情報
SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRET_FILE = Path(__file__).parent / 'client_id.json'  # ダウンロードしたOAuthクライアントIDファイル
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")  # 環境変数からカレンダーIDを取得

if not CALENDAR_ID:
    print("エラー: GOOGLE_CALENDAR_IDが環境変数に設定されていません")
    exit(1)

def get_calendar_service():
    creds = None
    token_path = 'token.json'
    # 既存のトークンがあれば再利用
    if os.path.exists(token_path):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # なければ認証フローを開始
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # トークン保存
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

def parse_datetime(dt_str):
    for fmt in ("%Y-%m-%d %H:%M", "%Y/%m/%d %H:%M"):
        try:
            return datetime.strptime(dt_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"日付フォーマット不明: {dt_str}")

def parse_csv_schedule(csv_path):
    import re
    events = []
    tried_encodings = ['shift_jis', 'cp932', 'utf-8-sig', 'utf-8', 'mbcs']
    last_exception = None
    for enc in tried_encodings:
        try:
            with open(csv_path, encoding=enc) as f:
                reader = csv.DictReader(f)
                print(f"CSVヘッダー({enc}):", reader.fieldnames)
                def get_value(row, key):
                    return row.get(key) or row.get('\ufeff' + key) or row.get(key.strip())
                for row in reader:
                    subject = get_value(row, 'タイトル') or ''
                    description = get_value(row, '内容') or ''
                    start_date = get_value(row, '開始日付')
                    start_time = get_value(row, '開始時刻')
                    end_date = get_value(row, '終了日付')
                    end_time = get_value(row, '終了時刻')

                    # 日付・時刻の組み立て
                    if not (start_date and start_time and end_date and end_time):
                        print("スキップ: 日付または時刻が見つかりません", row)
                        continue
                    start = f"{start_date} {start_time}"
                    end = f"{end_date} {end_time}"

                    # All Day Event判定
                    allday_keywords = ['公休', '有給', '休日']
                    all_day_event = not any(kw in subject for kw in allday_keywords)

                    # Googleカレンダー用イベント形式
                    event = {
                        'summary': subject,
                        'description': description,
                        'start': {
                            'dateTime': parse_datetime(start).isoformat(),
                            'timeZone': 'Asia/Tokyo',
                        },
                        'end': {
                            'dateTime': parse_datetime(end).isoformat(),
                            'timeZone': 'Asia/Tokyo',
                        },
                        'allDay': all_day_event,
                        'reminders': {'useDefault': True},  # Reminder On
                    }
                    events.append(event)
            print(f"{enc}のCSVファイルをGoogleカレンダー形式で変換しました: {len(events)}件の予定")
            return events
        except Exception as e:
            print(f"CSVファイル({enc})処理エラー: {e}")
            last_exception = e
            continue
    print(f"CSVファイル処理エラー: 全てのエンコーディングで失敗しました")
    if last_exception is not None:
        raise last_exception
    else:
        raise Exception("CSVファイルの読み込みに失敗しました（エンコーディング不明）")

def ensure_timezone(dt_str):
    # すでにタイムゾーンが付いていなければ+09:00を付与
    if dt_str and ('+' not in dt_str and 'Z' not in dt_str):
        return dt_str + '+09:00'
    return dt_str

def find_existing_event(service, calendar_id, event, is_kari):
    """
    指定したタイトル・開始・終了時刻・（仮）有無でイベントを検索
    """
    time_min = ensure_timezone(event['start']['dateTime'])
    time_max = ensure_timezone(event['end']['dateTime'])
    query = event['summary'].strip()
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    for item in events_result.get('items', []):
        item_summary = item['summary'].strip()
        # （仮）の有無を厳密に一致させる
        if (item_summary == query and
            item['start'].get('dateTime') == event['start']['dateTime'] and
            item['end'].get('dateTime') == event['end']['dateTime']):
            if (('（仮）' in item_summary) == is_kari):
                return item
    return None

def delete_kari_events(service, calendar_id, event):
    time_min = ensure_timezone(event['start']['dateTime'])
    time_max = ensure_timezone(event['end']['dateTime'])
    query = event['summary'].replace('(仮)', '').strip()
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    for item in events_result.get('items', []):
        if ('(仮)' in item['summary'] and
            item['summary'].replace('(仮)', '').strip() == query and
            item['start'].get('dateTime') == event['start']['dateTime']):
            service.events().delete(calendarId=calendar_id, eventId=item['id']).execute()
            print(f"（仮）予定を削除: {item['summary']}")

def get_events_on_date(service, calendar_id, date_str):
    """
    指定日（YYYY-MM-DD）の全イベントを取得
    """
    from datetime import datetime, timedelta
    import pytz
    jst = pytz.timezone('Asia/Tokyo')
    start_dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=jst)
    end_dt = start_dt + timedelta(days=1)
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=start_dt.isoformat(),
        timeMax=end_dt.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    return events_result.get('items', [])

def normalize_datetime(dt_str):
    # どちらも「YYYY-MM-DDTHH:MM:SS」に揃える
    dt = parse(dt_str)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")

def is_duplicate_event(service, calendar_id, event):
    """
    同じタイトル・開始・終了時刻のイベントがその日に存在するか判定し、比較内容をログ出力
    """
    date_str = event['start']['dateTime'][:10]
    events = get_events_on_date(service, calendar_id, date_str)
    for item in events:
        # print(f"[比較] 既存: title={item['summary'].strip()} start={item['start'].get('dateTime')} end={item['end'].get('dateTime')}")
        # print(f"[比較] 新規: title={event['summary'].strip()} start={event['start']['dateTime']} end={event['end']['dateTime']}")
        if (item['summary'].strip() == event['summary'].strip() and
            normalize_datetime(item['start'].get('dateTime')) == normalize_datetime(event['start']['dateTime']) and
            normalize_datetime(item['end'].get('dateTime')) == normalize_datetime(event['end']['dateTime'])):
            # print("→ 完全一致：重複と判定")
            return True
    return False

def insert_events_to_google_calendar(events):
    service = get_calendar_service()
    for event in events:
        is_kari = '（仮）' in event['summary']
        if not is_kari:
            delete_kari_events(service, CALENDAR_ID, event)
        if is_duplicate_event(service, CALENDAR_ID, event):
            # print(f"重複予定をスキップ: {event['summary']}")
            continue
        service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f"新規登録: {event['summary']}")

def get_latest_schedule_csv(download_dir):
    files = glob.glob(os.path.join(download_dir, "scheduleList*.csv"))
    if not files:
        raise FileNotFoundError("scheduleList-*.csv が見つかりません")
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

if __name__ == "__main__":
    # ダウンロードフォルダのパス
    download_dir = os.path.expanduser("~/Downloads")
    csv_path = get_latest_schedule_csv(download_dir)
    print(f"最新のスケジュールCSV: {csv_path}")
    events = parse_csv_schedule(csv_path)
    insert_events_to_google_calendar(events)
