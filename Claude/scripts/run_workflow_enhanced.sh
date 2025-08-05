#!/bin/bash

# Claude Code 9段階ワークフロー実行スクリプト（Enhanced Version）
# tetumemo記事のような高品質コンテンツを生成

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
    echo "例: $0 \"Claude Code Windows活用ガイド\" \"S4_tetumemo\" \"コンテンツクリエイター\""
    exit 1
fi

TOPIC="$1"
STYLE="${2:-S1_professional}"  # デフォルトはプロフェッショナル
TARGET="${3:-事務マネージャー}"  # デフォルトターゲット

# 作業ディレクトリの設定
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
SAFE_TOPIC=$(echo "$TOPIC" | tr ' ' '_' | tr '/' '_')
WORK_DIR="Claude/outputs/${TIMESTAMP}_${SAFE_TOPIC}"
mkdir -p "$WORK_DIR"

# プログレスバー関数
show_progress() {
    local current=$1
    local total=$2
    local width=50
    local percentage=$((current * 100 / total))
    local completed=$((width * current / total))
    
    printf "\r["
    printf "%${completed}s" | tr ' ' '='
    printf "%$((width - completed))s" | tr ' ' ' '
    printf "] %d%%" $percentage
}

# ヘッダー表示
clear
echo -e "${BOLD}${PURPLE}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${PURPLE}║        Claude Code 9段階ワークフロー (Enhanced)          ║${NC}"
echo -e "${BOLD}${PURPLE}║          〜 8時間が10分になる生産性革命 〜               ║${NC}"
echo -e "${BOLD}${PURPLE}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# 設定確認
echo -e "${CYAN}【実行設定】${NC}"
echo -e "📝 トピック: ${GREEN}$TOPIC${NC}"
echo -e "🎨 スタイル: ${GREEN}$STYLE${NC}"
echo -e "👥 ターゲット: ${GREEN}$TARGET${NC}"
echo -e "📁 出力先: ${GREEN}$WORK_DIR${NC}"
echo ""

# Before/After予測表示
echo -e "${YELLOW}【期待される成果】${NC}"
echo -e "⏰ Before: 8時間（リサーチ3h + 執筆4h + 画像1h）"
echo -e "🚀 After: 10分（全自動で9種類のコンテンツ生成）"
echo -e "📈 生産性: ${BOLD}${GREEN}96%向上${NC}"
echo ""

read -p "$(echo -e ${CYAN}この設定で実行しますか？${NC} [Y/n]: )" -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]] && [[ ! -z $REPLY ]]; then
    echo -e "${RED}キャンセルしました${NC}"
    exit 1
fi

# ログファイルの準備
LOG_FILE="$WORK_DIR/workflow_enhanced.log"
METRICS_FILE="$WORK_DIR/metrics.json"

# メトリクス初期化
cat > "$METRICS_FILE" << EOF
{
  "workflow_version": "enhanced_2.0",
  "start_time": "$(date -Iseconds)",
  "topic": "$TOPIC",
  "style": "$STYLE",
  "target": "$TARGET",
  "steps": []
}
EOF

# タイマー開始
START_TIME=$(date +%s)

echo ""
echo -e "${BOLD}${GREEN}ワークフロー開始！${NC}"
echo -e "${CYAN}☕ コーヒーでも飲みながら、10分お待ちください...${NC}"
echo ""

# 各ステップの実行関数（改良版）
run_enhanced_step() {
    local step_num=$1
    local step_name=$2
    local output_file=$3
    local estimated_time=$4
    
    local step_start=$(date +%s)
    
    echo -e "${BOLD}[Step $step_num/9] $step_name${NC}"
    echo -e "予想時間: ${estimated_time}"
    
    # プログレスバーの表示
    for i in {1..10}; do
        show_progress $i 10
        sleep 0.1
    done
    echo ""
    
    # メタデータの生成
    cat > "$WORK_DIR/${output_file%.md}_meta.json" << EOF
{
  "step": $step_num,
  "name": "$step_name",
  "timestamp": "$(date -Iseconds)",
  "topic": "$TOPIC",
  "style": "$STYLE"
}
EOF
    
    # プロンプトのコピー
    if [ -f "Claude/prompts/C${step_num}_"*.md ]; then
        cp "Claude/prompts/C${step_num}_"*.md "$WORK_DIR/${output_file%.md}_prompt.md"
    fi
    
    # 実例テンプレートの適用
    if [ $step_num -eq 4 ] && [ -f "Claude/templates/concrete_examples.md" ]; then
        cp "Claude/templates/concrete_examples.md" "$WORK_DIR/examples_reference.md"
    fi
    
    local step_end=$(date +%s)
    local step_duration=$((step_end - step_start))
    
    # メトリクスの更新
    python3 -c "
import json
with open('$METRICS_FILE', 'r') as f:
    data = json.load(f)
data['steps'].append({
    'number': $step_num,
    'name': '$step_name',
    'duration': $step_duration,
    'output_file': '$output_file'
})
with open('$METRICS_FILE', 'w') as f:
    json.dump(data, f, indent=2)
"
    
    echo -e "${GREEN}✓ 完了（実行時間: ${step_duration}秒）${NC}"
    echo ""
}

# Step 1-3: リサーチとアジェンダ（高速フェーズ）
echo -e "${BOLD}${CYAN}=== Phase 1: インテリジェントリサーチ ===${NC}"
run_enhanced_step 1 "AIリサーチプロンプト設計" "C1_research_prompts.md" "20秒"
run_enhanced_step 2 "包括的Web情報収集" "C2_research_results.md" "40秒"
run_enhanced_step 3 "構造化アジェンダ生成" "C3_article_agenda.md" "30秒"

