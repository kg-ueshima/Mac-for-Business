---
title: "n8n-MCP-Serverの使い方〜自然言語でワークフローを構築する方法〜｜Dify Base"
source: "https://note.com/dify_base/n/n99571781d7f8"
author:
  - "[[Dify Base]]"
published: 2025-07-18
created: 2025-07-19
description: "はじめに  業務自動化ツール「n8n」は強力ですが、ワークフローの構築には慣れが必要です。「もっと手軽に、話しかけるだけで自動化できれば」と考えたことはありませんか？  本記事で紹介する「n8n-mcp-server」は、それを実現するツールです。AIアシスタントのClaudeと連携させることで、Vibe Coding的にn8nのワークフローを自動で作成・操作できます。  この記事では、n8n-mcp-serverの仕組みから、具体的な設定、そして実際にClaudeと対話してワークフローを動かすまでを解説します。   n8nとは  n8nは、様々なWebサービスやアプリケーションを連携"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/202891274/rectangle_large_type_2_898406c304877e9a554060e6b3f14f01.png?width=1200)

## n8n-MCP-Serverの使い方〜自然言語でワークフローを構築する方法〜

[Dify Base](https://note.com/dify_base)

## はじめに

業務自動化ツール「n8n」は強力ですが、ワークフローの構築には慣れが必要です。「もっと手軽に、話しかけるだけで自動化できれば」と考えたことはありませんか？

本記事で紹介する「n8n-mcp-server」は、それを実現するツールです。AIアシスタントのClaudeと連携させることで、Vibe Coding的にn8nのワークフローを自動で作成・操作できます。

この記事では、n8n-mcp-serverの仕組みから、具体的な設定、そして実際にClaudeと対話してワークフローを動かすまでを解説します。

## n8nとは

n8nは、様々なWebサービスやアプリケーションを連携させ、定型的な作業を自動化するためのツールです。一般的に「ワークフローオートメーションツール」と呼ばれています。

[**n8n.io - a powerful workflow automation tool** *n8n is a free and source-available workflow automation tool* *n8n.io*](https://n8n.io/)

![画像](https://assets.st-note.com/img/1752396351-2RSh7UawWzmyjGeOCQ4poA0M.png?width=1200)

このツールの大きな特徴は、画面上で視覚的に操作するだけで、複雑な自動化の仕組みを構築できる点です。

n8nでは、以下のような要素を使って自動化を組み立てます。

- **ノード:** 「Gmailでメールを受信する」「Slackにメッセージを送る」といった、一つひとつの機能を持つブロック。
- **ワークフロー:** これらのノードを線でつなぎ合わせて作る、一連の自動化された作業の流れ。

例えば、Googleフォライブに音声ファイルが格納されたら、その音声をダウンロードし、文字起こし→議事録作成といったようなワークフローを、画面上でノードを並べてつなぐだけで作成できます。

![画像](https://assets.st-note.com/img/1752396351-OpTh1D25BHEmeFCgMI0dP7tL.png?width=1200)

特に、n8nはChatGPTに代表される生成AIとの連携が容易なため、AIを活用した業務自動化を検討する際に有力な選択肢となります。

直感的な操作で複雑な連携も設定できるのがn8nの大きな特長です。今回は、このワークフロー作成を「会話」という、さらに簡単な方法で行っていきます。

## n8n-mcp-serverとは？

n8nのワークフローを会話で作るために、中心的な役割を果たすのが「n8n-mcp-server」です。

![画像](https://assets.st-note.com/img/1752396558-c0g8xuiA6Xs2ty4qkWBeampT.png?width=1200)

これは、ClaudeやCursorなどのAIツールとn8nの"橋渡し役"となるソフトウェアです。私たちがClaudeに送る「〇〇するワークフローを作って」といった自然な言葉での指示を、n8nが実行できる形式の命令へと変換してくれます。

この連携は、MCPという技術によって実現されています。

### MCPとは？

AIと外部のツールやサービスが、安全かつ効率的に対話をするために定められた共通の通信ルール（プロトコル）です。

![画像](https://assets.st-note.com/img/1752396708-QJk6BuPVSG9zDFEU27TjbOiH.png?width=1200)

n8n-mcp-serverは、このMCPというルールに従ってClaudeと通信することで、私たちの指示を正確にn8nへ伝達します。

全体の流れは以下のようになります。

![画像](https://assets.st-note.com/img/1752397029-sCApWtI8keVhTJ2ql0ownKbf.png?width=1200)

1. **あなた:** Claudeに「ワークフローを作って」と指示を出す。
2. **Claude:** 指示を解釈し、MCPのルールに従ってn8n-mcp-serverに命令を送る。
3. **n8n-mcp-server:** 命令を受け取り、n8nが理解できるAPIリクエストに変換して実行する。
4. **n8n:** 命令通りにワークフローを作成・操作する。

この仕組みにより、私たちはn8nの専門的な操作方法を知らなくても、対話形式でn8nのワークフローを作成することができます。

## 【実践】n8n-mcp-serverの使い方

## ここから先は

2,509字 / 18画像

![PayPay](https://assets.st-note.com/poc-image/manual/note-common-images/production/svg/paypay-icon.svg) ｜PayPayで支払うと 抽選でお得

[

このメンバーシップの詳細

](https://note.com/dify_base/membership/join)

[ログイン](https://note.com/login?redirectPath=%2Fdify_base%2Fn%2Fn99571781d7f8)

- [
	#Claude
	](https://note.com/hashtag/Claude)
- [
	#n8n
	](https://note.com/hashtag/n8n)

この記事が気に入ったらチップで応援してみませんか？

n8n-MCP-Serverの使い方〜自然言語でワークフローを構築する方法〜｜Dify Base