# Teams通知機能

汎用的なTeams通知機能を提供するモジュールです。様々な通知機能で再利用可能です。

## 機能

- 基本的なメッセージ送信
- タイトル付き通知送信
- 環境変数による送信先設定
- 利用可能なチーム・チャンネル一覧表示
- トークンキャッシュ機能

## セットアップ

### 1. 環境変数の設定

`env.local`ファイルに以下を設定してください：

```bash
# Microsoft Graph API設定
MICROSOFT_CLIENT_ID=your_client_id
MICROSOFT_TENANT_ID=your_tenant_id

# Teams送信先設定（オプション）
TEAMS_TARGET_TEAM_ID=your_team_id
TEAMS_TARGET_CHANNEL_ID=your_channel_id
```

### 2. Microsoft Graph APIの設定

1. [Azure Portal](https://portal.azure.com)でアプリケーションを登録
2. 以下のスコープを追加：
   - `Channel.ReadBasic.All`
   - `ChannelMessage.Read.All`
   - `Chat.Read`
   - `User.Read`
   - `User.ReadBasic.All`
   - `ChannelMessage.Send`
   - `Team.ReadBasic.All`

## 使用方法

### 基本的な使用方法

```python
import teams_notification

# 簡単な通知送信
success = teams_notification.send_teams_notification(
    title="テスト通知",
    content="これはテストメッセージです。"
)

# 簡単なメッセージ送信
success = teams_notification.send_teams_message(
    "これはプレーンテキストのメッセージです。"
)
```

### クラスを使用した詳細な制御

```python
from teams_notification import TeamsNotifier

# 通知クラスのインスタンス作成
notifier = TeamsNotifier()

# 利用可能な送信先を表示
notifier.list_available_targets()

# 特定のチーム・チャンネルに送信
success = notifier.send_notification(
    title="エラー通知",
    content="システムエラーが発生しました。",
    team_id="specific_team_id",
    channel_id="specific_channel_id"
)
```

### 送信先の指定方法

1. **環境変数による指定**（推奨）
   ```bash
   TEAMS_TARGET_TEAM_ID=your_team_id
   TEAMS_TARGET_CHANNEL_ID=your_channel_id
   ```

2. **引数による指定**
   ```python
   success = teams_notification.send_teams_notification(
       title="通知",
       content="内容",
       team_id="team_id",
       channel_id="channel_id"
   )
   ```

3. **自動選択**
   - 環境変数が設定されていない場合、最初のチームの最初のチャンネルが自動選択されます

## 使用例

### エラー通知

```python
import teams_notification

error_content = """
**エラーが発生しました**

- **エラー種別**: データベース接続エラー
- **発生時刻**: 2025-01-15 14:30:25
- **影響範囲**: ユーザー認証機能
- **対応状況**: 調査中
"""

teams_notification.send_teams_notification(
    title="⚠️ エラー通知",
    content=error_content
)
```

### 日次レポート

```python
import teams_notification
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
report_content = f"""
**本日の業務サマリー**

✅ **完了タスク**
- システムメンテナンス完了
- データバックアップ実行

📋 **進行中タスク**
- 新機能開発（進捗: 75%）

**統計情報**
- 処理件数: 1,234件
- エラー件数: 2件
"""

teams_notification.send_teams_notification(
    title=f"📊 日次レポート - {today}",
    content=report_content
)
```

### システム通知

```python
import teams_notification

teams_notification.send_teams_notification(
    title="システム通知",
    content="バックアップが正常に完了しました。"
)
```

## テスト

### 利用可能な送信先の確認

```bash
python Agents/daily_report/modules/teams_notification.py
```

### 使用例の実行

```bash
python Agents/daily_report/modules/teams_notification_example.py
```

## 注意事項

1. **初回実行時**: Microsoft Graph APIの認証が必要です。ブラウザで認証コードを入力してください。

2. **トークンキャッシュ**: 認証トークンは`teams_token_cache.bin`ファイルに保存されます。

3. **送信先の確認**: 初回実行時に利用可能なチーム・チャンネルが表示されるので、適切な送信先を環境変数で設定してください。

4. **権限**: メッセージ送信には`ChannelMessage.Send`権限が必要です。

## トラブルシューティング

### 認証エラー

```
トークン取得失敗: {'error': 'invalid_grant'}
```

→ トークンキャッシュファイルを削除して再認証してください。

### 送信エラー

```
メッセージ送信エラー: 403 - Forbidden
```

→ アプリケーションに`ChannelMessage.Send`権限が付与されているか確認してください。

### 送信先が見つからない

```
送信先のチーム・チャンネルが見つかりませんでした
```

→ 利用可能なチーム・チャンネルを確認し、正しいIDを設定してください。

## 他の機能との連携

### 医療情報ダイジェスト

```python
# medifax_auto_login.pyで使用例
import teams_notification

def send_medical_digest(articles, file_path):
    content = f"本日取得した記事数: {len(articles)}件\n\n"
    # ... 記事内容の作成 ...
    
    teams_notification.send_teams_notification(
        title=f"医療情報ダイジェスト - {today}",
        content=content
    )
```

### 日次レポート

```python
# daily_reportで使用例
import teams_notification

def send_daily_report(report_content):
    teams_notification.send_teams_notification(
        title="日次業務レポート",
        content=report_content
    )
```

### エラー監視

```python
# エラー監視システムで使用例
import teams_notification

def send_error_alert(error_info):
    teams_notification.send_teams_notification(
        title="🚨 システムエラー",
        content=error_info
    )
```
