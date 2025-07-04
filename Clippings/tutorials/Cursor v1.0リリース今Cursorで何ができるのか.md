---
title: "[Cursor v1.0リリース]今Cursorで何ができるのか"
source: "https://zenn.dev/service/articles/dbb6123a4732ed"
author:
  - "[[Zenn]]"
published: 2025-06-05
created: 2025-06-06
description:
tags:
  - "clippings"
---
13

6

どうも、自分は1年前からCursorを使って開発しています。ようやく正式リリース版であるv1.0がリリースされたのでCursorについてまとめてみることに。前回は複数IDEを比較した記事も書いています。

---

## \[Cursor v1.0リリース\] 今、AIコードエディタCursorで何ができるのか？

AIによる開発支援が当たり前になりつつある現在、その先を行くツールとして注目を集めているのが「Cursor」です。単にコードを生成するだけでなく、開発ワークフロー全体をインテリジェントに支援し、生産性を劇的に向上させることを目指して設計されています。

待望の **v1.0がリリース** され、多くの新機能が搭載されると共に、既存機能も大幅に強化されました。本記事では、このCursor v1.0で何ができるようになったのか、特に開発者が注目すべきポイントを深掘りしていきます。

## 生産性をブーストする！AIコードエディタ「Cursor」でできること

Cursorは、VS Codeをベースとしながら、強力なAIモデル（Claude 4シリーズ、 Gemini 2.5 proなど）をエディタ内に深く統合。これにより、コーディング、デバッグ、リファクタリング、ドキュメント参照、さらにはチームでの協調作業に至るまで、開発のあらゆる局面でAIの恩恵を受けられます。

## Cursor v1の新機能

v1.0では、開発体験を根底から変える可能性を秘めた新機能が多数導入されました。

| 機能名 | 概要 | 特に注目すべきポイント |
| --- | --- | --- |
| **Multi-Cursor (MCP) の初期サポート🤖** | 同じファイル上で、複数の「カーソル」（自分自身、チームメイト、AIエージェント）が同時に作業するための基盤技術。 | リアルタイム共同編集の未来を示唆。AIとのよりシームレスなペアプログラミングや、チームでのAI支援型開発が加速します。 |
| **BugBot🐞** | GitHubのプルリクエストをAIが自動レビュー。潜在的なバグを検出し、コメントや修正案を提示。「Fix in Cursor」でエディタに直接修正を適用可能。 | コードレビューの効率化と品質向上。CI/CDパイプラインへの組み込みも視野に入り、より堅牢な開発体制の構築に貢献します。 |
| **Background Agent🕵️♂️** | ユーザーが他の作業中にも、AIエージェントがバックグラウンドでコード修正、調査、ドキュメント作成などのタスクを非同期に実行。 | 時間のかかる処理や、思考を中断させたくないタスクをAIに委任。コンテキストスイッチを減らし、開発者の集中力を維持します。 |
| **Agent in Jupyter Notebooks📊** | Jupyter Notebooks環境内でAIエージェントを直接利用可能。データ分析、可視化、実験コードの生成・編集をインタラクティブに支援。 | データサイエンスや機械学習のワークフローにおいて、AIの力をより直接的に活用できるようになります。 |
| **Memories🧠** | プロジェクトごとにAIとの会話履歴や重要なコンテキスト（ファイル、シンボルなど）を記憶・管理。次回以降の対話でその情報を自動的に参照・活用。 | プロジェクト特有の文脈をAIが理解し、よりパーソナライズされた的確なサポートを提供。同じ指示の繰り返しを削減します。 |
| **Richer Chat Responses🎨** | AIのチャット応答に、Mermaid.jsを利用した図（フローチャート、シーケンス図など）やMarkdown形式の表を埋め込み可能に。 | 複雑なロジックやデータ構造を視覚的に表現することで、AIとのコミュニケーションがより明確かつ効果的になります。 |
| **New Settings & Dashboard⚙️** | 設定画面とダッシュボードUIが刷新。より直感的な設定管理と、AI機能の利用状況（トークン消費量など）の可視化が実現。 | ツールのカスタマイズ性と透明性が向上。自身の利用パターンを把握し、より効率的な使い方を見つけるのに役立ちます。 |
| **Improved Diffing⬆️** | AIによるコード変更提案時の差分表示が大幅に改善。変更の意図や影響範囲をより正確かつ迅速に把握可能に。 | AIの提案をレビューし、適用する際の判断が容易になり、マージ作業の効率が向上します。 |
| **VS Code Extension Sync♾️** | 既存のVS Code環境から拡張機能や設定をCursorに同期する機能が強化。 | VS Codeからの移行がよりスムーズになり、使い慣れた開発環境をCursor上で素早く再現できます。 |

