import sys
import os
from datetime import datetime, timedelta
import re

# 使い方: python collect_weekly_report.py 2025-06-02

def main():
    if len(sys.argv) != 2:
        print("使い方: python collect_weekly_report.py 開始日(yyyy-mm-dd)")
        sys.exit(1)

    start_str = sys.argv[1]
    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
    except ValueError:
        print("日付形式が正しくありません。yyyy-mm-dd で指定してください。")
        sys.exit(1)

    # 5日分の日付リストを作成
    date_list = [(start_date + timedelta(days=i)).strftime("%m/%d") for i in range(5)]
    month_str = start_date.strftime("%Y-%m")
    fpath = os.path.join("80-業務日報", f"{month_str}.md")

    if not os.path.exists(fpath):
        print(f"{fpath} が存在しません。")
        sys.exit(1)

    with open(fpath, encoding="utf-8") as f:
        content = f.read()

    output_lines = []
    output_lines.append("#条件:")
    output_lines.append("以下のステップを踏んで{出力フォーマット} に従う必要があります。")
    output_lines.append("まずは{質問} を[解釈] してください。")
    output_lines.append("次に{質問} に対して[回答] をしてください。")
    output_lines.append("次にその[回答] が適切なのか[再考] してください。")
    output_lines.append("次に[再考] した上で[最終的な回答] を生成してください。")
    output_lines.append("最後にその回答が適切なのか[自己評価] を行ってください。")
    output_lines.append("")
    output_lines.append("#出力フォーマット:")
    output_lines.append("#経営管理部週報_{今日の日付}_上島")
    output_lines.append("1. ハイライト：{ここに内容を出力}")
    output_lines.append("2. 継続検討事項：{ここに内容を出力}")
    output_lines.append("その他：人材教育の視点：{ここに内容を出力}")
    output_lines.append("その他：DXで推進の視点：{ここに内容を出力}")
    output_lines.append("その他：業務整理の視点など出力：{ここに内容を出力}")
    output_lines.append("")
    output_lines.append("#質問:")
    output_lines.append("あなたは、プロの編集者です。最高の週次報告内容を出力してください。")
    output_lines.append("")
    output_lines.append("#指示")
    output_lines.append("・時系列")
    output_lines.append("・重複する内容は取りまとめる")
    output_lines.append("・完結にわかりやすく250文字以内")
    output_lines.append("")
    output_lines.append("#入力データ")

    for mmdd in date_list:
        # #### MM/DD の直後に空白や改行が複数入る場合も考慮
        pattern = rf"^#### {mmdd}\s*\n(.*?)(?=^#### |\Z)"
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            output_lines.append(f"#### {mmdd}")
            output_lines.append(match.group(1).strip())
            output_lines.append("")

    if len(output_lines) <= 20:  # データがない場合
        print("指定期間に該当する日報がありません。")
        sys.exit(0)

    with open("prompt_input.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(output_lines))
    print("prompt_input.txt に集約結果を出力しました。")

if __name__ == "__main__":
    main()
