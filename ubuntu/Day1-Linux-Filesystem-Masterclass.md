# 🐧 Day 1 Linux 檔案系統實戰課程
## 從零開始掌握 pwd、cd、ls、mkdir、cp、mv、rm

**日期**：2026.05.03  
**環境**：雲端 Ubuntu 主機  
**目標**：建立紮實的檔案系統導航和操作基礎  
**時長**：60-90 分鐘動手實踐  

---

## 🎯 Day 1 核心成果

完成本課程後，你將能夠：

✅ **精確定位**：用 `pwd` 隨時知道自己在哪裡  
✅ **靈活移動**：用 `cd` 在目錄樹中上下左右移動  
✅ **探索檔案**：用 `ls` 和各種選項查看檔案清單  
✅ **建立結構**：用 `mkdir` 創建目錄  
✅ **複製/移動**：用 `cp` 和 `mv` 管理檔案  
✅ **清理空間**：用 `rm` 安全刪除  
✅ **理解權限**：讀懂 `drwxr-xr-x` 這樣的權限碼  

---

## 📚 第一部分：Linux 檔案系統的核心概念

### 1.1 一切皆檔案（Everything is a file）

Linux 哲學的核心：

```
普通檔案       → 文本、代碼、數據（.txt, .sh, .py）
目錄           → 檔案的容器（資料夾）
設備檔案       → 硬件設備（/dev/sda, /dev/null）
符號連接       → 指向其他檔案的快捷方式（連結）
管道、套接字   → 進程通信的通道
```

這意味著 **Linux 中沒有「資料夾」的概念** — 只有特殊的檔案，裡面放著其他檔案的列表。

### 1.2 檔案系統的樹形結構

```
/                                    (根目錄，一切開始於此)
├── home/                           (用戶主目錄)
│   └── user/                       (你的家目錄 ~)
│       ├── documents/
│       ├── downloads/
│       └── .bashrc                 (隱藏檔，以 . 開頭)
├── etc/                            (系統配置檔案)
├── var/                            (日誌、緩存)
├── tmp/                            (臨時檔案，重啟後清空)
├── usr/                            (用戶應用程序)
├── bin/                            (執行檔)
└── root/                           (超級用戶的家目錄)
```

**關鍵點**：
- **絕對路徑**：從 `/` 開始（如 `/home/user/documents`）
- **相對路徑**：從當前位置開始（如 `documents` 或 `../downloads`）
- **當前目錄**：`.` 表示
- **父目錄**：`..` 表示
- **家目錄**：`~` 表示（等於 `/home/user`）

---

## 🎮 第二部分：核心命令深解

### 2.1 `pwd` — 我在哪裡？

**命令**：Print Working Directory

```bash
$ pwd
/home/user
```

**常用場景**：
- 你在深層目錄迷路了，執行 `pwd` 確認位置
- 寫腳本時需要記錄當前路徑

**進階用法**：
```bash
pwd -L    # 顯示邏輯路徑（如果有符號連接）
pwd -P    # 顯示物理路徑（跳過符號連接）
```

---

### 2.2 `cd` — 移動到新位置

**命令**：Change Directory

#### 基礎用法

```bash
# 進入子目錄
cd documents

# 進入根目錄（絕對路徑）
cd /home/user/downloads

# 返回父目錄
cd ..

# 返回兩層
cd ../..

# 回到家目錄
cd ~
# 或簡寫
cd

# 返回上一個位置
cd -
```

#### 實踐場景

```bash
# 你在 /home/user 
$ pwd
/home/user

# 進入 documents
$ cd documents
$ pwd
/home/user/documents

# 回到 user
$ cd ..
$ pwd
/home/user

# 用絕對路徑直接跳到 /tmp
$ cd /tmp
$ pwd
/tmp

# 回到家
$ cd ~
$ pwd
/home/user
```

**常見錯誤**：
```bash
# ❌ 錯誤：空格前後會被當作參數
cd my documents    # 會嘗試進入 my，忽略 documents

# ✅ 正確：用引號包裹含空格的路徑
cd "my documents"
cd 'my documents'
```

---

### 2.3 `ls` — 列出檔案

**命令**：List directory contents

#### 基礎用法

```bash
# 列出當前目錄
ls

# 列出特定目錄
ls /home/user/documents

# 列出隱藏檔（以 . 開頭）
ls -a

# 詳細列表（檔案大小、權限、日期）
ls -l

# 結合：詳細 + 隱藏
ls -la

# 人類可讀的大小（1K, 2M, 3G）
ls -lh

# 遞迴列出子目錄
ls -R

# 按文件大小排序
ls -lS

# 按修改時間排序
ls -lt
```

