# C6: セクション別画像プロンプトの自動生成

## 目的
記事の各セクションに最適な画像を生成するためのプロンプトを自動作成し、視覚的な理解を促進します。

## プロンプトテンプレート

### セクション分析
各セクションの内容を分析し、最適な画像タイプを決定します：

**セクションタイトル**: {{SECTION_TITLE}}
**セクション内容**: {{SECTION_SUMMARY}}
**情報タイプ**: {{INFO_TYPE}} // 概念説明/手順説明/比較/データ可視化

### 画像タイプ別プロンプトテンプレート

#### 1. 概念説明図（Conceptual Diagram）
```
A clear conceptual diagram illustrating {{CONCEPT}}.
Style: Infographic, educational
Elements: 
- Central concept: {{MAIN_ELEMENT}}
- Related components: {{SUB_ELEMENTS}}
- Connections: {{RELATIONSHIPS}}
Color scheme: Professional blues and grays with {{ACCENT_COLOR}} highlights
Layout: {{LAYOUT_TYPE}} // flowchart/mindmap/hierarchy
Text labels: {{KEY_TERMS}}
Background: Clean white or light gradient
Resolution: 1200x800, vector-style graphics
```

#### 2. ステップバイステップ図（Step-by-Step Guide）
```
A step-by-step visual guide showing {{PROCESS}}.
Style: Tutorial illustration
Number of steps: {{STEP_COUNT}}
Each step shows: {{STEP_DETAILS}}
Visual flow: Left to right / Top to bottom
Numbered indicators: Large, clear numbers (1, 2, 3...)
Color coding: {{PROGRESS_COLORS}}
Icons: {{RELEVANT_ICONS}}
Annotations: {{HELPFUL_NOTES}}
Resolution: 1200x800, clean and organized
```

#### 3. 比較表（Comparison Chart）
```
A comparison chart contrasting {{ITEM_A}} vs {{ITEM_B}}.
Style: Modern comparison infographic
Layout: Side-by-side or versus format
Categories compared: {{COMPARISON_POINTS}}
Visual indicators: Checkmarks, X marks, ratings
Color scheme: {{ITEM_A_COLOR}} vs {{ITEM_B_COLOR}}
Data representation: {{CHART_TYPE}} // bar/radar/table
Highlight: Key differences in {{HIGHLIGHT_COLOR}}
Resolution: 1200x800, data visualization style
```

#### 4. スクリーンショット風（Screenshot Style）
```
A realistic screenshot showing {{SOFTWARE_INTERFACE}}.
Style: Authentic software interface
Platform: {{OS_PLATFORM}}
Window elements: {{UI_ELEMENTS}}
Active content: {{SCREEN_CONTENT}}
Highlights: {{IMPORTANT_AREAS}} with arrows or boxes
Color accuracy: True to {{SOFTWARE_NAME}} design
Mouse cursor: Pointing to {{KEY_FEATURE}}
Resolution: 1200x800, pixel-perfect clarity
```

#### 5. アイコンセット（Icon Collection）
```
A collection of icons representing {{TOPIC_FEATURES}}.
Style: Modern flat design icons
Number of icons: {{ICON_COUNT}}
Icon subjects: {{ICON_LIST}}
Arrangement: Grid layout with labels
Color scheme: {{UNIFIED_PALETTE}}
Background: {{BG_STYLE}} // solid/gradient/pattern
Icon size: Uniform, clearly visible
Labels: {{LABEL_STYLE}} below each icon
Resolution: 1200x800, scalable vector style
```

## 実例：Claude Code記事のセクション画像

### セクション1: 「Claude Codeとは」
```
A clear conceptual diagram illustrating Claude Code's ecosystem.
Style: Infographic, educational
Elements: 
- Central concept: Claude AI brain icon
- Related components: Terminal, IDE integrations, API connections
- Connections: Flowing data streams between components
Color scheme: Professional blues and grays with purple highlights
Layout: Hub and spoke design
Text labels: "Natural Language", "Code Generation", "Multi-file Editing"
Background: Clean white with subtle grid pattern
Resolution: 1200x800, vector-style graphics
```

### セクション2: 「インストール手順」
```
A step-by-step visual guide showing Windows installation process.
Style: Tutorial illustration
Number of steps: 4
Each step shows: 
1. Download icon with Claude logo
2. Terminal window with install command
3. Configuration screen
4. Success checkmark with "Ready!" text
Visual flow: Left to right with arrows
Numbered indicators: Large, clear numbers in circles
Color coding: Progress from gray to green
Icons: Windows logo, terminal, settings gear, checkmark
Annotations: "30 seconds", "No WSL needed", "Native support"
Resolution: 1200x800, clean and organized
```

### セクション3: 「従来の方法との比較」
```
A comparison chart contrasting "Traditional Coding" vs "Claude Code".
Style: Modern comparison infographic
Layout: Split screen with dividing line
Categories compared: Time spent, Error rate, Learning curve, Output quality
Visual indicators: 
- Traditional: Red X marks, long time bars
- Claude Code: Green checkmarks, short time bars
Color scheme: Muted red vs vibrant green
Data representation: Horizontal bar charts
Highlight: "8 hours → 10 minutes" in bold
Resolution: 1200x800, data visualization style
```

## 画像配置ガイドライン
1. **導入部**: 概念図やアイキャッチ
2. **手順説明**: ステップバイステップ図
3. **機能説明**: スクリーンショットやUI図
4. **比較section**: 比較表やグラフ
5. **まとめ**: アイコンセットや総括図

## 最適化ポイント
- モバイル表示を考慮したレイアウト
- 圧縮しても判読可能なテキストサイズ
- アクセシビリティ（色覚多様性対応）
- ブランドガイドラインの遵守