### Multi-Cursor (MCP) の初期サポート

GUIでポチポチすれば連携できるようになりました。(自分のCursorではなぜかまだ反映されていない)

これはCursorが目指す「AIとの協調開発」の未来を具体的に示す一歩です。現段階では初期サポートですが、将来的には、自分だけでなく、チームメンバーや複数のAIエージェントが同じコードベース上で、それぞれの役割をこなしながらシームレスに連携する、といった開発スタイルが実現するかもしれません。

### Memories：プロジェクトの文脈をAIが記憶し、対話効率を劇的に向上

「Memories」機能は、プロジェクトごとにAIとの会話履歴や重要なコンテキスト（頻繁に参照するファイル、主要なシンボル、過去の決定事項など）をCursorが記憶し、後続のAIとの対話時にその情報を自動的に参照・活用する仕組みです。これにより、ユーザーは同じ背景説明を繰り返す必要がなくなり、AIはよりプロジェクトの文脈に即した、パーソナライズされた応答を返すことが可能になります。

主な特徴と利点:  
コンテキストの永続化:  
これまでのAIチャットでは、セッションが終了したり、時間が経過したりすると、以前の会話内容は忘れられてしまうことが一般的でした。Memories機能により、特定のプロジェクトに関する重要な情報は、ユーザーが明示的に削除しない限り保持されます。

繰り返しの削減:  
「このプロジェクトではTypeScriptを使用し、状態管理はZustandです」「先週決定したAPIのエンドポイント設計は…」といった情報を、AIに何度も教える必要がなくなります。これにより、対話の効率向上します。

より的確なAI応答:  
AIがプロジェクトの履歴や固有のルール（例: 特定のコーディング規約、ドメイン固有の用語など）を記憶しているため、生成されるコードや提案が、よりプロジェクトの文脈に適合しやすくなります。例えば、以前の会話で「常にエラーハンドリングを考慮して」と指示していれば、その後のコード生成でもその指示が暗黙的に反映されることが期待できます。

他にプロジェクト横断的な知識の断片化防止、長期プロジェクトでの一貫性維持、複雑なドメイン知識の共有、個人の開発スタイルの反映など応用できます

### Python使いは嬉しい Agent in Jupyter Notebooks - データサイエンスワークフローにAIが直接介入

「Agent in Jupyter Notebooks」は、データ分析や機械学習の分野で広く利用されているJupyter Notebooks環境内に、CursorのAIエージェント機能を直接統合するものです。これにより、Notebookのセル内で自然言語を使ってコードの生成、編集、デバッグ、さらにはデータ分析のアイデア出しや手順の相談などをインタラクティブに行えるようになります。

\[主な特徴と利点\]  
Notebook内でのシームレスなAI連携:  
従来、Jupyter NotebooksでAIの支援を得るには、別途チャットウィンドウを開いたり、生成されたコードをコピー＆ペーストしたりする必要がありました。この機能により、Notebookのフローを中断することなく、必要なセルで直接AIエージェントを呼び出し、対話しながら作業を進められます。

データ分析タスクの効率化:  
「このCSVファイルを読み込んで、欠損値の状況を表示して」「このデータフレームに対して、X列とY列の相関を計算し、散布図で可視化して」といった指示を出すだけで、AIが対応するPythonコード（Pandas, Matplotlib, Seabornなどを使用）を生成・挿入してくれます。

