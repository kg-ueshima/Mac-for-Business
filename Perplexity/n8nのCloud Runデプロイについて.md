n8nを**無料でCloud Runに環境構築**するには、以下のポイントを押さえるのが現実的かつ効率的です。

### 1. n8nのCloud Runデプロイについて
- n8nは公式のDockerイメージがあり、これをCloud Runのコンテナとして動かせます。  
- Cloud Runはサーバーレスでコンテナ実行が可能なので、インフラ管理が簡単です。  
- ただしCloud Runはステートレスなため、n8nのワークフロー設定や認証情報を永続化するために**外部データベースが必須**になります。

### 2. 永続化用データベースはSupabaseなど無料で使えるPostgreSQLが便利
- Google CloudのCloud SQLも使えますが、無料枠はすぐに限界になる可能性があります。  
- 無料枠の面では、PostgreSQLが無料で使えるSupabaseと組み合わせる方法がおすすめです。  
- Supabaseは無料枠があり、Cloud Runと相性が良いので、n8nのデータ永続化に最適です。  

### 3. 実際の構築手順
- n8nの公式Dockerイメージ（`n8nio/n8n`）をCloud Runにコンテナデプロイ。  
- SupabaseでPostgreSQLの無料データベースを作成し、環境変数（DB接続情報など）をCloud Runのサービスに設定。  
- Cloud Runのサービスを起動し、n8nに接続。  
- 可能ならPulumiやTerraformなどIaC（Infrastructure as Code）ツールでデプロイを自動化すると便利（Pulumiを使った紹介記事あり）。  

### 4. 料金について
- Cloud Runは無料枠があり、月間の一定時間・リクエストまで無料。  
- Supabaseも無料枠内でPostgreSQLを利用可能。  
- したがって、軽い利用や学習用途であれば基本料金を気にせず無料で構築・運用可能です。  

### 代表的な参考情報
- 実例記事「n8nをCloud Runにサクッとデプロイする方法（Supabase x Pulumi）」で、具体的なセットアップ手順やコード例が解説されています[5]。  
- TerraformでCloud Runへのn8nデプロイ＋IAP利用例も公開されており、アクセス制御の参考になります[6]。  
- DockerイメージダウンロードからCloud Runデプロイまで動画でも解説されているので、手順イメージがつかみやすいです[1][2][3]。  
- 公式クラウド版n8nは無料プランがなく、無料で使う場合はセルフホストが現実的です[7][11]。

### まとめ

| ポイント                    | 推奨内容・理由                               |
|---------------------------|-----------------------------------------|
| n8nの実行環境              | Cloud Run上でn8n公式Dockerイメージを利用     |
| データベース               | Supabaseの無料PostgreSQLを利用                |
| インフラコード管理（任意）  | PulumiやTerraformで自動化                     |
| 料金                      | Cloud Run無料枠＋Supabase無料枠で無料運用可能  |
| 注意点                    | Cloud RunはステートレスなのでDB連携必須、無料枠を超えると課金  |

この構成は、**小規模かつ軽い業務自動化用途に非常に適しており、Cloud Runの無料枠とSupabase無料枠を使うことでコストはかかりません**。ただし、本格的な大量処理や高負荷運用の場合は無料枠超過の可能性があるため注意してください。  

詳しいセットアップ方法は[5]の記事が体系的かつ最新の情報を提供しており、初心者にもわかりやすいです。Dockerの基本操作ができれば比較的スムーズに環境構築できます。

情報源
[1] How to self-host N8N in the cloud for FREE for UNLIMITED automations - YouTube https://www.youtube.com/watch?v=UHHkehy3SQk
[2] How To Install N8N FREE [Using Google Cloud] - AI Automation - YouTube https://www.youtube.com/watch?v=x49ZiJDIVPQ
[3] 【n8n インストール】はこれ一択！超格安【5ドル】運用方法！2025年5月最新！ - YouTube https://www.youtube.com/watch?v=BCYqyHPouDk
[4] ビジネスユーザーも仕事ですぐに使える Google の生成 AI サービス - YouTube https://www.youtube.com/watch?v=TcsywAiQFng
[5] n8nをCloud Runにサクッと（Supabase x Pulumi） - Zenn https://zenn.dev/sonicmoov/articles/1308fd9ce78555
[6] n8nをCloud RunにDeployしてIAPで内部アクセス許可する (Terraform) https://qiita.com/nakamasato/items/854031091ad82240728e
[7] n8n 無料で使い倒す！AI連携＆業務自動化：導入・活用・トラブル ... https://wzz.co.jp/ai_lab/n8n-free-ai-automation/
[8] コンテナは作った。でもその先が分からない人のためのGCP Cloud ... https://note.com/jones_shina/n/nb696adcc3b73
[9] 【無料】n8nとは？できることや使い方、活用事例をわかりやすく解説 https://www.ai-souken.com/article/what-is-n8n
[10] n8nを活用してAIエージェントを開発する方法〜AI技術を使った ... https://note.com/masaland/n/n01faa5449ee4
[11] n8n導入にかかる費用感を徹底比較｜Cloudプランと自前運用どっち ... https://aitaroblog.com/n8n-cost-compare/
[12] n8n徹底解説：初心者でもできるローカル自動化 - Apidog https://apidog.com/jp/blog/how-to-run-n8n-locally-jp/
[13] n8n入門ガイド：ノーコードで始める業務自動化の基本実践ステップ https://aiacademy.jp/media/?p=7712
[14] 生成AI連携でメールの自動要約なども、ワークフロー自動化ツール ... https://internet.watch.impress.co.jp/docs/column/shimizu/1544578.html
[15] n8nのセルフホスト設定方法を解説！初心者でも5分で構築可能 https://www.adcal-inc.com/column/n8n-localhost/


