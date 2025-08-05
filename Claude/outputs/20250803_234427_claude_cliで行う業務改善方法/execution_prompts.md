# claude cliで行う業務改善方法 - Claude Code実行プロンプト

## 🚀 一括実行プロンプト

以下のプロンプトをClaude Codeで実行してください：

```
「��について、9段階のコンテンツ生成ワークフローを実行します。

作業ディレクトリ: Claude/outputs/20250803_234427_claude_cliで行う業務改善方法
スタイル: S1_professional
ターゲット: 事務マネージャー

実行手順:
1. C1: Deep Research用プロンプト作成 → research_prompt.md
2. C2: Deep Research実行（Claude Code内で実行） → research-results.md
3. C3: アジェンダ生成 → agenda.md
4. C4: 記事執筆（S1_professional スタイル、10,000文字以上） → blog-post.md
5. C5: サムネイル画像プロンプト（3案） → main-images.md
6. C6: セクション画像プロンプト → section-images.md
7. C7: X投稿文（15投稿） → x-posts.md
8. C8: 対談形式台本（15-20分） → podcast-dialogue-script.md
9. C9: 一人語り台本（10-15分） → podcast-solo-script.md

各ステップの成果物は上記のファイル名で保存してください。
```

## 📋 個別実行用プロンプト（必要に応じて）

### C1-C2: Deep Research
```
「��について包括的なDeep Researchを実行してください。

重点項目：
1. 基本機能と特徴（��点）
2. 業務効率化への具体的な活用方法
3. 導入コストとROI
4. 実践的な使用例とケーススタディ
5. 他ツールとの比較
6. セキュリティとコンプライアンス
7. 導入時の注意点とベストプラクティス

調査結果は以下に保存：
- research_prompt.md（調査プロンプト）
- research-results.md（調査結果）
```

### C3: アジェンダ生成
```
research-results.mdを参照し、以下の構成でアジェンダを作成：
- タイトル: 【2025年最新】��全ガイド
- 文字数: 10,000～15,000文字
- 対象: 事務マネージャー
- 構成: イントロ + 5章 + 結論

agenda.mdに保存してください。
```

### C4: 記事執筆
```
agenda.mdに基づき、S1_professional スタイルで記事を執筆してください。
- 文字数: 10,000文字以上
- トーン: プロフェッショナル、信頼性重視
- 実務的な内容を重視

blog-post.mdに保存してください。
```

## 📍 作業ディレクトリ
Claude/outputs/20250803_234427_claude_cliで行う業務改善方法

## ⚡ 効率的な実行のコツ
1. 一括実行プロンプトを使用すれば、全工程が自動化されます
2. 各ファイルは自動的に適切な場所に保存されます
3. スタイルファイルは Claude/outputs/20250803_234427_claude_cliで行う業務改善方法/styles/ にあります
