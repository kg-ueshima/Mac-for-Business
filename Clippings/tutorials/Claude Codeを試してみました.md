---
title: "Claude Codeを試してみました"
source: "https://zenn.dev/karaage0703/articles/6699045b3cec5c"
author:
  - "[[Zenn]]"
published: 2025-06-06
created: 2025-06-07
description:
tags:
  - "clippings"
---
48

11[idea](https://zenn.dev/tech-or-idea)

## Claude Codeセットアップ

周りの人3人にオススメされたのでClaude Codeを試してみました（自分ルール）。macOS前提です。WindowsでもWSL2で同様に設定できるとは思いますが未確認です。

今から試す方は、公式のドキュメントをみながらすすめるのが良いかなと思います。

ただし、前提としてnpmは使える必要があります。以下記事参照してください。

あと、Claudeに課金しないと駄目かと思ってましたが、APIを利用していれば普通に使えました（詳しい条件はよく分かってないです）。

インストールはnpmが入っていたら、以下コマンドで一発です。

```bash
$ npm install -g @anthropic-ai/claude-code
```

あとは `claude` と実行すれば、起動します。

![](https://storage.googleapis.com/zenn-user-upload/a55508bb51c5-20250606.png)

`/init` とコマンドを打つと、リポジトリの内容を確認して `CLAUDE.md` というファイルを作成します。

CLIじゃなくてIDEで使いたいなーって思ったら、VS Codeエディタのターミナルで `claude` を実行すると、勝手に拡張が入ります。ClineやCursorっぽくClaude Codeを使うことができます。

![](https://storage.googleapis.com/zenn-user-upload/106beb451229-20250606.png)

## Claude Codeを試してみて

実際にコーディングさせてみた感じですが、自分はClineやCursorと大きな性能差は感じられませんでした。モデル同じClaude Sonnet 4を使ったので、それはそうかという印象です。

挙動としては、最初にプランニングをしたりと、プロンプトは工夫されているんだろうなとは感じましたが、とてつもない差があるとは思わなかったです。自分がClineやCursorのルールをある程度作り込んだり、MCP連携していたりしているのもあるかもしれません（Claudeはほぼデフォルト設定でMCPも連携せず使っていました）。

使い勝手は、Cline,Cursorの方がよいかなと思いましたが、細かい点なので慣れの問題かもしれません。

私はAPIで使いましたが、課金して定額で使えるのは凄い魅力的だなとは思いました。

## まとめ

Claude Code試してみました。個人的にはClineやCursorに比べて、性能差を感じられなかったのと、若干使いづらかったのもあり、とりあえずはいいかなという印象でした。

もちろん、定額というのは非常に魅力なので、そこだけでClaude Codeを使うという判断は全然ありかなと思いました。

AIエージェントのUIに関しては、私はエディタに組み込んで使うスタイルがベストとは思っていないですし、今後大きく変わるとは思っています。ただ、Calude CodeのCLIが良いのかと問われると、なんとも言えないです。ただ、ベースはCLIで独立して作っておいて、VS Codeの拡張含めて、今後どんどん拡張できるというコンセプトとすれば、それはそれで良さそうだなとは感じました。

## 参考リンク

色々参考にした記事です。

[話題のClaude 4とClaude Codeに入門！（KAGと学ぼう！勉強会） YouTube動画](https://www.youtube.com/watch?v=8BPfZKIa51k)

[How Anthropic teams use Claude Code(pdf)](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)

48

11

### Discussion

![](https://static.zenn.studio/images/drawing/discussion.png)

ログインするとコメントできます

48

11