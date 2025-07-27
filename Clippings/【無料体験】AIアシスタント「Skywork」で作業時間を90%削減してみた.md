---
title: "【無料体験】AIアシスタント「Skywork」で作業時間を90%削減してみた"
source: "https://qiita.com/tomada/items/1b0e2a231322ea33f9fb"
author:
  - "[[tomada]]"
published: 2025-07-18
created: 2025-07-27
description: "こんにちは、とまだです。 先日、YouTubeでAI関連の動画を見ていたら、Skywork というツールの紹介が流れてきました。 すごく簡単にいうと、資料作成をサクッとAIに任せられるサービスです。 他にも以前から似たようなサービスはいくつかありましたが、Skywork ..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## エンジニアとしての市場価値を測りませんか？PR

[無料でForkwellに登録する](https://lp.recruiting.forkwell.com/scout?argument=249xHStF&dmai=a67f4ef09e582b)

こんにちは、とまだです。

先日、YouTubeでAI関連の動画を見ていたら、 [Skywork](https://skywork.ai/p/VsQJZI) というツールの紹介が流れてきました。

すごく簡単にいうと、資料作成をサクッとAIに任せられるサービスです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/cfe9114e-22ac-43b2-8c4e-68088559e7cd.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fcfe9114e-22ac-43b2-8c4e-68088559e7cd.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2b7b0e5dc9262816066b0b90bc83274d)

他にも以前から似たようなサービスはいくつかありましたが、Skywork は **「ビジュアルがきれい」「出典付きで信頼性が高い」「無料クレジットがもらえる」** といった点が特に魅力的でした。

特に見た目はなかなか良く、後述しますが以下のようなプレゼン資料が簡単に作成できます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/7fa49aec-d0a5-4e3c-944e-28f60f83b3ce.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F7fa49aec-d0a5-4e3c-944e-28f60f83b3ce.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=30fc12105e37f78dc3c25b375287a8ed)

今後、資料を作るなら割と使えるのではないかと思い、早速試してみました。

今回は、個人的に好きじゃない仕事の筆頭である **「ドキュメント」「スライド」「スプレッドシート」** の 3 つの機能を使って、受託開発の提案資料を作成してみます。

体感ですが、資料作成時間を9割ぐらい短縮できるんじゃないかなという所感です。

## 時間がない人向けに総括

- Skywork は **AI を使って資料作成を効率化** するサービス
- ドキュメント機能では **出典付きで信頼性の高い情報** を集めてくれた
- スライド機能では **ビジュアルがきれいでわかりやすい** プレゼン資料を作成できた
- スプレッドシート機能では詳細な見積もりや比較資料を簡単に作成できた
- MCP にも対応しているようなので、AI を使った効率化に真剣な印象

## Skywork とは？

先述の通り、Skywork は AI を使って資料作成を効率化するサービスです。

[Skywork](https://skywork.ai/p/VsQJZI) の公式ホームページによると、以下のような機能を持っているようです。

- ドキュメント作成
- プレゼンテーション資料作成
- スプレッドシート作成
- Webページ作成
- ポッドキャスト作成
- AIチャット

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/442e8959-e183-4143-97c6-1e354cf8d7df.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F442e8959-e183-4143-97c6-1e354cf8d7df.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=81ba04453c8aef1fae174e90d7691f62)

ドキュメント作成やWebページ作成などは対応できるツールも多くなってきましたし、一部ではプレゼン資料などもAIが作成できるようになっています。

ただ、これだけの機能を一つのサービスで提供しているのは珍しいと思います。  
（知らないだけだったらすみません）

また、同じく公式ホームページで公開しているベンチマークによると、 **情報の正確性も売り** にしているようです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/6f2266d1-6d91-4c28-9e61-ad0c297c9a2f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F6f2266d1-6d91-4c28-9e61-ad0c297c9a2f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b371a50ce44679a5a8d8e7e169b3084b)

AI に資料を作らせると、出典が怪しいことがあります。

それを回避するため、私は先に Claude や Gemini のリサーチ機能を使って情報を集めてから資料作成をしていたので手間や待ち時間がかかっていました。

ただ、Skywork は最初から **出典付きで情報を提供** してくれるので、調査の手間が大幅に減りそうです。

試してみたところ、このあたりが特にすごかったので実際の使い方を紹介します。