#### 輸出解讀

```bash
$ ls -la
total 42
drwxr-xr-x  5 user user  4096 May  3 10:30 .
drwxr-xr-x  3 root root  4096 Apr 28 09:15 ..
-rw-r--r--  1 user user   220 May  3 08:45 .bashrc
drwxr-xr-x  2 user user  4096 May  2 14:20 documents
drwxr-xr-x  2 user user  4096 May  1 16:00 downloads
-rw-r--r--  1 user user   1024 May  3 10:30 welcome.txt

# 字段含義：
# drwxr-xr-x  ← 權限（見下文）
# 5            ← 硬連接數
# user user    ← 所有者 和 所屬群組
# 4096         ← 檔案大小（字節）
# May 3 10:30  ← 修改日期/時間
# welcome.txt  ← 檔案名
```

**權限解讀**：
```
d r w x r - x r - x
│ │ │ │ │ │ │ │ │ │
│ │ │ │ └─┬─┘ └─┬─┘ └─┬─┘
│ └─┬─┘   │      │      │
│  擁有者  │    群組   其他人
│         │
類型    所有者權限
(d=目錄)

r = read（讀）
w = write（寫）
x = execute（執行/進入）
- = 無權限

例：drwxr-xr-x
  - d: 這是目錄
  - rwx: 擁有者可讀、可寫、可進入
  - r-x: 群組可讀、不可寫、可進入
  - r-x: 其他人可讀、不可寫、可進入
```

---

### 2.4 `mkdir` — 建立目錄

**命令**：Make Directory

```bash
# 建立單個目錄
mkdir documents

# 建立多個目錄
mkdir folder1 folder2 folder3

# 建立嵌套目錄（需要 -p 選項）
mkdir -p projects/python/venv
# 這會建立 projects/、projects/python/、projects/python/venv/

# 設定權限（8 進制數字）
mkdir -m 755 public_folder
```

#### 實踐場景

```bash
$ cd /home/user
$ mkdir hermes-project
$ ls
documents  downloads  hermes-project

$ cd hermes-project
$ mkdir -p config/models data/inputs data/outputs
$ tree
.
├── config
│   └── models
├── data
│   ├── inputs
│   └── outputs
```

---

### 2.5 `cp` — 複製檔案

**命令**：Copy

```bash
# 複製檔案
cp source.txt destination.txt

# 複製到目錄
cp file.txt documents/

# 複製整個目錄（需要 -r）
cp -r old_folder new_folder

# 保留權限和日期
cp -p original.txt copy.txt

# 結合：遞迴 + 保留屬性 + 詢問覆蓋
cp -rip source_dir dest_dir
```

#### 實踐場景

```bash
$ cd /home/user
$ echo "Hello, Linux!" > hello.txt
$ cp hello.txt hello_backup.txt
$ ls
hello.txt  hello_backup.txt

$ mkdir projects
$ cp -r documents/project1 projects/
$ ls projects/
project1
```

**常見陷阱**：
```bash
# ❌ 目標是目錄，檔案進入目錄
cp file.txt documents/
# 結果：documents/file.txt

# ❌ 目標存在會被覆蓋，無提示（危險！）
cp important.txt backup.txt    # 如果 backup.txt 已存在，會被覆蓋

# ✅ 使用 -i 詢問
cp -i important.txt backup.txt
# 如果存在：cp: overwrite 'backup.txt'? (y/n)
```

---

### 2.6 `mv` — 移動/重命名

**命令**：Move

```bash
# 重命名檔案
mv old_name.txt new_name.txt

# 移動檔案到目錄
mv file.txt documents/

# 移動整個目錄
mv old_folder new_folder

# 移動並重命名
mv /home/user/file.txt /home/user/documents/renamed.txt

# 詢問覆蓋
mv -i source.txt dest.txt
```

#### 實踐場景

```bash
$ cd /home/user
$ ls
documents  downloads  test.txt

$ mv test.txt documents/note.txt
$ ls documents/
project.md  notes.txt  note.txt

$ mv downloads old_downloads
$ ls
documents  old_downloads
```

**與 cp 的區別**：
```bash
cp file.txt copy.txt     # file.txt 仍存在，多了一個 copy.txt
mv file.txt new.txt      # file.txt 消失，變成 new.txt（移動，不複製）
```

---

### 2.7 `rm` — 刪除檔案

**命令**：Remove

