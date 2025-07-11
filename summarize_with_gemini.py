import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# --- Load .env.local from the same directory as the script ---
env_path = Path(__file__).resolve().parent / 'env.local'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG: Attempting to load .env file from: {env_path}")

def summarize_text_with_gemini():
    """
    Google Gemini APIを使用して、指定したフォーマットでテキストを要約する。
    """
    try:
        # --- Use the consistent key 'GOOGLE_API_KEY' ---
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(f"APIキーが見つかりません。{env_path} に GEMINI_API_KEY='YOUR_KEY' を設定してください。")
        
        genai.configure(api_key=api_key)

        # --- Use a valid model name ---
        model = genai.GenerativeModel('gemini-2.0-flash')

        # --- The rest of the script is fine ---
        data_to_summarize = """
        2025年7月9日、株式会社GenAIは、画期的な新製品「オートマティック・レポートジェネレーター」を発表しました。
        このツールは、企業の持つ大量の売上データや顧客フィードバックを自動的に分析し、
        経営層向けの要約レポートをわずか数分で生成することができます。
        従来、専門のアナリストが数日かけて行っていた作業を大幅に効率化し、
        迅速な意思決定を支援することを目的としています。
        導入企業は、初期設定でレポートのフォーマットや重視する指標をカスタマイズでき、
        日次、週次、月次での自動レポート生成も可能です。
        """

        output_format_instructions = """
        以下のフォーマットで厳密に要約してください。

        - **タイトル:** 記事の主題を簡潔に表すタイトル
        - **要点 (3つ):**
            - 箇条書き1
            - 箇条書き2
            - 箇条書き3
        - **結論:** この情報から得られる最も重要な気づき
        """

        prompt = f"""
        以下の文章を分析し、{output_format_instructions}

        --- 文章 ---
        {data_to_summarize}
        ---
        """
        response = model.generate_content(prompt)

        print("--- 生成された要約 ---")
        print(response.text)

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    summarize_text_with_gemini()