コードのデバッグと改善,実験と仮説検証の高速化,学習ツールとしての活用などに使えます。

横道にそれますが機械学習分野では格安でクラウドGPUが扱えるGoogle Colabが人気ですがIDE側で扱いたい需要もあると思います。  
最近は安めのGPUクラウドサービスもあるようです(まだ試していない)

## 従来の強力な機能一覧 (v1.0でさらに洗練)

v1.0以前からCursorの中核を担ってきた機能群も、最新AIモデルへの対応やUI/UXの改善により、さらに使いやすく進化しています。

| 機能名 | 概要 | 活用ポイント |
| --- | --- | --- |
| **自然言語でのコード生成/編集 (Cmd+K)** | やりたいことを言葉で指示するだけで、AIがコードを生成・編集。選択範囲やファイル全体に対しても適用可能。 | プロトタイピング、定型コードの自動生成、新しい言語/ライブラリの学習支援など、あらゆる場面で開発を加速。 |
| **AIによる高度なオートコンプリート** | 文脈を理解したインテリジェントなコード提案。複数行の編集やスマートなリファクタリング提案も。Tabキーで簡単適用。 | コーディング速度の向上、タイプミスや構文エラーの削減。AIによる「より良い書き方」の提案から学べることも。 |
| **コードに関する質問応答 (Chat with selection)** | エディタ内のチャットで、選択したコードやシンボルについてAIに質問し、詳細な説明や解説を得られる。 | コードリーディングの効率化、複雑なロジックの理解、デバッグ支援、他者コードのキャッチアップに威力。 |
| **チャットベースでのコード生成と即時適用** | チャットウィンドウでAIと対話しながらコードを生成・編集し、「Apply」ボタンで即座にエディタに反映。 | トライ＆エラーのサイクルを高速化。AIと相談しながら、少しずつ目的のコードをインタラクティブに構築可能。 |
| **ウェブ検索の統合 (`@Web`)** | チャットで `@Web` に続けて検索クエリを入力すると、エディタ内でウェブ検索結果（Bing API）を参照可能。 | ドキュメントやエラーメッセージ検索時のコンテキストスイッチを削減。開発フローを中断させずに情報収集。 |
| **コードベース全体への問い合わせ** | `@Codebase` (プロジェクト全体)、 `@Folder` (指定フォルダ)、 `@File` (指定ファイル) を使い、広範な質問が可能。ローカルインデックスを活用。 | 大規模コードベースの構造把握、特定機能の実装箇所の特定、変更の影響範囲調査などに極めて有効。 |
| **画像からのUIコード生成 (試験的)** | UIデザインの画像（スクリーンショット等）をチャットにD&Dすると、AIが解釈し対応するUIコード（HTML/CSS、React等）を生成試行。 | デザインカンプからのコーディング初期段階の自動化、簡単なUIプロトタイプの迅速な作成に。 |
| **ライブラリドキュメントの参照 (`@Docs`)** | `@Docs` + ライブラリ名で、関連ドキュメントやAPIリファレンスをAIが参照し、質問応答やコード生成。 | 新しいライブラリ/FWの学習コスト削減、正確なAPIの使い方の確認、サンプルコードの取得などに便利。 |
| **Auto-run (Allowlist/Denylist)** | AIが提案するシェルコマンドの自動実行を制御。許可リスト/拒否リストを設定することで、安全性と利便性のバランスをユーザーがコントロール。 | リンター、フォーマッター、軽微なテストなどを自動化しつつ、危険なコマンドの偶発的な実行を防止します。 |

## 便利で柔軟なルール機能：AIの振る舞いをプロジェクトに最適化

AIの提案がどれほど優れていても、プロジェクトのコーディング規約や設計思想に合致していなければ意味がありません。Cursorの\*\*ルール機能（AI Settings / Custom Instructions）\*\*は、AIの挙動をプロジェクトごと、あるいはユーザーごとに細かくカスタマイズし、より文脈に即した支援を得るための強力な仕組みです。

