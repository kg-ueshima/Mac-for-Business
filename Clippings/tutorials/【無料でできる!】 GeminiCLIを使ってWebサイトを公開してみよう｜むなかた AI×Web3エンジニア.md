---
title: "【無料でできる!】 GeminiCLIを使ってWebサイトを公開してみよう｜むなかた AI×Web3エンジニア"
source: "https://note.com/munakata_souri/n/n2ccf7c4b1609"
author:
  - "[[むなかた AI×Web3エンジニア]]"
published: 2025-06-30
created: 2025-07-05
description: "この記事では「Gemini CLIのインストールはできたけど、これから何をしたらいの？」という方向けに、Webサイトの作成から公開までの手順をなるべく丁寧に解説していきます！  初心者の方にとっては手順が結構難しいのですが、、一度覚えると繰り返し作業なのでぜひ挑戦していただけると嬉しいです…！  事前準備として ① GeminiCLIのインストール ② GitとGitHubのセットアップ が終わっていることが前提なので、まだの方は以下の記事から準備をお願いします。  ① GeminiCLIのインストール  ② GitとGitHubのセットアップ  GeminiCLIを使ったWebサ"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/199299918/rectangle_large_type_2_5191f2103d6136205b371353bfaaab67.png?width=1200)

## 【無料でできる!】 GeminiCLIを使ってWebサイトを公開してみよう

