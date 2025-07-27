# Google Cloud Runとサーバーレスコンテナ実行サービスまとめ

## Google Cloud Runとは

Google Cloud Run（クラウドラン）は、Google Cloudが提供する**サーバーレスのコンテナ実行サービス**です。アプリケーションをコンテナ化してデプロイするだけで、インフラの構築や管理を気にせず、簡単にスケールするシステムをすぐに公開できます。

---

## 主な特徴

- **サーバーレス**：インフラの管理は不要。コンテナイメージを用意するだけで利用可能[^gcp1][^gcp2]。
- **フルマネージド**：デプロイ・スケーリング・負荷分散など運用面は全て自動化。
- **自動スケーリング**：リクエストやイベントに応じて、コンテナが0から必要な数まで瞬時にスケール[^gcp3][^gcp2]。
- **多言語対応**：Go, Node.js, Python, Java, .NET など幅広い言語・フレームワークに対応[^gcp1][^gcp4]。
- **HTTP/HTTPS/イベント駆動**：APIやウェブバックエンド、バッチ処理など多様な用途で利用可能。
- **無料枠あり**：テスト・小規模運用であれば無料で始めやすい[^gcp5][^gcp6]。
- **高い柔軟性**：Cloud SQLなど他GCPサービスとの連携やカスタムドメイン利用も可能[^gcp4][^gcp2]。

---

## サービスの種類

Cloud Runの「リソースタイプ」には以下の3つがあります[^gcp1]：

| タイプ        | 概要                                     |
|-------------|----------------------------------------|
| サービス        | HTTPリクエストに応じて自動でインスタンスを起動・処理し、エンドポイントを提供。 |
| ジョブ         | バッチ処理など、リクエスト不要な1回限りや定期実行のタスク向け。             |
| ワーカープール  | キューやPub/Subメッセージなど、プル型・連続処理に使う用途向け。             |

---

## 料金体系

Cloud Runは**従量課金制**で、実際に利用した分だけ料金が発生します。課金対象は**CPU時間・メモリ時間・リクエスト数**の3つです[^gcp5][^gcp6][^gcp7]。

### 無料枠

- vCPU使用：最初の180,000vCPU-秒/月（1リージョンごと）
- メモリ使用：最初の360,000GiB-秒/月
- リクエスト数：月間2,000,000リクエストまで

### 主な単価（例：2025年7月時点）

| 項目                    | 料金（無料枠超過後の例）                   |
|---------------------|------------------------------|
| vCPU                | $0.000024/秒                 |
| メモリ (GiB単位)        | $0.0000025/秒                |
| リクエスト            | $0.40/1,000,000リクエスト     |

※日本リージョン（asia-northeast1など）は米国・欧州など主要リージョンと同水準（Tier 1）です。小規模であれば無料枠内で利用可能ですが、商用や高負荷用途では従量課金分が発生します[^gcp5][^gcp6][^gcp7]。

#### 【計算例】
- 1vCPU・1GiBメモリで、計360,000秒利用（月100時間）＋300万リクエストの場合  
  → 無料枠分を超えた分のみ課金対象（CPU代・メモリ代・リクエスト追加分）

#### 補足
- 利用料金は**100ミリ秒単位で切り上げ**て計算されます[^gcp7]。
- 料金や無料枠は地域・時期によって微調整があるため、正確な見積もりには**料金計算ツールの利用**がおすすめ[^gcp8]。

---

## Cloud Runのメリット・ユースケース

- **スモールスタートやPoCに最適**：ランニングコストを抑えたまま、素早くサービス提供が可能。
- **トラフィック急増時も自動で対応**：イベントやキャンペーン等でアクセスが増えても自動スケール。
- **バッチ処理やバックエンドAPI、Webhook受信などさまざまな用途**で活用可。
- **Google Cloudの他サービスとの連携**が柔軟。

---

## まとめ

Google Cloud Runは、**簡単デプロイ・フルマネージド・従量課金・無料枠あり**という点で、開発～商用まで幅広いシーンで選ばれているクラウドサービスです。コストは**使った分だけ**、必要な時だけスケールするため非常に経済的です[^gcp5][^gcp6][^gcp2][^gcp7]。

---

## サーバーレスのコンテナ実行サービスとは

「サーバーレスのコンテナ実行サービス」とは、**コンテナ技術を使いながら、サーバーの管理や運用をユーザーが意識せずに済む環境でアプリケーションを動かせるサービス**のことです。

### 主なポイント

- **コンテナとは？**  
  コンテナは、アプリケーションとその実行に必要なライブラリや設定をパッケージ化した「軽量な仮想環境」です。これにより、どの環境でも同じように動作させやすくなります。通常はDockerなどのツールで作成し、Kubernetesなどで管理します[^srv3]。

- **サーバーレスとは？**  
  利用者は物理・仮想サーバーの準備や設定、運用・監視などの管理作業をしなくて済み、コードやコンテナをクラウドにデプロイするだけで、自動的に必要なリソースが割り当てられ、ユーザーの負担なしにスケールします。実行した分だけ課金されるのも特徴です[^srv6][^gcp8]。

