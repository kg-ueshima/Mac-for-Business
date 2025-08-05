# C4: 高品質記事執筆（Universal Version）

## 目的
agenda.mdとresearch-results.mdを基に、10,000～15,000文字の高品質な記事を生成します。Claude CodeとGemini CLI両対応。

## 記事メタ情報テンプレート
```markdown
# {{ARTICLE_TITLE}}

## 記事メタ情報
- 文字数: {{WORD_COUNT}}文字
- 読了時間: 約{{READING_TIME}}分
- キーワード: {{KEYWORDS}}
- 更新日: {{DATE}}
```

## 記事執筆テンプレート

### イントロダクション
```markdown
{{HOOK_QUESTION}}

{{EMPATHY_STATEMENT}}

{{SHOCKING_REVELATION}}

**{{BEFORE_METRIC}} → {{AFTER_METRIC}}**

{{VALUE_PROPOSITION}}
```

### 本文構成

#### 第1章テンプレート
```markdown
## {{CHAPTER_TITLE}}

{{CHAPTER_INTRO}}

### {{SECTION_1_TITLE}}
{{SECTION_1_CONTENT}}

**重要なポイント**：
- {{KEY_POINT_1}}
- {{KEY_POINT_2}}
- {{KEY_POINT_3}}

{{SUPPORTING_DATA}}

### {{SECTION_2_TITLE}}
{{SECTION_2_CONTENT}}

> {{EXPERT_QUOTE}}

{{DETAILED_EXPLANATION}}

### {{SECTION_3_TITLE}}
{{SECTION_3_CONTENT}}

```code
{{CODE_EXAMPLE}}
```

{{PRACTICAL_IMPLICATION}}
```

#### データ可視化テンプレート
```markdown
| {{METRIC_NAME}} | Before | After | 改善率 |
|----------------|---------|--------|---------|
| {{METRIC_1}} | {{BEFORE_1}} | {{AFTER_1}} | {{RATE_1}} |
| {{METRIC_2}} | {{BEFORE_2}} | {{AFTER_2}} | {{RATE_2}} |
| {{METRIC_3}} | {{BEFORE_3}} | {{AFTER_3}} | {{RATE_3}} |
```

#### 実践セクションテンプレート
```markdown
### {{ACTION_TITLE}}

#### ステップ1: {{STEP_1_TITLE}}
{{STEP_1_DESCRIPTION}}

```bash
{{COMMAND_OR_ACTION}}
```

**期待される結果**: {{EXPECTED_RESULT}}

#### ステップ2: {{STEP_2_TITLE}}
{{STEP_2_DESCRIPTION}}

💡 **プロのコツ**: {{PRO_TIP}}

#### ステップ3: {{STEP_3_TITLE}}
{{STEP_3_DESCRIPTION}}

⚠️ **注意点**: {{WARNING}}
```

### 結論テンプレート
```markdown
## {{CONCLUSION_TITLE}}

### 📊 数字で見る成果
{{METRICS_SUMMARY}}

### 🎯 今すぐできる3つのアクション
1. **{{ACTION_1}}**（所要時間: {{TIME_1}}）
   → {{BENEFIT_1}}

2. **{{ACTION_2}}**（所要時間: {{TIME_2}}）
   → {{BENEFIT_2}}

3. **{{ACTION_3}}**（所要時間: {{TIME_3}}）
   → {{BENEFIT_3}}

### 💬 最後に
{{PERSONAL_MESSAGE}}

{{CLOSING_STATEMENT}}

---
📌 **関連リソース**
- [{{RESOURCE_1}}]({{LINK_1}})
- [{{RESOURCE_2}}]({{LINK_2}})
- [{{RESOURCE_3}}]({{LINK_3}})
```

## スタイル別執筆ガイドライン

### S4_tetumemo スタイル
- 具体的な数値を太字で強調
- Before/Afterを明確に対比
- 「この差、どう思います？」などの問いかけ
- 失敗談を正直に共有
- 絵文字を効果的に使用（やりすぎない）

### S3_kensu スタイル
- 共感的な語りかけ
- 「私も同じでした」などの共感フレーズ
- 希望を持てる前向きな締めくくり
- 個人的な体験を交える

### S2_casual スタイル
- 話し言葉風の文体
- 「めっちゃ」「マジで」などのカジュアル表現
- 読者を「みんな」と呼ぶ
- 楽観的でフレンドリー

### S1_professional スタイル
- フォーマルな文体
- データと客観性重視
- 「です・ます」調
- 専門用語は正確に使用

## 文体リライト機能

### リライトプロンプト
```
以下の記事を、私の文体でリライトしてください。

【私の文体の特徴】
- {{STYLE_FEATURE_1}}
- {{STYLE_FEATURE_2}}
- {{STYLE_FEATURE_3}}

【サンプル文章】
{{SAMPLE_TEXT}}

【リライト対象】
{{ORIGINAL_ARTICLE}}
```

## プラットフォーム別の注意事項

### Gemini CLI
- ファイル名: `blog-post.md`
- 一度に生成可能
- Markdown形式を維持

### Claude Code
- Deep Research結果を活用
- Projects機能でコンテキスト管理
- 段階的な生成も可能

## 品質チェックリスト

### 必須項目
- [ ] 10,000文字以上
- [ ] アジェンダに沿った構成
- [ ] 具体的な数値・データ
- [ ] Before/Afterの明確な対比
- [ ] 実践可能なアクション
- [ ] 適切なスタイルの適用

### 推奨項目
- [ ] 個人的な体験談
- [ ] 視覚的な要素（表、リスト）
- [ ] 専門用語の説明
- [ ] 読者への問いかけ
- [ ] 関連リソースのリンク

## 実行例

```
C4を実行します。

参照ファイル:
- agenda.md（構成）
- research-results.md（調査データ）
- applied_style.md（S4_tetumemo）

記事を執筆中...

完成！
- 文字数: 12,857文字
- 読了時間: 約26分
- スタイル: tetumemo風（数値重視、実証的）
```