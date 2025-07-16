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
        model = genai.GenerativeModel("gemini-1.5-flash")
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
**回答**:
**再考**:
**最終的な回答**:
**自己評価**:

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
        model = genai.GenerativeModel("gemini-1.5-flash")
        output_format_instructions = """
# 業務日報自動要約プロンプト（経営管理部長向け）

## タスク
- 入力されたEメール、Teamsチャット、Teamsチャンネル投稿、OneDriveファイル履歴から、経営管理部長への業務日報を自動生成してください。

## 出力フォーマット
- Markdown形式で、以下のセクションに分けてください。

1. **ハイライト**
    - その日の最重要トピック・意思決定・進捗・成果・問題など（3件以内、簡潔に）
2. **継続検討事項**
    - 引き続き対応・検討が必要な事項、今後のアクションや期限も明記
3. **DX推進の視点**
    - 経理課・看護部・その他部門でのDX推進の進捗・課題・成果
    - ITソリューション課のシステム入れ替え（電子カルテ更新）や業務効率化の進捗
4. **人材育成・業務整理の視点**
    - ITソリューション課・総務課の人材育成、業務整理、創造的業務と日常保守の明確化
    - セルフマネジメント、部下の相談対応、次世代候補の育成など
5. **コスト最適化・広報・院内レストラン等の視点**
    - 物品請求・医療材料・委託業者契約の最適化
    - 院内レストラン（ショパン）の再生、広報機能の強化など
6. **その他・情報共有**
    - 上記以外の共有事項や軽微な報告

- 各セクションは**箇条書き**でまとめてください。

## ルール
- 入力データの事実のみを記載し、憶測や個人の感想は含めない
- 専門用語や社内用語は、必要に応じて簡単な説明を加える
- 氏名は敬称付きで記載
- 1件ごとに「誰が・何を・なぜ・どうした」を意識して簡潔に
- 余計な解説やプロンプト自体の説明は一切不要

## 出力例

```
### 経営管理部日報_2025/07/15_上島

**1. ハイライト**
- 電子カルテB2の接続障害が発生し、齋藤さん・天谷さん・吉田さんが対応
- 5F病棟スマートフォンのOSアップデートを実施（堀川さん）
- AI活用に関する打ち合わせ準備（上島さん、吉田さん、畠山さん）

**2. 継続検討事項**
- 電子カルテB2の恒久対策を検討
- 5F病棟スマホの画像検索設定を継続
- AI活用の具体的な計画立案

**3. DX推進の視点**
- 経理課の請求業務自動化に向けたRPAツールの検証を開始
- 看護部の業務日報電子化プロジェクト、要件定義を実施
- ITソリューション課で電子カルテ更新プロジェクトの進捗確認

**4. 人材育成・業務整理の視点**
- ITソリューション課の業務を「創造的業務」と「日常保守」に分類し、担当者を明確化
- 総務課の新人研修を実施、OJT体制を強化
- セルフマネジメントのため、週次で業務棚卸しを実施

**5. コスト最適化・広報・院内レストラン等の視点**
- 医療材料の発注先見直しでコスト削減を検討
- 院内レストラン「ショパン」の新メニュー企画会議を開催
- 広報掲示物のデザインを刷新

**6. その他・情報共有**
- 輸血実施手順の更新依頼（那須さん）
- Accessライセンス導入予定（天谷さん、上島さん）
- 緩和医学講演会の人員配分確認（畠山さん）
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