[むなかた AI×Web3エンジニア](https://note.com/munakata_souri)

この記事では「Gemini CLIのインストールはできたけど、これから何をしたらいの？」という方向けに、Webサイトの作成から公開までの手順をなるべく丁寧に解説していきます！

初心者の方にとっては手順が結構難しいのですが、、一度覚えると繰り返し作業なのでぜひ挑戦していただけると嬉しいです…！

事前準備として  
① GeminiCLIのインストール  
② GitとGitHubのセットアップ  
が終わっていることが前提なので、まだの方は以下の記事から準備をお願いします。

**① GeminiCLIのインストール**

**② GitとGitHubのセットアップ**

## GeminiCLIを使ったWebサイトの作成

作業はVSCodeというアプリを使って行います。WindSurfやCursorといった類似のテキストエディタでも同じ流れで行えますので、すでに使い慣れたものがあればそちらで進めていただいても大丈夫です。

### 1\. 拡張機能のインストール

まずはじめに、作成したwebサイトの確認を簡単にするために一つ拡張機能をインストールしておきます。

左メニューの「拡張機能」を選択し、検索バーに「live server」と入力してください。その結果の中から、画像のような「Live Server」という項目を選択してインストールをしましょう。

> ごくまれに偽物の拡張機能が潜んでいるので、事前にインストール数や評価数を確認して、明らかに数が少ないものは避けるクセを付けておくのがオススメです。  
>   
> 【追記】  
> WindsurfやCursorなど、VSCode以外のエディタを使っている場合は、ダウンロード数が画像のものよりかなり少ない数で表示されます。Live Serverの場合、検索結果が1つだけであればそのままインストールしていただいて問題ありません。

![画像](https://assets.st-note.com/img/1751276957-n856jiQdoRTmkMWayHZIfXLe.png?width=1200)

インストールが完了すると、VSCode左下のバーの部分に「Go Live」というボタンが追加されます。これで準備OKです。

![画像](https://assets.st-note.com/img/1751277180-RFxcazo03SjBhW5ZYmb2yeud.png?width=1200)

### 2\. 作業用のフォルダを作成

大前提として、プログラムを作るときにはファイル管理がめちゃめちゃにならないよう、毎回決まった場所にプログラム用のフォルダを作るのがオススメです。

ぼくの場合はPCのユーザ名のフォルダ以下に「code」というフォルダを作って、その中にフォルダを新たに作成してからプログラムの作成を進めています。

このとおりでなくても良いので、どこか1つ作業用フォルダを決めて、そこに空のフォルダを作成してみてくださいね！

例）"code"フォルダの中に、今回作業するための"my-lp"フォルダを作成

```python
C:Users/[ユーザ名]
 ┗ code
    ┣ my-lp # LPサイト用プログラム
       ⋮    # 他のプログラムを作るたびに空フォルダを作成
```

![画像](https://assets.st-note.com/img/1751277762-bUD47WjqPSxrg1zJ8l9AkoXO.png?width=1200)

  

### 3\. 作成した空フォルダを開く

フォルダ作成が完了したらVSCodeのメニューから「ファイル」>「フォルダを開く」を選択して、作成した空のフォルダを開いてください。

![画像](https://assets.st-note.com/img/1751277830-eF7snSH2crlUC8hTI0GXo1O6.png?width=1200)

　「エクスプローラー」画面の上部に開いたフォルダ名が表示されていればOKです。（すべて大文字で表示されますが気にせずで）　

![画像](https://assets.st-note.com/img/1751328245-fKFzJMVlNutYraeE62PLWdcb.png?width=1200)

### 4\. GeminiCLIの起動

続いて、VSCodeのメニューから「ターミナル」>「新しいターミナル」を選択してみましょう。

![画像](https://assets.st-note.com/img/1751277229-SIdxGZ7M98O5s2mtAEfUBFJD.png?width=1200)

画面下にターミナルが表示されるので、以下のコマンドを実行してGeminiCLIを起動します。ここでエラーが出る場合は、事前準備の記事を参考にインストール作業を行ってみてくださいね。

```python
gemini
```

![画像](https://assets.st-note.com/img/1751277302-jUHiWaeA9VGuo03RYfkTScyl.png?width=1200)

### 5\. サイト作成の指示を行う

ここからようやく作成開始！…なのですが、作成時の指示によってプログラム全体の構成が変わってくるので、 **最初の指示がかなり重要** になってきます。

ウェブサイトを作成する方法も様々あるのですが、個人レベルで作成するものの多くはシンプルな構成で実現可能です。そのため個人的には **「HTMLで作ってください」** という一文を入れるのがとてもオススメです。

> GeminiCLIでは何も指定しないとReactという仕組みを使うことが多いのですが、公開難易度が高くなるのと修正や確認も大変なので、目的がない限りはおすすめしません。

また、GeminiCLIは新しいプログラムを作り始めるときに **新たにフォルダを作成してから作業を開始** してくれるんですが、今回の流れではとても **邪魔です** 。笑

そのため、これらを加味して今回の手順では以下のような指示文を使っていきます。

```python
●●するサイトをHTMLで作ってください。フォルダを新たに作る必要はありません。
```

ぼくの手元の例としてはAIプログラミング学習コミュニティのLPを作成する想定でこちらのような指示を行っていきます。

```python
AIプログラミング学習コミュニティのLPをHTMLで作ってください。フォルダを新たに作る必要はありません。
```

画面としてはこのよう見た目ですね。

![画像](https://assets.st-note.com/img/1751278656-NGITJ0SrOzto7Y2imDXsUyxq.png?width=1200)

実行してしばらく待っていると、途中で選択肢が表示される場面があります。

軽く内容を見つつ2つ目の「● Yes, allow always」を選択すればOKです。上下矢印キーで選んでENTERで決定しましょう。

> 「Yes, allow always」を選択すると、2回目以降同じ操作に関しては確認無しで進めてくれるようになります。

![画像](https://assets.st-note.com/img/1751279313-130CesfAw2cvBatLmroPJHy8.png?width=1200)

何度か同様に「Yes, …」を選んでいくとメッセージの表示が止まり、最終的に入力欄が表示されたら処理完了です。

![画像](https://assets.st-note.com/img/1751279483-2EpBiGcn8C5yYPRaSMqTkt7e.png?width=1200)

この時点で左メニューの「エクスプローラー」画面を開いて「index.html」のようなファイルが作成されていればOKです。

![画像](https://assets.st-note.com/img/1751330410-6C2JWOkUYnspcE08ytdIw537.png?width=1200)

### 6\. Webサイトの確認

サイトの確認のために先ほどインストールした拡張機能を利用します。VSCode右下の「Go Live」をクリックしてみてください。

![画像](https://assets.st-note.com/img/1751279580-WdcR5MTun8e3FSAEVlq7PJD0.png?width=1200)

すると自動でウェブページが表示され、AIが作成したサイトの見た目を確認することができます。

![画像](https://assets.st-note.com/img/1751279708-LMed9D6TvQPYUGh431fAEj0N.png?width=1200)

> 127.0.0.1 や localhost というURLは「自分のパソコン内」を示すアドレスです。このURLを共有しても他の人から同じものを見ることはできません。

### 7\. コードの修正と確認

一発で思い通りのサイトが出てくることは基本ないと思うので、ここからは追加で指示を行っていきます。

指示内容は作成したもの次第で自由に行っていただいてOKですが、例えば以下のように追加で指示を行っていきます。こちらのようにざっくりでも良いですし、具体的なイメージがあればそれを伝えたほうが確実です。

![画像](https://assets.st-note.com/img/1751298150-ps4CJ1ySfvkGDBrVcbWadU5O.png?width=1200)

途中で許可を求められたら、先ほどと同じように「● Yes, allow always」を選択しながら進めていきましょう。プログラムが修正されると、先ほどと同じURLでリアルタイムで変更内容が反映されます。

![画像](https://assets.st-note.com/img/1751298150-726V4ykLKiCPun1JIYNaUDqp.png?width=1200)

このように、指示→確認を繰り返しながら、自分が思い描いたWebサイトを作っていきましょう！

## Webサイトの公開

サイトの見た目が出来上がったらいよいよ公開です。今回はGitという仕組みで履歴情報を保存して、それをGitHubというサービスにアップロードする手順で紹介していきます。

公開は **GitHub Pages** という仕組みを使って行いますが、事前準備がまだの方はこちらの記事からざっくりの内容理解と環境構築をお願いします。

### 1\. Gitの履歴を保存

Gitの履歴の管理は実はVSCode上から行うことができます。左メニューの「ソース管理」を選択して、「リポジトリを初期化する」というボタンをクリックしてみましょう。

![画像](https://assets.st-note.com/img/1751279833-FKZGe7j65rBzMHwfbkVvEcpY.png?width=1200)

これによって、Gitの履歴を管理するための箱（＝リポジトリ）が作成されます。

![画像](https://assets.st-note.com/img/1751355328-BXLn0l1ir7PR4wgJKk9ONxsW.png?width=1200)

作成された時点ではこのように「変更」という欄に今回作成されたindex.htmlが表示されています。

![画像](https://assets.st-note.com/img/1751355419-UoI9rp614Df7GxB8ARhFcvVn.png?width=1200)

VSCode上では「変更」と「ステージ」の2つの状態があり、デフォルトだと「変更」の部分に今回作成したHTMLファイルが表示されています。

![画像](https://assets.st-note.com/img/1751355491-KzqMLUHrvQa7pmeRPFkTj2xd.png?width=1200)

Git履歴を保存するときには「変更」からは直接行うことができず、一度「ステージ」に移動する必要があります。

![画像](https://assets.st-note.com/img/1751355564-08YHyC73lUTnxAaF95S4XieZ.png?width=1200)

  

VSCode内の「変更」の部分にマウスを持っていくと **+** ボタンが表示されるので押してみましょう。これによって「変更」→「ステージ」にファイルを移すことができます。

![画像](https://assets.st-note.com/img/1751282768-yvbG9YXP802SCnLBIxscaD7F.png?width=1200)

  
「ステージされている変更」という欄にファイルが移動したことを確認しましょう。

![画像](https://assets.st-note.com/img/1751355821-F1afjRoH2P3rQSgDLhVzEs7N.png?width=1200)

イメージとしてはこちらのような流れになります。

![画像](https://assets.st-note.com/img/1751355720-eyrTHPEuljkJn5qDSv2Rf4b3.png?width=1200)

続いて、ボタンの上にテキストエリアがあるので、履歴に保存するためのメッセージを入力しましょう。あとから自分が見返したときになんとなく分かる内容であれば何でもOKです。

メッセージを入力した後、「コミット」ボタンを押しましょう。

![画像](https://assets.st-note.com/img/1751356050-gfWYQMBHZznbqRsivV8wdJT7.png?width=1200)

コミットとはGitの履歴情報を保存する作業のことを指し、画像としてはこんなイメージです。

![画像](https://assets.st-note.com/img/1751356110-XVBYT7vlI8pd9mnaLfWAeGtD.png?width=1200)

成功するとファイルが表示されていた欄が空欄になります。それと同時に画面下部に履歴メッセージが表示されているはずです。

![画像](https://assets.st-note.com/img/1751283092-Vf8SwyPRA9Ztrz3neFiHvuG1.png?width=1200)

これによって、リポジトリという箱の中に履歴情報が追加されました。

![画像](https://assets.st-note.com/img/1751356198-vSclxbjaPFZGdf9u7rOERKg5.png?width=1200)

ここまでで「自分のパソコン内にGitの履歴情報を保存する」という作業まで完了しました、次はGitHubというサービスにアップロード作業を行います。

### 2\. GitHubに履歴をアップロード

> すでにやり方を知っている方はWebサイトやコマンドを使った方法で進めていただいても結構です。

それでは参考記事でインストールした「GitHub Desktop」を開きましょう。

**【 初めて開く場合 】**

初めて開く場合はTOP画面に大きなボタンが4つ表示されるので、一番下の「Add an Existing Repository from your Local Drive …」を選択してください

![画像](https://assets.st-note.com/img/1751283530-sjR3B6UDgdQzMT9xmJYHV84q.png?width=1200)

**【 2回目以降 】**

一度使用したことがある場合は、前回開いていたプロジェクトが表示されているはずなので、メニューの「File」>「Add Local Repository …」を選択してください。  

![画像](https://assets.st-note.com/img/1751283501-eoMx3ZdSjrq6aLtAK4swDkO2.png?width=1200)

その後「Choose」から先ほど作成したフォルダを選択して「Add Repository」をクリックしましょう。これによって先ほど保存したGit履歴情報が読み込まれます。

![画像](https://assets.st-note.com/img/1751283568-uLCoHbWn1IM6psaxilvw2FNA.png?width=1200)

このような画面が表示されるので「Publish Repository」を選択しましょう。ここからGitHubへのアップロード作業を行うことができます。

![画像](https://assets.st-note.com/img/1751283578-EYH2msdGKFaz3Cu5TZcQjDiM.png?width=1200)

「Publish Repository」というダイアログが表示されるので、Name（名前）を入力していきましょう。

Nameの部分には好きな名前をつけることができますが、GithubPagesという機能を使って公開するときのURLとして使用されるので、URLの後半で使用したい名前を入力しましょう。

```javascript
https://[アカウントID].github.io/[Nameの部分]
```

例えば画像の例の場合は

```javascript
https://munakata-eng.github.io/souri-lp
```

のようになります。他の方に共有するようなものであればなるべくシンプルなものが良いですね。

また、「Keep this code private」のチェックですが、通常はチェックを入れて他の人から見えないようにするのがオススメなのですが、今回のように **GitHub Pagesという機能を使うときはチェックを外して公開状態にする** 必要があります。

最後に「Publish Repository」をクリックすると手元のPC内のGit履歴情報が、GitHubというサイトにアップロードされます。

![画像](https://assets.st-note.com/img/1751283877-4UAPXroy80iSFVtscdOgkxuT.png?width=1200)

この作業を行うことで、自分のPC内のGit履歴情報が、GitHubにアップロードされました。

![画像](https://assets.st-note.com/img/1751356249-0hAQKcuX3ej7riZBwn4PUpl9.png?width=1200)

### 3\. GitHub Pagesで公開

いよいよサイト公開です。まずGitHub [**https://github.com/**](https://github.com/) にアクセスしてログインしましょう。

いま作成したプロジェクトはTOPページ左側のテキストエリアからキーワード入力で探すことができます。クリックして開きましょう。

![画像](https://assets.st-note.com/img/1751283948-TAUP8s7IWabp93SwBejJqG6N.png?width=1200)

画面上部の「Settings」を開いて左側のメニューの「Pages」を選択するとGitHub Pagesの画面が開かれます。

Branchの欄、「None」と書かれたところをクリックして「main」を選んでください。

![画像](https://assets.st-note.com/img/1751284080-p8TqwKeWcgXCfJhj1ytIkn4r.png?width=1200)

「main」の右側に「Save」ボタンが表示されるので、そのままクリックすればOKです。公開されるまで1分ほど少し時間差があるので待ちましょう。

![画像](https://assets.st-note.com/img/1751284129-swocYlCVMj3EOhGTI9mkW6iQ.png?width=1200)

1〜2分くらい待った後、ページをリロードして、画面上部に **Your site is live at...**のような表示がでれば公開完了です。「Visit site」をクリックしてページを確認しましょう。

![画像](https://assets.st-note.com/img/1751284202-2zpS1fa6A5hmo7cyeKXLNsjq.png?width=1200)

先ほど手元で確認したものと同じページが表示されれば完了です。このページは誰でも閲覧可能なものになっているので、URLを共有することで他の方にも見てもらえます！

![画像](https://assets.st-note.com/img/1751284242-4mB6bGkD8AXeaIgJrT5jU1VH.png?width=1200)

### 4\. コードの変更時のサイト反映方法

一度公開したけど後から修正したい、というときに備えて変更手順も紹介していきます。

VSCodeに戻って、GeminiCLIに変更内容を指示してみましょう。

![画像](https://assets.st-note.com/img/1751299426-LOfRbkjY6htdrIeyAZ1Xzx8F.png?width=1200)

プログラムが変更されたときには、「Go Live」ボタンを押して開かれたページ（ローカル環境）で一度見た目を確認することをおすすめします。問題なければ次の手順に進みましょう。

![画像](https://assets.st-note.com/img/1751299619-v54AWVTcRUXxorF7B8Cat1bn.png?width=1200)

修正時の反映にもGitを使用します。左メニューの「コード管理」を開きましょう。

「変更」欄に表示されていたファイルの「＋」ボタンをクリックして、「ステージされている変更」へ移動させてください。

その後、テキストエリアにメッセージを入力して「コミット」をクリックしたら履歴情報の保存が完了です。

![画像](https://assets.st-note.com/img/1751299725-Dl7IrmHMJXnRQN2kY4EFwtCG.png?width=1200)

コミットボタンを押すと、先ほどまで表示されていなかった「変更の同期」というボタンが表示されるようになっているので押してみましょう。このボタンを押すことでGitHubに変更内容がアップロードされます。

> GitHub Desktopは初回のアップロード時のみ使用します。同じサイトの変更を反映するときには特に使用しないので閉じておいてOKです。

![画像](https://assets.st-note.com/img/1751299855-pky8ihLfnzG604e2osOBTRWg.png?width=1200)

GitHub Pagesの仕組みでは、変更がGitHubにアップロードされると自動でサイトの内容が更新されるようになっています。「変更の同期」を押してから2~3分ほど経ってから公開URLを確認して、変更が反映されていれば無事完了です。

![画像](https://assets.st-note.com/img/1751300279-Tf1rYyuM3g7hPCds2lbV8qWk.png?width=1200)

手順としては以上です。特にGitとGitHubまわりで新しい用語や手順がたくさん出てきて非常に難しいとは思いますが、、ぜひ何度か試してみてやり方を覚えていただけると嬉しいです！

## 最後にちょっと宣伝

Discordというサービスを使ってAIプログラミング学習コミュニティを運営しています！今回のようなGeminiCLIといったAIツールの情報交換や質問回答、たまにボイスチャットでお話なんかもしています。

アカウントさえあれば無料で参加できますので、お気軽に参加してみてくださいね！参加はこちらから↓↓

[**Discordサーバー「AIプログラミング学習コミュニティ「創理」」に参加しよう！** *DiscordでAIプログラミング学習コミュニティ「創理」コミュニティをチェック！　677人のメンバーと交流し、無料の音声* *discord.com*](https://discord.com/invite/CCuV6RNFPe)

さらに有料コミュニティ部分では、体系的に学べる教材、メンバー限定の相談チャンネル、週1回のライブ配信会など行っていますので、よろしければそちらもご検討いただけると嬉しいです😊

コミュティの詳細はこちら↓↓

  

  

  

  

  

  

  

[![note会員1000万人突破記念　1000万ポイントみんなで山分け祭　エントリー7/8（火）まで](https://assets.st-note.com/poc-image/manual/production/20250623_1000_top_notedetail.jpg?width=620&dpr=2)](https://note.com/info/n/ncceb4a6506fc)

【無料でできる!】 GeminiCLIを使ってWebサイトを公開してみよう｜むなかた AI×Web3エンジニア