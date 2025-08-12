#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teams通知機能の使用例
様々な通知パターンを示すサンプルスクリプト
"""

import teams_notification
from datetime import datetime

def example_basic_notification():
    """基本的な通知の例"""
    print("=== 基本的な通知の例 ===")
    
    title = "システム通知"
    content = "これは基本的な通知メッセージです。\n\nシステムが正常に動作しています。"
    
    success = teams_notification.send_teams_notification(title, content)
    print(f"送信結果: {'成功' if success else '失敗'}")


def example_error_notification():
    """エラー通知の例"""
    print("\n=== エラー通知の例 ===")
    
    title = "⚠️ エラー通知"
    content = """
**エラーが発生しました**

- **エラー種別**: データベース接続エラー
- **発生時刻**: 2025-01-15 14:30:25
- **影響範囲**: ユーザー認証機能
- **対応状況**: 調査中

詳細なログは添付ファイルをご確認ください。
"""
    
    success = teams_notification.send_teams_notification(title, content)
    print(f"送信結果: {'成功' if success else '失敗'}")


def example_daily_report():
    """日次レポートの例"""
    print("\n=== 日次レポートの例 ===")
    
    today = datetime.now().strftime('%Y-%m-%d')
    title = f"📊 日次レポート - {today}"
    
    content = f"""
**本日の業務サマリー**

✅ **完了タスク**
- システムメンテナンス完了
- データバックアップ実行
- セキュリティパッチ適用

📋 **進行中タスク**
- 新機能開発（進捗: 75%）
- ドキュメント更新

⚠️ **注意事項**
- 明日の定期メンテナンス予定
- システム更新の準備が必要

**統計情報**
- 処理件数: 1,234件
- エラー件数: 2件
- 平均応答時間: 1.2秒
"""
    
    success = teams_notification.send_teams_notification(title, content)
    print(f"送信結果: {'成功' if success else '失敗'}")


def example_specific_channel():
    """特定のチャンネルへの送信例"""
    print("\n=== 特定チャンネルへの送信例 ===")
    
    # 環境変数で設定された送信先を使用
    title = "特定チャンネルテスト"
    content = "このメッセージは環境変数で設定された特定のチャンネルに送信されます。"
    
    # team_idとchannel_idをNoneにすると環境変数の値が使用される
    success = teams_notification.send_teams_notification(title, content, team_id=None, channel_id=None)
    print(f"送信結果: {'成功' if success else '失敗'}")


def example_list_targets():
    """利用可能な送信先の一覧表示"""
    print("\n=== 利用可能な送信先の一覧 ===")
    
    try:
        notifier = teams_notification.TeamsNotifier()
        notifier.list_available_targets()
    except Exception as e:
        print(f"エラー: {e}")


def main():
    """メイン関数"""
    print("Teams通知機能の使用例を実行します")
    print("=" * 50)
    
    # 利用可能な送信先を表示
    example_list_targets()
    
    # 各種通知例を実行
    example_basic_notification()
    example_error_notification()
    example_daily_report()
    example_specific_channel()
    
    print("\n" + "=" * 50)
    print("すべての例の実行が完了しました")


if __name__ == "__main__":
    main()
