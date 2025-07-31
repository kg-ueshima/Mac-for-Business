#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
医療情報RSSフィード取得・要約プログラム（自動ログイン対応版）
SafariでIDとPWを入れてサイトに自動ログインし、
RSSフィードから医療情報を取得してGeminiで要約する
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
import subprocess
import json
import re

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


class MedifaxAutoLogin:
    """医療情報RSSフィード取得・要約クラス（自動ログイン対応）"""
    
    def __init__(self):
        self.rss_url = "https://mfd.jiho.jp/genre/1/rss.xml"
        self.login_url = "https://mfd.jiho.jp/login"  # ログインページのURL
        self.output_dir = Path(current_file.parent.parent.parent / "80-MEDIFAX_DIGEST")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # ログイン情報（環境変数から取得）
        self.username = os.getenv("MEDIFAX_USERNAME")
        self.password = os.getenv("MEDIFAX_PASSWORD")
        
        # セッション管理
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def setup_safari_automation(self):
        """Safariでの自動ログイン設定"""
        print("Safariでの自動ログイン設定を確認中...")
        
        # AppleScriptでSafariを開いてログイン
        if self.username and self.password:
            print("環境変数からログイン情報を取得しました")
            return self.login_with_safari()
        else:
            print("環境変数 MEDIFAX_USERNAME と MEDIFAX_PASSWORD が設定されていません")
            print("手動でログインしてください")
            return self.manual_login_prompt()
    
    def login_with_safari(self):
        """Safariで自動ログイン（AppleScriptによるDOM操作）"""
        import subprocess

        def escape_quotes(s):
            return s.replace('"', '\\"') if s else ""

        login_url = escape_quotes(self.login_url)

        apple_script = f'''
        tell application "Safari"
            activate
            delay 1
            set loginTab to make new document
            set URL of loginTab to "{login_url}"
        end tell

        delay 5
        tell application "System Events"
        key code 102
            tell process "Safari"
                set frontmost to true
                delay 1
                keystroke "{self.username}"
                delay 0.5
                keystroke tab
                delay 0.5
                keystroke "{self.password}"
                delay 0.5
                keystroke return
            end tell
        end tell
        delay 2
        '''

        print("Safariで自動ログインを実行中...")

        try:
            result = subprocess.run(
                ['osascript', '-e', apple_script],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                print("Safariでの自動ログインが完了しました")
                return True
            else:
                print(f"Safari自動ログインエラー: {result.stderr}")
                return self.manual_login_prompt()
        except Exception as e:
            print(f"Safari自動ログインエラー: {e}")
            return self.manual_login_prompt()

    
    def manual_login_prompt(self):
        """手動ログインの案内"""
        print("\n=== 手動ログインが必要です ===")
        print(f"1. Safariで {self.login_url} を開いてください")
        print("2. ログイン情報を入力してログインしてください")
        print("3. ログイン後、このプログラムを再実行してください")
        
        input("\nログインが完了したら Enter キーを押してください...")
        return True
    
    def fetch_rss_feed(self) -> List[Dict]:
        """RSSフィードを取得して本日分の記事情報のみ抽出"""
        try:
            print(f"RSSフィードを取得中: {self.rss_url}")
            
            # ログイン済みセッションでRSSを取得
            response = self.session.get(self.rss_url, timeout=30)
            response.raise_for_status()
            
            print(f"RSSレスポンスステータス: {response.status_code}")
            print(f"RSSレスポンスサイズ: {len(response.content)} bytes")
            
            # 生のXML内容を確認（デバッグ用）
            xml_content = response.content.decode('utf-8', errors='ignore')
            print(f"\n=== RSSフィードの最初の1000文字 ===")
            print(xml_content[:1000])
            print("=== RSSフィード内容終了 ===\n")
            
            # RSSフィードをパース
            feed = feedparser.parse(response.content)
            
            print(f"RSSフィードから {len(feed.entries)} 件の記事を取得")
            
            # 最初の3件の記事の詳細を表示（デバッグ用）
            if feed.entries:
                print("\n=== 最初の3件の記事の詳細 ===")
                for i, entry in enumerate(feed.entries[:3]):
                    print(f"\n記事 {i+1}:")
                    print(f"  タイトル: {entry.get('title', 'No title')}")
                    print(f"  リンク: {entry.get('link', 'No link')}")
                    print(f"  dc_date: {entry.get('dc_date', 'No dc_date')}")
                    print(f"  published: {entry.get('published', 'No published')}")
                    print(f"  published_parsed: {entry.get('published_parsed', 'No published_parsed')}")
                    if hasattr(entry, 'dc_jdate'):
                        print(f"  dc_jdate: {entry.dc_jdate}")
                    print(f"  全キー: {list(entry.keys())}")
            
            articles = []
            today = datetime.date.today()
            print(f"\n今日の日付: {today}")
            
            for i, entry in enumerate(feed.entries):
                print(f"\n記事 {i+1}: {entry.get('title', 'No title')}")
                
                # 各種日付フィールドの取得
                dc_date = entry.get('dc_date', '')
                published = entry.get('published', '')
                published_parsed = entry.get('published_parsed', None)
                updated = entry.get('updated', '')
                updated_parsed = entry.get('updated_parsed', None)
                jdate = getattr(entry, 'dc_jdate', '') if hasattr(entry, 'dc_jdate') else ''
                
                # feedparserでの名前空間付き要素の確認
                print(f"  dc_date: {dc_date}")
                print(f"  published: {published}")
                print(f"  updated: {updated}")
                print(f"  jdate: {jdate}")
                
                # 名前空間付き要素の直接確認
                if hasattr(entry, 'dc_date'):
                    print(f"  entry.dc_date: {entry.dc_date}")
                if hasattr(entry, 'dc_jdate'):
                    print(f"  entry.dc_jdate: {entry.dc_jdate}")
                
                # 全属性を確認（デバッグ用）
                print(f"  entry.__dict__.keys(): {list(entry.__dict__.keys())}")
                
                # 日付判定
                is_today = False
                # 優先順位: dc_date > published > updated > jdate
                date_str = None
                if dc_date:
                    date_str = dc_date
                elif published:
                    date_str = published
                elif updated:
                    date_str = updated
                elif jdate:
                    date_str = jdate

                # ISO8601形式の日付をパース
                entry_date = None
                if date_str:
                    print(f"  処理する日付文字列: {date_str}")
                    # 例: 2025-08-01T05:00:05+09:00
                    try:
                        # タイムゾーン付きの場合
                        dt = datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                        entry_date = dt.date()
                        print(f"  パースされた日付: {entry_date}")
                    except Exception as e:
                        print(f"  ISO8601パースエラー: {e}")
                        # それ以外の形式の場合
                        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
                        if m:
                            entry_date = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                            print(f"  正規表現でパースされた日付: {entry_date}")
                
                # published_parsedまたはupdated_parsedがあればそちらも見る
                if not entry_date and published_parsed:
                    entry_date = datetime.date(published_parsed.tm_year, published_parsed.tm_mon, published_parsed.tm_mday)
                    print(f"  published_parsedから取得した日付: {entry_date}")
                elif not entry_date and updated_parsed:
                    entry_date = datetime.date(updated_parsed.tm_year, updated_parsed.tm_mon, updated_parsed.tm_mday)
                    print(f"  updated_parsedから取得した日付: {entry_date}")
                
                if entry_date and entry_date == today:
                    is_today = True
                    print(f"  ✓ 今日の記事として判定")
                else:
                    print(f"  ✗ 今日の記事ではありません (entry_date: {entry_date}, today: {today})")

                if not is_today:
                    continue

                article = {
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': published,
                    'dc:date': dc_date,
                    'jdate': jdate,
                    'summary': entry.get('summary', ''),
                    'content': ''
                }
                articles.append(article)
                print(f"  ✓ 記事を追加")
                
            print(f"\n{len(articles)}件の本日分の記事を取得しました")
            return articles
            
        except Exception as e:
            print(f"RSSフィード取得エラー: {e}")
            return []
    
    def fetch_article_content(self, url: str) -> str:
        """記事URLから本文を取得（ログイン済みセッション使用）"""
        try:
            print(f"記事内容を取得中: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 記事本文を抽出（一般的なセレクタ）
            content_selectors = [
                'article',
                '.article-content',
                '.post-content',
                '.entry-content',
                '#content',
                '.content',
                '.article-body',
                '.post-body'
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
                for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'menu']):
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
- 医療関係者にとって重要な情報を強調
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
            f.write(f"RSS URL: {self.rss_url}\n\n")
            
            for i, (article, summary) in enumerate(zip(articles, summaries), 1):
                f.write(f"## {i}. {article['title']}\n\n")
                f.write(f"**日付**: {article.get('dc_date') or article.get('published') or article.get('jdate','')}\n\n")
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
        
        # JSON形式でも保存（後で処理しやすい）
        json_file = self.output_dir / f"medifax_data_{today}_{timestamp}.json"
        
        json_data = {
            'date': today.isoformat(),
            'timestamp': datetime.datetime.now().isoformat(),
            'rss_url': self.rss_url,
            'articles': []
        }
        
        for article, summary in zip(articles, summaries):
            json_data['articles'].append({
                'title': article['title'],
                'link': article['link'],
                'published': article.get('published', ''),
                'dc:date': article.get('dc_date', ''),
                'jdate': article.get('jdate', ''),
                'summary': summary
            })
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        
        print(f"詳細ファイルを保存: {detail_file}")
        print(f"要約ファイルを保存: {summary_file}")
        print(f"JSONファイルを保存: {json_file}")
        
        return detail_file, summary_file, json_file
    
    def run(self):
        """メイン処理"""
        print("医療情報RSSフィード取得・要約を開始します")
        print(f"処理開始: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 1. ログイン設定
        login_success = self.setup_safari_automation()
        if not login_success:
            print("ログインに失敗しました")
            return
        
        # 2. RSSフィードを取得（本日分のみ）
        articles = self.fetch_rss_feed()
        if not articles:
            print("本日分の記事が取得できませんでした")
            return
        
        # 3. 各記事の内容を取得
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
        
        # 4. 結果を保存
        detail_file, summary_file, json_file = self.save_summary(articles, summaries)
        
        print(f"\n処理完了: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"処理した記事数: {len(articles)}")


def main():
    """メイン関数"""
    digest = MedifaxAutoLogin()
    digest.run()


if __name__ == "__main__":
    main() 