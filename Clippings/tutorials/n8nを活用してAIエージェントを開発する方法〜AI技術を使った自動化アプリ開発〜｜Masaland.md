---
title: "n8nを活用してAIエージェントを開発する方法〜AI技術を使った自動化アプリ開発〜｜Masaland"
source: "https://note.com/masaland/n/n01faa5449ee4"
author:
  - "[[Masaland]]"
published: 2025-01-08
created: 2025-07-13
description: "AI技術は快速に進化しています。自動化の重要性はさらに高まり、これに与して、オープンソースのワークフロー自動化ツールである「n8n」が注目を集めています。  本記事では、n8nを使用してAIエージェントを開発する方法について解説します。   n8nの概要  n8nとは？  n8nは400以上の外部サービスを統合可能なワークフロー自動化ツールです。ノーコードでも使用可能な直感的なUIを持ちながら、コードを活用した高度なカスタマイズにも対応しています。  人工知能を活用して特定のタスクを自動的に実行するソフトウェアである「AIエージェント」をノーコード・ローコードで開発することができます。"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/169196141/rectangle_large_type_2_e8cdfd8a64810dedaec2cfb4ca15a6ce.png?width=1200)

## n8nを活用してAIエージェントを開発する方法〜AI技術を使った自動化アプリ開発〜

[Masaland](https://note.com/masaland)

AI技術は快速に進化しています。自動化の重要性はさらに高まり、これに与して、オープンソースの **ワークフロー自動化ツールである「n8n」** が注目を集めています。

本記事では、n8nを使用してAIエージェントを開発する方法について解説します。

## n8nの概要

### n8nとは？

n8nは400以上の外部サービスを統合可能なワークフロー自動化ツールです。ノーコードでも使用可能な直感的なUIを持ちながら、コードを活用した高度なカスタマイズにも対応しています。

人工知能を活用して特定のタスクを自動的に実行するソフトウェアである「AIエージェント」をノーコード・ローコードで開発することができます。

AIエージェントには下記のような特徴があります。

**自律性：** 事前に設定されたルールやワークフローに基づき、使用者の中間に入ることなく自動でタスクを実行。

**高度な処理能力：** OpenAIやGoogleのAIモデルを使用し、自然言語処理や予測分析などを実現。

**統合性** ：他のシステムやAPIと連携して、データ収集、処理、出力を一貫して　実行。

## n8nの価格とライセンス

n8nは、その柔軟性と多機能性に比べて手頃な価格体系を提供しています。主に以下の2つのオプションがあります。

**クラウド版**

ここでは、StarterプランとProプランを紹介します。

**①Starterプラン: 月額20€(年支払いの場合)**

- 月2,500回のワークフロー実行
- 5個のアクティブワークフロー
- 小規模プロジェクトや個人利用向け

**②Proプラン: 月額50€(年支払いの場合)**

- 月10,000回のワークフロー実行
- 15個のアクティブワークフロー
- 成長中のチームや中規模プロジェクト向け
![画像](https://assets.st-note.com/img/1736318447-Jzimj9RMtkcOFdnI18q0vWK4.png?width=1200)

n8nのサイト に掲載されている価格

### セルフホスティング版

自分でサーバーやインフラをセットアップする必要があります。無料で利用可能ですが、別途サーバー維持費などが必要になります。

ライセンスとしては、下記の「Sustainable Use Lisense」が適用されます。

**無料利用**: 内部ビジネス目的、非商用、個人利用であれば無料で使用可能。  
**配布制限**: 無料かつ非商用目的での配布に限り許可。  
**禁止事項**:商用サービスとして提供すること（例: ホワイトラベル化や有料ホスティングサービス）。

[**Sustainable Use License | n8n Docs** *The n8n Sustainable Use License.**docs.n8n.io*](https://docs.n8n.io/sustainable-use-license/)

## n8nで連携できるサービス

n8nは幅広いサービスと統合でき、さまざまな業務で活用できます。

1\. **コミュニケーションツール**  
自動通知やリアルタイムのメッセージ送信を実現。  
例)Slack、Microsoft Teams、Discordなど。

2\. **クラウドストレージ** ：  
ファイルの自動アップロードやバックアップ管理が可能。  
例)Google Drive、Dropbox、Microsoft OneDrive。

3\. **データベース** ：  
データの自動入力や更新に最適。  
例)MySQL、PostgreSQL、MongoDB。

4\. **マーケティングツール** ：  
メール配信やリード管理を効率化。  
例)Mailchimp、HubSpot、ActiveCampaign。

5\. **プロジェクト管理** ：  
タスクの自動作成や進捗の追跡を簡単に。  
例)Trello、Asana、Jira

