---
title: "初心者でも分かる！VSCodeでGemini CLIを使いこなす方法 - インストールから応用まで徹底解説"
source: "https://qiita.com/Nakamura-Kaito/items/122963855d7b1deb8a9d"
author:
  - "[[Nakamura-Kaito]]"
published: 2025-07-04
created: 2025-07-05
description: "開発者の強い味方！Gemini CLIとは何か？ 最近、コードの解析や自動化タスクに悩んでいたんですよね。そんな時、Google Geminiチームが開発した「Gemini CLI」というオープンソースのコマンドラインAIツールを見つけました。これが想像以上に便利で、今日..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## Qiitaにログインして、便利な機能を使ってみませんか？

[ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2FNakamura-Kaito%2Fitems%2F122963855d7b1deb8a9d&realm=qiita) [新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2FNakamura-Kaito%2Fitems%2F122963855d7b1deb8a9d&realm=qiita)

## 開発者の強い味方！Gemini CLIとは何か？

最近、コードの解析や自動化タスクに悩んでいたんですよね。そんな時、Google Geminiチームが開発した「Gemini CLI」というオープンソースのコマンドラインAIツールを見つけました。これが想像以上に便利で、今日はその体験をシェアしたいと思います！

Gemini CLIは開発者向けに特化したツールで、コードを理解し、複雑なクエリを実行し、タスクを自動化できるんです。さらに、Geminiのマルチモーダル機能（画像認識など）を活用してクリエイティブなコンテンツも生成できます。

**主な特徴：**

- **大規模コードベースのサポート**: 100万トークン以上のコンテキストを処理できるので、大きなプロジェクトの分析が簡単です。
- **マルチモーダルアプリのプロトタイピング**: PDFやスケッチからアプリのプロトタイプを素早く生成できます。
- **DevOpsタスクの自動化**: Git操作、PRの取得、移行計画の作成などが可能です。
- **ツール統合**: MCPサーバーを介して、Imagen、Veo、Lyriaなどのメディア生成モデルに接続できます。
- **ウェブ検索対応**: 組み込みのGoogle検索により、最新で信頼性の高い回答が得られます。

## Gemini CLIのインストール方法

### 前提条件

Node.js 18以降がインストールされていることを確認してください。以下のコマンドで確認できます：

```text
node -v
```

