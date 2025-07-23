[cite_start]本プレゼンテーション「ObsidianをLLM時代のナレッジベースに！」は、服部励起氏による、大規模言語モデル（LLM）時代の知識管理におけるObsidianの活用に関するものです[cite_start]。服部氏はフリーランスで、以前はスマートフォンアプリ開発者でしたが、2020年からAIを独学しており、Ubuntu 22.04 LTS Desktopを開発PCとして使用しています。
[cite_start]プレゼンテーションでは、LLM時代によくある「ブラウザタブ地獄」の問題を取り上げています。これには、100以上のタブが開いていること、情報の出所を忘れてしまうこと、タブを閉じることへの不安、「後で読む」リストが恒久化することなどが含まれます[cite_start]。また、フォーマットのばらつき、面倒なコピペ、後からの検索の困難さといった、LLMに情報を読み込ませる際の課題も指摘されています。
[cite_start]ObsidianとMarkdownは、以下の3つの理由からLLM時代の最適な解決策として提示されています。
 * [cite_start]LLMとの相性抜群: MarkdownはLLMが最も理解しやすい形式であり、構造化された情報として認識され、Claude CodeやGemini CLIなどのdocsフォルダにそのまま配置可能です。
 * [cite_start]シームレスなワークフロー: 情報管理のワークフローは、Web記事をObsidian Clipperでクリッピングし、Markdownに変換し、LLM docsに配置し、プロンプトで参照するという流れです。
 * [cite_start]心理的効果とメリット: 情報が安全に保存されていることで、タブを安心して閉じることができ、情報の蓄積、検索、AI活用につながります。
[cite_start]しかし、従来のクリッピング方法には課題があることも認められています。note.comのようなサイトや動的なサイト、認証が必要なページ、複雑なレイアウトのサイトでは失敗することが多く、手動でのコピペや何度もリトライが必要となり、情報収集のワークフローが破綻する原因となります。
[cite_start]解決策として、Gemini CLIとPlaywright MCPの組み合わせが提案されています。
 * [cite_start]Obsidian TerminalプラグインでGemini CLIを起動します。
 * [cite_start]Playwright MCPを使用して、JavaScript実行環境ごとページを取得します。
 * [cite_start]カスタムプロンプトでObsidian用のMarkdownに変換します。
 * [cite_start]完璧なMarkdownをObsidianに保存します。
[cite_start]Gemini CLIの設定のポイントとして、web_fetchよりも精度を重視すること、Obsidianのプロパティを保護すること、画像URLの取得を最適化すること、HTMLテーブル形式を維持することなどが挙げられています[cite_start]。Playwright MCPはmcpServers設定で必須指定され、Ubuntu環境ではTerminalプラグインのShell設定の変更が必要とされています[cite_start]。実演では、Web https://www.google.com/search?q=Clipper%E3%81%A7%E5%A4%B1%E6%95%97%E3%81%97%E3%81%9Fnote.comの記事をGemini CLIで完璧なMarkdownとしてクリッピングする例が示されています。
[cite_start]さらに、LLM docs連携の実例として、Obsidianで収集・蓄積した情報をdocsフォルダに配置し、Claude Codeなどで参照して文脈理解に活用するワークフローが紹介されています[cite_start]。具体的な活用例として、技術ドキュメント調査から実装方針の相談、競合分析記事収集から戦略立案のブレスト、API仕様書クリッピングからコード生成時の参照などが挙げられています。
[cite_start]まとめとして、このアプローチにより、ブラウザタブ問題の解決、諦めていたサイトの確実な保存、LLMに最適化されたフォーマット、CLI連携による即時活用が実現できたとされています[cite_start]。これにより、情報収集の完全自動化、LLMとのシームレスな連携、調査・開発の大幅な時間短縮、外部脳としてのObsidian活用といった効果が期待されます[cite_start]。これは「LLM時代の情報管理革命」であり、ブラウザタブ地獄から体系的なナレッジベースへと変化すると締めくくられています。
[cite_start]補足として、GeminiはPDFファイルも処理できることが示されており、PDFファイルを読み取りMarkdownに変換するデモが行われました[cite_start]。詳細な設定方法やGEMINI.mdのルールは後日共有される予定です。


Obsidian入門: 魅力と活用法
[cite_start]このプレゼンテーションは、ノートアプリ「Obsidian」の魅力と活用法、おすすめのプラグインについて解説します。
[cite_start]発表のゴール
 * [cite_start]ミニマムで使えるようになる（デイリーノート、タグ、リンク機能など）
 * [cite_start]プラグインを理解する
 * [cite_start]Tasksによるタスク管理を知ってもらう
