# 医療情報RSS取得・要約プログラム

## 概要

このプログラムは、医療情報サイト（https://mfd.jiho.jp/genre/1/rss.xml）からRSSフィードを取得し、各記事の内容をGeminiで要約してファイルに保存するツールです。

## ファイル構成

- `medifax_digest.py` - 基本的なRSS取得・要約プログラム
- `medifax_auto_login.py` - Safari自動ログイン機能付きプログラム
- `README_medifax.md` - このファイル

## 必要な環境設定

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`env.local`ファイルに以下の設定を追加してください：

```bash
# Gemini API設定
GEMINI_API_KEY=your_gemini_api_key_here

# 医療情報サイトのログイン情報（自動ログイン機能を使用する場合）
MEDIFAX_USERNAME=your_username
MEDIFAX_PASSWORD=your_password
```

## 使用方法

### 基本的な使用方法（ログイン不要の場合）

```bash
cd Agents/medifax
python medifax_digest.py
```

### 自動ログイン機能付き（推奨）

```bash
cd Agents/medifax
python medifax_auto_login.py
```

## 機能

### 1. RSSフィード取得
- 指定されたRSS URLから記事情報を取得
- タイトル、リンク、日付（dc:jdate）を抽出

### 2. 記事内容取得
- 各記事のURLから本文を取得
- BeautifulSoupを使用してHTMLからテキストを抽出
- 複数のセレクタを試行して最適な内容を取得

### 3. Gemini要約
- 各記事の内容をGemini APIで要約
- 医療・病院経営に関連する重要なポイントを抽出
- 実務的に役立つ情報を優先

### 4. ファイル保存
- 詳細ファイル（Markdown形式）
- 要約のみのファイル（Markdown形式）
- JSON形式のデータファイル

## 出力ファイル

プログラムは以下のファイルを `80-業務日報/medifax_digest/` ディレクトリに保存します：

- `medifax_digest_YYYY-MM-DD_HHMMSS.md` - 詳細情報
- `medifax_summary_YYYY-MM-DD_HHMMSS.md` - 要約のみ
- `medifax_data_YYYY-MM-DD_HHMMSS.json` - JSON形式データ

## Safari自動ログイン機能

`medifax_auto_login.py`では、以下の機能が利用できます：

1. **環境変数による自動ログイン**
   - `MEDIFAX_USERNAME`と`MEDIFAX_PASSWORD`が設定されている場合
   - AppleScriptを使用してSafariで自動ログイン

2. **手動ログイン案内**
   - 環境変数が設定されていない場合
   - 手動でログインするよう案内

## トラブルシューティング

### RSSフィードが取得できない場合
- ネットワーク接続を確認
- RSS URLが正しいか確認
- ログインが必要な場合は自動ログイン機能を使用

### 記事内容が取得できない場合
- サイトの構造が変更された可能性
- ログインが必要な記事の場合、自動ログイン機能を使用

### Gemini要約でエラーが発生する場合
- `GEMINI_API_KEY`が正しく設定されているか確認
- API制限に達していないか確認

## カスタマイズ

### RSS URLの変更
プログラム内の `self.rss_url` を変更することで、他のRSSフィードも取得できます。

### 要約プロンプトの調整
`summarize_article`メソッド内のプロンプトを変更することで、要約の方向性を調整できます。

### 出力形式の変更
`save_summary`メソッドを修正することで、出力形式をカスタマイズできます。

## 注意事項

- API制限を避けるため、記事処理間に1秒の待機時間を設けています
- 大量の記事がある場合、処理に時間がかかる可能性があります
- ログイン情報は環境変数で管理し、ソースコードに直接記載しないでください 