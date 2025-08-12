#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
汎用的なTeams通知モジュール
様々な通知機能で再利用可能なTeams送信機能を提供
"""

import os
import datetime
import requests
from pathlib import Path
from dotenv import load_dotenv
from msal import PublicClientApplication, SerializableTokenCache
from typing import List, Dict, Optional, Union

# 環境変数を読み込み
env_path = Path(__file__).parent.parent.parent.parent / 'env.local'
load_dotenv(dotenv_path=env_path)

class TeamsNotifier:
    """汎用的なTeams通知クラス"""
    
    def __init__(self):
        self.client_id = os.getenv('MICROSOFT_CLIENT_ID')
        self.tenant_id = os.getenv('MICROSOFT_TENANT_ID')
        self.target_team_id = os.getenv('TEAMS_TARGET_TEAM_ID')
        self.target_channel_id = os.getenv('TEAMS_TARGET_CHANNEL_ID')
        
        if not self.client_id or not self.tenant_id:
            raise ValueError("環境変数 MICROSOFT_CLIENT_ID と MICROSOFT_TENANT_ID が設定されていません")
        
        self.authority = f'https://login.microsoftonline.com/{self.tenant_id}'
        self.scopes = [
            'Channel.ReadBasic.All',
            'ChannelMessage.Read.All',
            'Chat.Read',
            'User.Read',
            'User.ReadBasic.All',
            'ChannelMessage.Send',
            'Team.ReadBasic.All',
            'Files.ReadWrite.All'
        ]
        
        self.access_token = None
        self._authenticate()
    
    def _authenticate(self):
        """Microsoft Graph APIの認証"""
        # トークンキャッシュ設定
        token_cache_file = Path(__file__).parent / "teams_token_cache.bin"
        cache = SerializableTokenCache()
        
        if token_cache_file.exists():
            with open(token_cache_file, "r") as f:
                cache.deserialize(f.read())
        
        app = PublicClientApplication(
            client_id=self.client_id,
            authority=self.authority,
            token_cache=cache
        )
        
        accounts = app.get_accounts()
        result = None
        
        if accounts:
            result = app.acquire_token_silent(self.scopes, account=accounts[0])
        
        if not result:
            flow = app.initiate_device_flow(scopes=self.scopes)
            if "user_code" not in flow:
                raise Exception("デバイスコード認証に失敗しました")
            print(flow["message"])
            result = app.acquire_token_by_device_flow(flow)
        
        if "access_token" not in result:
            raise Exception(f"トークン取得失敗: {result}")
        
        # キャッシュを保存
        with open(token_cache_file, "w") as f:
            f.write(cache.serialize())
        
        self.access_token = result["access_token"]
    
    def get_headers(self):
        """APIリクエスト用のヘッダーを取得"""
        return {"Authorization": f"Bearer {self.access_token}"}
    
    def get_teams_and_channels(self) -> List[Dict]:
        """利用可能なチームとチャンネルの一覧を取得"""
        try:
            teams_list = []
            
            # 所属チーム一覧取得
            teams_url = 'https://graph.microsoft.com/v1.0/me/joinedTeams'
            teams_res = requests.get(teams_url, headers=self.get_headers())
            
            if teams_res.status_code != 200:
                print('チーム一覧取得失敗:', teams_res.text)
                return teams_list
                
            teams_data = teams_res.json().get('value', [])
            
            for team in teams_data:
                team_id = team.get('id')
                team_name = team.get('displayName', '不明なチーム')
                
                # チャンネル一覧取得
                channels_url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels'
                channels_res = requests.get(channels_url, headers=self.get_headers())
                
                if channels_res.status_code != 200:
                    print(f'チャンネル一覧取得失敗({team_name}):', channels_res.text)
                    continue
                    
                channels_data = channels_res.json().get('value', [])
                team_channels = []
                
                for channel in channels_data:
                    channel_id = channel.get('id')
                    channel_name = channel.get('displayName', '不明なチャンネル')
                    team_channels.append({
                        'id': channel_id,
                        'name': channel_name
                    })
                
                teams_list.append({
                    'id': team_id,
                    'name': team_name,
                    'channels': team_channels
                })
                
            return teams_list
            
        except Exception as e:
            print(f"チーム・チャンネル一覧取得エラー: {e}")
            return []
    
    def send_message(self, message: str, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
        """
        指定されたチームのチャンネルにメッセージを送信
        
        Args:
            message: 送信するメッセージ
            team_id: チームID（Noneの場合は環境変数または最初のチームを使用）
            channel_id: チャンネルID（Noneの場合は環境変数または最初のチャンネルを使用）
        
        Returns:
            bool: 送信成功時True
        """
        try:
            # 送信先の決定
            target_team_id = team_id or self.target_team_id
            target_channel_id = channel_id or self.target_channel_id
            
            if not target_team_id or not target_channel_id:
                # 環境変数が設定されていない場合は最初のチーム・チャンネルを使用
                teams_list = self.get_teams_and_channels()
                if not teams_list or not teams_list[0]['channels']:
                    print("送信先のチーム・チャンネルが見つかりませんでした")
                    return False
                
                target_team_id = teams_list[0]['id']
                target_channel_id = teams_list[0]['channels'][0]['id']
                print(f"デフォルト送信先を使用: チームID={target_team_id}, チャンネルID={target_channel_id}")
            
            # メッセージ送信
            url = f'https://graph.microsoft.com/v1.0/teams/{target_team_id}/channels/{target_channel_id}/messages'
            
            body = {
                "body": {
                    "contentType": "html",
                    "content": message
                }
            }
            
            response = requests.post(url, headers=self.get_headers(), json=body)
            
            if response.status_code == 201:
                print(f"メッセージを送信しました: {response.json().get('id', 'unknown')}")
                return True
            else:
                print(f"メッセージ送信エラー: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"メッセージ送信エラー: {e}")
            return False
    
    def send_notification(self, title: str, content: str, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
        """
        通知メッセージを送信（タイトル付き）
        
        Args:
            title: 通知のタイトル
            content: 通知の内容
            team_id: チームID
            channel_id: チャンネルID
        
        Returns:
            bool: 送信成功時True
        """
        message = f"# {title}\n\n{content}"
        return self.send_message(message, team_id, channel_id)
    
    def send_message_with_file(self, message: str, file_path: str, file_name: Optional[str] = None, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
        """
        ファイル添付付きメッセージを送信
        
        Args:
            message: 送信するメッセージ
            file_path: 添付ファイルのパス
            file_name: ファイル名（Noneの場合はパスから取得）
            team_id: チームID
            channel_id: チャンネルID
        
        Returns:
            bool: 送信成功時True
        """
        try:
            # 送信先の決定
            target_team_id = team_id or self.target_team_id
            target_channel_id = channel_id or self.target_channel_id
            
            if not target_team_id or not target_channel_id:
                teams_list = self.get_teams_and_channels()
                if not teams_list or not teams_list[0]['channels']:
                    print("送信先のチーム・チャンネルが見つかりませんでした")
                    return False
                
                target_team_id = teams_list[0]['id']
                target_channel_id = teams_list[0]['channels'][0]['id']
            
            # ファイルをアップロード
            file_path_obj = Path(file_path)
            if not file_path_obj.exists():
                print(f"ファイルが見つかりません: {file_path}")
                return False
            
            display_name = file_name or file_path_obj.name
            
            # OneDriveにファイルをアップロード
            upload_url = f'https://graph.microsoft.com/v1.0/me/drive/root:/Teams Uploads/{display_name}:/content'
            
            with open(file_path_obj, 'rb') as f:
                upload_response = requests.put(
                    upload_url,
                    headers=self.get_headers(),
                    data=f
                )
            
            if upload_response.status_code not in [200, 201]:
                print(f"ファイルアップロードエラー: {upload_response.status_code} - {upload_response.text}")
                return False
            
            file_info = upload_response.json()
            file_id = file_info.get('id')
            web_url = file_info.get('webUrl')
            
            # メッセージにファイルリンクを追加
            enhanced_message = f"{message}\n\n📎 添付ファイル: <a href=\"{web_url}\">{display_name}</a>"
            
            # メッセージ送信
            msg_url = f'https://graph.microsoft.com/v1.0/teams/{target_team_id}/channels/{target_channel_id}/messages'
            
            body = {
                "body": {
                    "contentType": "html",
                    "content": enhanced_message
                }
            }
            
            response = requests.post(msg_url, headers=self.get_headers(), json=body)
            
            if response.status_code == 201:
                print(f"ファイル付きメッセージを送信しました")
                return True
            else:
                print(f"メッセージ送信エラー: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"ファイル付きメッセージ送信エラー: {e}")
            return False
    
    def send_notification_with_file(self, title: str, content: str, file_path: str, file_name: Optional[str] = None, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
        """
        ファイル添付付き通知メッセージを送信
        
        Args:
            title: 通知のタイトル
            content: 通知の内容
            file_path: 添付ファイルのパス
            file_name: ファイル名
            team_id: チームID
            channel_id: チャンネルID
        
        Returns:
            bool: 送信成功時True
        """
        message = f"# {title}\n\n{content}"
        return self.send_message_with_file(message, file_path, file_name, team_id, channel_id)
    
    def list_available_targets(self):
        """利用可能な送信先を表示"""
        teams_list = self.get_teams_and_channels()
        
        if not teams_list:
            print("利用可能なチーム・チャンネルが見つかりませんでした")
            return
        
        print("利用可能なチームとチャンネル:")
        for team in teams_list:
            print(f"チーム: {team['name']} (ID: {team['id']})")
            for channel in team['channels']:
                print(f"  - チャンネル: {channel['name']} (ID: {channel['id']})")
        
        if self.target_team_id and self.target_channel_id:
            print(f"\n現在のデフォルト送信先: チームID={self.target_team_id}, チャンネルID={self.target_channel_id}")
        else:
            print("\nデフォルト送信先が設定されていません。最初のチーム・チャンネルが使用されます。")


# 便利な関数
def send_teams_message(message: str, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
    """簡単なTeamsメッセージ送信関数"""
    try:
        notifier = TeamsNotifier()
        return notifier.send_message(message, team_id, channel_id)
    except Exception as e:
        print(f"Teams通知エラー: {e}")
        return False


def send_teams_notification(title: str, content: str, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
    """簡単なTeams通知送信関数"""
    try:
        notifier = TeamsNotifier()
        return notifier.send_notification(title, content, team_id, channel_id)
    except Exception as e:
        print(f"Teams通知エラー: {e}")
        return False


def send_teams_notification_with_file(title: str, content: str, file_path: str, file_name: Optional[str] = None, team_id: Optional[str] = None, channel_id: Optional[str] = None) -> bool:
    """簡単なTeams通知送信関数（ファイル添付付き）"""
    try:
        notifier = TeamsNotifier()
        return notifier.send_notification_with_file(title, content, file_path, file_name, team_id, channel_id)
    except Exception as e:
        print(f"Teams通知エラー: {e}")
        return False


if __name__ == "__main__":
    # テスト用
    notifier = TeamsNotifier()
    notifier.list_available_targets()
    
    # テストメッセージ送信
    test_message = "これはテストメッセージです。\n\n汎用的なTeams通知機能のテストです。"
    success = notifier.send_notification("テスト通知", test_message)
    
    if success:
        print("テストメッセージの送信に成功しました")
    else:
        print("テストメッセージの送信に失敗しました")