なお余談ですが、Skywork では **MCP サーバも公式で公開** してくれているようです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/a4dcaeab-1c28-4ae6-9b1a-28306f9468eb.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fa4dcaeab-1c28-4ae6-9b1a-28306f9468eb.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=23408b44ec2bcaa8abb78f211c791e60)

このあたりから、AI を使って効率化していくことに対する真剣さが伝わってきますね。  
（機会があれば別記事で試してみたいと思います）

## よくある「WordPress構築」の提案資料作成

フリーランスや受託開発でWeb制作をしていると、クライアントからこんな依頼を受けることが多いです。

「企業サイトをリニューアルしたい。WordPressで作って、社内で更新できるようにしてほしい」

そして、提案資料には必ずこんな内容を含める必要があります。

- システム構成（AWSのインフラ構成図）
- 概算見積もり（初期費用と運用費用）
- 開発スケジュール
- WordPressのカスタマイズ内容
- セキュリティ対策
- 保守運用の体制

正直、これを一から作るのはなかなか大変です。

私はプログラミングやシステム構築は好きですが、資料を作るのは **正直嫌い** です。

特に、AWSの料金計算とか、最新のセキュリティ対策の情報を調べるのに時間がかかるんですよね。  
その割に絶対に間違えてはいけない部分でもあるので、慎重に調べる必要があります。

そこで、Skyworkを使ってこの提案資料を作成してみることにしました。

※今回は架空のクライアントを想定して実際の案件ではありませんが、私が作成したことのある資料の内容をベースにしています。

## まずは無料登録

会員登録はメールアドレスや Google アカウントなどでサクッとできます。

早速、会員登録すると **500 クレジットが無料でもらえました** 。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/99834385-91a6-4b1e-acb8-84f08d75e11e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F99834385-91a6-4b1e-acb8-84f08d75e11e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=94a0751210fd6cb5aae0a89b7b4cea9a)

ちなみに、Free プランでも **毎日 500 クレジットもらえる** そうです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/1fda9d76-293c-44e3-9614-ba419315cb20.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F1fda9d76-293c-44e3-9614-ba419315cb20.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=429abf9be75fadb7688007ab1ef9fdea)

よさそうであれば今後も使っていきたいと思っているので、今回はちゃんと試せるようクレジットたっぷりで使ってみました。

## Documents機能で調査レポート作成

最初に、Documents 機能を使って基本的な調査資料を作ってみます。

### ドキュメントのプロンプトを入力

ドキュメントを作成するモードだと、以下のような画面です。  
今更ですが、日本語にも対応しているのはありがたいですね。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/a9194771-eea5-4e9b-8680-a832f31ff7c8.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fa9194771-eea5-4e9b-8680-a832f31ff7c8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fbe4995180e84c9e757a79c0f0b11a5c)

入力したプロンプトはこんな感じです。

```text
企業向けWordPressサイト構築について、以下の内容で提案資料のベースとなる調査レポートを作成してください。
冗長構成は考慮せず、シンプルでコストを抑えた構成を前提とします。

1. AWSを使用したWordPress環境の構築方法
   - EC2、RDS、S3を使用した構成
   - 推奨スペックと料金試算

2. WordPressの企業サイト向けカスタマイズ
   - 必要なプラグイン一覧
   - 権限管理の設定

3. 概算費用
   - 初期構築費用の相場
   - 月額運用費用（AWS費用含む）
   - 保守費用の目安

具体的な数値や最新の情報を含めて、出典も明記してください。
```

ちなみにこの時、モードを選べるみたいです

通常のドキュメントはもちろん、マニュアル作成やブログ記事まで広く対応しています。

プロンプトを細かく指定しなくても目的に応じたモードを選ぶだけで、AI での資料作成に慣れていない人でも使いやすいのはありがたいですね。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/1d83ad5b-8905-4f8d-aa2c-8a0ae0abd037.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F1d83ad5b-8905-4f8d-aa2c-8a0ae0abd037.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b026af6baa0a0074d71e5aedc7ea0c25)

今回はデフォルトの「汎用」モードでいきます。

### 資料作成中の状況

資料作成を依頼すると、最初にタスクを計画しつつ、調査をスタートしたみたいです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/6c60dcd3-496a-4dc2-a9aa-4f23d6a1d85b.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F6c60dcd3-496a-4dc2-a9aa-4f23d6a1d85b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=53551c492b5ae1d6de01bff879c08e7d)

