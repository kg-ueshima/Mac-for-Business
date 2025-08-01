import sys
import os
from datetime import datetime, timedelta
import re
from pathlib import Path

# Gemini API用モジュール（パスは適宜修正）
sys.path.append(str(Path(__file__).parent / "modules"))
import gemini

# 使い方: python collect_weekly_report.py [基準日(yyyy-mm-dd)]（省略時は今日）

def get_last_7days_files(base_dir="80-業務日報", ref_date=None):
    """直近7日分の '日報' ファイルパスリストを返す"""
    if ref_date is None:
        ref_date = datetime.today()
    files = []
    for i in range(7):
        d = ref_date - timedelta(days=i)
        fname = f"{d.strftime('%Y-%m-%d')}_日報.txt"
        fpath = os.path.join(base_dir, fname)
        if os.path.exists(fpath):
            files.append((d.strftime('%Y-%m-%d'), fpath))
    return sorted(files)

def collect_daily_reports(files):
    """日付とファイルパスのリストから日報内容をまとめて返す"""
    daily_data = []
    for date_str, fpath in files:
        with open(fpath, encoding="utf-8") as f:
            content = f.read().strip()
        daily_data.append((date_str, content))
    return daily_data

def make_weekly_prompt(daily_data):
    """週報用Geminiプロンプトを生成"""
    today_str = datetime.today().strftime("%Y/%m/%d")
    prompt_lines = []
    prompt_lines.append("## 業務週報自動要約プロンプト（経営管理部長向け）")
    prompt_lines.append("")
    prompt_lines.append("### タスク")
    prompt_lines.append("- 直近1週間分の日報をもとに、経営管理部長向けの週報を自動生成してください。")
    prompt_lines.append("")
    prompt_lines.append("### 出力フォーマット")
    prompt_lines.append("#### 経営管理部週報_" + today_str + "_上島")
    prompt_lines.append("")
    prompt_lines.append("**1. 週間ハイライト**")
    prompt_lines.append("- 1週間の最重要トピック・意思決定・進捗・成果・問題など（3件以内、簡潔に）")
    prompt_lines.append("**2. 継続検討事項**")
    prompt_lines.append("- 引き続き対応・検討が必要な事項、今後のアクションや期限も明記")
    prompt_lines.append("**3. ITソ課：DX推進の視点**")
    prompt_lines.append("- 経理課・看護部・その他部門でのDX推進の進捗・課題・成果")
    prompt_lines.append("**4. 総務課：コスト最適化・広報・院内レストラン等の視点**")
    prompt_lines.append("- 物品請求・医療材料・委託業者契約の最適化、広報、院内レストラン等")
    prompt_lines.append("**5. マネジメント：人材育成・業務整理の視点**")
    prompt_lines.append("- ITソリューション課・総務課の人材育成、業務整理、創造的業務と日常保守の明確化")
    prompt_lines.append("**6. その他・情報共有**")
    prompt_lines.append("- 上記以外の共有事項や軽微な報告")
    prompt_lines.append("")
    prompt_lines.append("### ルール")
    prompt_lines.append("- 入力データの事実のみを記載し、憶測や個人の感想は含めない")
    prompt_lines.append("- 専門用語や社内用語は、必要に応じて簡単な説明を加える")
    prompt_lines.append("- 氏名は敬称付きで記載")
    prompt_lines.append("- 1件ごとに「誰が・何を・なぜ・どうした」を意識して簡潔に")
    prompt_lines.append("- 余計な解説やプロンプト自体の説明は一切不要")
    prompt_lines.append("")
    prompt_lines.append("### 入力データ")
    for date_str, content in daily_data:
        prompt_lines.append(f"#### {date_str}")
        prompt_lines.append(content)
        prompt_lines.append("")
    return "\n".join(prompt_lines)

def main():
    # 引数で基準日指定（省略時は今日）
    if len(sys.argv) == 2:
        try:
            ref_date = datetime.strptime(sys.argv[1], "%Y-%m-%d")
        except ValueError:
            print("日付形式が正しくありません。yyyy-mm-dd で指定してください。")
            sys.exit(1)
    else:
        ref_date = datetime.today()

    # 直近7日分の日報ファイルを取得
    files = get_last_7days_files(ref_date=ref_date)
    if not files:
        print("直近1週間分の日報ファイルが見つかりません。")
        sys.exit(0)

    # 日報内容を集約
    daily_data = collect_daily_reports(files)

    # 週報用プロンプト生成
    prompt = make_weekly_prompt(daily_data)

    # Geminiで週報生成
    print("Geminiで週報を集約中...")
    weekly_report = gemini.generate_daily_report(prompt)

    # 出力ファイル名
    week_start = files[0][0]
    week_end = files[-1][0]
    out_path = Path("80-業務日報") / f"{week_start}_to_{week_end}_週報.txt"
    with out_path.open("w", encoding="utf-8") as f:
        f.write(weekly_report)
    print(f"週報を保存しました: {out_path}")

if __name__ == "__main__":
    main()
