這頁面是 ngrok（一個能將你本地端伺服器對外公開的穿透工具）在 Windows 系統上的快速入門教學。以下為你詳細解釋這 4 個步驟分別在做什麼：

Step 1：安裝 ngrok 代理程式 (Install the ngrok agent)
這個步驟是要在你的 Windows 電腦上安裝 ngrok 的命令列工具（Agent）。

目的：讓你的電腦擁有 ngrok 這個指令可以使用。

方法：頁面提供了幾種安裝方式（如透過微軟商店 Microsoft Store、WinGet、Scoop 或是直接下載 .zip 壓縮檔）。官方最推薦使用 Microsoft Store 安裝，因為最安全且會自動更新。

Step 2：設定你的身份憑證 (Add your authtoken)
安裝好後，你需要讓 ngrok 知道這台電腦是連往你的帳號。

目的：進行安全驗證。因為免費版與付費版有不同的額度限制，綁定憑證後，ngrok 才能識別並授權你的連線。

方法：在終端機（如命令提示字元 CMD 或 PowerShell）中輸入以下指令：

Bash
ngrok config add-authtoken <你的憑證金鑰>
(畫面上系統已經幫你把憑證金鑰填在對應的位置，直接複製貼上執行即可)

Step 3：將你的本機專案產生一個公開網址 (Get a public URL for your app)
這一步是 ngrok 最核心的功能。

目的：將你電腦上正在運行的網頁或服務（例如跑在連接埠 80 的網站）轉發出去，產生一個暫時的公開網址。

方法：在命令列中執行：

Bash
ngrok http --url=unwhimsical-scholarly-myrle.ngrok-free.dev 80
這代表你要將你本地端連接埠 80 的流量，對應到 ngrok 配發給你的專屬域名 unwhimsical-scholarly-myrle.ngrok-free.dev。

Step 4：在瀏覽器打開網址測試 (Open your dev domain)
最後一步是用來驗證連線是否成功。

目的：確認外網的任何人是否已經可以透過 ngrok 提供的網址，瀏覽你電腦上的專案。

方法：直接在瀏覽器中輸入步驟 3 產生的網址（例如：[https://unwhimsical-scholarly-myrle.ngrok-free.dev](https://unwhimsical-scholarly-myrle.ngrok-free.dev)）。如果你的本機 80 連接埠有正常啟動網頁伺服器，此時就能順利看到畫面。