Skywork が自分で判断して MCP を使ってWeb検索を行い、情報を集めているようです。

調査内容も途中で確認できるのですが、しっかりと AWS 公式サイトの料金ページや、一般サイトの情報をかき集めてくれている様子がみてとれます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/ccd1dec9-033a-4706-bd6b-775fd3398743.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fccd1dec9-033a-4706-bd6b-775fd3398743.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=654b2eb8ab7ac3dfd1fd1a518c7de002)

適当な AI が情報収集すると、誰かが勝手に書いた情報をあたかも正しいかのように判断することも多いのですが、 **ちゃんと公式サイトを参照している** のは安心感があります。

また、思考過程を表示してくれるので、おかしいと思ったら一時停止して、指示を修正することもできます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/ea47e943-feed-4066-bfd2-606f1c2c2ae9.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fea47e943-feed-4066-bfd2-606f1c2c2ae9.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f875ee40d98d05dff838fcd804e8c3d3)

今回は特に修正も必要なかったので、そのまま待つことにしました。

### 約10分で充実したレポートが完成

待つこと約 10 分。レポートが出来上がったようです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/1b0808b0-31e6-4f82-adea-661856480abc.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F1b0808b0-31e6-4f82-adea-661856480abc.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=bc1b128953ed994ca55168739b7b7dad)

今回は Deep Research として、実に **213 ページ** を参照したとのことです。

数十ページにわたる詳細なレポートができあがりました。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/e10a0fd7-b380-4ff1-8799-755e53dea93f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fe10a0fd7-b380-4ff1-8799-755e53dea93f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ac98b83db8e201c8a9855d5035024acf)

ワードや PDF、HTML 形式でダウンロードできるので、必要に応じて使い分けられます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/8457e131-78e7-4fed-afcc-f67024ad70c3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F8457e131-78e7-4fed-afcc-f67024ad70c3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a9329bc441150a7543adb4a9ebe44ece)

### 生成されたドキュメントの中身を確認

内容を確認してみましょう。

かなり長かったので特にすごかったところを抜粋していきますと、こんな感じで推奨スペックにもとづき料金の試算をグラフィカルに資料化してくれます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/8d3c212d-a26a-4afd-a88d-41bf621ea4a9.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F8d3c212d-a26a-4afd-a88d-41bf621ea4a9.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=be4a2948e8b7ce025cde3cdc145a0f2f)

テーブルも見やすく整形されていて、必要な情報が整理されています。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/a36149a8-389f-485d-a77d-3ec40ebdd47f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fa36149a8-389f-485d-a77d-3ec40ebdd47f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2cccfc824559cffc14109e18339aa50f)

ちなみに、青い文字の部分はすべて出典のリンクがついています。

いくつかサンプリングしてみましたが、すべて **公式の AWS の料金ページなどと相違なく、最新の情報が反映** されていました。

資料内の情報と、実際の AWS の料金ページを比較してみたところ、以下のように一致していました。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/c4afa250-fef1-4a3a-a631-62bcc2cb6898.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fc4afa250-fef1-4a3a-a631-62bcc2cb6898.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=73be8ce05eeb741b9aa9da80e2127593)

これだけでも、個人的には資料作成の手間が大幅に減るので、かなり助かります。

あとは、構築費用の相場なんかも調べてくれます。

どうしても確からしい情報を集めるのが難しいのですが、Skywork は **しっかりと出典を明記してくれた上で、客観的に情報をまとめてくれます** 。

もう **社内の意思決定ぐらいだったら、これをそのまま使ってもいいレベル** です。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/e9a8c00a-599c-4720-88c4-7d583ababaf3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fe9a8c00a-599c-4720-88c4-7d583ababaf3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=db870e20e477a97a00d74512d16260df)

そしてレポートの一番最後には、すべての出典がまとめられています。

「この情報はどこから？」と聞かれても、すぐに答えられますので、 **クライアントからの質問にも安心して対応** できます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/b6c55a18-63d4-49ef-a701-4345cd854757.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fb6c55a18-63d4-49ef-a701-4345cd854757.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a226ca7753c85aff5fcb8bf3bf3e7498)

余談ですが、先述の通り HTML 形式でダウンロードすることもできます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/db0256e4-76a4-471a-8cf3-7ff359b16288.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fdb0256e4-76a4-471a-8cf3-7ff359b16288.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d1a895c8cbcf6ae3cc7812b8c0f042fd)

