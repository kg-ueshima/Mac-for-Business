---
title: "Google Analytics MCP Serverを利用し、AIで無料分析を開始する方法をわかりやすく解説（画像手順書付き）"
source: "https://www.ga4.guide/gamcp/"
author:
  - "[[小川卓]]"
published: 2025-07-25
created: 2025-07-27
description: "GA4の画面上で分析するのは面倒、だけどAIにデータを取り込むのも手間でデータ漏洩なども不安…そんな方にオスス…"
tags:
  - "clippings"
---
GA4の画面上で分析するのは面倒、だけどAIにデータを取り込むのも手間でデータ漏洩なども不安…そんな方にオススメなのが、GAのMCP Serverを使ったAI分析です。  
  
そもそもGAのMCP Serverって何？という感じかと思います。

> Google Analytics MCPサーバーは、AIアシスタントがGoogle Analyticsデータにアクセスして分析できるようにする **Model Context Protocol（MCP）サーバー** です。MCPは、AIモデルが外部データソースやツールに安全に接続できるようにするためにAnthropicが開発した標準化されたプロトコルです。

これでもよくわからないという感じかと思うので、ウェブマーケター向けにわかりやすく説明すると

１）GA4の指定したプロパティの最新データを常に取得することができ  
２）そのデータをAIサービス側で読み込むことができ  
３）自然言語を利用してローカル環境で（つまり外部データを出すことなく）分析を行うことが可能

という内容になります。

つまり「AIを活用したGA4分析が行える」という感じですね。以下が公式のYouTubeでの説明ですが、これだけ見ても設定方法がわかりにくいかと思います。

![](https://www.youtube.com/watch?v=PT4wGPxWiRQ)

そこで本記事では、このSTEP通りに行えば、皆さんもGA4の最新のデータで分析が行えるようになるための方法を非エンジニア向けに説明いたします。今回利用するAIサービスはAnthropic社が提供しているClaudeになります。

![](https://claude.ai/images/claude_ogimage.png)

## 大まかな手順

1. Google クラウドプロジェクトの作成
2. APIの有効化
3. デジタルキーの作成
4. 認証情報ファイルのダウンロード
5. GA4に権限の付与
6. GA4からプロパティIDの取得
7. node.jsのインストール
8. Claude Desktopのインストール
9. Claude Desktopでの設定
10. 完了！

### 1.Google クラウドプロジェクトの作成

Google クラウドのアカウントを事前に作成しておきましょう。以下、記事などを参考にするとよいでしょう。クレジットカードの情報登録は必ずしも必要ありません。すでに作成済みでアカウントをお持ちの場合は、そのまま利用できます。

![](https://devio2023-media.developers.io/wp-content/uploads/2023/09/eyecatch_GoogleCloud_1200x630.png)

Google Cloudの始め方（アカウント作成編） | DevelopersIO

作成後、Google Cloud Consoleにアクセスしてください。[Google Cloud Platform](https://console.cloud.google.com/)

[

Google Cloud Platform lets you build, deploy, and scale applications, websites, and services on the same infrastructure as Google.

console.cloud.google.com

](https://console.cloud.google.com/)

Google Cloudロゴの右側にあるボックスをクリックして、「新しいプロジェクト」を選んでください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-1024x287.png)

プロジェクト名を入れて、「作成」を押してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-1.png)

数秒で作成されますので、作成されたら該当プロジェクトを選択してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-2-1024x328.png)

### 2.APIの有効化

左側のメニューから「APIとサービス」＞「ライブラリ」を選択してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-3.png)

検索ボックスで「Google Analytics Data API」と入れて検索をしてください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-4-1024x627.png)

Google Analytics Data APIを選択して、「有効にする」を押します。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-5.png)

### 3.デジタルキーの作成

左上のナビゲーションメニューから「IAMと管理」＞「サービスアカウント」を選択してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-6.png)

「＋サービスアカウントを作成」を選択してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-7.png)

サービスアカウント名を入れて、「作成して続行」を押してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-8.png)

STEP2とSTEP3はそのまま省略し「完了」を押します。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-9.png)

### 4.認証情報ファイルのダウンロード

サービスアカウント名（claude-analytics-access 以下略）となっている部分を選択してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-10-1024x316.png)

上部メニューから「鍵」を選択し、ページ下部にある「キーを追加＞新しい鍵を作成」を選択します。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-11-1024x799.png)

JSON形式を選び「作成」を押します。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-12.png)

作成されたファイルが自動でダウンロードされます。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-13.png)

今後、このファイルを使うためにわかりやすい場所（例：ドキュメントフォルダ）にうつしておきます。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-14.png)

### 5.GA4に権限付与

ダウンロードされたJSONファイルをテキストエディタ（メモ帳など）で開いて、client\_emailのところに含まれているメールアドレス（下記画像の青ハイライト部分）をコピーしてください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-15-1024x463.png)

