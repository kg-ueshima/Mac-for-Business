import imaplib
import email
from email.header import decode_header
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG (email_client.py): Loading env from {env_path}")

# Gmail IMAP設定
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")
IMAP_PORT = int(os.getenv("IMAP_PORT", 993))
EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")  # .env.local に EMAIL_ACCOUNT を設定
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # .env.local に EMAIL_PASSWORD を設定
LABEL_NAME = os.getenv("LABEL_NAME", "ueshima@keiyukai-group.com")  # .env.local に LABEL_NAME を設定（なければデフォルト）


def decode_mime_words(s):
    if not s:
        return ""
    decoded_fragments = decode_header(s)
    return ''.join([
        fragment.decode(encoding or 'utf-8') if isinstance(fragment, bytes) else fragment
        for fragment, encoding in decoded_fragments
    ])

def get_yesterday_sent_emails(target_date=None):
    messages = []
    # ターゲット日付の設定
    if target_date:
        # 文字列の場合はdatetimeに変換
        if isinstance(target_date, str):
            target_date = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()
    else:
        target_date = datetime.date.today() - datetime.timedelta(days=1)
    try:
        # IMAPサーバへ接続
        imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        # Noneチェック（型安全のため）
        if EMAIL_ACCOUNT is None or EMAIL_PASSWORD is None:
            print("EMAIL_ACCOUNT または EMAIL_PASSWORD が設定されていません")
            return messages
        imap.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        print("IMAP接続成功")

        # ラベル"ueshima@keiyukai-group.com"のメールボックスを選択
        # GmailのIMAPラベルは "ラベル名" でアクセスできる
        # 例: imap.select('"ラベル名"')
        # ラベル名に日本語や記号が含まれる場合はエンコードが必要な場合もある
        label_name = 'ueshima@keiyukai-group.com'
        status, _ = imap.select(f'"{label_name}"')
        if status != "OK":
            print(f'ラベル"{label_name}"の選択に失敗しました')
            imap.logout()
            return messages

        # ターゲット日付で検索
        since = target_date.strftime("%d-%b-%Y")
        before = (target_date + datetime.timedelta(days=1)).strftime("%d-%b-%Y")
        # 送信済みメールから、ターゲット日付のメールを検索
        status, data = imap.search(None, f'SINCE {since}', f'BEFORE {before}')
        if status != "OK":
            print("メール検索失敗")
            imap.logout()
            return messages

        mail_ids = data[0].split()
        print(f"ラベル「{label_name}」の{target_date}のメール件数: {len(mail_ids)}")

        # 最新100件だけ取得（必要に応じて調整）
        fetch_count = min(100, len(mail_ids))
        for i in mail_ids[-fetch_count:]:
            try:
                status, msg_data = imap.fetch(i, "(RFC822)")
                if status != "OK":
                    print(f"{i}番目のメール取得失敗")
                    continue
                # msg_dataはリストで、各要素はタプル (b'RFC822', bytes) 形式
                # msg_data[0][1] がメール本体
                if not msg_data or not isinstance(msg_data[0], tuple) or len(msg_data[0]) < 2:
                    print(f"{i}番目のメールデータ形式不正")
                    continue
                msg = email.message_from_bytes(msg_data[0][1])
            except Exception as e:
                print(f"{i}番目のメール取得失敗: {e}")
                continue

            # 日付判定
            date_str = msg.get("Date", "")
            try:
                from email.utils import parsedate_to_datetime
                msg_date = parsedate_to_datetime(date_str)
                msg_date_local = msg_date.date()
            except Exception:
                msg_date_local = None

            # ターゲット日付のみ
            if msg_date_local != target_date:
                continue  # ターゲット日付以外はスキップ

            # fromアドレスが ueshima@keiyukai-group.com のみ抽出
            from_addr = decode_mime_words(msg.get("From", ""))
            if "ueshima@keiyukai-group.com" not in from_addr:
                continue  # 自分が送信したもの以外はスキップ

            subject = decode_mime_words(msg.get("Subject", "（件名なし）"))
            to = decode_mime_words(msg.get("To", "不明"))
            date = date_str if date_str else "不明"

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and part.get('Content-Disposition') is None:
                        charset = part.get_content_charset() or 'utf-8'
                        payload = part.get_payload(decode=True)
                        if isinstance(payload, bytes):
                            body = payload.decode(charset, errors="replace").strip()
                        elif isinstance(payload, str):
                            body = payload.strip()
                        else:
                            body = ""
                        break
            else:
                charset = msg.get_content_charset() or 'utf-8'
                payload = msg.get_payload(decode=True)
                if isinstance(payload, bytes):
                    body = payload.decode(charset, errors="replace").strip()
                elif isinstance(payload, str):
                    body = payload.strip()
                else:
                    body = ""

            messages.append(f"■ 件名: {subject}\n  宛先: {to}\n  日付: {date}\n  本文:\n{body}\n")

        imap.logout()
    except Exception as e:
        print("エラー:", e)

    return messages