ちょっとグラフや体裁などを調整したいなという場合には、生成 AI を使ってサクッと修正できるのもありがたいところです。

### ドキュメントを作ってみた所感

ひとまずドキュメント作成を試してみた所感として、良かった点はこんな感じです。

- **出典付きで信頼性が高い情報** を集めてくれる
- **資料の構成がしっかりしていて、社内レベルならそのまま使える**
- **料金試算や構成図など、人間がやると面倒な部分を自動化** してくれる

逆にちょっと気になった点は以下の通りです。

- 生成されたレポートはそのまま使うには情報量が多すぎる
- クライアントなどに提出するのであれば、情報を取捨選択した方が良い

とはいえ、基本的には「削る」方向で調整すればいいので、資料作成の手間は大幅に減ります。

### 補足： ドキュメントの修正依頼も可能

なお、気になる点があればチャットで修正依頼を投げることもできます。

図が崩れていたり、情報を追加・削除したい場合は、以下のようにチャットで指示を出せば、Skywork が自動で修正してくれるようです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/c28c6f13-6638-49ed-8eec-06f14bd1455a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fc28c6f13-6638-49ed-8eec-06f14bd1455a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9b2a058d21fcf46821d20b53426a31d4)

（今回は省略）

## スライド機能でプレゼン資料化

次に、同じような内容でプレゼン資料を作ってみます。

### ナレッジベースに登録

せっかくなので、先ほど作成されたドキュメントを **ナレッジベース** として登録しておきます。

プロンプトの中で内部情報を記載してもいいんですが、資料をナレッジベースとして登録しておくと、次回以降の提案資料作成時に自動で参照してくれるようです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/ad1cd206-eff3-4a95-8d69-0dbda269896d.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fad1cd206-eff3-4a95-8d69-0dbda269896d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=04e3ab804632778bb5f68f9677df96b3)

過去の案件や社内のベストプラクティスを蓄積しておくことで、 **さらに効率的な資料作成** ができそうですね。

### プレゼン資料のプロンプトを入力

では、こちらをもとにプレゼン資料を作成してみます。

```text
ナレッジベースを参照して、企業向けの WordPress サイト構築に関するプレゼン資料を作成してください。
以下の内容を含めてください。

## 対象
中小企業の経営者・ Web 担当者

## 枚数
4〜6 枚程度

## 目的
WordPress + AWS による企業サイト構築のメリットを伝える

## 構成
1. 現状の課題（古いサイトの問題点）
2. WordPress + AWS による解決策
3. システム構成図（わかりやすく）
4. 実装機能の説明
5. セキュリティ対策
6. 費用とスケジュール

## 制約事項
技術的な説明は最小限にして、メリットを中心に説明してください。
また、文字を多くせず、ビジュアル重視でお願いします。
```

先ほどのドキュメントではかなり詳細な情報が集まっているので、今回はビジュアル重視で簡潔なスライドを目指します。  
また、あまりに長くなりすぎないように、4〜6枚程度で収めるようにしました。

おそらく、本来であれば「企業向けのWordPressサイト構築プレゼン資料」と書く程度でもそれなりのスライドが作られるので、それを修正していく形でも全然良いと思います。  
ただ、最初からある程度の構成を指定しておくと、AIも意図を汲み取りやすいようです。

ちなみにですが、ナレッジベースの中でも参照すべき資料を明示的に指定できるようです。  
ファイル単位で指定することもできますので、複数案が混在している場合などは、特定の資料を参照するように指定しておくと良いでしょう。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/27582f44-2d36-4761-9853-7b6df30df98f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F27582f44-2d36-4761-9853-7b6df30df98f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5d2178e5e584adbcaee5c130c272ac65)

### スライド作成中の状況

では、早速スライドを作成してもらいます。

途中経過を見ていると、えぐい量のWeb検索や検討が挟まっています。  
（自分であればやりたくない...）

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/3e7c8534-9838-4103-b8fb-d18c1fdf48b4.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F3e7c8534-9838-4103-b8fb-d18c1fdf48b4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=62e6f9b2bd09b13e7dde8ec9d28c5f3f)

