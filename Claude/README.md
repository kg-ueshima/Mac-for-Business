# Claude Code 9段階自動化ワークフロー（Enhanced Version）

**8時間が10分になる生産性革命** - 1つのキーワードから9種類の高品質コンテンツを自動生成する、Claude Code用の包括的なワークフローシステムです。

## 概要

このワークフローは、以下の9段階で構成されています：

1. **C1: リサーチプロンプト設計** - 深い調査のためのプロンプトを自動設計
2. **C2: 包括的リサーチ** - Web検索を駆使した情報収集
3. **C3: 構造化アジェンダ** - 記事の詳細な構成を自動生成
4. **C4: 記事執筆** - スタイルファイルを適用した高品質記事
5. **C5: サムネイル画像プロンプト** - 3つの異なるアプローチ
6. **C6: セクション画像プロンプト** - 各セクション用の画像
7. **C7: Twitterスレッド** - 15投稿の魅力的なスレッド
8. **C8: 対談形式台本** - NewsPicks風の知的な対話
9. **C9: 一人語り台本** - kensu風の親しみやすいポッドキャスト

## ディレクトリ構造

```
Claude/
├── prompts/          # 各段階のプロンプトテンプレート
│   ├── C1_research_prompt_designer.md
│   ├── C2_comprehensive_research.md
│   ├── C3_structured_agenda.md
│   ├── C4_article_writer.md
│   ├── C5_thumbnail_prompt_generator.md
│   ├── C6_section_image_prompts.md
│   ├── C7_twitter_thread_generator.md
│   ├── C8_newspicks_dialogue_script.md
│   └── C9_kensu_style_podcast.md
├── styles/           # 記事スタイルテンプレート
│   ├── S1_professional.md    # プロフェッショナルスタイル
│   ├── S2_casual.md          # カジュアルスタイル
│   └── S3_kensu.md           # kensu風スタイル
├── scripts/          # 実行用スクリプト
│   └── run_workflow.sh
├── outputs/          # 生成されたコンテンツ
└── templates/        # その他のテンプレート
```

## 使い方

### 🚀 Enhanced Version（推奨）

```bash
cd Claude/scripts
./run_workflow_enhanced.sh "あなたのトピック"
```

### 基本的な実行

```bash
cd Claude/scripts
./run_workflow.sh "あなたのトピック"
```

### オプション指定

```bash
# デフォルト（S1_professional/事務マネージャー）で実行
./run_workflow.sh "業務効率化ガイド"

# スタイルとターゲット層を指定
./run_workflow.sh "Claude Code活用ガイド" "S3_kensu" "初心者開発者"

# プロフェッショナルスタイルで実行
./run_workflow.sh "AI開発の最新動向" "S1_professional" "企業の意思決定者"
```

### 利用可能なスタイル

- **S1_professional**: フォーマルで信頼性重視
- **S2_casual**: カジュアルで親しみやすい
- **S3_kensu**: 実体験ベースで共感的
- **S4_tetumemo**: 数値重視、Before/After、実証主義（Enhanced版のデフォルト）

## 出力例

実行すると、以下のようなファイルが生成されます：

```
outputs/20250803_141500_Claude_Code活用ガイド/
├── C1_research_prompts.txt      # リサーチ用プロンプト
├── C2_research_results.md       # 調査結果
├── C3_article_agenda.md         # 記事構成案
├── C4_article.md               # 完成記事（5,000文字以上）
├── C5_thumbnail_prompts.txt     # サムネイル画像プロンプト3案
├── C6_section_image_prompts.txt # セクション画像プロンプト
├── C7_twitter_thread.txt        # Twitterスレッド15投稿
├── C8_newspicks_dialogue.md     # 対談形式台本
├── C9_kensu_podcast.md         # 一人語りポッドキャスト台本
├── applied_style.md            # 適用されたスタイル
├── workflow.log                # 実行ログ
└── summary.md                  # サマリー
```

## カスタマイズ

### プロンプトのカスタマイズ

各プロンプトファイル（`prompts/`内）を編集することで、生成内容をカスタマイズできます。

### スタイルの追加

新しいスタイルを追加する場合：

1. `styles/`ディレクトリに新しいスタイルファイルを作成
2. 既存のスタイルファイルを参考に記述
3. スクリプト実行時に新しいスタイル名を指定

### ワークフローの拡張

`scripts/run_workflow.sh`を編集して、新しいステップを追加できます。

## 活用のコツ

1. **トピック選定**: 具体的で明確なトピックを選ぶ
2. **スタイル選択**: ターゲット層に合わせて適切なスタイルを選ぶ
3. **生成後の調整**: 生成されたコンテンツは下書きとして使い、必要に応じて編集
4. **フィードバック**: 生成結果を確認し、プロンプトを改善

## トラブルシューティング

### スクリプトが実行できない場合

```bash
chmod +x scripts/run_workflow.sh
```

### 出力ディレクトリが見つからない場合

```bash
mkdir -p Claude/outputs
```

## 今後の展開

- Claude APIとの直接統合
- GUI版の開発
- 多言語対応
- カスタムワークフローの作成機能

## ライセンス

このプロジェクトは個人利用を想定しています。商用利用の際はご相談ください。

---

**注意**: このワークフローは、Claude Codeと組み合わせて使用することを想定しています。実際の実行には、各ステップでClaude Codeへのプロンプト入力が必要です。