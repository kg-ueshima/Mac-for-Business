#!/usr/bin/env python3
"""
Enhanced ClippingsSorting Agent
Clippingsフォルダ内のコンテンツをタグ付けして内容別にフォルダ分けし、
テーマ別の永続ノート、インデックス、構造化ファイルを作成する
"""

import os
import re
import shutil
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Set
import hashlib
from collections import defaultdict

class EnhancedClippingsSorter:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        # プロジェクトルートからの相対パスを設定
        self.clippings_path = self.base_path / "Clippings"
        self.permanent_notes_path = self.base_path / "03-Permanent-Notes"
        self.index_notes_path = self.base_path / "04-Index-Notes"
        self.structure_notes_path = self.base_path / "05-Structure-Notes"
        
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
            "API", "データベース", "クラウド", "Azure", "AWS", "Git",
            "Docker", "Kubernetes", "DevOps", "CI/CD", "テスト", "デバッグ"
        ]
        
        # ビジネス関連キーワード
        self.business_keywords = [
            "経営", "マネジメント", "戦略", "マーケティング", "営業", "顧客",
            "財務", "会計", "人事", "組織", "リーダーシップ", "チーム"
        ]
        
        # テーマ別キーワード（永続ノート作成用）
        self.theme_keywords = {
            "Cursor": ["Cursor", "cursor", "エディタ", "IDE", "開発環境"],
            "Obsidian": ["Obsidian", "obsidian", "ノート", "知識管理", "Zettelkasten"],
            "AI": ["AI", "ai", "人工知能", "機械学習", "ChatGPT", "Claude", "Gemini"],
            "Python": ["Python", "python", "プログラミング", "スクリプト", "自動化"],
            "Microsoft": ["Microsoft", "microsoft", "Teams", "Azure", "Office"],
            "GitHub": ["GitHub", "github", "Git", "git", "バージョン管理"],
            "Docker": ["Docker", "docker", "コンテナ", "仮想化"],
            "クラウド": ["クラウド", "cloud", "Cloud", "AWS", "Azure", "GCP"],
            "DX": ["DX", "dx", "デジタル変革", "デジタル化", "DX推進"],
            "プロジェクト管理": ["プロジェクト", "project", "管理", "マネジメント", "PM"],
            "セキュリティ": ["セキュリティ", "security", "Security", "認証", "暗号化"],
            "データベース": ["データベース", "database", "Database", "SQL", "NoSQL"],
            "API": ["API", "api", "WebAPI", "REST", "GraphQL"],
            "フロントエンド": ["フロントエンド", "frontend", "Frontend", "React", "Vue", "Angular"],
            "バックエンド": ["バックエンド", "backend", "Backend", "サーバー", "サーバーサイド"],
            "DevOps": ["DevOps", "devops", "CI/CD", "継続的", "デプロイ"],
            "テスト": ["テスト", "test", "Test", "テスト駆動", "TDD"],
            "デバッグ": ["デバッグ", "debug", "Debug", "トラブルシューティング"],
            "パフォーマンス": ["パフォーマンス", "performance", "Performance", "最適化"],
            "スケーラビリティ": ["スケーラビリティ", "scalability", "Scalability", "拡張性"],
            "アーキテクチャ": ["アーキテクチャ", "architecture", "Architecture", "設計"]
        }

    def scan_clippings_folder(self) -> List[Path]:
        """Clippingsフォルダ内のファイルをスキャン"""
        if not self.clippings_path.exists():
            print(f"Clippingsフォルダが見つかりません: {self.clippings_path}")
            return []
        
        files = []
        for file_path in self.clippings_path.glob("*.md"):
            if file_path.is_file():
                files.append(file_path)
        
        print(f"スキャン完了: {len(files)}個のファイルを発見")
        return files

    def analyze_content(self, file_path: Path) -> Dict:
        """ファイルの内容を分析"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"ファイル読み込みエラー {file_path}: {e}")
            return {"tags": [], "category": "miscellaneous", "score": 0, "themes": []}

        # ファイル名からキーワード抽出
        filename = file_path.stem.lower()
        
        # 内容からキーワード抽出
        content_lower = content.lower()
        
        # タグ付け
        tags = []
        category_scores = {cat: 0 for cat in self.categories.keys()}
        themes = []
        
        # カテゴリ別キーワードチェック
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword.lower() in filename or keyword.lower() in content_lower:
                    category_scores[category] += 1
                    tags.append(keyword)
        
        # 技術キーワードチェック
        for keyword in self.tech_keywords:
            if keyword.lower() in filename or keyword.lower() in content_lower:
                category_scores["tutorials"] += 1
                tags.append(keyword)
        
        # ビジネスキーワードチェック
        for keyword in self.business_keywords:
            if keyword.lower() in filename or keyword.lower() in content_lower:
                category_scores["work_related"] += 1
                tags.append(keyword)
        
        # テーマ別キーワードチェック
        for theme, keywords in self.theme_keywords.items():
            for keyword in keywords:
                if keyword.lower() in filename or keyword.lower() in content_lower:
                    themes.append(theme)
                    break
        
        # 最もスコアの高いカテゴリを決定
        best_category = max(category_scores.items(), key=lambda x: x[1])[0]
        
        return {
            "file_path": file_path,
            "tags": list(set(tags)),  # 重複除去
            "category": best_category,
            "score": category_scores[best_category],
            "themes": list(set(themes)),  # 重複除去
            "content_preview": content[:200] + "..." if len(content) > 200 else content,
            "content": content
        }

    def assign_tags(self, analysis_results: List[Dict]) -> List[Dict]:
        """タグを割り当て"""
        for result in analysis_results:
            # スコアが低い場合はmiscellaneousに分類
            if result["score"] < 0.5:
                result["category"] = "miscellaneous"
                result["tags"].append("未分類")
        
        return analysis_results

    def create_category_folders(self):
        """カテゴリフォルダを作成"""
        for category in self.categories.keys():
            category_path = self.clippings_path / category
            category_path.mkdir(exist_ok=True)
            print(f"フォルダ作成/確認: {category_path}")

    def move_files_to_categories(self, analysis_results: List[Dict]):
        """ファイルをカテゴリフォルダに移動"""
        moved_files = []
        
        for result in analysis_results:
            file_path = result["file_path"]
            category = result["category"]
            
            # カテゴリフォルダのパス
            category_path = self.clippings_path / category
            
            # 移動先のファイルパス
            dest_path = category_path / file_path.name
            
            # 重複チェック
            if dest_path.exists():
                # ファイル名にタイムスタンプを追加
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name_parts = file_path.stem, timestamp, file_path.suffix
                new_filename = f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                dest_path = category_path / new_filename
            
            try:
                shutil.move(str(file_path), str(dest_path))
                moved_files.append({
                    "original": str(file_path),
                    "destination": str(dest_path),
                    "category": category,
                    "tags": result["tags"],
                    "themes": result["themes"]
                })
                print(f"移動完了: {file_path.name} → {category}/")
            except Exception as e:
                print(f"移動エラー {file_path}: {e}")
        
        return moved_files

    def create_theme_based_permanent_notes(self, analysis_results: List[Dict]) -> List[Path]:
        """テーマ別の永続ノートを作成"""
        if not self.permanent_notes_path.exists():
            print("03-Permanent-Notesフォルダが見つかりません")
            return []
        
        # テーマ別にファイルをグループ化
        theme_groups = defaultdict(list)
        for result in analysis_results:
            for theme in result["themes"]:
                theme_groups[theme].append(result)
        
        created_notes = []
        for theme, files in theme_groups.items():
            if len(files) < 2:  # 2つ以上のファイルがあるテーマのみ
                continue
            
            note_filename = f"{theme}について.md"
            note_path = self.permanent_notes_path / note_filename
            
            # 既存のノートがある場合は読み込み
            existing_content = ""
            if note_path.exists():
                try:
                    with open(note_path, 'r', encoding='utf-8') as f:
                        existing_content = f.read()
                except Exception as e:
                    print(f"既存ノート読み込みエラー {note_path}: {e}")
            
            # 新しい内容を追加
            new_content = f"\n\n## {datetime.now().strftime('%Y年%m月%d日')} 追加分\n\n"
            
            for file_info in files:
                new_content += f"### {file_info['file_path'].name}\n"
                new_content += f"- カテゴリ: {file_info['category']}\n"
                new_content += f"- タグ: {', '.join(file_info['tags']) if file_info['tags'] else 'なし'}\n"
                new_content += f"- 内容: {file_info['content_preview']}\n\n"
            
            # ファイルに書き込み
            try:
                with open(note_path, 'w', encoding='utf-8') as f:
                    if existing_content:
                        f.write(existing_content + new_content)
                    else:
                        f.write(f"# {theme}について\n\n{theme}に関する情報をまとめています。\n{new_content}")
                
                created_notes.append(note_path)
                print(f"テーマ別ノート作成: {note_path}")
            except Exception as e:
                print(f"テーマ別ノート作成エラー {note_path}: {e}")
        
        return created_notes

    def create_index_notes(self, analysis_results: List[Dict], moved_files: List[Dict]):
        """04-Index-Notesにインデックスファイルを作成"""
        if not self.index_notes_path.exists():
            print("04-Index-Notesフォルダが見つかりません")
            return
        
        # プロジェクト全体のインデックスを作成
        index_filename = f"project_index_{datetime.now().strftime('%Y%m%d')}.md"
        index_path = self.index_notes_path / index_filename
        
        index_content = f"""# Mac for Business プロジェクトインデックス