10分ぐらいでしょうか？作成されたようなので見てみましょう。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/0064616a-eb1f-424c-b21d-4ea0a8a1bbb1.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F0064616a-eb1f-424c-b21d-4ea0a8a1bbb1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=af924a9fc9c3de71fcf2a813af7882d9)

スライドも色んな形式でダウンロードできます。  
PDFやPowerPoint、Googleスライド形式など、用途に応じて選べます。

私は最近、個人的な資料を作るなら Google スライドを使うことが多いので、Google スライド形式に最初から対応しているのはありがたいです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/6e0ab37f-5857-4bcc-a164-c23b671eda35.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F6e0ab37f-5857-4bcc-a164-c23b671eda35.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4174db7ac354646a7531e2896be54e83)

### 生成されたスライドの中身を確認

それでは、中身を見てみましょう。

まず、トップページはこんな感じです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/584ab86e-48a5-4134-9866-f3481cbb416d.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F584ab86e-48a5-4134-9866-f3481cbb416d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b3b96a1a1b1ca0b9238362884c8f6775)

アイコン付きで、ちゃんと色分けやレイアウト調整もされています。

パッと見ただけでも、ビジュアル的にわかりやすいです。

2ページ目は現状の課題を整理しています。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/4ab40f68-e6bd-4b83-852a-fd2a03424f45.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F4ab40f68-e6bd-4b83-852a-fd2a03424f45.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9e453b2f05741114781ca1706fe9ab5d)

ただ文字を並べるのではなく、カード形式で情報を整理したり、見出しをつけたり、リード文を入れたりと、視覚的にわかりやすくなっているのが良いですね。

次はシステム構成図です。  
残念ながら、こういった図はAIにとって難しい部分もあるようで、少し崩れています。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/088193e8-27be-4bf9-b8e9-38250dde4335.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F088193e8-27be-4bf9-b8e9-38250dde4335.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c04a8f1bf65ab9aa922a901ea0296669)

とはいえ、システム構成図を書けるツールは無料でもたくさんありますし、企業で使うなら過去のプレゼン資料からコピペできることも多いでしょう。  
また、ベースとしてある程度のレイアウトを自動で作ってくれるので、調整すれば済むレベルかと思います。

少し飛びまして「費用とスケジュール」のページです。

こちらはグラフやタイムラインを使って、ぱっと見てわかるように整理されています。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/894e91ad-53b7-41b5-8814-e154d37f468f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F894e91ad-53b7-41b5-8814-e154d37f468f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=40ebb262b0d2efd2386f80460b1145f0)

おそらくは、ある程度パターン化されたレイアウト情報をもとに、Skyworkが自動でレイアウトを調整してくれたのでしょうかね。

こういったレイアウトは知っていれば発想として引き出しから出てくるのですが、私は「どうやって見せるのがいいんだろう？」と悩むことが多いです。

その点、Skyworkは最初からビジュアル的にわかりやすいレイアウトを提供してくれるので、資料作成のハードルが下がります。

### プレゼン資料を作ってみた所感

Skyworkを使ってプレゼン資料を作成してみた感想をまとめておきます。

良かった点は以下の通りです。

- ビジュアルがきれいで見やすい
- 情報が整理されていてわかりやすい
- 配色やレイアウトが統一されていてプロっぽい
- レイアウトパターンが豊富

逆に気になった点は以下の通りです。

- ごく一部ながら文字崩れの手直しは必要
- システム構成図など、AIにとって自由度が高い部分は手直しが必要
- とはいえ「見せ方」のベースは作ってくれるので調整は楽

一部調整は必要なものの、 **資料作りが上手い人がドラフトで作ってくれた** 感があるのがすごいと思いました。

プレゼン資料作りは個人的に苦手な仕事の筆頭です。  
そのため頑張って作っても自信を持てないことが多いのですが、Skyworkの資料ならそのままクライアントに提出しても問題ないレベルです。  
（繰り返しになりますが、内容の精査や調整は必要です）

### 生成されたスライド一覧

せっかくなので、生成された資料を全部スクショで残しておきます。

興味があれば、折りたたみを開いてご覧ください。

生成されたスライド一覧

### スライド1: トップ

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/584ab86e-48a5-4134-9866-f3481cbb416d.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F584ab86e-48a5-4134-9866-f3481cbb416d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b3b96a1a1b1ca0b9238362884c8f6775)

