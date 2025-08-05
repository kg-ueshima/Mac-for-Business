#!/bin/bash

# Claude Code 9段階ワークフロー - クイックスタート

echo "====================================="
echo "Claude Code 9段階ワークフロー"
echo "クイックスタートガイド"
echo "====================================="
echo ""

# サンプルトピックのリスト
echo "サンプルトピック:"
echo "1. Claude Code Windows活用ガイド"
echo "2. Python自動化スクリプト入門"
echo "3. AIを使った効率的なコンテンツ作成"
echo "4. リモートワークの生産性向上術"
echo "5. カスタムトピックを入力"
echo ""

read -p "番号を選択してください (1-5): " choice

case $choice in
    1)
        TOPIC="Claude Code Windows活用ガイド"
        STYLE="S1_professional"
        TARGET="事務マネージャー"
        ;;
    2)
        TOPIC="Python自動化スクリプト入門"
        STYLE="S1_professional"
        TARGET="事務マネージャー"
        ;;
    3)
        TOPIC="AIを使った効率的なコンテンツ作成"
        STYLE="S1_professional"
        TARGET="事務マネージャー"
        ;;
    4)
        TOPIC="リモートワークの生産性向上術"
        STYLE="S1_professional"
        TARGET="事務マネージャー"
        ;;
    5)
        read -p "トピックを入力してください: " TOPIC
        echo ""
        echo "スタイルを選択:"
        echo "1. S1_professional (フォーマル)"
        echo "2. S2_casual (カジュアル)"
        echo "3. S3_kensu (共感的)"
        echo "4. S4_tetumemo (数値重視)"
        read -p "番号を選択 (1-4) [デフォルト: 1]: " style_choice
        case $style_choice in
            1) STYLE="S1_professional" ;;
            2) STYLE="S2_casual" ;;
            3) STYLE="S3_kensu" ;;
            4) STYLE="S4_tetumemo" ;;
            *) STYLE="S1_professional" ;;
        esac
        read -p "ターゲット層を入力してください [デフォルト: 事務マネージャー]: " TARGET
        if [ -z "$TARGET" ]; then
            TARGET="事務マネージャー"
        fi
        ;;
    *)
        echo "無効な選択です。終了します。"
        exit 1
        ;;
esac

echo ""
echo "====================================="
echo "選択された設定:"
echo "トピック: $TOPIC"
echo "スタイル: $STYLE"
echo "ターゲット: $TARGET"
echo "====================================="
echo ""

read -p "この設定で実行しますか？ (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "ワークフローを開始します..."
        # Enhanced版とBasic版の選択
    echo ""
    echo "実行バージョンを選択:"
    echo "1. Enhanced版（高品質、tetumemo風）"
    echo "2. Basic版（シンプル）"
    read -p "番号を選択 (1-2) [デフォルト: 1]: " version_choice
    
    if [ "$version_choice" = "2" ]; then
        ./scripts/run_workflow.sh "$TOPIC" "$STYLE" "$TARGET"
    else
        ./scripts/run_workflow_enhanced.sh "$TOPIC" "$STYLE" "$TARGET"
    fi
else
    echo "キャンセルしました。"
fi