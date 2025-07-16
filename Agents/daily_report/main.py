import datetime
from modules import teams,chatwork,email_client,onedrive,gemini,calendar_client
from pathlib import Path


yesterday = datetime.date.today()- datetime.timedelta(days=1)
report_lines = []

# 1. Teams チャット/投稿取得
teams_logs = teams.get_yesterday_messages()
report_lines.append("【Teamsチャット投稿】\n" + "\n".join(teams_logs))

# チームのチャンネル投稿も取得
channel_logs = teams.get_yesterday_channel_messages()
report_lines.append("【Teamsチャンネル投稿】\n" + "\n".join(channel_logs))

# 2. Chatwork メッセージ取得
# chatwork_logs = chatwork.get_yesterday_messages()
# report_lines.append("【Chatwork】\n" + "\n".join(chatwork_logs))

# 3. 送信メール取得
sent_mails = email_client.get_yesterday_sent_emails()
report_lines.append("【送信メール】\n" + "\n".join(sent_mails))

# 4. OneDriveファイル取得
new_files = onedrive.get_yesterday_created_files()
report_lines.append("【OneDrive新規ファイル】\n")
for f in new_files:
    report_lines.append(f"- {f['name']}")
    # content = onedrive.get_file_content(f['id'])
    # if content:
    #     report_lines.append(gemini.summarize(content))
    # else:
    #     report_lines.append("（ファイル内容の取得に失敗）")

# 4. Googleカレンダー予定取得
calendar_events = calendar_client.get_events_on_date()
if calendar_events:
    for event in calendar_events:
        summary = gemini.summarize(event)
        report_lines.append(f"【Googleカレンダー予定】要約\n{summary}\n\n\n{event}")
else:
    report_lines.append("【Googleカレンダー予定】本日の予定はありません")

# 5. 日報保存
output_path = Path("reports") / f"{yesterday}_その日のやり取り.txt"
output_path.parent.mkdir(parents=True, exist_ok=True)

# 要約結果をまとめて保存（追記モードで書き込む）
with output_path.open("w", encoding="utf-8") as f:
    f.write("【Teamsチャット投稿 - 要約 -】\n" + gemini.summarize(teams_logs) + "\n")
    f.write("【Teamsチャンネル投稿 - 要約 -】\n" + gemini.summarize(channel_logs) + "\n")
    f.write("【送信メール - 要約 -】\n" + gemini.summarize(sent_mails) + "\n")
    f.write("【OneDrive新規ファイル - 要約 -】\n" + gemini.summarize(new_files) + "\n")
    f.write("\n\n\n".join(report_lines))

print(f"やり取りを保存しました：{output_path}")

# やり取りファイルを読み込んで日報を生成
with output_path.open("r", encoding="utf-8") as f:
    all_text = f.read()

daily_report = gemini.generate_daily_report(all_text)

# 日報の保存先をやり取りファイルと同じフォルダにする
daily_report_path = output_path.parent / f"{yesterday}_日報.txt"
with daily_report_path.open("w", encoding="utf-8") as f:
    f.write(daily_report)

print(f"日報を保存しました：{daily_report_path}")