#!/bin/bash

# 実行時のログを記録
LOG_DIR="/Users/ueshima/Workspace/Mac for Business/Agents/medifax/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/medifax_digest_$(date +%Y%m%d_%H%M%S).log"

echo "===========================================" >> "$LOG_FILE"
echo "Medifax Digest 実行開始: $(date)" >> "$LOG_FILE"
echo "===========================================" >> "$LOG_FILE"

# 作業ディレクトリに移動
cd "/Users/ueshima/Workspace/Mac for Business" || exit 1

# Python仮想環境をアクティベート
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "Python仮想環境をアクティベートしました" >> "$LOG_FILE"
else
    echo "エラー: Python仮想環境が見つかりません" >> "$LOG_FILE"
    exit 1
fi

# Pythonスクリプトを実行
echo "medifax_auto_login.pyを実行中..." >> "$LOG_FILE"
python3 Agents/medifax/medifax_auto_login.py >> "$LOG_FILE" 2>&1

# 実行結果を記録
if [ $? -eq 0 ]; then
    echo "正常に完了しました: $(date)" >> "$LOG_FILE"
else
    echo "エラーが発生しました: $(date)" >> "$LOG_FILE"
    # エラー通知（必要に応じて）
    osascript -e 'display notification "Medifax Digest の実行でエラーが発生しました" with title "Medifax Digest"'
fi

echo "===========================================" >> "$LOG_FILE"
echo "Medifax Digest 実行終了: $(date)" >> "$LOG_FILE"
echo "===========================================" >> "$LOG_FILE"