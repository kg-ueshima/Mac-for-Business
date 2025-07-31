import os
import re
import datetime
from Agents.daily_report.modules.gemini import gemini_generate_content, create_word_report

def sanitize_filename(filename: str) -> str:
    """
    Remove or replace characters that are unsafe for filenames.
    Only allow Japanese characters, alphanumerics and a subset of punctuation. Everything else becomes an underscore.
    """
    return re.sub(r'[^\w\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\-_.]', '_', filename)

def strip_markdown(text: str) -> str:
    """
    Remove common Markdown syntax from a string, returning plain text.
    """
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'!\[(.*?)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'\[(.*?)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    text = re.sub(r'^\s*#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*([\-*+]\s+|\d+\.\s+)', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def short_video_workflow_chopin() -> None:
    """
    レストランchopin専用のショート動画作成ワークフローを自動実行し、
    各工程ごとにGeminiでテキスト生成し、WordファイルにまとめてOneDriveに保存する。
    """
    print("=== レストランchopin ショート動画作成ワークフロー ===")
    topic = "レストランchopinの収益アップ施策"
    today = datetime.date.today().strftime("%Y%m%d")
    prompts = [
        ("調査", f"『{topic}』についてリサーチし、要点をまとめてください。"),
        ("構成案", "ショート動画の構成案を作成してください。"),
        ("本文", "ショート動画用のナレーション原稿を作成してください。"),
        ("要約", "動画内容をSNS投稿用に要約してください。"),
        ("SNS投稿文", "Instagram用の投稿文を作成してください。"),
        ("画像生成プロンプト", "サムネイル画像生成用のプロンプトを作成してください。"),
        ("音声台本", "ナレーション用の台本を作成してください。"),
    ]
    sections = []
    for title, prompt in prompts:
        print(f"{title}を生成中...")
        content = gemini_generate_content(prompt)
        content_plain = strip_markdown(content)
        sections.append((title, content_plain))
    safe_topic = sanitize_filename(topic)
    filename = f"{today}_{safe_topic}_ショート動画案.docx"
    # chopin専用のOneDrive保存先（必要に応じて変更）
    onedrive_dir = os.path.expanduser(
        "/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/00_Agents/chopin"
    )
    os.makedirs(onedrive_dir, exist_ok=True)
    save_path = create_word_report(sections, filename, onedrive_dir)
    print(f"\nショート動画案が作成されました: {save_path}")
    print("OneDriveで自動同期されます。") 