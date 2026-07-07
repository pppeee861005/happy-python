● 📚 PATH 是什麼？

  PATH 是一個「搜尋路徑清單」，告訴 Linux 系統去哪些目錄找可執行程式。

  ---
  🎯 用比喻解釋

  想像 PATH 是公路標誌：

  您輸入：claude
        ↓
  系統問：「我去哪裡找 claude 程式？」
        ↓
  系統查 PATH 清單：
    ① /usr/local/bin （查過，沒有）
    ② /usr/bin       （查過，沒有）
    ③ /bin           （查過，沒有）
    ④ ~/.local/bin   （❌ 這條路不在 PATH 中，所以不查）
        ↓
  系統放棄：「claude: command not found」

  如果 ~/.local/bin 在 PATH 中：
  系統查 PATH 清單：
    ① /usr/local/bin （查過，沒有）
    ② /usr/bin       （查過，沒有）
    ③ /bin           （查過，沒有）
    ④ ~/.local/bin   （✅ 找到 claude 程式！）
        ↓
  系統執行程式：Claude Code 啟動！

  ---
  🔧 具體例子

  查看目前的 PATH

  echo $PATH

  會顯示（例如）：
  /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  這表示系統會按順序在這些地方找程式：
  1. /usr/local/sbin
  2. /usr/local/bin
  3. /usr/sbin
  4. /usr/bin
  5. /sbin
  6. /bin

  ❌ 沒有 ~/.local/bin ← 這就是問題！

  ---
  ✅ 加入 PATH 的意思

  export PATH="$HOME/.local/bin:$PATH"

  逐部分解釋：

  | 部分               | 意思                          |
  |------------------|-----------------------------|
  | $HOME/.local/bin | Claude Code 的位置（~ 就是 $HOME） |
  | :                | 「或者」的意思（分隔符）                |
  | $PATH            | 原本的 PATH 清單                 |
  | export           | 讓整個系統都認識這個變數                |

  簡單說：告訴系統「除了原本的地方，也要去 ~/.local/bin 找程式」

  ---
  🔄 修改前後對比

  修改前

  PATH = /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  修改後

  PATH = /root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
                  ↑
              新加入的位置（放在最前面，優先搜尋）

  ---
  💾 為什麼要寫入 ~/.bashrc？

  您執行的完整命令：
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc

  分成三部分：

  | 命令                                  | 功能                |
  |-------------------------------------|-------------------|
  | echo 'export PATH=...' >> ~/.bashrc | 把 PATH 設置永久保存到配置檔 |
  | &&                                  | 如果上一個成功才執行下一個     |
  | source ~/.bashrc                    | 立即生效（不需要重新登入）     |

  如果不加入 ~/.bashrc

  export PATH="$HOME/.local/bin:$PATH"
  # ✅ 現在能用 claude
  # ❌ 但一旦您重新登入 VPS，PATH 又會恢復原樣

  ---
  🎬 視覺化流程

  您在 VPS 上輸入：claude

     ↓ 系統查詢 PATH ↓

  ┌─────────────────────┐
  │  /usr/local/sbin    │ → 查
  ├─────────────────────┤
  │  /usr/local/bin     │ → 查
  ├─────────────────────┤
  │ ~/.local/bin   ✅   │ → 找到！執行
  ├─────────────────────┤
  │  /usr/sbin          │ → （不用查了）
  ├─────────────────────┤
  │  /usr/bin           │ → （不用查了）
  └─────────────────────┘

  ---
  ✨ 簡化答案

  PATH = 系統去哪些資料夾找程式

  ~/.local/bin 是 Claude Code 的位置，但系統預設不會去那裡找，所以要告訴系統把這個資料夾加進搜尋清單。

  ---
  現在執行我之前說的命令，應該就能用 claude 了！
