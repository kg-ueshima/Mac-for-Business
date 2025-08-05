#!/bin/bash

# Claude Code 9段階ワークフロー実行スクリプト
# 使い方: ./run_workflow.sh "トピック名" "スタイル" "ターゲット層"

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 引数チェック
if [ $# -lt 1 ]; then
    echo -e "${RED}エラー: トピックを指定してください${NC}"
    echo "使い方: $0 \"トピック名\" [スタイル] [ターゲット層]"
    echo "例: $0 \"Claude Code Windows活用ガイド\" \"S3_kensu\" \"初心者開発者\""
    exit 1
fi

TOPIC="$1"
STYLE="${2:-S1_professional}"  # デフォルトはプロフェッショナル
TARGET="${3:-事務マネージャー}"  # デフォルトターゲット

# 作業ディレクトリの設定
WORK_DIR="Claude/outputs/$(date +%Y%m%d_%H%M%S)_$(echo $TOPIC | tr ' ' '_')"
mkdir -p "$WORK_DIR"

echo -e "${BLUE}=== Claude Code 9段階ワークフロー開始 ===${NC}"
echo -e "トピック: ${GREEN}$TOPIC${NC}"
echo -e "スタイル: ${GREEN}$STYLE${NC}"
echo -e "ターゲット: ${GREEN}$TARGET${NC}"
echo -e "作業ディレクトリ: ${GREEN}$WORK_DIR${NC}"
echo ""

# ログファイルの準備
LOG_FILE="$WORK_DIR/workflow.log"
echo "ワークフロー実行ログ - $(date)" > "$LOG_FILE"

# 各ステップの実行関数
run_step() {
    local step_num=$1
    local step_name=$2
    local output_file=$3
    
    echo -e "${YELLOW}[$step_num/9] $step_name を実行中...${NC}"
    echo "[$step_num/9] $step_name - $(date)" >> "$LOG_FILE"
    
    # ここで実際のClaude APIコールやスクリプト実行を行う
    # 以下は仮の処理
    echo "# $step_name" > "$WORK_DIR/$output_file"
    echo "トピック: $TOPIC" >> "$WORK_DIR/$output_file"
    echo "実行時刻: $(date)" >> "$WORK_DIR/$output_file"
    echo "" >> "$WORK_DIR/$output_file"
    
    sleep 1  # 実際の処理時間をシミュレート
    
    echo -e "${GREEN}✓ 完了${NC}"
    echo ""
}

# C1: リサーチプロンプト設計
run_step 1 "リサーチプロンプト設計" "C1_research_prompts.txt"

# C2: 包括的リサーチ実行
run_step 2 "包括的リサーチ実行" "C2_research_results.md"

# C3: 構造化アジェンダ生成
run_step 3 "構造化アジェンダ生成" "C3_article_agenda.md"

# C4: 記事執筆（スタイル適用）
echo -e "${YELLOW}[4/9] 記事執筆（$STYLE スタイル適用）を実行中...${NC}"
cp "Claude/styles/${STYLE}.md" "$WORK_DIR/applied_style.md" 2>/dev/null || echo "スタイルファイルが見つかりません"
run_step 4 "記事執筆" "C4_article.md"

# C5: サムネイル画像プロンプト生成
run_step 5 "サムネイル画像プロンプト生成（3案）" "C5_thumbnail_prompts.txt"

# C6: セクション画像プロンプト生成
run_step 6 "セクション画像プロンプト生成" "C6_section_image_prompts.txt"

# C7: Twitterスレッド生成
run_step 7 "X(Twitter)スレッド生成（15投稿）" "C7_twitter_thread.txt"

# C8: NewsPicks風対談台本生成
run_step 8 "NewsPicks風対談台本生成" "C8_newspicks_dialogue.md"

# C9: kensu風ポッドキャスト台本生成
run_step 9 "kensu風ポッドキャスト台本生成" "C9_kensu_podcast.md"

# 完了通知
echo -e "${GREEN}=== ワークフロー完了！ ===${NC}"
echo -e "全ての出力ファイルは以下に保存されました:"
echo -e "${BLUE}$WORK_DIR${NC}"
echo ""
echo -e "生成されたコンテンツ:"
ls -la "$WORK_DIR" | grep -E "\.(md|txt)$"
echo ""
echo -e "${GREEN}お疲れさまでした！${NC}"

# サマリーファイルの生成
cat > "$WORK_DIR/summary.md" << EOF
# ワークフローサマリー

## 基本情報
- **トピック**: $TOPIC
- **スタイル**: $STYLE
- **ターゲット層**: $TARGET
- **実行日時**: $(date)

## 生成されたファイル
1. C1_research_prompts.txt - リサーチプロンプト
2. C2_research_results.md - リサーチ結果
3. C3_article_agenda.md - 記事構成
4. C4_article.md - 完成記事（$STYLE スタイル）
5. C5_thumbnail_prompts.txt - サムネイル画像プロンプト（3案）
6. C6_section_image_prompts.txt - セクション画像プロンプト
7. C7_twitter_thread.txt - Twitterスレッド（15投稿）
8. C8_newspicks_dialogue.md - 対談形式台本
9. C9_kensu_podcast.md - 一人語り台本

## 次のステップ
1. 各ファイルの内容を確認
2. 必要に応じて微調整
3. 各プラットフォームに投稿

EOF

# オプション: 結果をブラウザで開く
if command -v open &> /dev/null; then
    read -p "結果をFinderで開きますか？ (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open "$WORK_DIR"
    fi
fi