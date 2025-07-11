---
title: "【生成AI】AIによるWebブラウザの自動操作を実現するには"
source: "https://qiita.com/ymd65536/items/1497a60c11ebe1d8dda5"
author:
  - "[[ymd65536]]"
published: 2025-07-04
created: 2025-07-10
description: "自分の言葉で書いています。 この記事で伝えたいこと（ポイント） ブラウザを操作する方法はたくさんある Microsoftの製品だけ生成AIによるブラウザ操作ができる 生成AIを使ったWebブラウザの自動操作はいろんな技術で可能 MCPやA2Aでも作り方次第でWe..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## Qiitaにログインして、便利な機能を使ってみませんか？

[ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fymd65536%2Fitems%2F1497a60c11ebe1d8dda5&realm=qiita) [新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fymd65536%2Fitems%2F1497a60c11ebe1d8dda5&realm=qiita)

自分の言葉で書いています。

## この記事で伝えたいこと（ポイント）

- ブラウザを操作する方法はたくさんある
- Microsoftの製品だけ生成AIによるブラウザ操作ができる
- 生成AIを使ったWebブラウザの自動操作はいろんな技術で可能
- MCPやA2Aでも作り方次第でWebブラウザの自動操作はいけちゃう

## はじめに

この記事ではAIによるWebブラウザ操作を実現する方法について  
[過去の登壇内容](https://speakerdeck.com/ymd65536/microsoftnoossdakedeainiyoruburauzatesutowogou-cheng-suru) を交えて解説する記事です。

まずはブラウザ操作について説明し、次にAIを使った場合をチェックしていきます。  
そして、どんなOSSがあったかを振り返りつつ、 MicrosoftのOSSだけでAIによるWebブラウザ操作や他のクラウド使ったブラウザ操作を実現する方法について解説します。

最後に最近話題のMCPやA2Aを取り入れた方法についてもみていきます。（余談程度）

## 定義：ブラウザ操作とは

Webオートメーションの分野でさまざまな文脈があります。どのような目的でブラウザ操作を実行するかによって意味が変わってきます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/527543/1396a850-bc24-4ecc-aa6b-207e7064c978.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F527543%2F1396a850-bc24-4ecc-aa6b-207e7064c978.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a8a72ea2565b6095f2afbc13210a1569)

筆者が考えるところによると、同じブラウザ操作でも `E2Eテスト` なのか `RPA` なのかで大きく異なると考えています。

ちなみに昔ながらのE2EテストではSeleniumがよく使われ、RPAにおいてはUiPathやWinActor、Power Automate Desktopなどが利用されます。

ただ、どちらにせよ技術的にはほぼ同じこと（ブラウザ操作）をやっているため、知らない人からすると同じように見えることがしばしばあります。

## 余談：古き良きブラウザ操作の手法・実装

ここで昔ながらのブラウザ操作について見ていこうと思います。

### Microsoftの製品で実現する方法

まずはMicrosoftの製品に近いものから紹介していくと主に3つあります。

- Playwrightを使ったブラウザ操作
- VBAとCOMを使ったInternet Explorer（IE）ブラウザの操作
- Windows32 APIを使ったブラウザ操作

2つ目のVBAとCOMを使ったInternet Explorer（IE）ブラウザの操作はIEがサポート終了していますのでこれはもはやないと言っても良いのですが

