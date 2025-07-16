import datetime
from modules import teams,chatwork,email_client,onedrive,gemini
from pathlib import Path


yesterday = datetime.date.today()- datetime.timedelta(days=1)
report_lines = []

# 1. Teams チャット/投稿取得
teams_logs = teams.get_yesterday_messages()
report_lines.append("【Teams】\n" + "\n".join(teams_logs))

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

# 5. 日報保存
output_path = Path("reports") / f"{yesterday}_その日のやり取り.txt"
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text("【Teams】\n" + gemini.summarize(teams_logs) + "\n", encoding="utf-8")
output_path.write_text("【送信メール】\n" + gemini.summarize(sent_mails) + "\n", encoding="utf-8")
output_path.write_text("【OneDrive新規ファイル】\n" + gemini.summarize(new_files) + "\n", encoding="utf-8")
output_path.write_text("\n\n\n".join(report_lines), encoding="utf-8")
print(f"やり取りを保存しました：{output_path}")