[![Node-1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/51764257-cd77-4e1e-9ce2-467d29b90723.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F51764257-cd77-4e1e-9ce2-467d29b90723.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b8ab8f6fdd71212bcdb158feabf93dc0)

このガイドでは **macOS** を例にしていますが、Windowsでも手順は似ています。すべての操作はターミナルで行います。

### 方法1：直接実行（インストール不要）

```text
npx https://github.com/google-gemini/gemini-cli
```

### 方法2：グローバルインストール（推奨）

ターミナルで以下のコマンドを実行します（sudoを使用する場合、システムパスワードの入力を求められることがあります）：

```text
sudo npm install -g @google/gemini-cli
```

インストール後は、ターミナルで `gemini` と入力するだけでインタラクティブCLIが起動します。初回実行時には、いくつかの権限を要求されることがありますが、確認して進めるだけでOKです。

## 初回セットアップ

起動すると、CLIは以下の手順でガイドしてくれます：

### ステップ1：テーマの選択

[![gemini-cli.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/1969d89c-4be2-4d0f-9742-f3ecf8f29c2a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F1969d89c-4be2-4d0f-9742-f3ecf8f29c2a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=08b7be9af53246bc0066d00e12263b39)

提供されたオプションから好みのテーマスタイルを選択します。 **Enter** キーを押して確定します。

### ステップ2：サインイン方法

[![gemini-cli-2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/234193bc-c7fd-40bf-8b8b-5929f53f096f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F234193bc-c7fd-40bf-8b8b-5929f53f096f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8cbba6de8b7e2e36ad489801db8da6c0)

ログイン方法を選択します。「Googleでログイン」がおすすめで、無料で **1分あたり60リクエスト** と **1日あたり1,000リクエスト** まで利用できます。選択して **Enter** キーを押します。

より高いレート制限やエンタープライズアクセスが必要な場合は、APIキーを使用できます：

1. [Google AI Studio](https://aistudio.google.com/apikey) からAPIキーを取得します。
2. 環境変数として設定します：

```text
export GEMINI_API_KEY="YOUR_API_KEY"
```

> 注：APIキーの使用は通常、直接APIコールのためのものです。このガイドではCLIの体験に焦点を当てています。Gemini APIについては、こちらのガイドで詳しく学べます： [ガイド: Google Gemini APIとは？その使い方を解説](https://apidog.com/jp/blog/google-gemini-api/)

### ステップ3：ブラウザ認証

[![ログイン-1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/2f6701ef-eee1-4cb5-8b95-31d4027ba126.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F2f6701ef-eee1-4cb5-8b95-31d4027ba126.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=46237034c75d332af5f22e804e67af32)

サインイン方法を選択すると、ブラウザウィンドウが開きます。Googleアカウントでログインするだけです。

**ログイン後**

認証が完了すると、次のような確認メッセージが表示されます：

「Gemini Code Assist からアカウントにアクセスできるようになりました」

[![Geminiログイン.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/6a96ddda-75f0-4462-887a-1eab80404a94.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F6a96ddda-75f0-4462-887a-1eab80404a94.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=77d81567a3846cea23715c06744af299)

### 使い始める

これでCLIに直接プロンプトを入力できるようになりました。例えば：

> 「Pythonでリスト内包表記を使う方法を教えて」

[![python-list-1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/094b0ef8-166a-4df6-9502-e3e41293fdb1.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F094b0ef8-166a-4df6-9502-e3e41293fdb1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=93a2e8e7f8d6a283c3335e97a7db991e)

ローカルファイルをアップロードして参照するには、CLIで `@` を使用してファイル選択をトリガーします：

> `@` （ファイル選択ダイアログが表示されます）

[![project-2.jpeg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/d034e186-5f43-40e0-bb2d-825bacfb9593.jpeg)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2Fd034e186-5f43-40e0-bb2d-825bacfb9593.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=dd5ea669a67e1a1d03adb015d9b84277)

## VSCodeでGemini CLIを使用する驚きの体験

私がGemini CLIを本当に気に入ったのは、VSCodeと組み合わせて使った時です。開発環境を離れることなく、AIの力を直接活用できるんですよ！

[![gemini-33.jpeg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/48171f14-a634-4084-9dcc-73ba7de2b0fe.jpeg)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2F48171f14-a634-4084-9dcc-73ba7de2b0fe.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=681999a0ad5378a26e36769275905cb4)

VSCodeの統合ターミナルで直接 `gemini` を実行してみてください。その後、 `@` コマンドを使用してファイルを選択し、会話を開始します。

### 驚きの効果1：コード生成の効率化

> 例えば：「五目並べを遊べるプログラムをHTMLで作成してください」

[![gemini-34.jpeg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/a855a745-765d-4e70-bc1b-b9ad850101c2.jpeg)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2Fa855a745-765d-4e70-bc1b-b9ad850101c2.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e766260517d8e2f34e794ad88a4c8633)

こんな簡単な指示だけで、基本的な五目並べのコードを生成してくれます。プロセス中に「書き込みアクセス」を要求されることがありますが、確認するだけでOKです。

[![五目並べ-1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/f1855de7-701e-4f29-9338-e86a7d7a9679.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2Ff1855de7-701e-4f29-9338-e86a7d7a9679.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ec0cd2935642c2e9f4b8afee8d27c408)

### 驚きの効果2：コード理解の爆速化

複雑なコードベースを理解するのに、以前は何時間もかかっていました。でもGemini CLIを使うと、プロジェクト内のファイルを選択して「このコードの概要を説明して」と尋ねるだけで、数分で全体像を把握できるようになりました。

例えば、あるReactプロジェクトで複雑なコンポーネントの仕組みがわからなかった時、Gemini CLIに質問したら、すぐに理解できる説明が返ってきて感動しました！

### 驚きの効果3：デバッグ時間の短縮

開発中に発生したバグの原因がわからず悩んでいた時、問題のコードをGemini CLIに見せて「このエラーの原因は何？」と質問したところ、すぐに問題点を指摘してくれました。以前なら何時間もかかっていたデバッグが、数分で解決できるようになったんです。

## ヒントとコツ

接続が不安定な場合、Gemini CLIは自動的に `gemini-2.5-pro` モデルから高速な `gemini-2.5-flash` モデルにフォールバックすることがあります。

利用可能なコマンドと使用方法のヒントを見つけるには、CLIで `/` と入力します。

[![gemini-help-1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/d22004e2-36f0-4b2c-b7e4-375e809aca87.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2Fd22004e2-36f0-4b2c-b7e4-375e809aca87.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=12003f4bcf5d6ca5b331c57800405cf2)

Gemini CLIは、開発者、DevOpsエンジニア、データアナリストにとって強力なAIコンパニオンです。コード分析を簡素化し、ワークフローを自動化し、クリエイティブな生成をサポートします - すべて自然言語の指示を通じて実現します。

## まとめ：VSCodeとGemini CLIの最強コンビが開発を変える

VSCodeにGemini CLIを導入してから、私の開発ワークフローは完全に変わりました。コードの理解、生成、デバッグの各フェーズで効率が劇的に向上し、以前の3倍のスピードで開発できるようになったと実感しています。

特に気に入っているのは、VSCodeという使い慣れた環境を離れることなく、AIの力を直接活用できる点です。コードエディタとAIの統合により、思考の流れを中断することなく開発に集中できるんですよね。

AIツールは日々進化していますが、VSCodeとGemini CLIの組み合わせは、私たちプログラマーの働き方を根本から変える可能性を秘めていると思います。今後はさらに高度な機能が追加され、より多くの開発タスクを効率化できるようになるでしょう。

みなさんもぜひVSCodeでGemini CLIを試してみてください。きっと開発の新しい可能性が広がりますよ！

---

## API開発に欠かせないツール – Apidog

Gemini CLIと並んで、開発者にとってもう一つの強力な生産性ツールがあります：「 [Apidog](http://www.apidog.com/jp/?utm_source=opr&utm_medium=a2qiita2&utm_content=gemini-cli) 」。

[Apidog](http://www.apidog.com/jp/?utm_source=opr&utm_medium=a2qiita2&utm_content=gemini-cli) は、APIドキュメント作成、APIデバッグ、API設計、APIテスト、モック、自動化のためのオールインワンプラットフォームです。APIワークフロー全体を効率化し、開発効率を向上させる最高のツールの一つです。

[![apidog-client-JP-1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3968588/bb92280d-5e18-41e6-8fdd-6c9cd08774a9.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3968588%2Fbb92280d-5e18-41e6-8fdd-6c9cd08774a9.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=40f809101ec2a4c3e7c92c297a7ad30e)

私も最近のプロジェクトで [Apidog](http://www.apidog.com/jp/?utm_source=opr&utm_medium=a2qiita2&utm_content=gemini-cli) を使い始めたのですが、API設計からテスト、ドキュメント作成まで一貫して管理できるようになり、チーム全体の効率が格段に上がりました。特に日本語対応している点は、英語が苦手な同僚にも好評でした。

PostmanやSwagger形式との完全な互換性も大きなメリットです。以前これらのツールを使用していた場合、既存のデータのインポートは簡単です。直感的なインターフェースも初心者に優しく、初めてのユーザーでもすぐに使い始めることができます。

[0](https://qiita.com/Nakamura-Kaito/items/#comments)

コメント一覧へ移動

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2FNakamura-Kaito%2Fitems%2F122963855d7b1deb8a9d&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2FNakamura-Kaito%2Fitems%2F122963855d7b1deb8a9d&realm=qiita)

[22](https://qiita.com/Nakamura-Kaito/items/122963855d7b1deb8a9d/likers)

いいねしたユーザー一覧へ移動

21