### スライド2: 現状の課題

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/4ab40f68-e6bd-4b83-852a-fd2a03424f45.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F4ab40f68-e6bd-4b83-852a-fd2a03424f45.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9e453b2f05741114781ca1706fe9ab5d)

### スライド3: WordPress + AWS でお悩み解決

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/761de573-41ac-4ee4-9884-9de38c04b2f1.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F761de573-41ac-4ee4-9884-9de38c04b2f1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=33631f830521311fdda40c4b3cab5f60)

### スライド4: システム構成図

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/088193e8-27be-4bf9-b8e9-38250dde4335.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F088193e8-27be-4bf9-b8e9-38250dde4335.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c04a8f1bf65ab9aa922a901ea0296669)

### スライド5: 実装機能の説明

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/a921370d-3a17-472c-84ca-24090444d4f5.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fa921370d-3a17-472c-84ca-24090444d4f5.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=22442efa9500351ac121939f954f0b73)

### スライド6: セキュリティ対策

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/7fa49aec-d0a5-4e3c-944e-28f60f83b3ce.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F7fa49aec-d0a5-4e3c-944e-28f60f83b3ce.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=30fc12105e37f78dc3c25b375287a8ed)

### スライド7: 費用とスケジュール

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/894e91ad-53b7-41b5-8814-e154d37f468f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F894e91ad-53b7-41b5-8814-e154d37f468f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=40ebb262b0d2efd2386f80460b1145f0)

## スプレッドシート機能で詳細見積もり作成

最後に、Skyworkのスプレッドシート機能を使って、詳細な見積もりと比較資料を作成してみます。

プレゼン資料でも十分な内容でしたが、実際に契約に進むためには、詳細な見積もりや比較資料が必要です。

そういった資料は Excel や Google スプレッドシートで作成することが多いですが、Skyworkはそのあたりも対応しているようですのでやってみましょう。

### スプレッドシート用のプロンプトを入力

今回は以下のようなプロンプトを入力しました。

```text
WordPress企業サイト構築の詳細見積もりと比較資料を作成してください。

シート1：詳細見積もり
- 作業項目別の工数と単価
- AWSの初年度費用試算
- オプション機能の価格表

シート2：ホスティング比較
- AWS vs レンタルサーバー vs WordPress.com
- 機能、性能、価格の比較表

シート3：プラグイン比較
- セキュリティ、SEO、バックアップの主要プラグイン比較
- 無料版と有料版の違い
```

また、ここまでの内容と齟齬が出ないよう、作成してもらったドキュメントとスライドをナレッジベースとして登録しておきました。

AI で資料作りをしていると、どうしても情報の整合性が取れなくなることがありますので、ナレッジベースを活用して情報の一貫性を保つのは良い方法だと思います。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/a7d67c70-fc47-424a-ae45-e8617e8ec1df.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2Fa7d67c70-fc47-424a-ae45-e8617e8ec1df.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=0513c88d25b364f381dd641707f2ac4c)

### スプレッドシートの確認

しばらく待つと、スプレッドシートが完成しました。

今回は `.xlsx` または `.html` 形式でダウンロードできるようですので `.xlsx` 形式でダウンロードしてみます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/827e49b4-5a6c-4e68-9c63-07ce687c0e59.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F827e49b4-5a6c-4e68-9c63-07ce687c0e59.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c5a99915c8f6fcf7f6defbc779d9f04b)

それでは、生成されたスプレッドシートの中身を確認してみましょう。

指定した通り、3つのシートが作成されています。

1. 詳細見積もり
2. ホスティング比較
3. プラグイン比較

一番メインの「詳細見積もり」シートを見てみましょう。

「初期構築費用」「AWS月額費用試算」「運用保守オプション費用」など、必要な項目がしっかりと整理されています。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/364501/14186e6e-db6f-4fd1-81e7-e2789d762d14.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F364501%2F14186e6e-db6f-4fd1-81e7-e2789d762d14.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5735e7afd6a9c12882e0c0e820881086)

地味に、各項目について色付きのヘッダーを付けていたり、セルごとに交互の色が付いていたりと、見やすい工夫がされています。

また、備考欄にすでに詳しく説明が書かれているのもありがたいです。

今回はデータの出典などは特にプロンプトで指示はしなかったのですが、料金などの出典元を明記するように指示しておくと、さらに安心感が増すと思います。

### スプレッドシート機能を使ってみた所感