### .cursor/rulesへのルール記載

![](https://storage.googleapis.com/zenn-user-upload/3f6a72140b24-20250605.png)

プロジェクトルートに `.cursor` ディレクトリを作成し、その中に `rules` ディレクトリ を配置することで、プロジェクト固有の指示をAIに与えることができます。これにより、チームメンバー間で共通のAI設定を共有し、一貫性のあるAI支援を受けることが可能になります。

私もフル活用しています。

**ルールファイルのトリガータイプと記述例 (mdc: Markdown Code Block):**

ルールは、AIがいつその指示を参照すべきかを示すトリガータイプと共に記述します。

- **`Always` (常に参照):** AIが応答を生成する際に常に考慮されるべき基本的な指示。
	```markdown
	\`logger.info()\`
	```
- **`Auto Attached` (自動付与):** 特定のファイルタイプやディレクトリ構造に基づいて、自動的にAIのコンテキストに追加される指示。 (※このトリガータイプはCursorのドキュメントで明示されていない場合、カスタム指示の高度な使い方として解釈。通常は `Always` やユーザープロンプトでの制御が主)
- **`Agent Requested` (エージェント要求時):** Background Agentのような特定のAIエージェントがタスクを実行する際に参照する専用の指示。(※同上)
- **`Manual` (手動):** ユーザーがチャットで明示的に「このルールを参照して」と指示した場合にのみ適用されるルール。特定の複雑なタスクや、実験的な指示を試す際に有用。

これらのルールを効果的に設定することで、AIは以下のような具体的な支援を提供できるようになります。

- **コーディング規約の遵守:** 「変数名はcamelCaseで」「Promiseはasync/awaitで扱う」など。
- **推奨ライブラリ/フレームワークの利用:** 「状態管理はRedux Toolkitを使って」「APIクライアントはaxiosで実装」など。
- **非推奨パターンの回避:** 「 `any` 型は極力使用しない」「 `innerHTML` への直接代入は避ける」など。
- **ドメイン特有の用語やロジックの理解:** プロジェクト固有のビジネスルールや専門用語をAIに教え込む。

このルール機能は、AIを単なる汎用ツールから、プロジェクトに特化した「頼れる専門家」へと育て上げるための鍵となります。

## Auto-Run機能で自動運転：開発プロセスの効率を極限まで高める

AIによるコード生成やリファクタリングは強力ですが、その後に続くリンティング、フォーマット、テスト実行といった定型作業は、開発者の時間を奪いがちです。Cursorの **Auto-Run機能** は、これらの作業を自動化し、開発フローをシームレスに繋げることで、生産性を飛躍的に向上させます。

AIがコード変更と同時に実行を提案するシェルコマンド（例: `eslint --fix`, `pytest specific_file.py` ）を、ユーザーの承認なしに実行できるこの機能は、まさに「自動運転」のような開発体験を提供します。

### rm -rf や sh で全データ削除しないようにDenylistの設定は怠らないように

![](https://storage.googleapis.com/zenn-user-upload/aa023b4de6eb-20250605.png)

Auto-Runの利便性は絶大ですが、その力を無制御に解放することは極めて危険です。意図しないコマンドが自動実行されれば、ソースコードの破壊、機密情報の漏洩、さらにはシステム全体への損害といった深刻な事態を招きかねません。

そこで不可欠となるのが、 **Denylist (拒否リスト)** の設定です。

- **Denylistに必ず含めるべきコマンドの例:**
	- `rm` (特に `rm -rf`)
	- `git push --force`, `git reset --hard`
	- `sudo`, `su`
	- `npm install -g`, `pip uninstall -y`
	- `sh`, `bash`, `zsh` (引数なし、または任意のスクリプト実行の可能性がある場合)
	- `docker system prune -a -f`
	- その他、環境変数や設定ファイルを書き換える可能性のあるコマンド

**Allowlist (許可リスト) とのバランス:**

Denylistで危険なコマンドをブロックする一方、Allowlistには日常的に安全に使用でき、作業効率を確実に向上させるコマンドのみを厳選して登録します。

- **Allowlistに適したコマンドの例:**
	- `eslint --fix {filepath}`
	- `prettier --write {filepath}`
	- `black {filepath}`
	- `go fmt {filepath}`
	- `pytest -k TestSpecificFeature --quiet {filepath}` (実行範囲が限定されたテスト)
	- `touch {filepath}`, `mkdir -p {dirpath}` (AIによるファイル/ディレクトリ作成支援)

**Auto-Run運用のベストプラクティス:**

1. **デフォルトDenyの原則:** 基本的に全てのコマンドはDenylistにあるものと考え、本当に安全かつ有用なものだけをAllowlistに追加します。
2. **最小権限:** コマンドに渡す引数も可能な限り具体的にし、影響範囲を限定します（例：ファイルパス指定）。
3. **定期的なレビュー:** プロジェクトの進化やツールの変更に伴い、Allowlist/Denylistを定期的に見直します。
4. **チームでの共有と合意:** チームで開発する場合、Auto-Runの設定内容について共通認識を持ち、合意形成を行うことが重要です。

Auto-Runは、正しく設定し運用すれば、開発プロセスから多くの摩擦を取り除き、AIの提案をよりスムーズにワークフローに統合できる強力な武器となります。しかし、その設定には細心の注意を払い、常にセキュリティを最優先に考える必要があります。

## 複数チャットで並列実装：思考を止めない、コンテキストを切り替えない開発体験

![](https://storage.googleapis.com/zenn-user-upload/a056c21253d7-20250605.png)

複雑な機能開発やデバッグ作業では、複数の視点からアプローチしたり、異なるタスクを並行して進めたりすることが頻繁にあります。Cursorの **複数チャットタブ機能** は、このようなマルチタスクな思考プロセスを強力にサポートし、コンテキストスイッチのコストを最小限に抑えます。

各チャットタブは独立した会話履歴とAIのコンテキストを保持するため、以下のような並列作業が極めて効率的に行えます。

- **新機能のロジック実装と、関連する既存コードのリファクタリングを同時に検討。**
- **バグの原因調査をAIと進めながら、別のタブでそのバグに関するドキュメントやテストケースの草案を作成。**
- **あるAPIの仕様についてAIに質問しつつ、別のタブではそのAPIを利用するクライアントコードの生成を試みる。**
- **同じ課題に対して、異なるAIモデル（GPT-4 vs Claude 3 Opus）や異なるカスタム指示を与え、その結果を比較検討する。**

従来の開発スタイルでは、上記のような並列作業を行うために、複数のエディタウィンドウを開いたり、頻繁にGitブランチを切り替えたりする必要がありました。X (旧Twitter) などのSNSでも、熟練した開発者が複数のウィンドウやターミナルを駆使して作業している様子がしばしば見受けられます。

やり方としてはプロジェクトのコピーを複数作りそれぞれでブランチを切ってwindowを開いて並列実行しています。

Cursorの複数チャットタブ機能は、これらの作業の多くを単一のウィンドウ内で、よりスムーズかつ効率的にAIに複数の異なるタスクを同時に依頼したりできます。これにより、Window切り替え祭りを避けられより深い集中状態を維持しながら開発を進めることができます。

もちろん、Gitブランチの戦略的な活用は依然として重要ですが、Cursorの複数チャットは、ブランチレベルよりも細かい粒度での思考の分岐や実験を強力に支援するツールと言えるでしょう。

## Cursorのコアな基本機能詳解：AIとの対話を深化させる「@」コマンド

Cursorのチャットインターフェースは、単に自然言語でAIと会話するだけでなく、「 `@` 」記号に続けて特定のコマンドを入力することで、AIの能力をより的確に引き出し、特定のコンテキストを参照させるための多彩な機能を提供しています。

### チャット上で「@」入力で便利な機能一覧呼び出し

チャット入力欄で「 `@` 」を入力すると、利用可能なコマンドのサジェストリストが表示されます。これにより、どのような機能が使えるのかを簡単に把握し、選択できます。

以下は、特に使用頻度が高く、強力な「@」コマンドの例です。

- **`@Codebase`**: 現在開いているプロジェクト（ワークスペース）全体をAIの参照コンテキストに含めます。「このプロジェクトで〇〇という機能はどこに実装されていますか？」といった広範な質問に非常に有効です。
- **`@Folder <フォルダパス>`**: 指定したフォルダとその配下のファイル群をコンテキストに含めます。特定のモジュールや機能コンポーネント群について集中的に質問したり、リファクタリングを依頼したりする際に便利です。
- **`@File <ファイルパス>`**: 指定した単一または複数のファイルをコンテキストに含めます。特定のファイルのバグ修正や機能追加、ドキュメント生成などに使います。複数のファイルを指定することで、ファイル間の関連性を考慮したAIの応答が期待できます。
- **`@Symbols <シンボル名>`**: コード中の特定の関数名、クラス名、変数名などを指定し、それに関連する定義や参照箇所をAIに認識させます。「 `@Symbols MyClass` このクラスの責務を教えて」のように使います。
- **`@Docs <ライブラリ名/キーワード>`**: 指定したライブラリの公式ドキュメントや、関連する技術文書をAIが参照し、それに基づいて質問に回答したり、コードを生成したりします。
	- **例: `@Docs react useState`** -> Reactの `useState` フックに関する公式ドキュメントを参照して、使い方や注意点を説明してくれます。
	- **例: `@Docs python fastapi sqlalchemy`** -> PythonのFastAPIとSQLAlchemyを組み合わせる際のドキュメントやベストプラクティスを参照します。
- **`@Web <検索クエリ>`**: エディタ内でウェブ検索（Bing APIを利用）を行い、その結果をAIのコンテキストに含めます。最新の情報や、Cursorが直接アクセスできない外部リソースについて調べる際に有用です。
- **`@Terminal`**: (もし実装されていれば) 統合ターミナルの出力をAIのコンテキストに含める、またはAIにターミナルコマンドの実行を指示する機能。エラーメッセージの解析などに役立つ可能性があります。

これらの「@」コマンドを使いこなすことで、AIに対してより正確かつ豊富なコンテキスト情報を提供し、その結果として得られる応答の質と関連性を劇的に向上させることができます。自然言語による指示と「@」コマンドによるコンテキスト指定を組み合わせることが、CursorのAI機能を最大限に活用する鍵となります。

## セキュリティに注意すべき

最近は特に非エンジニアが罠にハマりそうなマルウェアを仕込む手法が誕生しているようです。DL先のアプリは偽サイトかどうか確認する必要があります。

ライブラリでも悪意あるコードが仕込まれることがあります。あまり更新されていないリポジトリやスターが少ないリポジトリは初心者ほど避けるべきです。

例えば、Auto-Runの機能を使用したい場合、不本意にインストールされないようにしタイのであれば npm install もしくは yarn add, pnpm add を Denylistに入れるなどの対策が必要です。

### プライバシーモードは基本Enabled

データをCursorと同期させないようにする機能です。設定ページのGeneralにあります。Background Agentやmemoriesの機能も魅力的ですがこれらはプライバシーモードを切る必要があるためAPIキーや機密情報を同期させない自信のある人だけが扱うべきです。

![](https://storage.googleapis.com/zenn-user-upload/da4dc78b3c14-20250605.png)

---

以上、Cursor v1.0で実現された新機能と、既存機能の進化、そしてそれらを活用するための具体的なポイントを解説しました。Cursorは、AIを開発ワークフローのあらゆる側面に統合することで、これまでにないレベルの生産性と創造性をもたらす可能性を秘めています。ぜひこれらの機能を実際に試し、あなたの開発スタイルを次のレベルへと引き上げてください。

13

6

13

6