#### 【Cloud Run＋Supabaseでn8nを無料セルフホストする具体的な手順】

**おすすめプロジェクト名例**  
- `n8n-cloudrun-supabase-demo`
- `n8n-automation-lab`
- `my-n8n-freehost`
- `n8n-gcp-supabase-sample`

---

1. **Google Cloudプロジェクトの作成・Cloud Run有効化**
   - Google Cloud Consoleで新規プロジェクトを作成。  
     例：`n8n-cloudrun-supabase-demo` など上記のおすすめ名から選択。
   - Google Cloud Consoleの「APIとサービス」→「ライブラリ」から、以下3つのAPIを順番に検索して「有効にする」をクリックする。
     1. Cloud Run Admin API（Cloud Run APIと表記されることもあります。検索時は「Cloud Run Admin API」で探してください）
     2. Artifact Registry API
        - 有効化の際に「認証情報の作成」を求められる場合があります。その場合は、画面の案内に従って「サービスアカウント」を新規作成してください。
        - サービスアカウント名は任意（例：`artifact-registry-access`）でOKです。
        - 「ロールの選択」では「Artifact Registry 管理者」または「編集者」など、Artifact Registryへの操作権限があるロールを割り当てます。
        - サービスアカウントを作成したら、Google Cloud Consoleの「サービスアカウント」画面で該当アカウントを選択します。
        - 「鍵」タブを開き、「鍵を追加」ボタンをクリックします。
        - 「新しい鍵を作成」を選択し、キータイプは「JSON」を選びます。
        - 「作成」ボタンを押すと、自動的に認証情報ファイル（JSON形式）がPCにダウンロードされます。
        - このJSONファイルは後ほどDockerイメージのPushやgcloudコマンドを使う際に必要になるため、必ず安全な場所に保管してください。
        - この認証情報（JSONファイル）は、後のDockerイメージPush時やgcloudコマンド利用時に必要になるので、安全な場所に保存してください。
     3. Cloud Build API
   - すべて「有効」になっていることを確認する。

2. **Supabaseで無料PostgreSQLデータベース作成**
   - [Supabase公式サイト](https://supabase.com/)でアカウント作成＆新規プロジェクト作成。
   - プロジェクト名も上記の例を参考に命名可能。
   - プロジェクト作成後、「Project Settings」→「Database」から接続情報（ホスト名、DB名、ユーザー名、パスワード、ポート）を控える。

3. **n8n公式Dockerイメージの準備**
   - Cloud ShellやローカルPCで以下コマンドを実行し、n8nの公式イメージを取得（例: `docker pull n8nio/n8n:latest`）。
   - 必要に応じて`Dockerfile`を作成し、環境変数や設定ファイルを追加（ただし公式イメージのままでもOK）。

4. **Artifact RegistryへイメージをPush**
   - Google CloudのArtifact Registryでリポジトリを作成（例: `gcr.io/<プロジェクトID>/n8n`）。
   - `docker tag`でイメージにタグ付けし、`docker push`でアップロード。

5. **Cloud Runサービスの作成**
   - Cloud Consoleまたは`gcloud` CLIでCloud Runサービスを新規作成。
   - イメージURLに先ほどPushしたn8nイメージを指定。
   - 「環境変数」設定で、SupabaseのDB接続情報を`DB_TYPE=postgresdb`、`DB_POSTGRESDB_HOST`、`DB_POSTGRESDB_PORT`、`DB_POSTGRESDB_DATABASE`、`DB_POSTGRESDB_USER`、`DB_POSTGRESDB_PASSWORD`などとして入力。
   - ポート番号は`5678`（n8nデフォルト）を指定。
   - 認証は「未認証の呼び出しを許可」またはIAP等で制御。

6. **n8nへアクセス・初期設定**
   - Cloud RunのエンドポイントURLにアクセスし、n8nの初期セットアップを実施。
   - 必要に応じてn8nの認証やWebhook設定を行う。

7. **（任意）PulumiやTerraformでIaC自動化**
   - PulumiやTerraformの公式GCPプロバイダーを使い、上記手順をコード化して自動デプロイ可能。
   - 参考: [n8nをCloud Runにサクッと（Supabase x Pulumi）](https://zenn.dev/sonicmoov/articles/1308fd9ce78555)

---

**ポイント**
- Cloud Run無料枠内であれば、月間180,000vCPU秒・360,000GiB秒・200万リクエストまで無料。
- Supabaseも無料枠でPostgreSQLが利用可能（商用や高負荷用途は有料プラン検討）。
- n8nはステートレスなので、必ず外部DB（Supabase）と連携すること。

---

**参考コマンド例（Cloud Shell）**

