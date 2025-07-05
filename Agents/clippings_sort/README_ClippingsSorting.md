# Enhanced ClippingsSorting Agent

## 概要

Enhanced ClippingsSorting Agentは、`Clippings`フォルダ内のMarkdownファイルを自動的に分析し、内容に基づいてカテゴリ別に分類し、さらに以下の機能を提供します：

- **テーマ別永続ノート作成**: 関連する内容をまとめたファイル（例：Cursorについて.md）
- **インデックスファイル作成**: プロジェクト全体の情報インデックス
- **構造化ファイル作成**: テーマに沿った関係性の整理

## 機能

### 1. 自動分類
- **work_related**: 業務関連の記事
- **personal_notes**: 個人メモ・アイデア
- **research**: 研究・調査関連
- **tutorials**: チュートリアル・学習資料
- **miscellaneous**: その他・未分類

### 2. テーマ別永続ノート作成
以下のテーマで関連ファイルをまとめたノートを作成：
- **Cursor**: Cursorエディタ関連
- **Obsidian**: Obsidian関連
- **AI**: 人工知能・機械学習関連
- **Python**: Pythonプログラミング関連
- **Microsoft**: Microsoft製品関連
- **GitHub**: Git・GitHub関連
- **Docker**: Docker・コンテナ関連
- **クラウド**: クラウドサービス関連
- **DX**: デジタル変革関連
- その他多数のテーマ

### 3. インデックスファイル作成
- カテゴリ別インデックス
- テーマ別インデックス
- タグ別インデックス

### 4. 構造化ファイル作成
- テーマ別の関連性分析
- 学習の流れの整理
- 共通キーワードの抽出

### 5. キーワード分析
- ファイル名と内容からキーワードを抽出
- 技術関連キーワード（AI、Python、開発など）
- ビジネス関連キーワード（経営、マネジメントなど）
- カテゴリ別キーワードによるスコアリング

### 6. 自動処理
- カテゴリフォルダの自動作成
- ファイルの自動移動
- 重複ファイルの検出
- 分析結果の永続ノート作成

## 使用方法

### 手動実行

```bash
# プロジェクトルートで実行
python Agents/clippings_sort/enhanced_clippings_sorter.py

# または
python Agents/clippings_sort/run_enhanced_clippings_sorter.py
```

### スケジュール実行

#### macOS (crontab)
```bash
# crontabを編集
crontab -e

# 毎日09:00に実行
0 9 * * * cd /path/to/Mac\ for\ Business && python Agents/clippings_sort/run_enhanced_clippings_sorter.py
```

#### Windows (タスクスケジューラ)
1. タスクスケジューラを開く
2. 「基本タスクの作成」を選択
3. トリガー: 毎日 09:00
4. 操作: プログラムの開始
5. プログラム: `python`
6. 引数: `Agents/clippings_sort/run_enhanced_clippings_sorter.py`
7. 開始場所: プロジェクトルート

## 設定

### カテゴリとキーワードのカスタマイズ

`Agents/clippings_sort/enhanced_clippings_sorter.py`の以下の部分を編集：

```python
# カテゴリフォルダの定義
self.categories = {
    "work_related": ["業務", "仕事", "プロジェクト", "会議", "報告", "管理"],
    "personal_notes": ["個人", "メモ", "アイデア", "思考"],
    "research": ["研究", "調査", "分析", "データ", "統計"],
    "tutorials": ["チュートリアル", "使い方", "手順", "ガイド", "学習"],
    "miscellaneous": ["その他", "雑記", "興味"]
}

# 技術関連キーワード
self.tech_keywords = [
    "AI", "機械学習", "Python", "JavaScript", "プログラミング", "開発",
    # 必要に応じて追加
]

# ビジネス関連キーワード
self.business_keywords = [
    "経営", "マネジメント", "戦略", "マーケティング", "営業", "顧客",
    # 必要に応じて追加
]
```

## 出力

### 1. カテゴリフォルダ
```
Clippings/
├── work_related/
├── personal_notes/
├── research/
├── tutorials/
└── miscellaneous/
```

### 2. テーマ別永続ノート
`03-Permanent-Notes/`にテーマ別のノートが保存されます：
- `Cursorについて.md`
- `Obsidianについて.md`
- `AIについて.md`
- その他テーマ別ファイル

### 3. インデックスファイル
`04-Index-Notes/`にインデックスが保存されます：
- `project_index_YYYYMMDD.md`

### 4. 構造化ファイル
`05-Structure-Notes/`に構造化ファイルが保存されます：
- `Cursor_structure.md`
- `Obsidian_structure.md`
- その他テーマ別構造化ファイル

### 5. 分析結果ノート
`03-Permanent-Notes/`に分析結果が保存されます：
- `clippings_analysis_YYYY-MM-DD_HH-MM-SS.md`

### 6. ログファイル
`logs/`フォルダに実行ログが保存されます：
- `enhanced_clippings_sorter_YYYYMMDD.log`

### 7. 処理レポート
プロジェクトルートに処理結果レポートが生成されます：
- `enhanced_clippings_sorting_report_YYYYMMDD_HHMMSS.md`

## 注意事項

### セキュリティ
- 機密情報が含まれるファイルは事前に確認してください
- 重要なファイルはバックアップを取ってから実行してください

### パフォーマンス
- 大量のファイルがある場合、処理に時間がかかる可能性があります
- 初回実行時は特に時間がかかります

### エラーハンドリング
- ファイル読み込みエラーは自動的にスキップされます
- 重複ファイルは検出されますが、自動削除は行いません
- ログファイルでエラー内容を確認できます

## トラブルシューティング

### よくある問題

1. **ファイルが見つからない**
   - `Clippings`フォルダが存在することを確認
   - ファイルパスが正しいことを確認

2. **権限エラー**
   - ファイルの読み書き権限を確認
   - 管理者権限で実行を試行

3. **文字エンコーディングエラー**
   - ファイルがUTF-8で保存されていることを確認
   - 特殊文字が含まれていないか確認

### ログの確認

```bash
# 最新のログを確認
tail -f logs/enhanced_clippings_sorter_$(date +%Y%m%d).log
```

## 更新履歴

- 2025-01-XX: 初回作成
- 機能: 自動分類、キーワード分析、永続ノート作成
- 2025-01-XX: Enhanced版作成
- 機能: テーマ別永続ノート、インデックス、構造化ファイル作成 