## 概要
- 作成日: {datetime.now().strftime('%Y年%m月%d日')}
- 総ファイル数: {len(analysis_results)}個
- 処理ファイル数: {len(moved_files)}個

## カテゴリ別インデックス

"""
        
        # カテゴリ別に整理
        category_files = defaultdict(list)
        for moved in moved_files:
            category_files[moved["category"]].append(moved)
        
        for category, files in category_files.items():
            index_content += f"### {category}\n"
            index_content += f"- ファイル数: {len(files)}個\n\n"
            
            for file_info in files:
                index_content += f"- [{Path(file_info['destination']).name}]({file_info['destination']})\n"
                if file_info["themes"]:
                    index_content += f"  - テーマ: {', '.join(file_info['themes'])}\n"
                if file_info["tags"]:
                    index_content += f"  - タグ: {', '.join(file_info['tags'])}\n"
                index_content += "\n"
        
        # テーマ別インデックス
        index_content += "## テーマ別インデックス\n\n"
        theme_files = defaultdict(list)
        for moved in moved_files:
            for theme in moved["themes"]:
                theme_files[theme].append(moved)
        
        for theme, files in theme_files.items():
            index_content += f"### {theme}\n"
            index_content += f"- ファイル数: {len(files)}個\n\n"
            
            for file_info in files:
                index_content += f"- [{Path(file_info['destination']).name}]({file_info['destination']})\n"
            index_content += "\n"
        
        # タグ別インデックス
        index_content += "## タグ別インデックス\n\n"
        tag_files = defaultdict(list)
        for moved in moved_files:
            for tag in moved["tags"]:
                tag_files[tag].append(moved)
        
        for tag, files in tag_files.items():
            index_content += f"### {tag}\n"
            index_content += f"- ファイル数: {len(files)}個\n\n"
            
            for file_info in files:
                index_content += f"- [{Path(file_info['destination']).name}]({file_info['destination']})\n"
            index_content += "\n"
        
        try:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
            print(f"インデックスファイル作成: {index_path}")
        except Exception as e:
            print(f"インデックスファイル作成エラー: {e}")

    def create_structure_notes(self, analysis_results: List[Dict]) -> List[Path]:
        """05-Structure-Notesに構造化ファイルを作成"""
        if not self.structure_notes_path.exists():
            print("05-Structure-Notesフォルダが見つかりません")
            return []
        
        # テーマ別の構造化ファイルを作成
        theme_structures = defaultdict(list)
        for result in analysis_results:
            for theme in result["themes"]:
                theme_structures[theme].append(result)
        
        created_structures = []
        for theme, files in theme_structures.items():
            if len(files) < 2:  # 2つ以上のファイルがあるテーマのみ
                continue
            
            structure_filename = f"{theme}_structure.md"
            structure_path = self.structure_notes_path / structure_filename
            
            structure_content = f"""# {theme} の構造化

