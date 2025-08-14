#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
医療情報RSSフィード取得・要約プログラム（自動ログイン対応版）
SafariでIDとPWを入れてサイトに自動ログインし、
RSSフィードから医療情報を取得してGeminiで要約する
"""

from string import Template
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
import re
import json
import pickle

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
import teams
import teams_notification


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

        # ログインキャッシュファイル
        self.cache_dir = Path(current_file.parent / ".cache")
        self.cache_dir.mkdir(exist_ok=True)
        self.login_cache_file = self.cache_dir / "medifax_login.pkl"
        self.cookie_cache_file = self.cache_dir / "medifax_cookies.pkl"

        # キャッシュからセッション情報を復元
        self._load_cached_session()

    def _load_cached_session(self):
        """キャッシュからセッション情報を読み込む"""
        try:
            if self.login_cache_file.exists():
                # ログイン情報の有効期限をチェック（24時間）
                cache_time = datetime.datetime.fromtimestamp(self.login_cache_file.stat().st_mtime)
                if datetime.datetime.now() - cache_time < datetime.timedelta(hours=24):
                    with open(self.login_cache_file, 'rb') as f:
                        login_info = pickle.load(f)
                        print("キャッシュされたログイン情報を使用します")
                        self.cached_login = True

                        # クッキー情報も復元
                        if self.cookie_cache_file.exists():
                            with open(self.cookie_cache_file, 'rb') as f:
                                cookies = pickle.load(f)
                                self.session.cookies.update(cookies)
                        return
                else:
                    print("キャッシュされたログイン情報が期限切れです")

            self.cached_login = False

        except Exception as e:
            print(f"キャッシュ読み込みエラー: {e}")
            self.cached_login = False

    def _save_cached_session(self):
        """セッション情報をキャッシュに保存"""
        try:
            # ログイン成功の記録
            with open(self.login_cache_file, 'wb') as f:
                pickle.dump({'logged_in': True, 'timestamp': datetime.datetime.now()}, f)

            # クッキー情報を保存
            with open(self.cookie_cache_file, 'wb') as f:
                pickle.dump(dict(self.session.cookies), f)

            print("ログイン情報をキャッシュに保存しました")

        except Exception as e:
            print(f"キャッシュ保存エラー: {e}")

    def _clear_cache(self):
        """キャッシュをクリア"""
        try:
            if self.login_cache_file.exists():
                self.login_cache_file.unlink()
            if self.cookie_cache_file.exists():
                self.cookie_cache_file.unlink()
            print("キャッシュをクリアしました")
        except Exception as e:
            print(f"キャッシュクリアエラー: {e}")

    def setup_safari_automation(self):
        """Safariでの自動ログイン設定"""
        # キャッシュされたログイン情報がある場合はスキップ
        if hasattr(self, 'cached_login') and self.cached_login:
            print("キャッシュされたログイン情報を使用中 - Safariログインをスキップします")
            return True

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

        # Safariで新しいウィンドウを開くAppleScript（エラーハンドリング改善）
        apple_script = f'''
        tell application "Safari"
            activate
            delay 1
            -- 新しいドキュメントを作成
            set loginDoc to make new document
            delay 1
            -- URLを設定（documentに対して直接設定）
            set URL of loginDoc to "{login_url}"
            -- ページの読み込みを待つ
            delay 6
        end tell
        
        -- フォームに入力
        tell application "System Events"
            tell process "Safari"
                set frontmost to true
                delay 1
                -- 英数入力に切り替え
                key code 102
                delay 0.5
                -- ユーザー名を入力
                keystroke "{self.username}"
                delay 0.5
                -- Tabでパスワードフィールドに移動
                keystroke tab
                delay 0.5
                -- 英数入力を再確認
                key code 102
                delay 0.5
                -- パスワードを入力
                keystroke "{self.password}"
                delay 0.5
                -- Enterでログイン
                keystroke return
            end tell
        end tell
        delay 3
        '''

        print("Safariで自動ログインを実行中...")

        try:
            result = subprocess.run(
                ['osascript', '-e', apple_script],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                print("Safariでの自動ログインが完了しました")
                # ログイン後にセッション情報を取得
                success = self.get_safari_session()
                if success:
                    # ログイン成功時にキャッシュを保存
                    self._save_cached_session()
                return success
            else:
                print(f"Safari自動ログインエラー: {result.stderr}")
                return self.manual_login_prompt()
        except Exception as e:
            print(f"Safari自動ログインエラー: {e}")
            return self.manual_login_prompt()

    def get_safari_session(self):
        """Safariのセッション情報を取得してrequestsセッションに反映"""
        try:
            print("Safariのセッション情報を取得中...")

            # Safariのクッキー情報を取得
            # (ウィンドウindexは使わないが、今後拡張する場合は利用可)
            apple_script = '''
            tell application "Safari"
                set cookieData to ""
                if (count of windows) > 0 then
                    repeat with t in tabs of front window
                        set currentURL to URL of t
                        if currentURL contains "mfd.jiho.jp" then
                            set cookieData to "found"
                            exit repeat
                        end if
                    end repeat
                end if
                return cookieData
            end tell
            '''

            result = subprocess.run(
                ['osascript', '-e', apple_script],
                capture_output=True, text=True
            )

            if result.returncode == 0 and "found" in result.stdout:
                print("Safariでログイン済みセッションを確認しました")
                # Safariのセッションを模倣するためのヘッダーを設定
                self.session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
                    'Accept': 'application/rss+xml, application/xml, text/xml, */*',
                    'Accept-Language': 'ja-JP,ja;q=0.9,en;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1'
                })
                return True
            else:
                print("Safariでログイン済みセッションが見つかりません")
                return self.manual_login_prompt()

        except Exception as e:
            print(f"セッション情報取得エラー: {e}")
            return self.manual_login_prompt()

    def fetch_rss_with_safari(self) -> List[Dict]:
        """SafariでRSSフィードを取得してスクレイピング"""
        try:
            print("SafariでRSSフィードを取得中...")

            # SafariでRSSフィードを開く（シンプルなアプローチ）
            apple_script = f'''
            tell application "Safari"
                activate
                delay 1
                -- 既存のウィンドウがあればそれを使用、なければ新規作成
                if (count of windows) > 0 then
                    set rssDoc to front document
                else
                    set rssDoc to make new document
                end if
                delay 0.5
                set URL of rssDoc to "{self.rss_url}"
                -- ページの読み込みを待つ
                delay 5
                -- ソースを取得
                set rssContent to source of rssDoc
                return rssContent
            end tell
            '''

            result = subprocess.run(
                ['osascript', '-e', apple_script],
                capture_output=True, text=True
            )

            if result.returncode == 0 and result.stdout.strip():
                print("SafariからRSSフィードを取得しました")
                xml_content = result.stdout.strip()

                # RSSフィードをパース
                feed = feedparser.parse(xml_content)

                print(f"RSSフィードから {len(feed.entries)} 件の記事を取得")

                # 記事情報を抽出
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

                    print(f"  dc_date: {dc_date}")
                    print(f"  published: {published}")
                    print(f"  updated: {updated}")
                    print(f"  jdate: {jdate}")

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
                        try:
                            dt = datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                            entry_date = dt.date()
                            print(f"  パースされた日付: {entry_date}")
                        except Exception as e:
                            print(f"  ISO8601パースエラー: {e}")
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
                        'dc_date': dc_date,
                        'jdate': jdate,
                        'content': ''
                    }
                    articles.append(article)
                    print(f"  ✓ 記事を追加")

                print(f"\n{len(articles)}件の本日分の記事を取得しました")
                return articles

            else:
                print("SafariからRSSフィードを取得できませんでした")
                return []

        except Exception as e:
            print(f"Safari RSS取得エラー: {e}")
            return []

    def manual_login_prompt(self):
        """手動ログインの案内"""
        print("\n=== 手動ログインが必要です ===")
        print(f"1. Safariで {self.login_url} を開いてください")
        print("2. ログイン情報を入力してログインしてください")
        print("3. ログイン後、このプログラムを再実行してください")
        print("   ※ 既存のSafariウィンドウを使用します")

        input("\nログインが完了したら Enter キーを押してください...")
        # 手動ログイン後もキャッシュを保存
        self._save_cached_session()
        return True

    def fetch_rss_feed(self) -> List[Dict]:
        """RSSフィードを取得して本日分の記事情報のみ抽出"""
        try:
            print(f"RSSフィードを取得中: {self.rss_url}")

            # まずrequestsセッションで試行
            response = self.session.get(self.rss_url, timeout=30)
            response.raise_for_status()

            print(f"RSSレスポンスステータス: {response.status_code}")
            print(f"RSSレスポンスサイズ: {len(response.content)} bytes")

            # 生のXML内容を確認（デバッグ用）
            xml_content = response.content.decode('utf-8', errors='ignore')
            print(f"\n=== RSSフィードの最初の1000文字 ===")
            print(xml_content[:1000])
            print("=== RSSフィード内容終了 ===\n")

            # ログインが必要な場合のチェック
            if "ログイン" in xml_content or "login" in xml_content.lower() or len(xml_content) < 1000:
                print("ログインが必要なようです。Safariでスクレイピングを試行します...")
                return self.fetch_rss_with_safari()

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

            # まずrequestsセッションで試行
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

            # ログインが必要な場合のチェック
            if len(content) < 500 or "ログイン" in content or "login" in content.lower():
                print("ログインが必要なようです。Safariでスクレイピングを試行します...")
                return self.fetch_article_content_with_safari(url)

            return content[:5000]  # 長すぎる場合は切り詰め

        except Exception as e:
            print(f"記事内容取得エラー ({url}): {e}")
            return self.fetch_article_content_with_safari(url)

    def fetch_article_content_with_safari(self, url: str) -> str:
        """Safariで記事内容を取得（ログイン状態を維持）"""
        try:
            print(f"Safariで記事内容を取得中: {url}")
            
            # エスケープ処理
            escaped_url = url.replace('"', '\\"')

            # Safariで記事を開く（ログインセッションを維持したまま）
            apple_script = f'''
            tell application "Safari"
                activate
                
                -- ログイン済みのウィンドウ/タブを探す
                set foundLoggedIn to false
                set targetWindow to missing value
                
                repeat with w in windows
                    repeat with t in tabs of w
                        try
                            set tabURL to URL of t
                            if tabURL contains "mfd.jiho.jp" then
                                set foundLoggedIn to true
                                set targetWindow to w
                                exit repeat
                            end if
                        end try
                    end repeat
                    if foundLoggedIn then exit repeat
                end repeat
                
                -- ログイン済みウィンドウがあればそこで開く、なければ新規
                if foundLoggedIn and targetWindow is not missing value then
                    set current tab of targetWindow to make new tab at targetWindow
                    set URL of current tab of targetWindow to "{escaped_url}"
                else
                    -- 新規ウィンドウで開く
                    set newDoc to make new document
                    set URL of newDoc to "{escaped_url}"
                end if
                
                -- ページの読み込みを長めに待つ（認証やリダイレクトがある場合）
                delay 8
                
                -- 現在のドキュメントのソースを取得
                set articleContent to source of front document
                return articleContent
            end tell
            '''

            result = subprocess.run(
                ['osascript', '-e', apple_script],
                capture_output=True, text=True
            )

            if result.returncode == 0 and result.stdout.strip():
                html_content = result.stdout.strip()
                
                # ログインページにリダイレクトされていないかチェック
                if "ログイン" in html_content[:500] or "login" in html_content[:500].lower():
                    print("ログインページが表示されています。ブラウザで手動ログインが必要です。")
                    return self.fetch_article_with_manual_safari(url)
                
                print("Safariから記事内容を取得しました")
                soup = BeautifulSoup(html_content, 'html.parser')

                # MEDIFAXの記事構造に特化したセレクタ
                content_selectors = [
                    '.article-detail',  # MEDIFAX特有
                    '.article-body',
                    '.article-content', 
                    '.main-content',
                    'article',
                    '.post-content',
                    '.entry-content',
                    'main',
                    '#content',
                    '.content'
                ]

                content = ""
                for selector in content_selectors:
                    element = soup.select_one(selector)
                    if element:
                        content = element.get_text(strip=True)
                        if len(content) > 100:  # 有効なコンテンツか確認
                            break

                # セレクタで見つからない場合はbody全体から抽出
                if not content or len(content) < 100:
                    # 不要な要素を削除
                    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'menu', 'button']):
                        tag.decompose()
                    content = soup.get_text(strip=True)

                # コンテンツが短すぎる場合は手動取得を促す
                if len(content) < 200:
                    print(f"取得したコンテンツが短すぎます（{len(content)}文字）。手動取得を試みます。")
                    return self.fetch_article_with_manual_safari(url)

                return content[:5000]  # 長すぎる場合は切り詰め

            else:
                print("Safariから記事内容を取得できませんでした")
                return self.fetch_article_with_manual_safari(url)

        except Exception as e:
            print(f"Safari記事内容取得エラー ({url}): {e}")
            return self.fetch_article_with_manual_safari(url)
    
    def fetch_article_with_manual_safari(self, url: str) -> str:
        """Safariで記事を開いて手動で内容を確認してもらう"""
        try:
            print(f"\n=== 手動での記事確認が必要です ===")
            print(f"URL: {url}")
            
            # Safariで記事を開く
            escaped_url = url.replace('"', '\\"')
            apple_script = f'''
            tell application "Safari"
                activate
                open location "{escaped_url}"
            end tell
            '''
            
            subprocess.run(['osascript', '-e', apple_script])
            
            print("\n1. Safariで記事が開きました")
            print("2. 必要に応じてログインしてください")
            print("3. 記事が表示されたら、Enterキーを押してください")
            print("   ※ 記事の内容を自動的に取得します\n")
            
            input("準備ができたらEnterキーを押してください...")
            
            # 現在表示されているページのソースを取得
            apple_script_get = '''
            tell application "Safari"
                set pageSource to source of front document
                return pageSource
            end tell
            '''
            
            result = subprocess.run(
                ['osascript', '-e', apple_script_get],
                capture_output=True, text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                html_content = result.stdout.strip()
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # コンテンツ抽出
                content_selectors = [
                    '.article-detail',
                    '.article-body',
                    '.article-content',
                    '.main-content',
                    'article',
                    'main',
                    '.content'
                ]
                
                content = ""
                for selector in content_selectors:
                    element = soup.select_one(selector)
                    if element:
                        content = element.get_text(strip=True)
                        if len(content) > 100:
                            break
                
                if not content or len(content) < 100:
                    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'menu', 'button']):
                        tag.decompose()
                    content = soup.get_text(strip=True)
                
                if content and len(content) > 100:
                    print(f"記事内容を取得しました（{len(content)}文字）")
                    return content[:5000]
                else:
                    print("記事内容の取得に失敗しました")
                    return "記事内容を自動取得できませんでした。手動で確認が必要です。"
            
            return "記事内容を取得できませんでした。"
            
        except Exception as e:
            print(f"手動取得エラー: {e}")
            return f"記事取得エラー: {e}"

    def summarize_article(self, title: str, content: str) -> str:
        """Geminiで記事を要約"""
        try:
            prompt = f"""