Skyworkのスプレッドシート機能を使ってみた感想をまとめます。

- 作業項目ごとに詳細な見積もりが自動で作成される
- 比較資料が簡単に作れる
- 備考や内容説明など、文章も同時に書いてくれるので資料としてそのまま使いやすい

個人的にはあまり気になる点はありませんでした。

実務で使う場合には、定型的なフォーマットに合わせて調整する必要があるかもしれませんが、基本的な内容はしっかりと作成されているので、あとは自分の会社のフォーマットに合わせるだけで済みます。

または、ナレッジベースに自社のフォーマットを登録しておくことで、次回以降は自動でそのフォーマットに合わせて作成してくれるかと思います。

## Skywork を実際に使ってみて感じたこと

実際に Skywork を使ってみた感想としては **「資料作りが得意な人」** と **「データ収集が得意な人」** が助けてくれるサービスだなと感じました。

私は正直、資料作成が苦手です。

コードを書くのは大好きなんですが、スライド作りなどは自由度が高すぎて急に手が止まってしまうタイプなんですよね。

「情報をどう配置すればいいんだろう」  
「この色使いで大丈夫かな」  
「グラフはどのタイプがわかりやすい？」

そんな悩みを抱えながら、いつも時間をかけて資料を作っていました。

一方、Skywork ならそのあたりをドラフトで作ってくれるので、あとは自分の意図に合わせて調整するだけで済みます。

### Deep Research の安心感がすごい

もう一つ良かったと思うのが、 **出典の正確さ** です。

AI に資料を作らせると、たまに「この情報、本当に正しいの？」と思うことがあります。

その点、Skywork だと **ちゃんと出典を明記** してくれますので、ファクトチェックも安心です。

試しにいくつかクリックしてみたら、ちゃんと AWS の公式ページや信頼できるサイトにつながっていたので、自分で調べる際にも安心感があります。

流石に全部を信頼するのは危険なので、最終的には自分で確認する必要がありますが、Skywork が提供してくれる情報をベースにすれば、 **かなりの時間を節約** できそうです。

### 時間の使い方が変わりそう

今回、3 つの資料を作るのに手を動かした時間は合計で **約 30 分程度** でした。

もし自分でゼロから作るとしたら、おそらく **半日はかかっていた** と思います。

- 情報収集：2 時間
- ドキュメント作成：1 時間
- プレゼン資料作成：2 時間（デザインで悩む）
- 見積もり作成：1 時間

資料は中身が大事なのはもちろんですが、個人的には見せ方やデザインも重要だと思っています。

そのあたりに時間をかけるのは正直もったいないと思っているので、そこを Skywork に任せられるのは **大きなメリット** です。

### 一部だけ自分で頑張る必要もある

もちろん、完璧なツールではありません。

システム構成図やレイアウトが一部崩れていたり、ドキュメントの場合は生成される情報量が多すぎて取捨選択が必要だったりします。

ですが、 **「ゼロから作る」のと「調整だけ」** では大違いです。

資料作成が苦手な私からすると、ベースがあるだけでものすごく楽になります。

なお、今回はクレジット節約のためにあまり細かい調整はしませんでしたが、Skywork のチャット機能を使えば、生成された資料の修正依頼も可能です。

そのあたりをうまく活用すれば、自分で調整する手間も減らせるかもしれません。

## まとめ

Skywork は、こんな人におすすめかと思います。

- 資料をよく作る人
- 資料のデザインセンスに自信がない人（私のような）
- 情報の正確性を重視する人
- 調査に時間をかけたくない人

フリープランでも毎日ログインでクレジットをもらえるみたいなので、 **まずは無料で試してみてもいいかもしれません** 。

まだ試していない MCP や Web ページ作成機能もあるようなので、もう少し使い込んでみたいと思います。

一応、 [Skywork の公式サイト](https://skywork.ai/p/VsQJZI) も貼っておきます。

ちなみに概要を掴むだけなら、Weel の記事も参考になりますのでおすすめです。

[0](https://qiita.com/tomada/items/#comments)

コメント一覧へ移動

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Ftomada%2Fitems%2F1b0e2a231322ea33f9fb&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Ftomada%2Fitems%2F1b0e2a231322ea33f9fb&realm=qiita)

[21](https://qiita.com/tomada/items/1b0e2a231322ea33f9fb/likers)

8