## 概要
{theme}に関する情報の構造化と関連性の整理

## 主要トピック

"""
            
            # ファイルを内容でグループ化
            topic_groups = defaultdict(list)
            for file_info in files:
                # ファイル名からトピックを推測
                filename = file_info['file_path'].stem
                if any(keyword in filename.lower() for keyword in ['使い方', 'tutorial', 'guide']):
                    topic_groups['使い方・ガイド'].append(file_info)
                elif any(keyword in filename.lower() for keyword in ['比較', 'review', '感想']):
                    topic_groups['比較・レビュー'].append(file_info)
                elif any(keyword in filename.lower() for keyword in ['設定', 'config', 'setup']):
                    topic_groups['設定・セットアップ'].append(file_info)
                else:
                    topic_groups['その他'].append(file_info)
            
            for topic, topic_files in topic_groups.items():
                structure_content += f"### {topic}\n"
                structure_content += f"- ファイル数: {len(topic_files)}個\n\n"
                
                for file_info in topic_files:
                    structure_content += f"- **{file_info['file_path'].name}**\n"
                    structure_content += f"  - カテゴリ: {file_info['category']}\n"
                    if file_info["tags"]:
                        structure_content += f"  - キーワード: {', '.join(file_info['tags'])}\n"
                    structure_content += f"  - 概要: {file_info['content_preview']}\n\n"
            
            # 関連性の分析
            structure_content += "## 関連性分析\n\n"
            
            # 共通タグの分析
            all_tags = []
            for file_info in files:
                all_tags.extend(file_info["tags"])
            
            tag_counts = defaultdict(int)
            for tag in all_tags:
                tag_counts[tag] += 1
            
            common_tags = {tag: count for tag, count in tag_counts.items() if count > 1}
            if common_tags:
                structure_content += "### 共通キーワード\n"
                for tag, count in sorted(common_tags.items(), key=lambda x: x[1], reverse=True):
                    structure_content += f"- {tag}: {count}回\n"
                structure_content += "\n"
            
            # 学習の流れ
            structure_content += "## 学習の流れ\n\n"
            structure_content += "1. **基礎知識**: 基本概念と概要\n"
            structure_content += "2. **実践**: 使い方と設定\n"
            structure_content += "3. **応用**: 高度な機能と活用方法\n"
            structure_content += "4. **評価**: 比較とレビュー\n\n"
            
            try:
                with open(structure_path, 'w', encoding='utf-8') as f:
                    f.write(structure_content)
                created_structures.append(structure_path)
                print(f"構造化ファイル作成: {structure_path}")
            except Exception as e:
                print(f"構造化ファイル作成エラー {structure_path}: {e}")
        
        return created_structures

    def remove_duplicates(self, analysis_results: List[Dict]):
        """重複ファイルの検出と処理"""
        content_hashes = {}
        duplicates = []
        
        for result in analysis_results:
            file_path = result["file_path"]
            try:
                with open(file_path, 'rb') as f:
                    content_hash = hashlib.md5(f.read()).hexdigest()
                
                if content_hash in content_hashes:
                    duplicates.append({
                        "original": content_hashes[content_hash],
                        "duplicate": file_path,
                        "hash": content_hash
                    })
                else:
                    content_hashes[content_hash] = file_path
            except Exception as e:
                print(f"重複チェックエラー {file_path}: {e}")
        
        if duplicates:
            print(f"重複ファイルを{len(duplicates)}個発見:")
            for dup in duplicates:
                print(f"  - {dup['duplicate'].name} (重複: {dup['original'].name})")
        
        return duplicates

    def generate_report(self, analysis_results: List[Dict], moved_files: List[Dict], 
                       duplicates: List[Dict], theme_notes: List[Path], 
                       index_file: Path, structure_files: List[Path]):
        """処理結果レポートを生成"""
        report_content = f"""# Enhanced ClippingsSorting処理レポート

