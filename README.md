# GIT-DEMO

- git --version
    版本檢視


- git config --global user.name "Tina"
- git config --global user.email "ddyy2864@gmail.com"
    設定使用者資訊(全域參數)   # 要設定好,才能做版本發布
                               # 資料存在"C:\Users\hsuyawen\.gitconfig"裡

- git config --list
    顯示git目前設定值

切換目錄--> cd (Change Directory)
            cd\      -->到根目錄
            cd d:\   -->到D槽
先輸入cd\到C槽，
再輸入cd "C:\Users\hsuyawen\Desktop\Django\GIT\demo"(目標檔案位址)


初始本地倉庫  #下完此指令才能做版本控管,下第二次會洗掉之前的版本(初始化)
              #下完此指令會出現 .git檔案 (隱藏的檔案)
    - git init (初始化)

檢視目前狀態
    - git status
          - Untrack (未控管)
      

加入控管(以文字檔為主)
    - git add <filename>   # GIT\demo\.git\objects會跑出新檔案
                           # 若內容一樣，不會產生新檔案

          - 加入控管後  Untracked -> Added
          - 若有修改    Added -> Modified
          - 確認修改    Modified -> Added   需再輸入git add <filename>

==========================================================================
(下載Vscode)
1.File -> open folder (彈跳視窗會詢問是否信任它，選yes)
2.Terminal -> new terminal
3.powershell -> command prompt
    預設Terminal
    ctrl+shift+p -> 搜尋欄輸入default -> 點Terminal:Select Default Profile -> command prompt
  清空Terminal --> cls

以下設定僅需做一次:

**設定程式碼顯示區縮放功能:
File -> Preferences -> Settings ->搜尋欄輸入zoom -> mouse wheel zoom打勾

**儲存程式碼後，自動格式化:
File -> Preferences -> Settings ->搜尋欄輸入format -> format on save打勾

**在VScode中，讓隱藏的.git檔顯示出來
File -> Preferences -> Settings ->搜尋欄輸入file.ex -> **/.git點叉


新增忽略檔案
    - .gitignore (輸入要忽略的檔案後，按ctrl+s)
                 ex:   *.jpg  (代表所有jpg檔)
                 若想忽略.vscode檔案，因為它是一個目錄，需輸入".vscode/"

將.gitignore以外的檔案一次變成Added狀態
    -git add .

@@@@重點整理@@@@
打開專案後:

1.設定資訊
2.初始化(git init)
3.控管檔案
@@@@@@@@@@@@@@@@


ctrl+s  ==> 儲存
ctrl+z  ==> 恢復上一動

恢復上一動(Added前的所有動作)
    - git checkout .


修改(刪除)後的確認 A==>M、M==>D
    - git add <filename> - 確定修改(刪除)
    - git restore <filename> - 反悔修改


查看暫存區控管的檔案
    - git ls-files     (僅顯示檔案名稱)
    - git ls-files -s  (查看完整資訊，含sha-1編碼)


檢視object內容
    - git cat-file -t sha-1(通常為檔案名稱+編碼前四碼)
       	           -p (檔案內容)
	           -t (型態 大部分是blob，二進制檔案)


儲存至倉庫區
    - git commit -m "填入自訂名稱"
                 -am => add+message
    - git commit --amend ==>合併上一次的commit
                         - 會進入VIM編輯模式(一進去先按i進入"編輯模式"才能活動)
                         - 編輯完按esc離開編輯模式(先打一個":"才能進入命令列模式輸入指令)
                         - 輸入wq，代表寫入並離開


檢視目前有幾個commit
    - git log 
      **能看到commit的編碼
        git cat-file -t <sha-1> -> 會顯示 commit
        git cat-file -p <commit-sha-1> -> tree(樹狀)+一段編碼
        git cat-file -p <tree-sha-1> (輸入上一動得到的編碼前6碼) -> 顯示出所有檔案
    - q  (強制離開)
    - git log --oneline  (commit一行輸出)


    - git rm -f <filename>在不同區域:
      1.暫存區: 可強制刪除指定檔案，不會出現確認修改的訊息
      2.倉庫區: 若不想刪除 輸入git restore --staged <filename>，會回到暫存區 -git add(確認刪除)
                                                                             -git restore(恢復)

從暫存/倉庫區移至工作目錄(不控管:A-->U)
    - git rm --cached <filename>


檢視目前分支(*為所在分支)
    - git branch
產生新分支
    - git branch <自訂名稱> 
切換分支
    - git checkout <想去的分支的名稱>
    - git checkout <任一段commit的sha-1編碼>
切換+產生新分支一次完成
    - git checkout -b <自訂新增名稱>

branch建立commit前 : (HEAD -> test, master)
branch建立commit後 : (HEAD -> test)
** HEAD永遠會指向最新的commit 

合併分支(*需先轉換到master分支)
    - git merge <master要合併的分支名稱>  ex: git merge test
          合併前 : (HEAD -> master)
          合併後 : (HEAD -> master,test)
          - 若合併發生衝突:
                 - 選取以哪一個分支為主(current/incoming/both)
                 - git merge --abort  (取消合併)

刪除分支(*需先轉換到別的分支)
    - git branch -D <要刪除的分支名稱>


重置指令
    - git reset <commit的sha1編碼>
          @保留在Untrack模式

    - git reset --soft <commit的sha1編碼>
          @恢復在暫存區，等待commit

    - git reset --hard <commit的sha1編碼>
          @真的刪除
             - git reset ORIG_HEAD      
                   @恢復到reset前的commit (反悔reset)


查找過往的commit紀錄
    - git reflog
         **只要有sha1編碼，就可以 git checkout <任一段commit的sha-1編碼>


搭配簡報最後一頁
    - git checkout/reset --hard HEAD      @恢復到最新的commit
                       	      - HEAD~1    @恢復到上一次的commit


github

- echo "# git-demo" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/YAWENHSU/git-demo.git
- git push -u origin main



- git remote add origin https://github.com/YAWENHSU/git-demo.git
    - 加入遠端倉庫

- git remote -v
    - 檢視目前連結的遠端倉庫

- git push -u origin master
- git push --set-upstream origin master
- 以上兩行等義
    - 從本地推送至遠端(首次推送，須建立遠端分支master)

- git push -f
    - 強行從本地端推送至遠端

- git clone <https://github.com/YAWENHSU/git-demo.git>
    - 從遠端複製專案至本地端
    - 本地端新增修改後
        - git add .
        - git commit -m "message"
        - git push (確保遠端為最新版本)
