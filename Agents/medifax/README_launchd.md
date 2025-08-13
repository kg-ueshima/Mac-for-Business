# Medifax Digest 自動実行設定

## 概要
medifax_auto_login.pyを平日8:00に自動実行するためのmacOS launchd設定です。

## ファイル構成

```
Agents/medifax/
├── medifax_auto_login.py      # メインのPythonスクリプト
├── run_medifax_digest.sh      # 実行用ラッパースクリプト
├── com.medifax.digest.plist   # launchd設定ファイル
├── setup_launchd.sh           # セットアップスクリプト
├── README_launchd.md          # このドキュメント
└── logs/                      # ログファイル保存ディレクトリ
    ├── medifax_digest_*.log   # 実行ログ
    ├── stdout.log             # 標準出力
    └── stderr.log             # エラー出力
```

## セットアップ方法

### 1. 自動セットアップ（推奨）

```bash
cd "/Users/ueshima/Workspace/Mac for Business/Agents/medifax"
./setup_launchd.sh
```

### 2. 手動セットアップ

```bash
# plistファイルをLaunchAgentsディレクトリにコピー
cp com.medifax.digest.plist ~/Library/LaunchAgents/

# 権限を設定
chmod 644 ~/Library/LaunchAgents/com.medifax.digest.plist

# ジョブを登録
launchctl load ~/Library/LaunchAgents/com.medifax.digest.plist
```

## 実行スケジュール

- **実行時間**: 平日（月〜金）8:00
- **実行内容**:
  1. Python仮想環境をアクティベート
  2. medifax_auto_login.pyを実行
  3. 医療情報RSSフィードを取得・要約
  4. Teamsに通知を送信

## 管理コマンド

### ジョブの状態確認
```bash
launchctl list | grep medifax
```

### 手動実行（テスト用）
```bash
launchctl start com.medifax.digest
```

### ジョブの停止
```bash
launchctl stop com.medifax.digest
```

### ジョブの無効化
```bash
launchctl unload ~/Library/LaunchAgents/com.medifax.digest.plist
```

### ジョブの再有効化
```bash
launchctl load ~/Library/LaunchAgents/com.medifax.digest.plist
```

### ジョブの完全削除
```bash
launchctl unload ~/Library/LaunchAgents/com.medifax.digest.plist
launchctl remove com.medifax.digest
rm ~/Library/LaunchAgents/com.medifax.digest.plist
```

## ログファイル

ログは以下の場所に保存されます：

- **実行ログ**: `logs/medifax_digest_YYYYMMDD_HHMMSS.log`
- **標準出力**: `logs/stdout.log`
- **エラー出力**: `logs/stderr.log`

### ログの確認方法

```bash
# 最新の実行ログを確認
ls -la logs/medifax_digest_*.log | tail -1

# エラーログを確認
tail -f logs/stderr.log

# 今日の実行ログを確認
cat logs/medifax_digest_$(date +%Y%m%d)*.log
```

## トラブルシューティング

### ジョブが実行されない場合

1. ジョブが登録されているか確認
```bash
launchctl list | grep medifax
```

2. plistファイルの構文を確認
```bash
plutil -lint ~/Library/LaunchAgents/com.medifax.digest.plist
```

3. 実行権限を確認
```bash
ls -la run_medifax_digest.sh
# 実行権限がない場合
chmod +x run_medifax_digest.sh
```

4. Python仮想環境の存在を確認
```bash
ls -la "/Users/ueshima/Workspace/Mac for Business/.venv"
```

### エラーが発生する場合

1. エラーログを確認
```bash
cat logs/stderr.log
```

2. 環境変数の設定を確認
```bash
cat "/Users/ueshima/Workspace/Mac for Business/env.local"
```

3. 手動でスクリプトを実行してテスト
```bash
cd "/Users/ueshima/Workspace/Mac for Business"
./Agents/medifax/run_medifax_digest.sh
```

### Macの通知が表示されない場合

システム環境設定 > 通知とフォーカス で、ターミナルまたはスクリプトエディタの通知が有効になっているか確認してください。

## 注意事項

- Macがスリープ状態の場合、ジョブは実行されません
- システム起動時には自動実行されません（RunAtLoad=false）
- ログファイルは定期的に削除することをお勧めします
- 環境変数（MEDIFAX_USERNAME、MEDIFAX_PASSWORD等）が正しく設定されている必要があります

## 関連ファイル

- `medifax_auto_login.py`: メインスクリプト
- `env.local`: 環境変数設定ファイル（要事前設定）
- `.cache/`: ログインキャッシュディレクトリ

===========================================
Medifax Digest 自動実行セットアップ
===========================================

設定ファイルをインストールしています...
ログディレクトリを作成しています...
ジョブを登録しています...

✅ セットアップが完了しました！

設定内容:
  - 実行時間: 平日（月〜金）8:00
  - ログファイル: /Users/ueshima/Workspace/Mac for Business/Agents/medifax/logs

コマンド一覧:
  状態確認:    launchctl list | grep medifax
  手動実行:    launchctl start com.medifax.digest
  停止:        launchctl stop com.medifax.digest
  無効化:      launchctl unload ~/Library/LaunchAgents/com.medifax.digest.plist
  再有効化:    launchctl load ~/Library/LaunchAgents/com.medifax.digest.plist