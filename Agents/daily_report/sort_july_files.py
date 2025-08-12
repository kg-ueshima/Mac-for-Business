import os
import shutil
from datetime import datetime
from pathlib import Path

def get_july_files(base_dir="80-業務日報"):
    """7月分の日報とその日のやり取りファイルを取得"""
    base_path = Path(base_dir)
    july_files = []
    
    # 7月分のファイルを検索
    for file_path in base_path.glob("2025-07-*"):
        if file_path.is_file():
            # 日報またはその日のやり取りファイルかチェック
            if "_日報.txt" in file_path.name or "_その日のやり取り.txt" in file_path.name:
                # 日付を抽出
                date_str = file_path.name.split("_")[0]
                try:
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    july_files.append((date_str, str(file_path)))
                except ValueError:
                    continue
    
    return sorted(july_files)

def move_files_to_monthly_folder(files):
    """ファイルを年月フォルダに移動する"""
    base_dir = Path("80-業務日報")
    
    for date_str, fpath in files:
        # 日付から年月を取得
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        year_month = date_obj.strftime("%Y-%m")
        
        # 年月フォルダを作成
        monthly_folder = base_dir / year_month
        monthly_folder.mkdir(exist_ok=True)
        
        # ファイルを移動
        source_path = Path(fpath)
        dest_path = monthly_folder / source_path.name
        
        try:
            shutil.move(str(source_path), str(dest_path))
            print(f"移動完了: {source_path.name} → {year_month}/")
        except Exception as e:
            print(f"移動エラー: {source_path.name} - {e}")

def main():
    print("7月分のファイルを仕分け中...")
    
    # 7月分のファイルを取得
    july_files = get_july_files()
    
    if not july_files:
        print("7月分のファイルが見つかりません。")
        return
    
    print(f"移動対象ファイル数: {len(july_files)}")
    
    # ファイルを移動
    move_files_to_monthly_folder(july_files)
    
    print("7月分のファイル仕分けが完了しました。")

if __name__ == "__main__":
    main()
