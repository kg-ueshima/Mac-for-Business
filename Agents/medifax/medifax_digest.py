#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
医療情報RSSフィード取得・要約プログラム
https://mfd.jiho.jp/genre/1/rss.xml からRSSを取得し、
各記事の内容をGeminiで要約してファイルに保存する
"""

import requests
import feedparser
from bs4 import BeautifulSoup
import datetime
from pathlib import Path
import sys
import os
from dotenv import load_dotenv
from typing import List, Dict, Optional
import time

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)

# Geminiモジュールをインポート
import sys
import os
# 現在のファイルの絶対パスを取得
current_file = Path(__file__).resolve()
# modulesディレクトリの絶対パスを取得
modules_path = current_file.parent.parent / 'daily_report' / 'modules'
# パスを追加
sys.path.insert(0, str(modules_path))
# 直接geminiモジュールをインポート
import gemini


class MedifaxDigest:
    """医療情報RSSフィード取得・要約クラス"""
    
    def __init__(self):
        self.rss_url = "https://mfd.jiho.jp/genre/1/rss.xml"
        self.output_dir = Path("80-業務日報/medifax_digest")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def fetch_rss_feed(self) -> List[Dict]:
        """RSSフィードを取得して記事情報を抽出"""
        try:
            print(f"RSSフィードを取得中: {self.rss_url}")
            response = requests.get(self.rss_url, timeout=30)
            response.raise_for_status()
            
            # RSSフィードをパース
            feed = feedparser.parse(response.content)
            
            articles = []
            for entry in feed.entries:
                article = {
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'summary': entry.get('summary', ''),
                    'content': ''
                }
                
                # dc:jdate（日本日付）を取得
                if hasattr(entry, 'dc_jdate'):
                    article['jdate'] = entry.dc_jdate
                else:
                    article['jdate'] = ''
                
                articles.append(article)
                
            print(f"{len(articles)}件の記事を取得しました")
            return articles
            
        except Exception as e:
            print(f"RSSフィード取得エラー: {e}")
            return []
    
    def fetch_article_content(self, url: str) -> str:
        """記事URLから本文を取得"""
        try:
            print(f"記事内容を取得中: {url}")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 記事本文を抽出（一般的なセレクタ）
            content_selectors = [
                'article',
                '.article-content',
                '.post-content',
                '.entry-content',
                '#content',
                '.content'
            ]
            
            content = ""
            for selector in content_selectors:
                element = soup.select_one(selector)
                if element:
                    content = element.get_text(strip=True)
                    break
            
            # セレクタで見つからない場合はbody全体から抽出
            if not content:
                # 不要な要素を削除
                for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                    tag.decompose()
                content = soup.get_text(strip=True)
            
            return content[:5000]  # 長すぎる場合は切り詰め
            
        except Exception as e:
            print(f"記事内容取得エラー ({url}): {e}")
            return ""
    
    def summarize_article(self, title: str, content: str) -> str:
        """Geminiで記事を要約"""
        try:
            prompt = f"""
以下の医療情報記事を要約してください。

タイトル: {title}

内容:
{content}

要約の条件:
- 医療・病院経営に関連する重要なポイントを抽出
- 実務的に役立つ情報を優先
- 簡潔で分かりやすい日本語で
- 箇条書きで整理
- 必要に応じて今後の影響や注意点も含める
"""
            return gemini.summarize(prompt)
            
        except Exception as e:
            return f"要約エラー: {e}"
    
    def save_summary(self, articles: List[Dict], summaries: List[str]):
        """要約結果をファイルに保存"""
        today = datetime.date.today()
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 詳細ファイル
        detail_file = self.output_dir / f"medifax_digest_{today}_{timestamp}.md"
        
        with open(detail_file, 'w', encoding='utf-8') as f:
            f.write(f"# 医療情報ダイジェスト - {today}\n\n")
            f.write(f"取得日時: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for i, (article, summary) in enumerate(zip(articles, summaries), 1):
                f.write(f"## {i}. {article['title']}\n\n")
                f.write(f"**日付**: {article['jdate'] or article['published']}\n\n")
                f.write(f"**URL**: {article['link']}\n\n")
                f.write(f"**要約**:\n{summary}\n\n")
                f.write("---\n\n")
        
        # 要約のみのファイル
        summary_file = self.output_dir / f"medifax_summary_{today}_{timestamp}.md"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# 医療情報要約 - {today}\n\n")
            f.write(f"取得日時: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for i, (article, summary) in enumerate(zip(articles, summaries), 1):
                f.write(f"## {i}. {article['title']}\n\n")
                f.write(f"{summary}\n\n")
        
        print(f"詳細ファイルを保存: {detail_file}")
        print(f"要約ファイルを保存: {summary_file}")
        
        return detail_file, summary_file
    
    def run(self):
        """メイン処理"""
        print("医療情報RSSフィード取得・要約を開始します")
        print(f"処理開始: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 1. RSSフィードを取得
        articles = self.fetch_rss_feed()
        if not articles:
            print("記事が取得できませんでした")
            return
        
        # 2. 各記事の内容を取得
        summaries = []
        for i, article in enumerate(articles, 1):
            print(f"\n記事 {i}/{len(articles)} を処理中...")
            print(f"タイトル: {article['title']}")
            
            # 記事内容を取得
            content = self.fetch_article_content(article['link'])
            if content:
                # Geminiで要約
                summary = self.summarize_article(article['title'], content)
                summaries.append(summary)
                print("要約完了")
            else:
                summaries.append("記事内容の取得に失敗しました")
                print("記事内容の取得に失敗")
            
            # API制限を避けるため少し待機
            time.sleep(1)
        
        # 3. 結果を保存
        detail_file, summary_file = self.save_summary(articles, summaries)
        
        print(f"\n処理完了: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"処理した記事数: {len(articles)}")


def main():
    """メイン関数"""
    digest = MedifaxDigest()
    digest.run()


if __name__ == "__main__":
    main() 