コピーしたメールアドレスに対してGA4で「アナリスト」権限を付与します。GA4で権限を付与したいプロパティを選択し、「管理＞プロパティのアクセス管理」を選んでください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-16-1024x467.png)

先ほどのメールアドレスを貼りつけ、権限を付与します。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-17-1024x807.png)

### 6.GA4からプロパティIDを取得

管理＞プロパティ＞プロパティの詳細を選択してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-18-1024x423.png)

右上に表示されているプロパティ IDをコピーしてください。G-からはじまる測定IDを混同しないようにしましょう。

### 7.node.jsのインストール

nodejs.orgにアクセスしてください。

![](https://nodejs.org/en/next-data/og/announcement/Node.js%20%E2%80%94%20Run%20JavaScript%20Everywhere)

Node.js — Run JavaScript Everywhere

上のメニューから「ダウンロード」を選択し、自分が使っているOSを選んでください。Versionに関しては「LTS」とついている最新のバージョンを選択し、ページ下部にあるインストーラーをクリックします。

下記の例であれば「Windows」用のNode.js「v22.17.1(LTS)」を選んだ後に、ページ下部にある「Windows インストーラー (.msi)」を選択します。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-19-1024x772.png)

ダウンロードが完了したら、ファイルを実行。特に何も変更せずインストールを進めてください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-20.png)

### 8.Claude Desktopのインストール

Claudeのダウンロードページに移動してください。

![](https://claude.ai/images/claude_ogimage.png)

Download Claude

WindowsあるいはmacOSを選んでダウンロードをしてください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-21.png)

Claudeのアカウントを持っていない場合は事前に作成しておきましょう。

![](https://claude.ai/images/claude_ogimage.png)

下記画面から、アカウントを作成できます。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-22.png)

### 9.Claude Desktopの設定

Claude Desktopがインストールされたら起動をして、左上のハンバーガーメニューから「ファイル＞設定」と選びます。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-23.png)

設定内にある「開発者」を選び、「設定を編集」を押してください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-24-1024x908.png)

エクスプローラーが表示されますので、「claude\_desktop\_config.json」というファイルをメモ帳で開いてください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-25.png)

メモ帳の中身を以下の通り編集していきます。

A)以下内容に差し替えをしてください。（開いた時には{}」としか書いていないので、それを差し替えます）。

```
{
"mcpServers": {
"google-analytics": {
"command": "npx",
"args": ["-y", "mcp-server-google-analytics"],
"env": {
"GOOGLE_CLIENT_EMAIL": "your-service-account@project.iam.gserviceaccount.com",
"GOOGLE_PRIVATE_KEY": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----",
"GA_PROPERTY_ID": "123456789"
}
}
}
}
```

B)GOOGLE\_CLIENT\_EMAILの部分をSTEP5で作成したjsonファイルの中身と差し替えます。

“your-service-account@project.iam.gserviceaccount.com”  
↓  
“claude-analytics-access-2@claude-ga4-connection-2.iam.gserviceaccount.com”

C)GOOGLE\_PRIVATE\_KEYの部分をSTEP5で作成したJSONファイル内にあるprivate\_keyと差し替えます。

“—–BEGIN PRIVATE KEY—–\\nYOUR\_PRIVATE\_KEY\_HERE\\n—–END PRIVATE KEY—–“  
↓  
“—–BEGIN PRIVATE KEY—–\\nMIIEvQIBADANBgkqhkiG9（中略）FqyNgfwfoXobOf+hY5DNXthV\\nEZNwc1++1mDnMuwlmJlullw=\\n—–END PRIVATE KEY—–\\n

D)GA\_PROPERTY\_IDの部分をSTEP6で取得したプロパティIDと差し替えます

“123456789”  
↓  
“308259408”  

ファイルを保存し、Cluade Desktopを閉じてください。

タスクマネージャーでも確認し、残っている場合は、「タスクの終了」を選んでください。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-26.png)

Ctrl+Shift+escで起動。Claudeを右クリックて「タスクの終了」を選択

### 10.完了！

Claude Desktopを再度立ち上げます。「ファイル＞コネクタ」を確認し、google-analyticsがローカルで追加されていれば設定終了です。お疲れ様でした。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-27-1024x596.png)

後は「新規チャット」を開き、日本語で指示をしてみましょう。

![](https://www.ga4.guide/wp-content/uploads/2025/07/image-28-1024x758.png)

## 最後に

今回はGAのMCPサーバーを利用し、GA4とCaludeを連携してデータを取得してくる方法を紹介いたしました。データの精度やどういったことを聞けばよいかは、次回の記事で検証してみようと思います。

今回の内容が皆さんの分析の敷居を下げるものになることを願っています。