---
title: "Azure AI Foundry とは?使い方やできることを解説"
source: "https://www.avepoint.co.jp/blog/about-azure-ai-studio/"
author:
  - "[[SharePointのアクセス権限とは？種類や設定方法、注意点を解説]]"
published: 2024-05-05
created: 2025-06-09
description: "Azure AI Foundry は、 Microsoft が提供する複数の AI サービスを一元管理できるツールです。Azure AI Foundry を利用すると、効率的にアプリ開発を行え、画像生成や音声認識、テキス […]"
tags:
  - "clippings"
---
![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/Designer-4-1024x610.png)

Azure AI Foundry は、 Microsoft が提供する複数の AI サービスを一元管理できるツールです。Azure AI Foundry を利用すると、効率的にアプリ開発を行え、画像生成や音声認識、テキスト生成などに必要な AI モデルを簡単に活用できます。

本記事では、Azure AI Foundry の概要や使い方を詳しく解説します。主な機能やできること、使用するメリットなども紹介しますので、 Azure AI Foundry の導入を検討している方はぜひ参考にしてください。

**『Microsoft Copilot Studio』についてはこちらから。**  
[**Microsoft Copilot Studioとは？料金や活用事例について解説**](https://www.avepoint.com/blog/ja/microsoft-365-ja/about-microsoft-copilot-studio)

**『Microsoft 365 Copilot』についてはこちらから。**  
[**Microsoft 365 Copilot とは？できることやメリット、料金を解説**](https://www.avepoint.com/blog/ja/microsoft-365-ja/about-copilot-for-microsoft-365)

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/afbf652c104d63cb8b31a08e53ebbd18.png)

## Azure AI Foundry とは

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/b8064a1f4198225295efcf7492467242.webp)

Azure AI Foundry は、クラウドプラットフォーム Microsoft Azure で提供される AI サービスを 1 つの開発環境にまとめたものです。 Azure AI Foundry を使えば、あらゆるサービスを一元管理でき、簡単にアプリ開発や AI モデルの構築ができます。

また、 Azure AI Foundry は Azure OpenAI のほか、 Hugging Face 社や Meta 社が提供している AI モデルなども選べるため、作業に適したものを選択できます。なお、現時点（2024年4月）では正式版ではなく、パブリックプレビュー版として提供されています。

### Azure AI Foundry に統合されているサービス

Azure AI Foundry には、次のサービスが統合されています。

- Azure Machine Learning のモデルカタログとプロンプトフローの開発機能
- Azure OpenAI Service の生成 AI モデルのデプロイやテスト、カスタムデータの統合機能
- 視覚、音声、言語などの Azure AI サービスとの統合

Azure Machine Learning は、さまざまなデータを学習させ、そのデータをもとに予測や判断を行う機械学習のプラットフォームです。Azure AI Foundry では、 Azure Machine Learning のモデルカタログを利用できます。

また、 Azure Machine Learning のプロンプトフローの開発機能も備わっています。プロンプトフローとは、生成 AI を利用してアプリケーション開発を支援するツールのことです。テンプレートを使って AI に指示するプロンプトを生成でき、プログラミング言語の 1 つである Python コードで処理できます。

さらに複数の Azure AI サービスと統合できるため、音声認識機能などを活用でき、自然言語にも対応しています。

## Azure AI Foundry の機能

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/34f357c2c56eef23054a3dd15b02c26f.webp)

Azure AI Foundry には、主に次のような機能が搭載されています。

- モデルカタログ
- ベンチマーク
- プロンプトカタログ

それぞれの機能の詳細について見ていきましょう。

### モデルカタログ

モデルカタログ機能では、 Azure OpenAI のほか、 Hugging Face 社や Meta 社、NVIDIA 社などで提供されている言語モデルが一覧で表示されます。これらの中から使いたいモデルを検索して探し出すことが可能です。

また「推論タスク」という機能を使うと、画像生成や音声認識、テキスト生成など、タスクごとに適したモデルをフィルタリングできます。

### ベンチマーク

モデルの性能を比較するテストや評価を行う、ベンチマーク機能もあります。ベンチマーク機能を使うことで、 AI モデルが特定のタスクやデータセットにおいて、どのくらい機能するかを可視化できます。

Azure AI Foundry のモデルの中で、どれが最も目的のタスクに適しているのか、簡単に比較できることがメリットです。

### プロンプトカタログ

プロンプトカタログは、生成 AI で使用するプロンプトを一覧で見られる機能です。モデルカタログと同じように、使用例ごとに適したプロンプトを検索できます。

## Azure AI Foundry でできること

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/0cdfac479c2fb9d1b60d6525d2e5034b.webp)

Azure AI Foundry は、主に次のような作業に活用できます。

- 独自の Copilot を構築する
- アプリにマルチモダリティを取り入れる
- カスタム AI アシスタントを構築する

詳しく解説しますので、自社のニーズに合うか検討してみてください。

### 独自の Copilot を構築する

Azure AI Foundry を使えば、ユーザーの要望に合わせた独自の Copilot を構築できます。Copilot とは、 Microsoft が提供する生成 AI ツールです。対話型のインターフェースを持ち、ユーザーの質問に応じて適切なテキストや画像、コードを生成してくれます。

Azure AI Foundry を使う大きなメリットは、ユーザーが保有しているデータをもとにオリジナルの Copilot を生成できることです。自社のナレッジを活用したり、データをカスタマイズしたりすることにより、自社特有のニーズに応える生成 AI を構築でき、業務の効率化につながります。

### アプリにマルチモダリティを取り入れる