```bash
# 刪除檔案
rm unwanted.txt

# 刪除多個檔案
rm file1.txt file2.txt file3.txt

# 刪除目錄（需要 -r）
rm -r old_folder

# 詢問確認（安全模式）
rm -i suspicious.txt
# 會問：rm: remove regular file 'suspicious.txt'? (y/n)

# 詢問 + 遞迴
rm -ri entire_folder/

# 強制刪除，無確認（小心！）
rm -f protected_file.txt
```

#### 實踐場景

```bash
$ cd /home/user
$ touch temp1.txt temp2.txt temp3.txt
$ ls
temp1.txt  temp2.txt  temp3.txt  documents

$ rm -i temp1.txt
rm: remove regular file 'temp1.txt'? y
$ rm temp2.txt temp3.txt
$ ls
documents
```

**⚠️ 危險警告**：
```bash
# ❌ 永遠不要執行（會刪除系統根目錄！）
rm -rf /
rm -rf /*

# ❌ 小心 rm 的通配符
rm *.txt     # 刪除所有 .txt 檔案！確保你知道有哪些

# ✅ 安全做法
rm -i *.txt  # 每個檔案都要確認
```

**注意**：Linux 沒有「回收筒」，`rm` 是永久刪除！

---

## 🏆 第三部分：實踐練習

### 練習 1：導航基本功

```bash
# 1. 確認你在家目錄
pwd

# 2. 列出家目錄的所有檔案（含隱藏）
ls -la ~

# 3. 進入 /tmp
cd /tmp

# 4. 確認位置
pwd

# 5. 返回家
cd ~
pwd
```

**預期輸出**：
```
/home/user
total 42
drwxr-xr-x  5 user user  4096 May  3 10:30 .
...
/tmp
/home/user
```

---

### 練習 2：建立 Hermes 專案結構

```bash
# 1. 進入家目錄
cd ~

# 2. 建立專案根目錄
mkdir hermes-agent-setup

# 3. 進入專案
cd hermes-agent-setup

# 4. 建立子目錄結構（一行命令）
mkdir -p config/{models,providers} data/{input,output,logs} scripts

# 5. 查看結構（如果有 tree 命令）
tree
# 或用 ls -R
ls -R
```

**預期結構**：
```
hermes-agent-setup/
├── config/
│   ├── models/
│   └── providers/
├── data/
│   ├── input/
│   ├── output/
│   └── logs/
└── scripts/
```

---

### 練習 3：檔案操作實戰

```bash
# 1. 進入專案目錄
cd ~/hermes-agent-setup

# 2. 建立一個配置檔案
echo "model=claude-opus-4.6" > config/hermes.conf
echo "provider=anthropic" >> config/hermes.conf

# 3. 檢視內容
cat config/hermes.conf

# 4. 複製配置檔案作為備份
cp config/hermes.conf config/hermes.conf.backup

# 5. 建立初始化腳本
echo "#!/bin/bash" > scripts/setup.sh
echo "echo 'Hermes Agent setup starting...'" >> scripts/setup.sh

# 6. 檢視腳本
cat scripts/setup.sh

# 7. 複製整個 config 目錄
cp -r config config_v2

# 8. 列出所有目錄
ls -la

# 9. 刪除 v2 備份
rm -r config_v2
```

---

### 練習 4：權限和隱藏檔

```bash
# 1. 建立一個敏感檔案
echo "API_KEY=sk-xxxxx" > config/.env

# 2. 列出隱藏檔
ls -la config/

# 3. 檢查目錄權限
ls -ld .

# 4. 建立只有你能讀的檔案
touch config/secret.txt
chmod 600 config/secret.txt
ls -la config/secret.txt

# 5. 讀懂權限碼
# -rw------- 意思：只有所有者可讀可寫，其他人無法訪問
```

---

### 練習 5：認識常用目錄

```bash
# 列出根目錄
cd /
ls -la

# 查看各目錄用途
cd /etc && ls | head -10          # 系統設定
cd /var && ls                      # 日誌和資料
cd /home && ls                     # 用戶目錄
cd /usr && ls                      # 應用程序
cd /tmp && ls                      # 臨時檔案
cd /root && ls                     # root 用戶的家
```

---

## 📋 Day 1 完成清單

執行完以下步驟後，你已掌握 Day 1 基礎：

