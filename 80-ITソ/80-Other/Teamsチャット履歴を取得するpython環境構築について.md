# Teams・Outlook・OneDriveの履歴を自動取得して日報を作るPython環境まとめ

## 概要

日々の業務報告（日報）を自動化したい方向けに、Microsoft Teamsのチャット、Outlookの送信済みメール、OneDriveのファイル操作履歴をPythonでまとめて取得し、作業記録を自動生成する仕組みの構築方法を分かりやすくまとめました。

---

## できること

- Teamsの自分の発言履歴を自動取得
- Outlook（送信済み）メールの件名・宛先を自動取得
- OneDriveで自分が操作したファイルの履歴を自動取得
- 取得した内容を日付ごとにまとめて日報として活用

---

## システム全体像

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

## 構築手順

### 1. Microsoft Entra ID（旧Azure AD）でアプリ登録

1. [Azureポータル](https://portal.azure.com/)にサインイン
2. 「Microsoft Entra ID」→「アプリの登録」→「新規登録」
   - 名前：任意（例：DailyWorkReportGenerator）
   - サポートされているアカウント：この組織ディレクトリのみ
   - リダイレクトURI：`http://localhost`
3. 「APIのアクセス許可」→「Microsoft Graph」→「委任されたアクセス許可」
   - `Chat.Read.All`（Teamsチャット）
   - `Mail.Read`（メール）
   - `Sites.Read.All`（OneDrive/SharePointファイル）
   - 追加後、「管理者の同意」を付与
4. 「アプリケーション(クライアント)ID」「ディレクトリ(テナント)ID」を控える

---

### 2. Python環境セットアップ