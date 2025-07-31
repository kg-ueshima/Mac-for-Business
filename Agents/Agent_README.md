#!/bin/bash
# @Agents/Agent_README.md
# このファイルにカーソルを合わせて「@」で実行できるようにする

cd '/Users/ueshima/Workspace/Mac for Business'

# Python仮想環境の有効化
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

# 平日毎朝出勤時に実行するスクリプト
python3 Agents/schedule_updater/auto_schedule_sync.py
python3 Agents/daily_report/main.py

# バックアップの実行
rsync -avh --delete --exclude '.git' --exclude '.venv' --exclude '.obsidian' '/Users/ueshima/Workspace/Mac for Business/' '/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/Mac for Business-backup' 


# 自宅環境用
rsync -avh --delete --exclude '.git' --exclude '.venv' --exclude '.obsidian' '/Users/ueshima/Workspace/Mac for Private/' '/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/Mac for Business-backup' 