Azure AI Foundry では、画像や音声、テキストなど、複数のモダリティ（情報の入出力が行われるコミュニケーション経路のこと）を組み合わせたアプリ開発ができます。

たとえば自然言語で画像にキャプションを付けて分類を行い、必要な画像を抽出しやすくします。また、音声をテキストに変換し、文章を要約することも可能です。これらの機能を駆使することで、あらゆるモダリティに対応したアプリを作成できます。

### カスタム AI アシスタントを構築する

ユーザーの要望に合わせてカスタム AI アシスタントを構築することもできます。カスタム AI アシスタントとは、特定のタスクに合わせて高度なツールで強化された AI アシスタントです。

たとえばコードインタープリターやカスタム関数などを使用して強化すると、アシスタントがコードを解釈し、ユーザーの指示に応じて特定のタスクをスムーズに実行できるようになります。これにより特定の業務プロセスを自動化し、作業の効率を大幅に向上させることが可能です。

## Azure AI Foundry のメリット

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/867831a958545452caf2aff96869bd12.webp)

Azure AI Foundry を活用すると、次のようなメリットが得られます。

- 開発プロセスを効率化できる
- さまざまなモデルを利用できる
- 好みのエディタで作業ができる

それぞれ詳しく解説します。

### 開発プロセスを効率化できる

Azure AI Foundry には、複数の AI サービスが統合されています。そのため AI モデルの構築からテスト、デプロイまでを一括で管理でき、開発プロセス全体を効率化できることがメリットです。

また一連の作業をツールを活用して自動化することで、スピードの向上だけでなくヒューマンエラーの抑制にもつながります。

### さまざまなモデルを利用できる

Azure AI Foundry では Microsoft が提供する AI モデルだけでなく、他社が提供するモデルを活用できます。 Open AI が提供している GPT-35-turbo 、 GPT-4 、 GPT-4-32k などに加え、 Meta 社の Llama2 や、 Google 社の T5-small なども利用可能です。

ビジネスニーズに合わせて最適な AI モデルを選択し、柔軟に対応できることも大きなメリットです。

### 好みのエディタで作業ができる

Azure AI Foundry では、 Azure AI サービスへのアクセスを提供する Azure AI SDK を利用できます。これにより、サービスへ直接アクセスして日頃から使用しているコードエディタや開発環境で作業を進めることが可能です。普段から使い慣れているものを活用することで、導入時の負担を軽減できます。

## Azure AI Foundry の使い方

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/9034257f12a22a8d40a6d279ea30a9a4.webp)

ここでは Azure AI Foundry を活用するための前提条件と、 AI アシスタントを作成する手順を紹介します。これから Azure AI Foundry を導入する方は、ぜひ参考にしてください。

### 前提条件

Azure AI Foundry を使う際は、 以下の条件を満たす必要があります。

- Azure サブスクリプションを取得している
- [Azure OpenAI Service へのアクセス申請](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUNTZBNzRKNlVQSFhZMU9aV09EVzYxWFdORCQlQCN0PWcu) が承認されている

Azure アカウントがなくても、 Azure AI Foundry へのアクセスは可能です。しかし、すべての機能を使うには Azure サブスクリプションの取得と、 Azure OpenAI Service へのアクセス申請が必要になります。

### AI アシスタントの作成手順

Azure AI Foundry で AI アシスタントを作成する手順は次のとおりです。

1. [Azure AI Foundry](https://ai.azure.com/) にアクセスする
2. 新しいプロジェクトを作成する
3. 「ホーム」ページから「ビルド」、「プレイグラウンド」の順で選択する
4. 「デプロイ」のドロップダウンメニューから使用するデプロイを選択する
5. 「モード」のドロップダウンメニューから「アシスタント」を選択する
6. 「アシスタントのセットアップ」のドロップダウンメニューから「新規」を選択する
7. アシスタントの名称と指示を入力する
8. デプロイするモデルを選択する
9. コードインタープリターを有効にする
10. 「保存」を選択する

必要に応じてデータの前処理や学習を実行し、テストを行ってパフォーマンスを確認しておきましょう。

## Azure AI Foundry は AI 開発を効率化するプラットフォーム

![](https://www.avepoint.co.jp/cms/wp-content/uploads/2025/04/Designer-2_2024-12-23-021111_cvdl.webp)

複数の AI サービスを一元管理できる Azure AI Foundry を活用すれば、 AI 技術を活用したアプリをこれまでよりも容易かつ効率的に開発できます。ビジネスニーズに合わせて複数の AI モデルから柔軟に適切なモデルを選択できることも、他社との差別化につながるでしょう。

ぜひこの記事を参考に、 Azure AI Foundry の導入を検討されてみてはいかがでしょうか。

Copilotの機能拡張についてはこちらから。  
[CopilotはAPI連携できる？活用できるプラグインやプラグインの作成についても解説](https://www.avepoint.com/blog/ja/microsoft-365-ja/copilot-api-connection)

**★AvePointでは、Microsoft 365 Copilot のセキュアな導入に向けたサポートをいたします。**  
**Copilotを最大限活用するために必要な情報をぜひご参考ください！**  
**【無料オンデマンドセミナー】**  
[**Microsoft 365 Copilot の導入準備、AvePoint が提供できる価値**](https://www.avepoint.com/jp/events/webinar/solutions-for-copilot "https://www.avepoint.com/jp/events/webinar/solutions-for-copilot")  
**【お問い合わせはこちらから】**  
[**Microsoft 365 Copilot の導入を成功させるために**](https://www.avepoint.com/jp/solutions/microsoft-365-copilot-success-at-work "https://www.avepoint.com/jp/solutions/microsoft-365-copilot-success-at-work")