- **サーバーレスのコンテナ実行サービスの仕組み**  
  Cloud RunやAWS Fargateのようなサービスでは、クラウドプロバイダーがサーバーやインフラ全体の管理を代行し、ユーザーはコンテナイメージを提供するだけで済みます。これにより、  
  - 仮想マシンの設定やセキュリティパッチ適用等の負担が不要  
  - 自動でスケールアップ/ダウンし、アクセス変動に強い  
  - インフラの運用監視から開発者を解放し、開発に集中できる  
  というメリットがあります[^srv1][^srv2][^gcp5][^gcp7][^gcp9][^srv10]。

- **サービスの例**  
  - Google Cloud Run：Knativeをベースに、コードやコンテナをデプロイすると自動的にサーバー管理なしに動かせる  
  - AWS Fargate：Amazon ECS/EKS上でコンテナを実行する際に、サーバーの管理ではなくコンテナ単位でリソースを割り当てる仕組み[^srv1][^gcp7][^srv10]
  - Azure Container Appsも同様にサーバーレスでコンテナを実行し、自動スケーリングやセキュリティ管理を提供[^gcp9]

まとめると、「サーバーレスのコンテナ実行サービス」は、**コンテナの持つ環境の一貫性や柔軟さはそのままに、クラウド側がインフラ管理を肩代わりし、ユーザーはコンテナのデプロイとアプリケーションに集中できる仕組み**です。これにより、開発効率が大幅に上がり、負荷変動に強いサービスを手軽に構築できます。

---

## 参考情報源

### Google Cloud Run関連

[^gcp1]: [Cloud Run とは | Cloud Run Documentation](https://cloud.google.com/run/docs/overview/what-is-cloud-run)
[^gcp2]: [Cloud Runの概要について初学者向けにまとめた - DevelopersIO](https://dev.classmethod.jp/articles/google-cloud-cloud-run/)
[^gcp3]: [Cloud Runを徹底解説！](https://blog.g-gen.co.jp/entry/cloud-run-explained)
[^gcp4]: [Cloud Run - Everything you need to know](https://s-peers.com/en/sap-analytics/google-cloud-platform/computing/cloud-run/)
[^gcp5]: [Google Cloud Run Pricing Savings Guide](https://www.pump.co/blog/google-cloud-run-pricing)
[^gcp6]: [Demystifying Google Cloud Run Pricing: Untangling CPU ... - LinkedIn](https://www.linkedin.com/pulse/demystifying-google-cloud-run-pricing-untangling-cpu-memory-zakaria)
[^gcp7]: [Cloud Run pricing](https://cloud.google.com/run/pricing)
[^gcp8]: [Cloud Run](https://cloud.google.com/run)
[^gcp9]: [Cloud Run のドキュメント | Cloud Run Documentation](https://cloud.google.com/run/docs)
[^gcp10]: [入門！Cloud Runのススメ](https://blog.g-gen.co.jp/entry/introduction-to-cloud-run-service)

### サーバーレスコンテナ全般

[^srv1]: [AWS Fargateとは？サーバレスで実行できるコンテナ向け ...](https://dx.nid.co.jp/column/what-is-aws-fargate)
[^srv2]: [サーバーレスコンテナ実行環境サービス『アプリクラウド Rana8 ...](https://www.nttpc.co.jp/technology/rana8.html)
[^srv3]: [コンテナとサーバーレスの特長、使い分け（初心者・非 ...](https://ncdc.co.jp/columns/7886/)
[^srv4]: [マネージドサービス、コンテナ、サーバレス](https://digital-gov.note.jp/n/n9e0354fadc2d)
[^srv5]: [初めてのサーバーレスコンテナを AWS に素早くデプロイ](https://aws.amazon.com/jp/blogs/news/fast-forward-on-your-first-serverless-container-deployment-on-aws/)
[^srv6]: [サーバレスKubernetesを活用する理由ってなに？Alibaba, ...](https://www.softbank.jp/biz/blog/cloud-technology/articles/202209/serverless-comparison/)
[^srv7]: [AWS Fargateとは？クラウドネイティブな開発を実現する ...](https://www.i3design.jp/in-pocket/11706)
[^srv8]: [サーバーレスとコンテナの適切な利用とハイブリッドの考え方](https://engineering.monstar-lab.com/jp/post/2024/06/21/Serverless-and-Container/)
[^srv9]: [Azure でサーバーレス コンテナーを使用する](https://learn.microsoft.com/ja-jp/azure/container-apps/start-serverless-containers)
[^srv10]: [Fargateとは何か？AWS上でのサーバーレスコンテナ実行 ...](https://www.issoh.co.jp/tech/details/3870)

---

> ※このファイルは「Google Cloud Runとサーバーレスコンテナ実行サービスまとめ.md」などのファイル名で保存するのが適切です。
