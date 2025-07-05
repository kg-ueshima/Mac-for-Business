# アカウント情報（機密情報は環境変数で管理）

## GitHub
- website: github.com
- username: [環境変数で管理]
- password: [環境変数で管理]
- email: [環境変数で管理]

## Microsoft Entra (Teams Daily Report)
- website: Microsoft Entra管理センター
- app_registration:
  - display_name: TeamsDailyReportUserApp
  - application_client_id: [環境変数で管理]
  - object_id: [環境変数で管理]
  - directory_tenant_id: [環境変数で管理]
  - secret_id: [環境変数で管理]

## 環境変数設定
機密情報は`env.local`ファイルで管理されています：
- MICROSOFT_CLIENT_ID
- MICROSOFT_TENANT_ID
- MICROSOFT_OBJECT_ID
- MICROSOFT_SECRET_ID
- GITHUB_USERNAME
- GITHUB_PASSWORD
- GITHUB_EMAIL

## 注意事項
- `env.local`ファイルはGitにコミットされません
- 実際の値はローカル環境でのみ管理
- 新しい環境では`env.local`ファイルを手動で作成する必要があります