## 処理概要
- 処理日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 対象ファイル数: {len(analysis_results)}個
- 移動ファイル数: {len(moved_files)}個
- 重複ファイル数: {len(duplicates)}個
- 作成テーマ別ノート数: {len(theme_notes)}個
- 作成構造化ファイル数: {len(structure_files)}個

## カテゴリ別統計
"""
        
        category_stats = {}
        for result in analysis_results:
            category = result["category"]
            category_stats[category] = category_stats.get(category, 0) + 1
        
        for category, count in category_stats.items():
            report_content += f"- {category}: {count}個\n"
        
        # テーマ別統計
        theme_stats = defaultdict(int)
        for result in analysis_results:
            for theme in result["themes"]:
                theme_stats[theme] += 1
        
        if theme_stats:
            report_content += "\n## テーマ別統計\n"
            for theme, count in sorted(theme_stats.items(), key=lambda x: x[1], reverse=True):
                report_content += f"- {theme}: {count}個\n"
        
        report_content += "\n## 作成されたファイル\n"
        report_content += "### テーマ別永続ノート\n"
        for note in theme_notes:
            report_content += f"- {note.name}\n"
        
        report_content += "\n### 構造化ファイル\n"
        for structure in structure_files:
            report_content += f"- {structure.name}\n"
        
        report_content += "\n### インデックスファイル\n"
        report_content += f"- {index_file.name}\n"
        
        report_content += "\n## 処理結果\n"
        report_content += "✅ ファイル分類完了\n"
        report_content += "✅ カテゴリフォルダ作成\n"
        report_content += "✅ テーマ別永続ノート作成\n"
        report_content += "✅ インデックスファイル作成\n"
        report_content += "✅ 構造化ファイル作成\n"
        
        if duplicates:
            report_content += "⚠️ 重複ファイル検出\n"
        
        report_content += "\n処理が正常に完了しました。"
        
        # レポートを保存
        report_path = self.base_path / f"enhanced_clippings_sorting_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"レポートを保存: {report_path}")
        except Exception as e:
            print(f"レポート保存エラー: {e}")

    def run(self):
        """メイン処理を実行"""
        print("=== Enhanced ClippingsSorting Agent 開始 ===")
        
        # 1. Clippingsフォルダをスキャン
        files = self.scan_clippings_folder()
        if not files:
            print("処理対象のファイルがありません")
            return
        
        # 2. 各ファイルの内容を分析
        print("ファイル分析中...")
        analysis_results = []
        for file_path in files:
            result = self.analyze_content(file_path)
            analysis_results.append(result)
        
        # 3. タグを割り当て
        analysis_results = self.assign_tags(analysis_results)
        
        # 4. カテゴリフォルダを作成
        self.create_category_folders()
        
        # 5. ファイルをカテゴリに移動
        print("ファイル移動中...")
        moved_files = self.move_files_to_categories(analysis_results)
        
        # 6. 重複ファイルを検出
        duplicates = self.remove_duplicates(analysis_results)
        
        # 7. テーマ別永続ノートを作成
        print("テーマ別永続ノート作成中...")
        theme_notes = self.create_theme_based_permanent_notes(analysis_results) or []
        
        # 8. インデックスファイルを作成
        print("インデックスファイル作成中...")
        self.create_index_notes(analysis_results, moved_files)
        index_file = self.index_notes_path / f"project_index_{datetime.now().strftime('%Y%m%d')}.md"
        
        # 9. 構造化ファイルを作成
        print("構造化ファイル作成中...")
        structure_files = self.create_structure_notes(analysis_results) or []
        
        # 10. レポートを生成
        self.generate_report(analysis_results, moved_files, duplicates, 
                           theme_notes, index_file, structure_files)
        
        print("=== Enhanced ClippingsSorting Agent 完了 ===")

if __name__ == "__main__":
    # プロジェクトルートを指定して実行
    project_root = Path(__file__).parent.parent.parent
    sorter = EnhancedClippingsSorter(str(project_root))
    sorter.run() 