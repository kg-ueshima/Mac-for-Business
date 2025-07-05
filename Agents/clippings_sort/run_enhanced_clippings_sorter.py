#!/usr/bin/env python3
"""
Enhanced ClippingsSorting Agent 実行スクリプト
テーマ別永続ノート、インデックス、構造化ファイルを作成
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import logging

# プロジェクトルートをパスに追加（clippings_sortフォルダから2階層上）
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from enhanced_clippings_sorter import EnhancedClippingsSorter

# ログ設定
def setup_logging():
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"enhanced_clippings_sorter_{datetime.now().strftime('%Y%m%d')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return logging.getLogger(__name__)

def main():
    """メイン実行関数"""
    logger = setup_logging()
    
    try:
        logger.info("Enhanced ClippingsSorting Agent 開始")
        
        # エージェントを実行（プロジェクトルートを指定）
        sorter = EnhancedClippingsSorter(str(project_root))
        sorter.run()
        
        logger.info("Enhanced ClippingsSorting Agent 正常完了")
        
    except Exception as e:
        logger.error(f"Enhanced ClippingsSorting Agent エラー: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 