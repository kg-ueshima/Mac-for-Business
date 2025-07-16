import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pytz

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)

SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRET_FILE = Path(__file__).parent.parent.parent / 'schedule_updater' / 'client_id.json'
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")

if not CALENDAR_ID:
    raise ValueError("GOOGLE_CALENDAR_IDが環境変数に設定されていません")

def get_calendar_service():
    creds = None
    token_path = Path(__file__).parent / 'token_calendar.json'
    if os.path.exists(token_path):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

def get_events_on_date(date: Optional[datetime] = None):
    """
    指定日（datetime型, JST, デフォルトは昨日）の全予定をリストで返す
    """
    if date is None:
        JST = pytz.timezone('Asia/Tokyo')
        now_jst = datetime.now(JST)
        date = now_jst - timedelta(days=1)
    JST = pytz.timezone('Asia/Tokyo')
    start_dt = datetime(date.year, date.month, date.day, tzinfo=JST)
    end_dt = start_dt + timedelta(days=1)
    service = get_calendar_service()
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_dt.isoformat(),
        timeMax=end_dt.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    # 予定の要点だけ抽出
    event_list = []
    for ev in events:
        summary = ev.get('summary', '')
        start = ev.get('start', {}).get('dateTime', ev.get('start', {}).get('date', ''))
        end = ev.get('end', {}).get('dateTime', ev.get('end', {}).get('date', ''))
        description = ev.get('description', '')
        event_list.append(f"{summary}（{start}〜{end}）{(' ' + description) if description else ''}")
    return event_list 