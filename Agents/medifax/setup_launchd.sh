#!/bin/bash

# Medifax Digest LaunchDaemon セットアップスクリプト

echo "==========================================="
echo "Medifax Digest 自動実行セットアップ"
echo "==========================================="
echo ""

# 設定ファイルのパス
PLIST_FILE="/Users/ueshima/Workspace/Mac for Business/Agents/medifax/com.medifax.digest.plist"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
TARGET_PLIST="$LAUNCH_AGENTS_DIR/com.medifax.digest.plist"

# LaunchAgentsディレクトリが存在しない場合は作成
if [ ! -d "$LAUNCH_AGENTS_DIR" ]; then
    echo "LaunchAgentsディレクトリを作成しています..."
    mkdir -p "$LAUNCH_AGENTS_DIR"
fi

# 既存のジョブがある場合は停止してアンロード
if [ -f "$TARGET_PLIST" ]; then
    echo "既存のジョブを停止しています..."
    launchctl unload "$TARGET_PLIST" 2>/dev/null
    launchctl remove com.medifax.digest 2>/dev/null
fi

# plistファイルをコピー
echo "設定ファイルをインストールしています..."
cp "$PLIST_FILE" "$TARGET_PLIST"

# 権限を設定
chmod 644 "$TARGET_PLIST"

# ログディレクトリを作成
LOG_DIR="/Users/ueshima/Workspace/Mac for Business/Agents/medifax/logs"
if [ ! -d "$LOG_DIR" ]; then
    echo "ログディレクトリを作成しています..."
    mkdir -p "$LOG_DIR"
fi

# ジョブをロード
echo "ジョブを登録しています..."
launchctl load "$TARGET_PLIST"

# 登録確認
if launchctl list | grep -q "com.medifax.digest"; then
    echo ""
    echo "✅ セットアップが完了しました！"
    echo ""
    echo "設定内容:"
    echo "  - 実行時間: 平日（月〜金）8:00"
    echo "  - ログファイル: $LOG_DIR"
    echo ""
    echo "コマンド一覧:"
    echo "  状態確認:    launchctl list | grep medifax"
    echo "  手動実行:    launchctl start com.medifax.digest"
    echo "  停止:        launchctl stop com.medifax.digest"
    echo "  無効化:      launchctl unload ~/Library/LaunchAgents/com.medifax.digest.plist"
    echo "  再有効化:    launchctl load ~/Library/LaunchAgents/com.medifax.digest.plist"
    echo ""
else
    echo ""
    echo "❌ セットアップに失敗しました"
    echo "エラーログを確認してください: $LOG_DIR/stderr.log"
fi