以下の医療情報記事を読みやすく整理し、詳細な解説と要約を提供してください。

タイトル: {title}

記事内容:
{content}

出力形式:
【概要】
記事の内容を1-2段落で簡潔に説明

【重要ポイント】
• ポイント1
• ポイント2
• ポイント3
（医療・病院経営に関連する重要な内容を箇条書きで）

【詳細解説】
記事の重要な部分について、背景や意味を含めて詳しく解説
（読みやすいように段落を分けて記載）

【実務への影響】
• 病院運営への影響
• 医療従事者が注意すべき点
• 今後予想される変化

【まとめ】
記事全体の要点を1段落でまとめる

注意事項:
- 専門用語は必要に応じて説明を加える
- 数値や日付などの具体的な情報は正確に記載
- 読みやすいように適切に改行を入れる
- 医療関係者にとって実用的な情報を重視
"""
            return gemini.summarize(prompt)

        except Exception as e:
            return f"要約エラー: {e}"

    def save_digest(self, articles: List[Dict]):
        """記事情報をファイルに保存（記事内容を取得して要約を含める）"""
        today = datetime.date.today()
        # ファイル名を修正
        md_file = self.output_dir / f"medifax_digest_{today}.md"
        txt_file = self.output_dir / f"medifax_digest_{today}.txt"

        # 内容を作成
        content_lines = []
        content_lines.append(f"医療情報ダイジェスト - {today}")
        content_lines.append("=" * 80)
        content_lines.append(f"取得日時: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        content_lines.append("=" * 80)
        content_lines.append("")

        for i, article in enumerate(articles, 1):
            print(f"\n記事 {i}/{len(articles)} を処理中: {article['title']}")

            # 記事内容を取得
            content = self.fetch_article_content(article['link'])

            # 内容を要約
            if content:
                summary = self.summarize_article(article['title'], content)
            else:
                summary = "記事内容を取得できませんでした。"

            # 新しいフォーマットで出力
            content_lines.append(f"【記事 {i}】")
            content_lines.append("")
            content_lines.append("タイトル：")
            content_lines.append(article['title'])
            content_lines.append("")
            content_lines.append("解説と要約：")
            content_lines.append(summary)
            content_lines.append("")
            content_lines.append("URL：")
            content_lines.append(article['link'])
            content_lines.append("")
            content_lines.append("-" * 80)
            content_lines.append("")

        # MDファイルとして保存
        with open(md_file, 'w', encoding='utf-8') as f:
            # Markdown版
            f.write(f"# 医療情報ダイジェスト - {today}\n\n")
            f.write(f"取得日時: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("=" * 80 + "\n\n")

            for i, article in enumerate(articles, 1):
                # MDファイルには既に取得済みの要約を使用
                idx = content_lines.index(f"【記事 {i}】")
                title_idx = content_lines.index("タイトル：", idx) + 1
                summary_idx = content_lines.index("解説と要約：", idx) + 1
                url_idx = content_lines.index("URL：", idx) + 1

                f.write(f"## 記事 {i}\n\n")
                f.write(f"**タイトル：**\n{content_lines[title_idx]}\n\n")

                # 要約部分を取得
                summary_end_idx = content_lines.index("URL：", summary_idx)
                summary_text = "\n".join(content_lines[summary_idx:summary_end_idx-1])
                f.write(f"**解説と要約：**\n{summary_text}\n\n")
                f.write(f"**URL：**\n{content_lines[url_idx]}\n\n")
                f.write("-" * 80 + "\n\n")

        # TXTファイルとして保存（Teams用、UTF-8 with BOM）
        with open(txt_file, 'w', encoding='utf-8-sig') as f:
            f.write("\n".join(content_lines))

        print(f"\nMDファイルを保存: {md_file}")
        print(f"TXTファイルを保存: {txt_file}")

        # 月別フォルダへの移動処理
        self.move_to_monthly_folder(md_file, today)
        self.move_to_monthly_folder(txt_file, today)

        return txt_file  # Teams送信用にTXTファイルを返す

    def move_to_monthly_folder(self, file_path: Path, date: datetime.date):
        """前月作成のファイルのみ月別フォルダに移動。今月作成のファイルは移動しない"""
        try:
            # ファイルの作成日を取得
            stat = file_path.stat()
            created_dt = datetime.datetime.fromtimestamp(stat.st_mtime)
            created_date = created_dt.date()
            # 今月の1日
            first_day_of_this_month = datetime.date(date.year, date.month, 1)
            # 前月の1日
            if date.month == 1:
                prev_month = 12
                prev_year = date.year - 1
            else:
                prev_month = date.month - 1
                prev_year = date.year
            first_day_of_prev_month = datetime.date(prev_year, prev_month, 1)
            first_day_of_next_month = (first_day_of_this_month + datetime.timedelta(days=32)).replace(day=1)

            # 作成日が前月に該当する場合のみ移動
            if first_day_of_prev_month <= created_date < first_day_of_this_month:
                monthly_folder = self.output_dir / f"{prev_year:04d}-{prev_month:02d}"
                monthly_folder.mkdir(parents=True, exist_ok=True)
                new_file_path = monthly_folder / file_path.name
                file_path.rename(new_file_path)
                print(f"ファイルを前月フォルダに移動: {new_file_path}")
            else:
                print("今月作成のファイルのため移動しません")
        except Exception as e:
            print(f"月別フォルダへの移動エラー: {e}")
            # エラーが発生しても元のファイルは残す

    def send_to_teams(self, articles: List[Dict], file_path: Path):
        """Teamsのチャンネルに @一般 メンション付きでメッセージを投稿し、ファイルをアップロードしてリンクを挿入"""
        try:
            # teams.pyのtoken_cacheの仕組みを参考にaccess_tokenを取得
            import teams
            # MSALのPublicClientApplicationとキャッシュを利用
            app = teams.app
            accounts = app.get_accounts()
            result = None
            if accounts:
                # 既存アカウントでサイレント認証
                result = app.acquire_token_silent(teams.SCOPES, account=accounts[0])
            if not result:
                print("Teams認証: サイレント認証に失敗しました。手動で認証してください。")
                flow = app.initiate_device_flow(scopes=teams.SCOPES)
                if "user_code" not in flow:
                    raise Exception("デバイスフローの初期化に失敗しました")
                print(flow["message"])
                result = app.acquire_token_by_device_flow(flow)
            if "access_token" not in result:
                raise Exception("アクセストークンの取得に失敗しました: {}".format(result.get("error_description")))
            access_token = result["access_token"]

            team_id    = os.environ["TEAMS_TARGET_TEAM_ID"]    # 対象Team
            channel_id = os.environ["TEAMS_TARGET_CHANNEL_ID"] # 対象Channel（一般 など）

            today = datetime.date.today()

            # ------------------------------
            # 1) チャンネルのFilesフォルダを取得 → その配下にファイルをアップロード
            # ------------------------------
            base = "https://graph.microsoft.com/v1.0"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }

            # チャンネルのFilesフォルダ情報を取得
            r = requests.get(f"{base}/teams/{team_id}/channels/{channel_id}/filesFolder", headers=headers)
            r.raise_for_status()
            files_folder = r.json()
            drive_id = files_folder["parentReference"]["driveId"]
            parent_item_id = files_folder["id"]

            # アップロード（小～中サイズファイル想定。大きい場合はUploadSession推奨）
            upload_headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/octet-stream"
            }
            file_name = file_path.name

            with open(file_path, "rb") as f:
                ur = requests.put(
                    f"{base}/drives/{drive_id}/items/{parent_item_id}:/{file_name}:/content",
                    headers=upload_headers,
                    data=f
                )
            ur.raise_for_status()
            uploaded = ur.json()
            file_web_url = uploaded["webUrl"]  # SharePoint上のWeb URL

            # ------------------------------
            # 2) HTML本文を生成（<at id="0">一般</at> + 記事一覧 + ファイルリンク）
            # ------------------------------
            content_parts = []
            content_parts.append(f"<h2>本日の医療情報ダイジェストを作成しました</h2>")
            content_parts.append("<at id='0'>一般</at><br/>")
            content_parts.append(f"<strong>📅 日付:</strong> {today}<br/>")
            content_parts.append(f"<strong>📊 取得記事数:</strong> {len(articles)}件<br/>")
            content_parts.append("<br/>")
            content_parts.append("<strong>📰 本日の記事一覧:</strong><br/>")
            content_parts.append("<br/>")

            for i, article in enumerate(articles, 1):
                title = article.get("title", "(無題)")
                url = article.get("url")
                if url:
                    content_parts.append(f"{i}. <a href=\"{url}\">{title}</a><br/>")
                else:
                    content_parts.append(f"{i}. {title}<br/>")

            content_parts.append("<br/>")
            content_parts.append("<strong>📎 詳細な解説と要約は以下のファイルをご確認ください。</strong><br/>")
            content_parts.append(f"<a href=\"{file_web_url}\">{file_name}</a><br/>")
            content = "".join(content_parts)

            # ------------------------------
            # 3) mentions 配列を付けてメッセージを投稿
            #    ※ <at id='0'> の "0" と下記 mentions[].id を一致させる
            # ------------------------------
            payload = {
                "body": {
                    "contentType": "html",
                    "content": content
                },
                "mentions": [
                    {
                        "id": 0,
                        "mentionText": "一般",
                        "mentioned": {
                            "conversation": {
                                "id": channel_id,
                                "displayName": "一般"
                            }
                        }
                    }
                ]
            }

            mr = requests.post(
                f"{base}/teams/{team_id}/channels/{channel_id}/messages",
                headers=headers,
                json=payload
            )
            mr.raise_for_status()

            print("Teamsにメッセージを送信しました")

        except KeyError as ke:
            print(f"環境変数が未設定です: {ke}. 必要: TEAMS_TARGET_TEAM_ID, TEAMS_TARGET_CHANNEL_ID")
        except requests.HTTPError as he:
            # Graphからの詳細エラーを可視化
            try:
                err_detail = he.response.json()
            except Exception:
                err_detail = he.response.text
            print(f"Teams送信エラー (HTTP): {he} | 詳細: {err_detail}")
        except Exception as e:
            print(f"Teams送信エラー: {e}")

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

        # 3. 結果を保存（要約・jsonは出力しない）
        txt_file = self.save_digest(articles)

        # 4. Teamsに送信
        self.send_to_teams(articles, txt_file)

        # 5. TXTファイルを削除（Teams送信後）
        try:
            if txt_file.exists():
                txt_file.unlink()
                print(f"TXTファイルを削除しました: {txt_file}")
        except Exception as e:
            print(f"TXTファイル削除エラー: {e}")

        print(f"\n処理完了: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"処理した記事数: {len(articles)}")


def main():
    """メイン関数"""
    digest = MedifaxAutoLogin()
    digest.run()


if __name__ == "__main__":
    main()