6\. **AIとデータ解析** ：  
AIによるデータ処理や分析をスムーズに。  
例)OpenAI（GPT系）、Google Analytics。

7\. **ソーシャルメディア** ：  
投稿の自動化やコメントへの対応が可能。  
例)Twitter、Facebook

8\. **eコマース** ：  
注文処理や顧客管理を自動化。  
例)Shopify、WooCommerce、Stripe

## n8nの利用開始方法

n8nを使うには、クラウド版とセルフホスティング版があります。

### クラウド版

下記のn8nのサイトにアクセスして、簡単に利用開始できます。まずは利用してみたいという方はこちらがおすすめです。

[**n8n.io - a powerful workflow automation tool** *n8n is a free and source-available workflow automation tool* *n8n.io*](https://n8n.io/)

### セルフホスティング版

データを自社で管理するサーバで管理することができます。

**STEP1 Dockerのインストール**

[**Docker: コンテナー アプリケーション開発の加速** *Docker は、開発者がコンテナー アプリケーションを構築、共有、実行できるように設計されたプラットフォームです。面倒な* *www.docker.com*](https://www.docker.com/ja-jp/)

**STEP2 n8nインスタンスの起動**

```ruby
docker run -it --rm \
--name n8n \
-p 5678:5678 \
-v ~/.n8n:/home/node/.n8n \
n8nio/n8n
```

**STEP3 ブラウザで下記のサイトにアクセスしてセットアップ完了**

```javascript
http://localhost:5678
```

## AIエージェントの開発

### 事前準備

**STEP1 Credentialsの設定**

- n8nダッシュボードの右上にある「Create」ボタンをクリック。
- ドロップダウンメニューから「Credentials」を選択し、接続したいサービスの認証情報を登録。
- 各サービスに必要なAPIキーやトークンを取得し、n8nに入力。
![画像](https://assets.st-note.com/img/1736309929-zeCZjEXkQrTAv83Dhstc5VHm.png?width=1200)

Credentialsの追加

![画像](https://assets.st-note.com/img/1736309421-3tHF018oNrBQKIWwyiUCxglX.png?width=1200)

サービスの利用設定

**STEP2 ワークフローの作成**

- ダッシュボード右上の「Create」ボタンをクリック。
- 「Workflow」を選択し、新規ワークフローを作成。
![画像](https://assets.st-note.com/img/1736309575-VlFkuSQB4d8Hw7NYfxWL3qeX.png)

ワークフローの追加

**STEP3 ワークフローの実装**

- ノードを追加し、サービス間の接続をドラッグ＆ドロップで構築。
- 必要なトリガー（例：Webhook）やアクション（例：Slackへの通知）を設定。
![画像](https://assets.st-note.com/img/1736309889-4mPXDMCWwIUSBAOp1kHjq8Vb.png?width=1200)

ワークフローの例

### 例)案件状態の要約通知

以下は、n8nを使用して作成したAIエージェントのワークフローの例です。

![画像](https://assets.st-note.com/img/1736308997-3hfVI4uCq7HAlaYzQjPEndTS.png?width=1200)

AIエージェントのワークフロー

1. **Googleスプレッドシートから案件一覧を取得**
	- Google Sheetsノードを設定し、特定のスプレッドシートからデータを取得。
2. **ChatGPTで案件データを要約**
	- OpenAIノードを追加し、取得したデータを要約するプロンプトを設定。
3. **要約結果をSlackに送信**
	- Slackノードを使用して、要約結果を特定のチャンネルやユーザーに通知。

## Difyとの比較

n8nとDifyは、それぞれ異なる特徴を持つツールですが、違いとしては下記の通りです。

### サービス連携の数

- n8nは200以上のサービスと連携可能で、メール受信、データ解析、外部サービスの実行など、多用途のワークフローを構築できます。
- Difyは1,000以上の統合を提供しており、特にLLM（大規模言語モデル）を利用したAIアプリケーションに特化しています。
![画像](https://assets.st-note.com/img/1736317038-DeEnmGNpTq4jboQc12Y7SB5l.png?width=1200)

n8nのサイト に掲載されている使えるサービス

## まとめ

n8nを活用することで、AIエージェントを簡単に構築し、業務効率化やユーザー体験の向上を実現できます。

次のステップとして、n8nのドキュメントを参照し、さらに高度なワークフローやAIツールの統合を試してみましょう！

下記の記事ではn8nを使って、情報収集を効率化する方法についてご紹介しています。

## いいなと思ったら応援しよう！

n8nを活用してAIエージェントを開発する方法〜AI技術を使った自動化アプリ開発〜｜Masaland