[cite_start]目次
 * [cite_start]Obsidianのはじめ方
   a.  [cite_start]使い方とタグ機能
 * [cite_start]プラグインの説明
   a.  [cite_start]コアプラグイン
   b.  [cite_start]コミュニティプラグイン
 * [cite_start]Tasksによるタスク管理
[cite_start]なぜ流行っているのか？
[cite_start]Obsidianとは
 * [cite_start]ローカルフォルダ上のマークダウンファイルで保存するノート管理アプリ
 * [cite_start]個人利用は無料で使える（商用利用や同期機能は有料オプション）
 * [cite_start]クラウドに依存しないため高速
 * [cite_start]Vault（ボルト）とはノートを保存するフォルダ単位
 * [cite_start]オフラインで利用可能
 * [cite_start]VSCodeなどからVaultのフォルダを開くことができ、AIでの利用がしやすい
[cite_start]Obsidianのはじめ方
 * [cite_start]https://obsidian.md/ から自分の環境に合ったものをダウンロード
 * [cite_start]Windows版、MacOS版、Linux版、iOS/iPadOS版、Android版がある
[cite_start]Obsidianのとりあえずの使い方の提案
 * [cite_start]「デイリーノート」という、その日のあらゆることを書けるノートを作成
   * [cite_start]daily/2025-07-20のように日付をつけたノートを作り、メモを書き込みます[cite_start]。どんな些細なことでもたくさん書くほど良いです。
 * [cite_start]プロジェクト、まとまったアイデア、WebClipなどは独立のノートとして作成します。
   * [cite_start]関連するノートはリンクで繋げます。
 * [cite_start]ノートが増えてくると、グラフビューを見るとノートとノートが繋がってきて楽しくなってきます。
[cite_start]タグ機能と強力な検索
 * [cite_start]階層型タグで柔軟な分類が可能: 例：#プログラミング言語、#プログラミング言語/Python、#プログラミング言語/Python/matplotlib、#プログラミング言語/JavaScript[cite_start]。何階層になっても問題ありません。
 * [cite_start]検索やタグペインからタグを便利に使うことができます。
 * [cite_start]高速な全文検索: tag:#プログラミング言語 "関数型" のように使えます。
 * [cite_start]フォルダ・タグ・リンクを組み合わせた横断的な情報管理が可能です。
 * [cite_start]タグがあるため、ノートはどのフォルダに作成しても良いと割り切って使うことができます。
[cite_start]プラグインの魅力
[cite_start]プラグイン拡張とカスタマイズ
 * [cite_start]プラグインにより機能を追加できます。
 * [cite_start]Obsidianに含まれる「コアプラグイン」と、Obsidianの機能を拡張する「コミュニティプラグイン」があります。
 * [cite_start]設定ボタンからコアプラグインやコミュニティプラグインの設定が可能です。
[cite_start]コアプラグイン (個人的にすごいもの)
 * [cite_start]アウトライン: アウトラインペインを表示でき、ドラッグで順番の入れ替えが可能です。
 * [cite_start]タグペイン: タグペインを表示できます。
 * [cite_start]グラフビュー: ノートのつながりをグラフで表示します。
 * [cite_start]テンプレート: 既存のノートにテンプレートを追加できます。コミュニティプラグインの「Templater」でさらに細かい設定が可能です。
[cite_start]コミュニティプラグイン (個人的に必須)
 * [cite_start]QuickAdd: デイリーノートに素早く入力できます。ホットキーを押すと入力画面が立ち上がり、入力してOKを押すとその日のデイリーノートに追記されます。
 * [cite_start]Tasks: タスクを任意のノートに書き、任意のノートでクエリを使ってタスクを抽出できます[cite_start]。詳細は後述します。
 * [cite_start]TagFolder: タグをフォルダとして表示してくれます。
 * [cite_start]Kindle Highlights: Kindleの自分のハイライトとメモをダウンロードし、ノートを作成します。
[cite_start]同期とホットキー
[cite_start]同期 (複数のPC / スマホで同期して使いたい)
 * [cite_start]Obsidian Sync: 公式が提供しており、月5ドルまたは10ドル（月払い）で利用できます。
 * [cite_start]iCloud: MacとiPhoneを使っている人にはiCloudが良いかもしれません。PCからの更新もiCloudからの更新も自動で同期されます。
 * [cite_start]その他、GoogleDriveやGitHubを使う方法など、いろいろな同期方法があります。
[cite_start]ホットキー（キーボードショートカット）、コマンドパレット
 * [cite_start]設定のホットキーから、ホットキーの確認・割当ができます。
 * [cite_start]プラグインのホットキーは、設定のプラグインの+ボタンから設定できます。
 * [cite_start]コマンドパレットは、MacはCommand⌘+P、WindowsはCtrl+Pで開きます[cite_start]。行いたい操作や表示したいタブがある場合は、コマンドパレットに打ち込みましょう（例：「タグ」や「アウトライン」と入力）。