Microsoft EdgeにはIEモードというものがあり、これが2029年までサポートされるため、まだまだ活きているかもしれない手法になります。  
※IEモードの場合はCOMを使わない。Internet ExplorerServerを使う。  
※IEモードを使った方法については [過去に解説](https://qiita.com/ymd65536-ms/items/320f889e9fc35fe375f1) しています。

最後のWindows32 APIはブラウザというよりネイティブアプリケーションのUI操作に使われる方法です。 `OSを操作する` と言っても差し支えない方法です。

### 今でも使われていそうな方法

それ以外では有名なフレームワークとしてSeleniumを使う方法があったり、SeleniumのバックエンドにあるWebDriverに対して直接リクエストを送る方法があります。

- Seleniumと特定のプログラミング言語を使ったブラウザ操作
- WebDriverエンドポイントを使ったブラウザ操作

なお、WebDriverに対して直接リクエストを送ってブラウザを操作する方法については以下の記事で解説しています。

- [SeleniumなしでWebDriverを操作するには - Part1](https://zenn.dev/ymd65536/articles/e13f278a5d9803)
- [SeleniumなしでWebDriverを操作するには - Part2](https://zenn.dev/ymd65536/articles/0ab63cd4a41411)
- [SeleniumなしでWebDriverを操作するには - Part3](https://zenn.dev/ymd65536/articles/webdriver_without_selenium_part3)
- [SeleniumなしでWebDriverを操作するには - GenAI編](https://zenn.dev/ymd65536/articles/webdriver_without_selenium_genai)

### 以下、今は使われていないと思われる方法

もっと古き方法としては以下のようなテクニックがあります。（今でも使われているものもあり）

- ヘッドレス専用のブラウザ（PhantomJSなど）を使ったブラウザ操作
- AutoItを使ったブラウザ操作
- UWSCを使ったInternet Explorer（IE）ブラウザの操作

ヘッドレスブラウザというのは要するにUIが存在しないブラウザのことでレンダリングをしない分、通常のブラウザより動作が速いです。PhantomJSはヘッドレスブラウザとJavaScriptを使って自動化をするという試みでしたが、今はメンテナンスがされていません。  
（ちなみに当時はまだNode.js、サーバサイドJavaScriptという仕組みが確立されたばかりの時代でした。）

※その当時ですが、JavaScriptをサーバサイドで動く言語と表現したときは「 `JavaScript` はクライアントサイドの言語だろ」とよく言われたものです。

AutoItやUWSCもブラウザ操作ができますが、どちらかというと画面操作に特化した製品で独自の言語構造を持ったプログラミング言語でスクリプトを書くというものになっています。

とくにUWSCはPro版を契約すると書いたスクリプトをWindows環境であれば、どこでも実行できる実行可能形式に変換できます。  
※現在において、UWSCのサイトは閉鎖されており、利用は制限されています。

### さらに余談：とても古典的だけど今でもできる方法

VBAやUWSC、WebDriverによるブラウザ操作を体験した人の多くはお気づきかもしれませんが  
JavaScriptのコードをインジェクションすることによってブラウザを操作することも可能です。  
ただ、多くの場合、セキュリティでブロックされてしまうため、推奨される方法ではありません。

## AIによるブラウザ操作とは

では、AIによるブラウザ操作について見ていきましょう。

簡単に説明すると `自然言語（人が普段コミュニケーションに使う言葉）だけを使ってWebブラウザを自動で操作する` ということになります。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/527543/08495210-411c-468b-8b9c-c07c7b27f26e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F527543%2F08495210-411c-468b-8b9c-c07c7b27f26e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=52b75b5f30edda754e9a25f7cc91fb8a)

ブラウザの操作となると、技術的にはToolを呼び出すというということに等しいです。

### 余談：AIによるブラウザ操作って何がいいの

大きなところとしてたくさんのコードや実装を必要としないところと言えるでしょう。  
最低限の実装のみで済ませることができるとも言います。

必要最低限の処理のみをAIに教えて自然言語で実行するという手軽さが良い。

- 入力：要素の状態を取得、ページソースを取得
- 出力：クリック/選択/D&D、テキストを入力（ブラウザにテキストを出力）
- ウィンドウ操作：ウィンドウハンドルを取得、ウィンドウタイトルを取得
- パース：HTML、XML、JSON
- スクリプトの実行：JavaScriptの同期・非同期実行

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/527543/584ebc62-cd14-42ef-a7b3-740bfcce1d40.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F527543%2F584ebc62-cd14-42ef-a7b3-740bfcce1d40.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fcbb7f9c9994cdf210d1a226a80eaf68)

## 自然言語でブラウザ操作を実行する製品・OSS（紹介できる限り）

生成AIによるブラウザ操作は製品やOSSとしていくつか登場しており、今年の1月までの情報では以下の製品が登場していました。

- Open AI社からはOperator
	- [https://openai.com/ja-JP/index/introducing-operator/](https://openai.com/ja-JP/index/introducing-operator/)
- AnthropicからはComputer use (beta)
	- [https://docs.anthropic.com/en/docs/build-with-claude/computer-use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
- Google DeepMindからはProject Mariner
	- [https://deepmind.google/technologies/project-mariner/](https://deepmind.google/technologies/project-mariner/)

登壇資料公開時にはbrowser-useも流行していました。

- browser-use
	- [https://docs.browser-use.com/introduction](https://docs.browser-use.com/introduction)

最近（2025年7月4日）では `Nanobrowser` や `Playwright MCP` もあります。

- Nanobrowser - Open Source AI Web Agent
	- [https://nanobrowser.ai/](https://nanobrowser.ai/)
- Playwright MCP
	- [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

それ以外にも例えば、mabl社が自然言語によるテスト作成・アサーションなどを提供しています。  
参考： [Automated Testing Tool for AI Applications | mabl](https://www.mabl.com/ja/ai-application-testing)

それ以外にもAutifyやMagicPodなどさまざまです。

- Autify
	- [Autify Nexus - AIへのチャット指示とノーコード操作で誰でも自動テストを作成 - Autify(オーティファイ)](https://autify.jp/products/nexus)
- MagicPod
	- [MagicPod MCPサーバー（ベータ版）](https://support.magic-pod.com/hc/ja/articles/46186888063769-MagicPod-MCP%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC-%E3%83%99%E3%83%BC%E3%82%BF%E7%89%88)

## 生成AIによるブラウザ操作を実装する方法

既製品の紹介をいくつかしましたが、もっとフットワーク軽く実行したい場合は自分で作ることも可能です。いろんなフレームワークがありますが、生成AIによるブラウザ操作を実装するには以下の仕組みを用意すれば、なんでも良いです。

- プロンプト管理
- AIエージェントフレームワーク
- ブラウザ操作が実行できるフレームワークあるいはライブラリ

プロンプト管理についてはなくても動作しますが、運用保守の観点からあった方が良いです。では、具体例を見ていきましょう。

## 生成AIによるブラウザ操作を実装するその前に

AIによるブラウザ操作は見ていて楽しいところがありますが、AIに操作を指示して動かすため  
意図せぬ動作を引き起こすことがあります。安全のため、サンドボックス環境を構築して実行の確認を行うことを推奨します。

具体的には以下のとおりです。

- リモートサーバ上で実行する
- Dev Containerを使って実行する
- クラウド上でインスタンスを作成して実行する

いずれかの方法で実装するようにしてください。そうでない場合、サンドボックス環境ではない環境で動かす場合は自己責任でお願いします。

## MicrosoftのOSSだけでブラウザ操作を実行する

結論から述べるとPrompty、SemanticKernel、Playwrightの3つで開発できます。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/527543/563c84ab-6f04-4bc8-b231-5d675abebb0c.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F527543%2F563c84ab-6f04-4bc8-b231-5d675abebb0c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5f6c5047abd5ac00e760dbfafc7d5b81)

どんなOSSで実装するのか順番に見ていきましょう。

### Prompty

プロンプト管理に特化したOSSであり、YAML形式でAIの設定を記述してAIエージェントの設定として読み込めます。

公式サイトでは以下のように説明されています。（翻訳）

> Prompty は、開発者に可観測性、理解可能性、移植性を提供することを目的とした LLM プロンプトの資産クラスおよび形式です。主な目的は、開発者の内部ループを高速化することです。

公式サイト： [https://prompty.ai/](https://prompty.ai/)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/527543/30f56201-db0a-4ece-8dd0-104886e5cfc3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F527543%2F30f56201-db0a-4ece-8dd0-104886e5cfc3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=6ab6e3a5554072ec8db60ff6cbb0eea4)

概要はzennにまとめていますので入門したい人は以下のリンクを参照していただけますと幸いです。

[Promptyに入門したい](https://zenn.dev/ymd65536/articles/prompty_get_started_1)

### SemanticKernel

AIエージェント構築フレームワーク、Enterprise Readyです。  
LangChain的な立ち位置のフレームワークとよく説明されますが、Microsoft Learnでは次のように説明されています。

> AI エージェントを簡単に構築し、最新の AI モデルを C#、Python、または Java コードベースに統合できる、軽量のオープンソース開発キットです。 エンタープライズ レベルのソリューションを迅速に配信できる効率的なミドルウェアとして機能します。

引用： [SemanticKernelの概要 | Microsoft Learn](https://learn.microsoft.com/ja-jp/semantic-kernel/overview??wt.mc_id=MVP_357747)

### Playwright

さまざまなプラットフォームで動作するE2Eテストフレームワークです。

[Fast and reliable end-to-end testing for modern web apps | Playwright](https://playwright.dev/)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/527543/d8efc439-07a3-4860-bede-7548c4ac2b73.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F527543%2Fd8efc439-07a3-4860-bede-7548c4ac2b73.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d6607a1b6d7cd963c35c0702d39d753e)

Playwrightについては過去の登壇で何回か説明しているため、以下の資料を参照いただけたらと思います。

- [Microsoft Playwrightで始めるブラウザテスト - Speaker Deck](https://speakerdeck.com/ymd65536/microsoft-playwrightdeshi-meruburauzatesuto)
- [Microsoft Playwright Testing 再入門 - Speaker Deck](https://speakerdeck.com/ymd65536/microsoft-playwright-testing-zai-ru-men)

また、AzureにはPlaywrightの名前を冠する `Microsoft Playwright Testing` というサービスがあります。

## 3つのOSSを組み合わせて作ってみると？

作成したアプリケーションは以下のとおりです。

[SemanticBrowser](https://github.com/ymd65536/SemanticBrowser)

## 他の実装方法

- AWS SDKで実装する
- Vertex AI SDKで実装する

### AWS SDKで実装する

AWS SDKでは推論APIあたりを使うと実現できます。（他にも方法はありそう）

- 関数定義
- 関数のtoolSpecを作成
- Converse APIを渡して実行  
	※model\_Id、プロンプト、toolconfig、inferrence\_configが必要

実際に実装した内容について過去の登壇で紹介しています。

参考： [Amazon Bedrockでブラウザを操作するAIエージェントを作ってみた](https://speakerdeck.com/ymd65536/amazon-bedrockdeburauzawocao-zuo-suruaiezientowozuo-tutemita)

デモ動画もあります。  
[第159回 雲勉 Amazon Bedrock でブラウザを操作する AI エージェントを作ってみた](https://www.youtube.com/watch?v=c3vdlpFceVA)

※AWS Summit 2025の弊社のブースでも紹介されました。

### Vertex AI SDKで実装する

Flash系のモデルで以下の3ステップを実行できるようにすれば良いです。

- 関数定義
- FunctionDeclarationで定義した関数を登録
- generate\_contentでレスポンスを取得

※Vertex AI SDKは移行ガイドが示されており、これから非推奨となります。新しく作る場合は `Google Gen AI SDK ` を推奨します。

公式ドキュメントでは以下のように説明されています。

> Vertex AI SDK の生成 AI モジュールは非推奨になり、2026 年 6 月 24 日以降は使用できなくなります。Google Gen AI SDK には Vertex AI SDK のすべての機能が含まれており、多くの追加機能をサポートしています。

参考： [Vertex AI SDK 移行ガイド | Generative AI on Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk?hl=ja)

## モダンにしていく

最近はMCPやA2Aなどサーバを別で構築してエージェントを手軽に動かす方法が主流になりつつあります。最後にMCPやA2Aで実装する方法について見ていきましょう。

## MCPで実装する

MCPで実装する場合は最初に思い浮かぶ方法として `Playwright MCP` があります。

- Playwright MCP
	- [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

これはE2EテストフレームワークのPlaywrightをMCPで利用できるようにしたものです。  
サーバにPlaywrightを内蔵させ、MCPクライアントからアクセスすることにより効果を発揮します。

仕組みとしてはMCPサーバを構築したのち、サーバ内でPlaywrightを実行すれば良いため  
セルフで実装しようと思えば、実装は可能です。

たとえば、以下のような最小限のMCPサーバにPlaywrightを実装することで実現できるでしょう。

[mcp-handson/MinimalMcpServer/Program.cs at main · ymd65536/mcp-handson](https://github.com/ymd65536/mcp-handson/blob/main/MinimalMcpServer/Program.cs)

手軽に実装できますが、大変であることに変わりはないのでとくに理由がない限りはPlaywright MCPで良いと思います。

## A2Aで実装する

MCPだけでなくA2Aで実装する方法もあります。  
まだ実装したことはないですが、Agent Development Kit(ADK)を使った方法が有効です。

以下のコードは簡単な例ですが、ここにPlaywrightやSelenium、WebDriverの実行コードを実装することでA2Aによるブラウザ操作は実現できます。

[ymd65536/adk\_quick\_start: ADKに触ってみる](https://github.com/ymd65536/adk_quick_start)

ADKに関してはLINE Botの例ではありますが、以下の登壇資料で説明していますので参考にしていただけますと幸いです。

[Google Agent Development Kit でLINE Botを作ってみた](https://speakerdeck.com/ymd65536/google-agent-development-kit-deline-botwozuo-tutemita)

## まとめ

今回は生成AIによるWebブラウザ操作を実現する方法についてチェックしました。  
既製品を使うもよし、自分で作るもよし、作り方がわからなかったらAIに聞くもよしで  
夢が広がります。ぜひ、自分だけのWebブラウザ操作を作ってみてください。

## おわり

[0](https://qiita.com/ymd65536/items/#comments)

コメント一覧へ移動

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fymd65536%2Fitems%2F1497a60c11ebe1d8dda5&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fymd65536%2Fitems%2F1497a60c11ebe1d8dda5&realm=qiita)

[29](https://qiita.com/ymd65536/items/1497a60c11ebe1d8dda5/likers)

30