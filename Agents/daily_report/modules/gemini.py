import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# --- Load .env.local from the same directory as the script ---
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)
print(f"DEBUG: Attempting to load .env file from: {env_path}")

def summarize(text):
    """
    Google Gemini APIを使用して、指定したフォーマットでテキストを要約する。
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(f"APIキーが見つかりません。{env_path} に GEMINI_API_KEY='YOUR_KEY' を設定してください。")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')
        data_to_summarize = text

        output_format_instructions = """
        ```yaml
        # 業務日報作成プロンプト
        # Eメール、Teamsチャット、OneDriveの変更履歴から日報を生成します。

        # タスク定義
        task:
        name: "業務日報の自動生成"
        description: "指定された入力データ（Eメール、Teamsチャット履歴、OneDriveファイル変更履歴）を解析し、構造化された業務日報を生成する。"

        # 入力データソース
        input_data:
        sources:
            - type: "Eメール"
            description: "その日の送受信メールの内容"
            - type: "Teamsチャット"
            description: "関連するチャネルや個人チャットの履歴"
            - type: "OneDrive"
            description: "ファイルの作成、更新、共有などの変更履歴"

        # 出力フォーマットと指示
        output_format:
        file_name: "経営管理部日報_{YYYY/MM/DD}_{氏名}"
        sections:
            - title: "1. ハイライト"
            instruction: "その日の業務の中で最も重要度や緊急度が高いトピックを3つ程度の箇条書きで要約してください。特に、意思決定がなされたこと、問題が発生したこと、重要なマイルストーンの達成などを中心に記述してください。"
            - title: "2. 継続検討事項"
            instruction: "すぐには完了せず、引き続き対応や検討が必要な事項を箇条書きで記述してください。今後のアクションプランや期限も明確にしてください。"
            - title: "3. その他・情報共有"
            instruction: "上記以外で、情報共有すべき事項や軽微な報告を箇条書きで記述してください。直接の担当ではないが、把握しておくべき情報などが含まれます。"

        # 生成にあたってのルール
        rules:
        - "提供されたデータのみに基づいて報告書を作成し、憶測を含めないでください。"
        - "専門用語や社内用語は、文脈から意味が分かるように記述してください。"
        - "客観的な事実を記述し、個人の感想や意見は含めないでください。"
        - "各項目は、具体的かつ簡潔に記述してください。"
        - "氏名は敬称を付けてください。"

        # 出力例 (Few-shot example)
        example:
        input: "（2025年7月7日のEメール、Teamsチャット、OneDriveのデータ）"
        output: |
            ### 経営管理部日報_2025/07/07_上島

            **1. ハイライト**

            * **電子処方箋システム導入遅延**: アイ・ティ・エス社より、担当の天野氏が忌引きで長期不在のため、日程調整に時間を要するとの連絡がありました。 加算要件に関わるため、7月中の完了を目指し、引き続き催促していきます。
            * **ベースアップ評価料等手当**: エムスリーキャリア社との打ち合わせが、明日7月8日(火)の13時半に設定されました。 人事課の髙田さんと連携し、職員説明会での使用資料などを確認しました。
            * **Bizimo光契約問題への対応**: しんまちで誤って契約したBizimo光について、NTTの既存サービスが全て利用不可になることや、解約時に違約金が発生する可能性があることを確認しました。 営業電話への対応が難しいとの判断から、今後は総務で対応する方向で調整中です。

            **2. 継続検討事項**

            * **電子処方箋システムの早期稼働**: アイ・ティ・エス社の担当者復帰後、速やかに日程を再調整し、7月中の稼働開始を目指します。
            * **Bizimo光契約の解消**: 契約内容を精査し、違約金の有無を確認します。 また、NTT東日本のサービスへ戻すため、Bizimo光から「事業者変更承諾番号」を取得する手順を総務と連携して進めます。
            * **地域医療介護総合確保基金への意見提出**: 上川総合振興局より、基金活用事業に関する意見照会の依頼がありました（7月22日締切）。 内容を精査し、提出要否を検討します。

            **3. その他・情報共有**

            * **ティールームのエアコン更新**: 三菱電機ビルソリューションズ社より、PAC-11（ティールーム）の更新見積（4方向カセット案）を総務課が受領しました（Ccにて内容確認）。 ダクト工事が不要となるため、前回提示額より減額となっています。
            * **ネットワークセキュリティ関連**: エイチ・シー・ネットワークス社より、先日問い合わせたCisco社のネットワークセキュリティ製品（SNA）と連携するアダプタに関する資料を受領しました。
            * **NTS総合弁護士法人からの報告**: 7月7日付の入金処理件数は0件、金額は0円であったとの報告を受け取りました。
        ```
        """

        prompt = f"""
        以下の文章を分析し、{output_format_instructions}

        --- 文章 ---
        {data_to_summarize}
        ---
        """
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"エラーが発生しました: {e}"

