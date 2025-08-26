#!/bin/bash

# Claude専用 9段階ワークフロー実行スクリプト
# Claude Codeのみで実行

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# 引数チェック
if [ $# -lt 1 ]; then
    echo -e "${RED}エラー: トピックを指定してください${NC}"
    echo "使い方: $0 \"トピック名\" [スタイル] [ターゲット層]"
    echo "例: $0 \"AIツール活用術\" \"S1_professional\" \"事務マネージャー\""
    exit 1
fi

TOPIC="$1"
STYLE="${2:-S1_professional}"
TARGET="${3:-事務マネージャー}"

# Claude Codeの存在確認
if ! command -v claude &> /dev/null; then
    echo -e "${RED}エラー: Claude Codeが見つかりません${NC}"
    echo "インストール方法: https://claude.ai/download"
    exit 1
fi

# 作業ディレクトリの設定
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
# スクリプト位置とリポジトリルートの特定
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
# Pythonでトピック名を要約・安全化（40バイト以内）。
# 依存関係が不足している場合は安全なフォールバックを使用。
SAFE_TOPIC=$(PYTHONPATH="$REPO_ROOT" python3 - "$TOPIC" <<'PY'
import sys, re
topic = sys.argv[1] if len(sys.argv) > 1 else ""
try:
    from Agents.daily_report.modules.gemini import summarize_for_folder
    print(summarize_for_folder(topic))
except Exception:
    safe_topic = re.sub(r'[^\w\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\-_.]', '_', topic)
    if len(safe_topic.encode('utf-8')) > 40:
        # 40バイトに収まるように調整
        enc = safe_topic.encode('utf-8')[:40]
        try:
            safe_topic = enc.decode('utf-8')
        except UnicodeDecodeError:
            safe_topic = enc.decode('utf-8', 'ignore')
    print(safe_topic)
PY
)
WORK_DIR="Claude/outputs/${TIMESTAMP}_${SAFE_TOPIC}"
mkdir -p "$WORK_DIR"

# プロジェクトのルートディレクトリを取得
PROJECT_ROOT="$REPO_ROOT"

# ヘッダー表示
clear
echo -e "${BOLD}${PURPLE}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${PURPLE}║        Claude専用 9段階ワークフロー                      ║${NC}"
echo -e "${BOLD}${PURPLE}║     Deep ResearchもClaude Codeで完全自動化              ║${NC}"
echo -e "${BOLD}${PURPLE}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# 設定確認
echo -e "${CYAN}【実行設定】${NC}"
echo -e "🤖 プラットフォーム: ${GREEN}Claude Code${NC}"
echo -e "📝 トピック: ${GREEN}$TOPIC${NC}"
echo -e "🎨 スタイル: ${GREEN}$STYLE${NC}"
echo -e "👥 ターゲット: ${GREEN}$TARGET${NC}"
echo -e "📁 出力先: ${GREEN}$WORK_DIR${NC}"
echo ""

# ファイル名定義（通常の変数として定義）
FILE_C1="research_prompt.md"
FILE_C2="research-results.md"
FILE_C3="agenda.md"
FILE_C4="blog-post.md"
FILE_C5="main-images.md"
FILE_C6="section-images.md"
FILE_C7="x-posts.md"
FILE_C8="podcast-dialogue-script.md"
FILE_C9="podcast-solo-script.md"

# 初期ファイル作成
touch "$WORK_DIR/$FILE_C1"
touch "$WORK_DIR/$FILE_C2"
touch "$WORK_DIR/$FILE_C3"
touch "$WORK_DIR/$FILE_C4"
touch "$WORK_DIR/$FILE_C5"
touch "$WORK_DIR/$FILE_C6"
touch "$WORK_DIR/$FILE_C7"
touch "$WORK_DIR/$FILE_C8"
touch "$WORK_DIR/$FILE_C9"

# 実行プロンプトの生成
cat > "$WORK_DIR/execution_prompts.md" << EOF
# $TOPIC - Claude Code実行プロンプト

## 🚀 一括実行プロンプト

以下のプロンプトをClaude Codeで実行してください:

\`\`\`
「$TOPIC」について、9段階のコンテンツ生成ワークフローを実行します。

作業ディレクトリ: $WORK_DIR
スタイル: $STYLE
ターゲット: $TARGET

実行手順:
1. C1: Deep Research用プロンプト作成 → research_prompt.md
2. C2: Deep Research実行（Claude Code内で実行） → research-results.md
3. C3: アジェンダ生成 → agenda.md
4. C4: 記事執筆（$STYLE スタイル、10,000文字以上） → blog-post.md
5. C5: サムネイル画像プロンプト（3案） → main-images.md
6. C6: セクション画像プロンプト → section-images.md
7. C7: X投稿文（15投稿） → x-posts.md
8. C8: 対談形式台本（15-20分） → podcast-dialogue-script.md
9. C9: 一人語り台本（10-15分） → podcast-solo-script.md

各ステップの成果物は上記のファイル名で保存してください。
\`\`\`

## 📋 個別実行用プロンプト（必要に応じて）

### C1-C2: Deep Research
\`\`\`
「$TOPIC」について包括的なDeep Researchを実行してください。

重点項目：
1. 基本機能と特徴（$TARGET視点）
2. 業務効率化への具体的な活用方法
3. 導入コストとROI
4. 実践的な使用例とケーススタディ
5. 他ツールとの比較
6. セキュリティとコンプライアンス
7. 導入時の注意点とベストプラクティス

調査結果は以下に保存：
- research_prompt.md（調査プロンプト）
- research-results.md（調査結果）
\`\`\`

### C3: アジェンダ生成
\`\`\`
research-results.mdを参照し、以下の構成でアジェンダを作成：
- タイトル: 【2025年最新】$TOPIC完全ガイド
- 文字数: 10,000～15,000文字
- 対象: $TARGET
- 構成: イントロ + 5章 + 結論

agenda.mdに保存してください。
\`\`\`

### C4: 記事執筆
\`\`\`
agenda.mdに基づき、$STYLE スタイルで記事を執筆してください。
- 文字数: 10,000文字以上
- トーン: プロフェッショナル、信頼性重視
- 実務的な内容を重視

blog-post.mdに保存してください。
\`\`\`

## 📍 作業ディレクトリ
$WORK_DIR

## 📁 参照ファイル
- プロンプトテンプレート: ../../prompts/
- スタイルファイル: ../../styles/

## ⚡ 効率的な実行のコツ
1. 一括実行プロンプトを使用すれば、全工程が自動化されます
2. 各ファイルは自動的に適切な場所に保存されます
3. スタイルファイルは ../../styles/ から参照されます
EOF

# 完了メッセージ
echo -e "${BOLD}${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${GREEN}║           準備完了！次のステップへ                       ║${NC}"
echo -e "${BOLD}${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}【次の操作】${NC}"
echo ""
echo -e "${CYAN}方法: 手動でClaude Codeを起動${NC}"
echo -e "1. ターミナルで以下を実行:"
echo -e "   ${GREEN}cd $WORK_DIR${NC}"
echo -e "   ${GREEN}claude .${NC}"
echo ""
echo -e "2. Claude Codeで以下を入力:"
echo -e "   ${GREEN}@execution_prompts.md${NC}"
echo ""
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}💡 ポイント${NC}"
echo -e "- Deep ResearchもClaude Code内で自動実行されます"
echo -e "- 全9ステップが一括で完了します（約10-15分）"
echo -e "- 各ファイルは自動的に保存されます"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"