#!/usr/bin/env python3
"""
自動スケジュール同期プログラム
アップルスクリプトを実行してCSVファイルがダウンロードされたら自動的にGoogleカレンダーに同期
"""

import os
import time
import subprocess
import glob
from pathlib import Path
from datetime import datetime
import logging
from gs_schedule_to_google import get_latest_schedule_csv, parse_csv_schedule, insert_events_to_google_calendar
import datetime

print(f"処理開始：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
# logsディレクトリ作成
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, 'auto_schedule_sync.log')

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AutoScheduleSync:
    def __init__(self):
        # OneDrive上のファイルを/Users/ueshima/Scripts/にコピーしてから実行する
        original_applescript_path = "/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/00_Automate/groupsession_schedule_to_google.scpt"
        self.applescript_path = "/Users/ueshima/Scripts/groupsession_schedule_to_google.scpt"
        # コピー処理（初期化時に毎回上書きコピー）
        try:
            import shutil
            shutil.copy2(original_applescript_path, self.applescript_path)
            os.chmod(self.applescript_path, 0o755)  # 実行権限付与
        except Exception as e:
            logger.error(f"AppleScriptのコピーまたは権限付与に失敗: {e}")
        
        self.download_dir = os.path.expanduser("~/Downloads")
        self.last_processed_file = None
        self.last_processed_time = None
        
    def run_applescript(self):
        """アップルスクリプトを実行"""
        try:
            logger.info("アップルスクリプトを実行中...")
            result = subprocess.run(['osascript', self.applescript_path], 
                                 capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                logger.info("アップルスクリプトが正常に完了しました")
                if result.stdout.strip():
                    logger.info(f"スクリプト出力: {result.stdout.strip()}")
                return True
            else:
                logger.error(f"アップルスクリプトが失敗しました: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            logger.error("アップルスクリプトがタイムアウトしました")
            return False
        except Exception as e:
            logger.error(f"アップルスクリプト実行エラー: {e}")
            return False
    
    def wait_for_csv_file(self, timeout=300):
        """CSVファイルがダウンロードされるまで待機"""
        logger.info("CSVファイルのダウンロードを待機中...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                files = glob.glob(os.path.join(self.download_dir, "scheduleList-*.csv"))
                if files:
                    latest_file = max(files, key=os.path.getmtime)
                    file_time = os.path.getmtime(latest_file)
                    
                    # 新しいファイルかチェック
                    if (self.last_processed_file != latest_file or 
                        self.last_processed_time != file_time):
                        logger.info(f"新しいCSVファイルを検出: {latest_file}")
                        return latest_file
                        
            except Exception as e:
                logger.error(f"ファイル監視エラー: {e}")
                
            time.sleep(5)  # 5秒間隔でチェック
            
        logger.warning(f"タイムアウト: {timeout}秒以内にCSVファイルが見つかりませんでした")
        return None
    
    def process_csv_file(self, csv_path):
        """CSVファイルを処理してGoogleカレンダーに同期"""
        try:
            logger.info(f"CSVファイルを処理中: {csv_path}")
            
            # ファイルの内容を解析
            events = parse_csv_schedule(csv_path)
            
            if not events:
                logger.warning("処理するイベントが見つかりませんでした")
                return False
            
            # Googleカレンダーに同期
            insert_events_to_google_calendar(events)
            
            # 処理済みとして記録
            self.last_processed_file = csv_path
            self.last_processed_time = os.path.getmtime(csv_path)
            
            logger.info(f"同期完了: {len(events)}件のイベントを処理しました")
            return True
            
        except Exception as e:
            logger.error(f"CSVファイル処理エラー: {e}")
            return False
    
    def run_sync_cycle(self):
        """1回の同期サイクルを実行"""
        logger.info("=== 同期サイクル開始 ===")
        
        # 1. アップルスクリプトを実行
        if not self.run_applescript():
            logger.error("アップルスクリプトの実行に失敗しました")
            return False
        
        # 2. CSVファイルのダウンロードを待機
        csv_path = self.wait_for_csv_file()
        if not csv_path:
            logger.error("CSVファイルのダウンロードが確認できませんでした")
            return False
        
        # 3. CSVファイルを処理してGoogleカレンダーに同期
        if not self.process_csv_file(csv_path):
            logger.error("CSVファイルの処理に失敗しました")
            return False
        
        logger.info("=== 同期サイクル完了 ===")
        return True
    
    def run_continuous(self, interval=3600):
        """継続的に同期を実行"""
        logger.info(f"自動同期を開始します（間隔: {interval}秒）")
        
        while True:
            try:
                self.run_sync_cycle()
                logger.info(f"次の同期まで {interval}秒 待機します...")
                time.sleep(interval)
                
            except KeyboardInterrupt:
                logger.info("ユーザーによって停止されました")
                break
            except Exception as e:
                logger.error(f"予期しないエラー: {e}")
                logger.info("30秒後に再試行します...")
                time.sleep(30)

def main():
    """メイン関数"""
    sync = AutoScheduleSync()
    
    # コマンドライン引数の処理
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--once":
            # 1回だけ実行
            success = sync.run_sync_cycle()
            sys.exit(0 if success else 1)
        elif sys.argv[1] == "--interval":
            # 指定された間隔で継続実行
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 3600
            sync.run_continuous(interval)
        else:
            print("使用方法:")
            print("  python auto_schedule_sync.py --once     # 1回だけ実行")
            print("  python auto_schedule_sync.py --interval [秒数]  # 継続実行")
            sys.exit(1)
    else:
        # デフォルト: 1回だけ実行
        success = sync.run_sync_cycle()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 