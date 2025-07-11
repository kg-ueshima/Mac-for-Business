/*
Macで自動的にメール送信する手順（例：Python + AppleScript + Automator）

------------------------------------------------------------------------
-- Safari で Web からコピー → Excel に貼り付け → 保存して終了
-- 追加機能
--   1) Excel を保存して閉じる（quit）
--   2) 最初に開いたプライベートウィンドウを Excel 保存後に閉じる
------------------------------------------------------------------------
property excelPath : "/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/00_受け渡し/m3_data/病棟別データ/病棟別入退履歴_auto.xlsx"
tell application "Safari"
	activate
	
	-- 新規プライベートウィンドウを開く
	tell application "System Events" to keystroke "n" using {shift down, command down}
	delay 1
	
	-- 最前面のプライベートウィンドウを取得
	set privateWindow to front window
	
	-- タブを開く
	tell privateWindow
		set current tab to (make new tab with properties {URL:"http://192.168.1.207/k-share/MedicalOffice/ntHistory"})
	end tell
	delay 5
	
	-- ログイン処理
	do JavaScript "document.getElementById('ksid').value='700009';" in current tab of privateWindow
	do JavaScript "document.getElementById('password').value='a123a123';" in current tab of privateWindow
	do JavaScript "document.forms[0].submit();" in current tab of privateWindow
	delay 2.5
	
	-- 表示切替
	do JavaScript "document.querySelector('span.btn-info[ng-click=\"showType = \\'転棟含\\'\"]').click();" in current tab of privateWindow
	delay 1
	
	-- テーブルをクリップボードへ（HTML＋Text）
	do JavaScript "
	  var table = document.querySelector('div[ng-show=\"showType==\\'転棟含\\'\"] table');
	  if(table){
	    var html = table.outerHTML;
	    function copyToClipboard(html){
	      var listener=function(e){
	        e.clipboardData.setData('text/html',html);
	        e.clipboardData.setData('text/plain',table.innerText);
	        e.preventDefault();
	      };
	      document.addEventListener('copy',listener);
	      document.execCommand('copy');
	      document.removeEventListener('copy',listener);
	    }
	    copyToClipboard(html);
	  }
	" in current tab of privateWindow
	delay 1
	
	
	------------------------------------------------------------------------
	-- Excel 操作
	------------------------------------------------------------------------
	tell application "Microsoft Excel"
		activate
		set wb to open workbook workbook file name ¬
			excelPath
		delay 1
		
		-- 本日の日付からyyyymm形式のシート名を取得し、該当シートをアクティブにする
		set yyyymm to do shell script "date +%Y%m（転棟含）"
		set targetSheet to null
		set sheetName to null
		-- 各ワークシートをループ処理
		set sheetCount to count of worksheets of wb
		repeat with i from 1 to sheetCount
			set s to worksheet i of wb
			set sheetName to (get name of s) as text
			if sheetName is yyyymm then
				set targetSheet to s
				exit repeat
			end if
		end repeat
		
		if targetSheet is null then
			-- シートがなければ新規作成
			tell wb
				set targetSheet to make new worksheet at before worksheet 1
			end tell
		end if
		set name of targetSheet to yyyymm
		delay 1
		
		activate object targetSheet
		-- 貼り付け先セルを選択
		select range "A1" of active sheet
		-- クリップボードの内容を書式付きで貼る
		paste worksheet active sheet
		
		-- ■ テーブル貼り付け直後にセルを挿入して右へシフト
		--   ① A2 ② C1 ③ E1 ④ G1 ⑤ I1 ⑥ K1 ⑦ M1 ⑧ O1 ⑨ Q1
		--
		--   ※ 左→右の順で挿入すると次のターゲット列がずれてしまうので、
		--      右端から順に処理するのが安全
		set insertCells to {"A2", "C1", "E1", "G1", "I1", "K1", "M1", "O1", "Q1"}
		
		repeat with addr in insertCells
			-- 例: insert range "C1" of targetSheet shift shift to right
			select range addr of active sheet
			insert into range (range addr of targetSheet) shift shift to right
		end repeat
		
		-- 保存して閉じる
		tell wb
			save wb
			close wb saving yes
			quit -- Excel を終了
		end tell
		
	end tell
end tell

tell application "Safari"
	activate
	
	-- 最前面のプライベートウィンドウを取得
	set privateWindow to front window
	
	-- 表示切替
	do JavaScript "document.querySelector('span.btn-info[ng-click=\"showType = \\'病棟別\\'\"]').click();" in current tab of privateWindow
	delay 1
	
	-- テーブルをクリップボードへ（HTML＋Text）
	do JavaScript "
	  var table = document.querySelector('div[ng-show=\"showType==\\'病棟別\\'\"] table');
	  if(table){
	    var html = table.outerHTML;
	    function copyToClipboard(html){
	      var listener=function(e){
	        e.clipboardData.setData('text/html',html);
	        e.clipboardData.setData('text/plain',table.innerText);
	        e.preventDefault();
	      };
	      document.addEventListener('copy',listener);
	      document.execCommand('copy');
	      document.removeEventListener('copy',listener);
	    }
	    copyToClipboard(html);
	  }
	" in current tab of privateWindow
	delay 1
	
	------------------------------------------------------------------------
	-- Excel 操作
	------------------------------------------------------------------------
	tell application "Microsoft Excel"
		activate
		set wb to open workbook workbook file name ¬
			excelPath
		delay 1
		
		-- 本日の日付からyyyymm形式のシート名を取得し、該当シートをアクティブにする
		set yyyymm to do shell script "date +%Y%m"
		set targetSheet to null
		set sheetName to null
		-- 各ワークシートをループ処理
		set sheetCount to count of worksheets of wb
		repeat with i from 1 to sheetCount
			set s to worksheet i of wb
			set sheetName to (get name of s) as text
			if sheetName is yyyymm then
				set targetSheet to s
				exit repeat
			end if
		end repeat
		
		if targetSheet is null then
			-- シートがなければ新規作成
			tell wb
				set targetSheet to make new worksheet at before worksheet 1
			end tell
		end if
		set name of targetSheet to yyyymm
		delay 1
		
		activate object targetSheet
		-- 貼り付け先セルを選択
		select range "A1" of active sheet
		-- クリップボードの内容を書式付きで貼る
		paste worksheet active sheet
		
		-- ■ テーブル貼り付け直後にセルを挿入して右へシフト
		--   ① A2 ② C1 ③ E1 ④ G1 ⑤ I1 ⑥ K1 ⑦ M1 ⑧ O1 ⑨ Q1
		--
		--   ※ 左→右の順で挿入すると次のターゲット列がずれてしまうので、
		--      右端から順に処理するのが安全
		set insertCells to {"A2", "C1", "E1", "G1", "I1", "K1", "M1", "O1", "Q1"}
		
		repeat with addr in insertCells
			-- 例: insert range "C1" of targetSheet shift shift to right
			select range addr of active sheet
			insert into range (range addr of targetSheet) shift shift to right
		end repeat
		
		do shell script "rm -f " & quoted form of excelPath
		delay 5
		-- 保存して閉じる
		tell wb
			-- ▼ 保存（同じパス・ファイル名で上書き）
			save workbook as wb filename (POSIX file excelPath) file format Excel XML file format
			
			-- ▼ 閉じる（すでに保存済みなので saving no）
			close wb saving yes
			quit -- Excel を終了
		end tell
	end tell
	
	-- プライベートウィンドウを閉じる
	tell privateWindow
		close privateWindow
	end tell
end tell

/*
【病棟別入退院数データ送信_to_m3.scpt をMacで自動実行する方法】

1. Automatorで「アプリケーション」を作成し、AppleScriptを実行する
----------------------------------------------------------
1) Automatorを起動し、「新規書類」→「アプリケーション」を選択
2) 「アクション」から「AppleScriptを実行」を検索し、右側にドラッグ
3) 下記のようにスクリプトを記述

例:
do shell script "osascript '/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/00_Automatecpt/病棟別入退院数データ送信_to_m3.scpt'"

4) ファイル名を「病棟別入退院数データ送信.app」などで保存

2. カレンダーやcronで自動実行する
----------------------------------------------------------
【カレンダー.appで自動化】
1) カレンダー.appで新規イベントを作成
2) 「通知」→「カスタム」→「ファイルを開く」→上記で作成した.appを指定
3) 実行したい時刻にイベントを設定

【cronで自動化（ターミナル利用）】
1) ターミナルで下記コマンドを実行し、crontabを編集
crontab -e

2) 例えば毎朝7時に実行したい場合（パスは適宜修正）
0 7 * * * osascript '/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/00_Automatecpt/病棟別入退院数データ送信_to_m3.scpt'

※cronからosascriptを使う場合、権限や環境変数に注意

3. シェルスクリプトで直接実行
----------------------------------------------------------
【ターミナルやLaunchAgentによる自動実行方法まとめ】

1. ターミナルからAppleScriptを直接実行する場合
----------------------------------------------------------
osascript '/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/00_Automatecpt/病棟別入退院数データ送信_to_m3.scpt'

2. LaunchAgent（macOSの自動起動機能）を使う場合
----------------------------------------------------------
① 設定ファイル（例: com.keiyukai.m3upload.plist）を作成し、下記ディレクトリに配置
~/Library/LaunchAgents/com.keiyukai.m3upload.plist

② ターミナルで以下のコマンドを順に実行
launchctl load ~/Library/LaunchAgents/com.keiyukai.m3upload.plist   # 読み込み
launchctl start com.keiyukai.m3upload                               # 手動起動（必要に応じて）
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.keiyukai.m3upload.plist  # macOS Ventura以降

※launchctl bootstrapはmacOSのバージョンによって必要な場合があります。

【注意】
- AppleScript/Automator/cronの実行権限やセキュリティ設定（システム環境設定→セキュリティとプライバシー→フルディスクアクセス等）に注意
- ファイルパスに全角文字が含まれる場合、ターミナルやcronでのパス指定は特に注意
- osascriptコマンドはmacOS標準搭載

*/
