# Teamsチャット履歴を取得するPython環境構築について

## 概要

毎日の日報作成作業をPythonプログラムで自動化します。  
MacBook環境で、以下の情報を自動取得し、日報として保存します。

- Microsoft Teams のチャット・投稿
- Chatwork のメッセージ
- 送信済みメール（Outlook/Gmail）
- OneDrive 上に作成された新規ファイルのタイトルと内容
- Gemini CLI を活用した要約または分析

---

## システム構成概要

Microsoft Entra管理センターにアクセス
https://entra.microsoft.com/#home

| 対象      | 取得方法                                      |
|-----------|-----------------------------------------------|
| Teams     | Microsoft Graph API（認証要：Azure登録）      |
| Chatwork  | Chatwork API（トークン発行要）                |
| メール    | Gmail API / Outlook: Microsoft Graph API      |
| OneDrive  | Microsoft Graph API またはローカルファイル監視 |
| Gemini CLI| ローカルで起動（geminiコマンドで要約等実行）  |

---

## 環境前提

- macOS（Python 3.10以上推奨）
- pip, venv使用可能
- Microsoft アカウント（Graph API利用）
- Chatwork APIトークン
- Gmail/OutlookのAPI認証設定済
- Gemini CLI インストール済

---

## スクリプトの骨組み（概要）
### Agents/daily_report/ のプログラム概要

`Agents/daily_report/` ディレクトリには、業務日報を自動収集・生成するためのPythonスクリプト群が含まれています。  
主な機能と構成は以下の通りです。

#### 主な機能

- **Teamsメッセージの自動取得**  
  Microsoft Graph APIを利用し、Teamsのチャットや投稿を自動で取得します。

- **Chatworkメッセージの自動取得**  
  Chatwork APIを利用し、指定したルームのメッセージを取得します。

- **送信済みメールの取得**  
  Outlook（Microsoft Graph API）やGmail APIを利用し、前日に送信したメールを取得します。

- **OneDrive新規ファイルの取得**  
  OneDrive上で新規作成されたファイルのタイトルや内容を取得します。

- **Gemini CLIによる要約・分析**  
  取得したファイルやメッセージ内容をGemini CLIで要約・分析します。

- **日報ファイルの自動生成・保存**  
  取得した情報をまとめ、日付ごとに日報ファイルとして自動保存します。

#### 構成ファイル例

- `main.py`  
  各種APIから情報を取得し、日報を生成・保存するメインスクリプト。

- `modules/teams.py`  
  Teamsのチャット・投稿をGraph API経由で取得するモジュール。

- `modules/chatwork.py`  
  ChatworkのメッセージをAPI経由で取得するモジュール。

- `modules/email_client.py`  
  OutlookやGmailの送信済みメールを取得するモジュール。

- `modules/onedrive.py`  
  OneDriveの新規ファイルを取得するモジュール。

- `modules/gemini.py`  
  Gemini CLIを呼び出して要約・分析を行うモジュール。

#### 日報生成の流れ（例）

1. 各種APIから前日分のデータを取得
2. 取得したデータを整形し、要約や分析を実施
3. 日付ごとに日報ファイル（テキスト）として保存

#### 備考

- 認証情報やAPIキーは `env.local` などの環境変数ファイルで管理します。
- macOS環境での動作を想定していますが、他のOSでもPython環境があれば動作可能です。

---