- [ ] 執行 `pwd` 確認當前位置 5 次以上
- [ ] 用 `cd` 導航到至少 5 個不同目錄
- [ ] 用 `ls`、`ls -la`、`ls -lh` 查看目錄
- [ ] 用 `mkdir` 建立嵌套目錄結構（-p 選項）
- [ ] 用 `cp` 複製檔案和目錄（-r 選項）
- [ ] 用 `mv` 移動和重命名檔案
- [ ] 用 `rm` 刪除檔案（帶 -i 確認）
- [ ] 理解並讀懂權限碼（drwxr-xr-x）
- [ ] 在 /tmp、/var、/etc 中各執行一次導航
- [ ] 建立完整的專案目錄結構

---

## 🔥 Day 1 進階挑戰

如果你已掌握上述基礎，嘗試這些：

### 挑戰 1：一行命令建立完整結構

```bash
mkdir -p ~/project/{src/{modules,config},tests,docs,build} && \
cd ~/project && \
ls -R
```

### 挑戰 2：批量複製和組織

```bash
# 建立多個檔案
touch file{1..10}.txt

# 複製到新目錄
mkdir backup
cp file*.txt backup/

# 重命名（一行）
for f in backup/file*.txt; do mv "$f" "${f%.txt}_backup.txt"; done
ls backup/
```

### 挑戰 3：理解相對和絕對路徑

```bash
# 在 ~/hermes-agent-setup 中
cd ~/hermes-agent-setup

# 相對路徑
cp ./config/hermes.conf ./data/

# 絕對路徑
cp /home/user/hermes-agent-setup/config/hermes.conf /home/user/hermes-agent-setup/data/

# 使用 ~ 簡寫
cp ~/hermes-agent-setup/config/hermes.conf ~/hermes-agent-setup/data/

# 驗證三個複製結果相同
ls -la data/
```

---

## 💡 Day 1 的關鍵洞察

### 1. **絕對 vs 相對路徑**
- 絕對路徑總是從 `/` 開始，無論你在哪裡都有效
- 相對路徑從當前位置開始，更簡潔但容易迷路
- 用 `pwd` 時刻確認位置

### 2. **Linux 中沒有 Undo**
- `rm` 是永久刪除，沒有回收筒
- 養成用 `rm -i` 確認的習慣
- 批量操作前用 `ls` 驗證

### 3. **隱藏檔的重要性**
- `.bashrc`、`.env`、`.gitignore` 等以 `.` 開頭
- `ls` 默認不顯示，需要 `ls -a`
- 系統配置都在隱藏檔中

### 4. **權限是安全的基礎**
- `rwx` 對應 7、5、1（二進制轉換）
- 檔案默認 644（rw-r--r--），目錄默認 755（rwxr-xr-x）
- 後續會學 `chmod` 修改權限

### 5. **目錄就是檔案**
- Linux 中 `mkdir` 建立的是特殊檔案，包含其他檔案的列表
- 這就是為什麼 `cd` 需要 `x`（執行）權限進入目錄

---

## 🎬 Day 2 預告

掌握了檔案系統後，Day 2 將深入：

- **文本編輯**：nano、vim、cat、grep
- **文件查看**：less、head、tail、wc
- **用戶和權限**：sudo、chmod、chown、whoami

到時候，Hermes Agent 的安裝會變得輕而易舉！

---

## 📞 常見問題

**Q: 我不小心用 `rm -r` 刪除了重要資料，能恢復嗎？**  
A: 通常無法恢復。Linux 默認無回收筒。下次要用 `rm -i` 確認。對於 Git 倉庫，可能可以恢復。

**Q: 為什麼 `cd` 進入某些目錄失敗？**  
A: 通常是權限不足（沒有 `x` 權限）。用 `ls -ld dirname` 檢查權限。

**Q: `cp` 和 `mv` 的本質區別是什麼？**  
A: `cp` 複製（增加），`mv` 移動（原位置消失）。如果源和目標在同一磁碟，`mv` 只改變索引（快速）。

**Q: 可以一次複製多個檔案嗎？**  
A: 可以。`cp file1.txt file2.txt file3.txt destination/` 或用通配符 `cp *.txt backup/`。

---

## 🚀 Day 1 完成時間表

| 階段 | 內容 | 時間 |
|------|------|------|
| 導入 | 理解檔案系統概念 | 5 分 |
| 講解 | 逐一深解 7 個命令 | 20 分 |
| 練習 1-2 | 導航 + Hermes 結構 | 15 分 |
| 練習 3-5 | 檔案操作 + 權限 + 探索 | 20 分 |
| 挑戰 | 進階任務（可選） | 15 分 |

---

祝你 Day 1 學習順利！🎉

掌握這些命令後，你將對 Linux 系統有截然不同的理解。  
下一步就是在這個基礎上部署 Hermes Agent！

