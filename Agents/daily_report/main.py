import datetime
import sys
from modules import teams,chatwork,email_client,onedrive,gemini,calendar_client
from pathlib import Path
import datetime

# コマンドライン引数から日付を取得
if len(sys.argv) > 1:
    # 引数がある場合は指定日を使用
    try:
        target_date = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d').date()
    except ValueError:
        print("エラー: 日付は YYYY-MM-DD 形式で指定してください")
        sys.exit(1)
else:
    # 引数がない場合は昨日を使用
    target_date = datetime.date.today() - datetime.timedelta(days=1)

print(f"処理開始：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

report_lines = []

# 1. Teams チャット/投稿取得
teams_logs = teams.get_yesterday_messages(target_date)
report_lines.append("【Teamsチャット投稿】\n" + "\n".join(teams_logs))

# チームのチャンネル投稿も取得
channel_logs = teams.get_yesterday_channel_messages(target_date)
report_lines.append("【Teamsチャンネル投稿】\n" + "\n".join(channel_logs))

# 2. Chatwork メッセージ取得
# chatwork_logs = chatwork.get_yesterday_messages(target_date)
# report_lines.append("【Chatwork】\n" + "\n".join(chatwork_logs))

# 3. 送信メール取得
sent_mails = email_client.get_yesterday_sent_emails(target_date)
report_lines.append("【送信メール】\n" + "\n".join(sent_mails))

# 4. OneDriveファイル取得
new_files = onedrive.get_yesterday_created_files(target_date)
report_lines.append("【OneDrive新規ファイル】\n")
for f in new_files:
    report_lines.append(f"- {f['name']}")
    # content = onedrive.get_file_content(f['id'])
    # if content:
    #     report_lines.append(gemini.summarize(content))
    # else:
    #     report_lines.append("（ファイル内容の取得に失敗）")

# 4. Googleカレンダー予定取得
# calendar_clientはdatetime型を期待しているので変換
target_datetime = datetime.datetime.combine(target_date, datetime.datetime.min.time())
calendar_events = calendar_client.get_events_on_date(target_datetime)
if calendar_events:
    for event in calendar_events:
        summary = gemini.summarize(event)
        report_lines.append(f"【Googleカレンダー予定】要約\n{summary}\n\n\n{event}")
else:
    report_lines.append("【Googleカレンダー予定】本日の予定はありません")

# 5. 日報保存
output_path = Path("80-業務日報") / f"{target_date}_その日のやり取り.txt"
output_path.parent.mkdir(parents=True, exist_ok=True)

# 要約結果をまとめて保存（追記モードで書き込む）
with output_path.open("w", encoding="utf-8") as f:
    f.write("【Teamsチャット投稿 - 要約 -】\n" + gemini.summarize(teams_logs) + "\n")
    f.write("【Teamsチャンネル投稿 - 要約 -】\n" + gemini.summarize(channel_logs) + "\n")
    f.write("【送信メール - 要約 -】\n" + gemini.summarize(sent_mails) + "\n")
    f.write("【OneDrive新規ファイル - 要約 -】\n" + gemini.summarize(new_files) + "\n")
    f.write("【Googleカレンダー予定 - 要約 -】\n" + gemini.summarize(calendar_events) + "\n")
    f.write("\n\n\n".join(report_lines))

print(f"やり取りを保存しました：{output_path}")

# やり取りファイルを読み込んで日報を生成
with output_path.open("r", encoding="utf-8") as f:
    all_text = f.read()

daily_report = gemini.generate_daily_report(all_text)

# 日報の保存先をやり取りファイルと同じフォルダにする
daily_report_path = output_path.parent / f"{target_date}_日報.txt"
with daily_report_path.open("w", encoding="utf-8") as f:
    f.write(daily_report)

print(f"処理終了：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"日報を保存しました：{daily_report_path}")