---
title: "browser-use で Gemini と DeepSeek を使用する"
source: "https://zenn.dev/gunjo/articles/72d30b516e68c1"
author:
  - "[[Zenn]]"
published: 2025-01-04
created: 2025-06-11
description:
tags:
  - "clippings"
---
25

2

[![](https://static.zenn.studio/images/drawing/tech-icon.svg)](https://zenn.dev/tech-or-idea)

[tech](https://zenn.dev/tech-or-idea)

## はじめに

browser-use を使用している方で恐らくほとんどの人がトークンの使用量と料金について気になっていると思います。  
無料枠のある Gemini を使用したいところですが、現在 Issue に上がっているように Gemini は使用できません。  
本家ではありませんが、つい最近 Gemini と DeepSeek を利用できるように改良したリポジトリを見つけたため紹介します。

リポジトリは以下です。

## 環境構築

まず、Python 3.11 以上がインストールされていることを確認してください。

**browser-use のインストール:**

```bash
pip install browser-use
```

**Playwright のインストール:**

```bash
playwright install
```

**依存関係のインストール:**

```bash
pip install browser-use
```

### 仮想環境を使用する場合

```bash
# venv環境を作成
python -m venv venv

# venv環境を有効化
# macOS/Linux の場合:
source venv/bin/activate
# Windows の場合:
venv\Scripts\activate
```

**パッケージのインストール:**

```bash
pip install browser-use
playwright install
pip install -r requirements.txt
```

**環境変数の設定:**  
`.env.example` を`.env` にコピーし、LLM の API キーを含む環境変数を設定

```bash
GEMINI_API_KEY=your_gemini_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```

**既存のブラウザを使用する場合:**

- `CHROME_PATH` にブラウザの実行ファイルのパスを設定（例：Windows の場合は `C:\Program Files\Google\Chrome\Application\chrome.exe` ）。
- `CHROME_USER_DATA` にブラウザのユーザーデータディレクトリを設定（例： `C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data` ）。

```bash
# Windowsの場合
CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
CHROME_USER_DATA=C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data

# macOS/Linuxの場合
CHROME_PATH=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
CHROME_USER_DATA=/Users/<YourUsername>/Library/Application Support/Google/Chrome/<profile name>
```

## 使い方

### WebUI の実行

```bash
python webui.py --ip 127.0.0.1 --port 7788
```

**WebUI へのアクセス:** Web ブラウザを開き、 `http://127.0.0.1:7788` にアクセスすると WebUI が表示されます。

![WebUI](https://res.cloudinary.com/zenn/image/fetch/s--pq1Mgx35--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/f74bd8b833cf21a47d949e0d.png%3Fsha%3De557bf2894c753f224651069c14cb35f64a58e4f)

### 既存のブラウザを使用する場合

以下の手順で既存のブラウザを使用することができます。

- すべての Chrome ウィンドウを閉じる
- Firefox や Edge など、Chrome 以外のブラウザで WebUI を開く
- `Browser Settings` の `Use Own Browser` オプションをチェックする

![既存のブラウザを使用](https://res.cloudinary.com/zenn/image/fetch/s--hUIVlOZQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/4a4e1d10811e87ec5b094f3d.png%3Fsha%3D9585ee2bfcce18f401e80c4bd57ff238336de417)

### Gemini を使用する

画像の通りで Gemini が使用できます。 `LLM API Key` は.env ファイルで設定している場合は不要です。

![Gemini](https://res.cloudinary.com/zenn/image/fetch/s--0tJZhDlo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/a6a195325939ac1add9d9bd1.png%3Fsha%3D1851aaad4e4307023043539eac2583919ef39b99)

### DeepSeek を使用する

画像の通りで DeepSeek が使用できます。 `LLM Base URL` と `LLM API Key` は.env ファイルで設定している場合は不要です。  
一点注意点として、 `use vision` をチェックすると JSON のデシリアライズで失敗するためチェックを外してください。

![DeepSeek](https://res.cloudinary.com/zenn/image/fetch/s--aa0JsnYv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/76d5dce3066906b544cd0762.png%3Fsha%3D0f03939a2f25d9c93b3fb84e2d491295e2277894)

### カスタムアクション

WebUI からはカスタムアクションの登録はできないため、src/controller/custom\_controller.py を編集することで本家と同様に登録できそうです。  
custom\_controller.py のコードは以下です。

25

2

### Discussion

![](https://static.zenn.studio/images/drawing/discussion.png)

ログインするとコメントできます

25

2