[cite_start]タスク管理
[cite_start]1. Obsidian Tasksとは
 * [cite_start]Obsidian内のあらゆるタスクを一元管理できるコミュニティプラグインです。
 * [cite_start]Vault（保管庫）内の全ノートから-[]形式のチェックボックスを自動で収集し、一覧表示や絞り込み、並び替えを可能にします。
 * [cite_start]メリット: 会議の議事録、デイリーノート、プロジェクトノートなど、タスクが発生したその場所で記録できます[cite_start]。情報とタスクが分断されず、文脈の中でタスクを管理できます[cite_start]。専用のToDoアプリは必要ありません。
[cite_start]2. まずは使ってみよう
 * [cite_start]インストール方法: Obsidianの設定＞コミュニティプラグインを開き、コミュニティプラグインを有効にして「閲覧」ボタンをクリック。「Tasks」と検索してインストールし、有効化します。
 * [cite_start]タスクの書き方: 基本は簡単！Markdownのチェックリスト記法で書くだけです[cite_start]。例：- [ ] 資料を作成する。
 * [cite_start]タスクの完了: チェックボックスをクリックするか、[]を[x]に書き換えるだけです[cite_start]。完了すると、自動で完了日が追記されます[cite_start]。例：- [x] 資料を作成する ✅ 2025-07-18。
[cite_start]3. タスクをパワーアップさせる属性
[cite_start]タスクの行に決まった書き方で情報を追加すると、Tasksプラグインが自動で認識し、より強力なタスク管理が可能になります。
 * [cite_start]期限日（📅）: - [ ] レポート提出 📅 2025-07-31 (タスクの締切日を設定)
 * [cite_start]開始日（🛫）: - [ ] プロジェクト準備 🛫 2025-07-31 (タスクを開始する日を設定)
 * [cite_start]予定日（⏳）: - [ ] 会議の準備 ⏳ 2025-07-20 (「この日にやるぞ！」という計画日を設定)
 * [cite_start]繰り返し（🔁）: - [ ] ゴミ出し 🔁 every week (完了すると自動で次回のタスクが生成)
 * [cite_start]優先度: - [ ] タスク ⏫ (🔺（最高）、⏫（高）、🔼（中）、🔽（低）、⏬（最低）の5段階で設定可能、優先度なしもあり)
 * [cite_start]タグ: - [ ] 議事録を書く #仕事 (#タグを使ってタスクを分類・絞り込み)
[cite_start]4. 「クエリ」でタスクを自在に操る
[cite_start]クエリは、条件に合うタスクだけを抽出できる検索機能です[cite_start]。「tasks」と書いたコードブロック内に、英語で条件を書くだけで使えます。
 * 未完了のタスクを全て表示:
   not done

 * 今日やるタスク（今日が期限 or 予定日）:
   not done
(due today) OR (scheduled today)

 * 期限が近いタスク（今日から7日以内が期限、期限日でソート）:
   not done
due after yesterday
due before in 7days
sort by due

 * 特定のプロジェクトのタスク（ファイルパスに「プロジェクトA」が含まれるノートのタスクだけ表示）:
   not done
path includes プロジェクトA

 * [cite_start]explainとクエリにつけると、そのクエリの説明が表示されます。
[cite_start]5. 自分だけの「タスクダッシュボード」を作ろう
 * [cite_start]クエリを使ってタスクのダッシュボードを作成することができます。
 * [cite_start]前ページのクエリなどを使って、デイリーノートやプロジェクトに複数の条件でタスクを表示できます。
 * [cite_start]Obsidianでは、ノートを自由な位置に配置できます。
 * [cite_start]![[ノート名]]と書くことで、リンク先のノートを表示することが可能です。
[cite_start]6. Tasksまとめ
 * [cite_start]好きなノートにタスクを書いても、クエリで抽出して見ることができます。
 * [cite_start]まずはデイリーノートやプロジェクトのノートに自由にタスクを書き、デイリーノートにクエリを書いて今日やるタスクを表示してみることから始めるのがおすすめです。
[cite_start]まとめ
 * [cite_start]Obsidianを初めて使うときに知りたかったことをまとめています。
 * [cite_start]Gemini CLIとの連携も非常に推奨されています。
 * [cite_start]Zettelkastenによるノート管理・アイデア管理はまだピンと来ていないが、できるようになればまた発表したいと考えています。
 * [cite_start]本発表は、いくつかの書籍を参考にしています。