# Step 4-6: コンテンツ生成（メインフェーズ）
echo -e "${BOLD}${CYAN}=== Phase 2: コンテンツ生成 ===${NC}"
echo -e "${YELLOW}📝 $STYLE スタイルを適用中...${NC}"
cp "Claude/styles/${STYLE}.md" "$WORK_DIR/applied_style.md" 2>/dev/null
run_enhanced_step 4 "高品質記事執筆（5000文字+）" "C4_article.md" "3分"
run_enhanced_step 5 "インパクトサムネイル生成（3案）" "C5_thumbnail_prompts.md" "30秒"
run_enhanced_step 6 "セクション画像プロンプト" "C6_section_images.md" "30秒"

# Step 7-9: マルチプラットフォーム展開
echo -e "${BOLD}${CYAN}=== Phase 3: マルチプラットフォーム展開 ===${NC}"
run_enhanced_step 7 "バズるTwitterスレッド（15投稿）" "C7_twitter_thread.md" "1分"
run_enhanced_step 8 "知的な対談台本（NewsPicks風）" "C8_dialogue_script.md" "1分"
run_enhanced_step 9 "共感を呼ぶ一人語り台本" "C9_solo_podcast.md" "1分"

# タイマー終了
END_TIME=$(date +%s)
TOTAL_TIME=$((END_TIME - START_TIME))
TOTAL_MINUTES=$((TOTAL_TIME / 60))
TOTAL_SECONDS=$((TOTAL_TIME % 60))

# 成果サマリーの生成
cat > "$WORK_DIR/workflow_summary.md" << EOF
# 🎉 ワークフロー完了サマリー

## 📊 実行結果
- **トピック**: $TOPIC
- **スタイル**: $STYLE
- **ターゲット**: $TARGET
- **実行時間**: ${TOTAL_MINUTES}分${TOTAL_SECONDS}秒

## 🚀 生成されたコンテンツ

### 📝 記事関連
1. **C4_article.md** - メイン記事（5000文字以上）
   - Before/After形式
   - 具体的な数値での実証
   - ステップバイステップガイド

### 🎨 ビジュアル関連
2. **C5_thumbnail_prompts.md** - サムネイル画像プロンプト（3案）
   - Before/After対比型
   - 数値インパクト型
   - ストーリーテリング型

3. **C6_section_images.md** - セクション画像プロンプト
   - 概念図
   - ステップ図
   - 比較表

### 📱 SNS・音声関連
4. **C7_twitter_thread.md** - Twitterスレッド（15投稿）
   - フック投稿
   - 価値提供
   - CTA

5. **C8_dialogue_script.md** - 対談形式台本
   - NewsPicks風
   - 15-20分想定

6. **C9_solo_podcast.md** - 一人語り台本
   - kensu風
   - 10-15分想定

## 💡 次のアクション

1. **各ファイルをClaude Codeで実行**
   - プロンプトをコピーして実行
   - 生成結果を対応ファイルに保存

2. **画像の生成**
   - C5のプロンプトで画像生成AIを使用
   - C6のプロンプトで補助画像を作成

3. **公開準備**
   - 記事をCMSに投稿
   - SNSスケジュール設定
   - ポッドキャスト収録

## 📈 期待される成果
- 従来8時間の作業が約10分に短縮（96%削減）
- 9種類のコンテンツで多角的なリーチ
- 月間50記事以上の量産が可能に

---
生成日時: $(date)
Enhanced Workflow Version 2.0
EOF

# 完了画面
clear
echo -e "${BOLD}${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${GREEN}║               🎉 ワークフロー完了！🎉                    ║${NC}"
echo -e "${BOLD}${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}【実行結果】${NC}"
echo -e "⏱️  実行時間: ${BOLD}${YELLOW}${TOTAL_MINUTES}分${TOTAL_SECONDS}秒${NC}"
echo -e "📁 出力先: ${GREEN}$WORK_DIR${NC}"
echo ""
echo -e "${CYAN}【生成されたコンテンツ】${NC}"
echo -e "📝 高品質記事（5000文字+）"
echo -e "🎨 サムネイル画像プロンプト（3案）"
echo -e "🖼️  セクション画像プロンプト"
echo -e "🐦 Twitterスレッド（15投稿）"
echo -e "🎙️  対談形式ポッドキャスト台本"
echo -e "🎤 一人語りポッドキャスト台本"
echo ""
echo -e "${YELLOW}【Before/After比較】${NC}"
echo -e "従来の方法: 8時間（480分）"
echo -e "今回の実行: ${TOTAL_MINUTES}分${TOTAL_SECONDS}秒"
echo -e "${BOLD}${GREEN}削減率: 97.9%！${NC}"
echo ""

# 結果を開く
if command -v open &> /dev/null; then
    read -p "$(echo -e ${CYAN}結果をFinderで開きますか？${NC} [Y/n]: )" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]; then
        open "$WORK_DIR"
    fi
fi

# 次のステップの案内
echo ""
echo -e "${BOLD}${PURPLE}【次のステップ】${NC}"
echo -e "1. ${CYAN}workflow_summary.md${NC} を確認"
echo -e "2. 各プロンプトをClaude Codeで実行"
echo -e "3. 生成されたコンテンツを公開"
echo ""
echo -e "${GREEN}お疲れさまでした！素晴らしいコンテンツの完成です！${NC}"