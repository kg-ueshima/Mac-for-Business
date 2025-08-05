# Universal 9段階コンテンツ生成ワークフロー

**Claude Code & Gemini CLI 完全対応版** - テツメモさんの実証済みワークフローを再現

## 🎯 概要

1つのキーワードから9種類の高品質コンテンツを自動生成する、包括的なワークフローシステムです。

**実績**: 8時間の作業を10分に短縮（96%の時間削減）

## 🤖 対応プラットフォーム

- **Claude Code** - Anthropic公式のAI開発環境
- **Gemini CLI** - Google AIの無料コマンドラインツール

## 📁 生成されるコンテンツ

| ファイル名 | 内容 | 文字数/規模 |
|-----------|------|------------|
| research_prompt.md | Deep Research用プロンプト | - |
| research-results.md | 調査結果 | 5,000文字+ |
| agenda.md | 記事構成案 | 2,000文字+ |
| blog-post.md | 完成記事 | 10,000-15,000文字 |
| main-images.md | サムネイル画像プロンプト | 3案 |
| section-images.md | セクション画像プロンプト | 5-10個 |
| x-posts.md | X(Twitter)投稿文 | 15投稿 |
| podcast-dialogue-script.md | 対談形式台本 | 15-20分 |
| podcast-solo-script.md | 一人語り台本 | 10-15分 |

## 🚀 クイックスタート

### 1. セットアップ

```bash
# リポジトリをクローン
git clone [repository-url]
cd Claude

# スクリプトに実行権限を付与
chmod +x scripts/*.sh
chmod +x *.sh
```

### 2. プラットフォームの準備

#### Claude Code
```bash
# インストール（30秒）
# https://claude.ai/download からダウンロード
```

#### Gemini CLI
```bash
# Node.js環境で
npm install -g @google/generative-ai-cli

# APIキーの設定
export GOOGLE_AI_API_KEY="your-api-key"
```

### 3. 実行

```bash
# Universal版（自動判定）- デフォルトはS1_professional/事務マネージャー
./scripts/run_workflow_universal.sh "あなたのトピック"

# スタイルとターゲットを指定
./scripts/run_workflow_universal.sh "業務効率化ガイド" "S1_professional" "事務マネージャー"

# プラットフォーム指定
./scripts/run_workflow_universal.sh "AIツール活用術" "S4_tetumemo" "クリエイター" "gemini"
```

## 📋 ワークフローの詳細

### C1: Deep Research用プロンプト生成
- 包括的な調査項目を自動設計
- 5つの観点から体系的なリサーチプロンプトを生成

### C2: Deep Research実行（手動）
- **重要**: Gemini CLIはDeep Research機能がないため手動実行
- ChatGPT/Geminiで調査を実行し、結果を保存

### C3: 詳細アジェンダ生成
- 10,000-15,000文字の記事構成を設計
- SEO最適化された章立て

### C4: 高品質記事執筆
- 指定スタイルで自動執筆
- Before/After、具体的数値を含む説得力のある内容

### C5-C6: 画像プロンプト生成
- インパクトのあるサムネイル（3案）
- 各セクション用の説明画像

### C7: SNS展開
- 15投稿のTwitterスレッド
- エンゲージメント最適化

### C8-C9: 音声コンテンツ
- NewsPicks風の知的な対談台本
- kensu風の親しみやすい一人語り

## 🎨 利用可能なスタイル

| スタイル | 特徴 | 適用場面 |
|---------|------|---------|
| S1_professional | フォーマル、信頼性重視 | ビジネス文書、技術解説 |
| S2_casual | カジュアル、親しみやすい | ブログ、初心者向け |
| S3_kensu | 共感的、実体験ベース | 個人ブログ、体験記 |
| S4_tetumemo | 数値重視、Before/After | 実証記事、検証系 |

## 💡 文体リライト機能

生成された記事を、あなた独自の文体に変換：

```bash
# 文体分析シートを記入
cat templates/style_rewrite_guide.md

# リライトプロンプトを実行
"blog-post.mdの内容を、私の文体でリライトしてください"
```

## 📊 実績と効果

### Before（従来の手動作業）
- リサーチ: 3時間
- 執筆: 4時間
- 画像・SNS: 1時間
- **合計: 8時間**

### After（本ワークフロー）
- 全工程: 10分（C2除く）
- **時間削減: 96%**
- **生産性: 10倍以上**

## 🔧 トラブルシューティング

### Gemini CLIが動かない
```bash
# Node.jsバージョン確認
node --version  # v16以上推奨

# 再インストール
npm uninstall -g @google/generative-ai-cli
npm install -g @google/generative-ai-cli
```

### Claude Codeが検出されない
```bash
# パスを通す
export PATH="/Applications/Claude.app/Contents/MacOS:$PATH"
```

### C2のリサーチが不十分
- より具体的な質問を追加
- 複数のAIツールで交差検証
- 最新情報を重視する指示を追加

## 📚 関連ドキュメント

- [プロンプトテンプレート集](prompts/)
- [スタイルガイド](styles/)
- [具体例集](templates/concrete_examples.md)
- [文体リライトガイド](templates/style_rewrite_guide.md)

## 🙏 クレジット

このワークフローは、テツメモさんの以下の記事を参考に作成されました：

- [Gemini CLIでヤバい「コンテンツ工場」を完全無料で構築する裏技](https://note.com/tetumemo/)
- [Claude 4を「コンテンツ制作チーム」に変える裏技](https://note.com/tetumemo/)

## 📄 ライセンス

個人利用・商用利用可能。再配布時は出典を明記してください。

---

**質問・要望**: Issues または Discussions でお気軽にどうぞ！

**最終更新**: 2025年8月3日