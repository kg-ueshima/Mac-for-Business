#!/bin/bash
# Claude Code起動スクリプト

echo "Claude Codeを起動します..."

# 作業ディレクトリに移動
cd "$(dirname "$0")"

# Claude Codeを起動（プロジェクトディレクトリを指定）
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open -a "Claude" .
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    claude . &
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    start claude .
fi

echo ""
echo "Claude Codeが起動したら、execution_prompts.mdの内容を実行してください。"
echo ""
echo "ヒント: "
echo "1. '@execution_prompts.md' と入力してファイルを参照"
echo "2. 一括実行プロンプトをコピー＆ペースト"
echo "3. Enterキーで実行開始"
