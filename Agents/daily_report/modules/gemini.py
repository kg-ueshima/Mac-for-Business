import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG (gemini.py): Loading env from {env_path}")

def summarize(text):
    """
    指定の思考ステップで最高の要約を出力する。
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(f"APIキーが見つかりません。{env_path} に GEMINI_API_KEY='YOUR_KEY' を設定してください。")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"""
#条件:
以下のステップを踏んで{{出力フォーマット}} に従う必要があります。

まずは{{質問}} を[解釈] してください。
次に{{質問}} に対して[回答] をしてください。
次にその[回答] が適切なのか[再考] してください。
次に[再考] した上で[最終的な回答] を生成してください。
最後にその回答が適切なのか[自己評価] を行ってください。

#出力フォーマット:
**解釈**:
**最終的な回答**:

#質問:
あなたは、プロの編集者です。最高の要約を出力してください。

#要約対象:
{text}
"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"エラーが発生しました: {e}"


def generate_daily_report(text):
    """
    経営管理部長向け日報フォーマットで要約を生成する。
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(f"APIキーが見つかりません。{env_path} に GEMINI_API_KEY='YOUR_KEY' を設定してください。")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        output_format_instructions = """
```
# 日報要約テンプレート（Markdown出力形式）

# 提出者情報
report_date: "2025-07-15"

# 1. ハイライト（重要トピック／対応事項の要約）
highlights:
  - "[具体的な業務名]：対応内容、関係者、状況（例：電子カルテB2接続障害の対応、天谷・吉田が処置）"
  - "[例：アプリ不具合対応]：機種・バージョン、原因、担当者、今後の対応予定"
  - "[例：対外対応]：業者名、日程、進捗状況"

# 2. 業務報告（当日実施した主な業務を分類別に記録）
tasks:
  - category: "電子カルテ・システム・IT"
    items:
      - "[業務名]：目的、実施内容、関係者、成果（例：スマートフォンOS更新）"
  - category: "総務・契約・調整"
    items:
      - "[業務名]：相手先、調整事項、進捗（例：システム導入契約の進捗共有）"
  - category: "その他院内対応"
    items:
      - "[業務名]：病棟・部門名、内容、担当、特記事項"

# 3. 継続検討・課題
ongoing_issues:
  - "[課題名]：現在の状況、阻害要因、次アクション（例：恒久対策の検討）"
  - "[例：設定変更未完了]：対象部署、原因、予定対応日"

# 4. 人材育成・指導対応（あれば記載）
people_management:
  - "[例：部下の対応支援]：対象者、場面、対応内容、所感"
  - "[例：指示内容]：目的、実施内容、反応"

# 5. その他連絡・情報共有
shared_info:
  - "[例：社内連絡]：担当者、内容（例：HP更新業務引継ぎ日程）"
  - "[例：会議日程]：タイトル、出席者、調整内容"
  - "[例：資料作成・更新]：ファイル名、保存先（OneDrive）、利用目的"

# 6. コメント・所感（自由記述欄）
comments: >
  [例：今日の全体的な所感や、改善点、気づきなど。不要な場合は記載なしでも可]

```
"""
        prompt = f"""
以下の指示に従い、日報を生成してください。

{output_format_instructions}

--- 入力データ ---
{text}
---
"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"エラーが発生しました: {e}"

