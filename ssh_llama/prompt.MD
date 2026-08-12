請建立一個 Codex Skill，名稱為 vultr-ollama-deployer。

目標：
在一台既有的 Ubuntu Vultr VPS 上，使用 Docker Compose 部署 Ollama，
並下載指定的 Ollama 模型。

專案必須包含：

1. SKILL.md
2. scripts/deploy.py
3. scripts/check_server.py
4. scripts/destroy_stack.py
5. templates/docker-compose.yml
6. .env.example
7. requirements.txt
8. README.md

deploy.py 需求：

- 使用 SSH 連線 VPS
- SSH private key 路徑由環境變數或 CLI 參數傳入
- 檢查 Ubuntu、CPU、RAM、磁碟空間與架構
- Docker 已存在時不得重裝
- 使用 docker compose 啟動 Ollama
- 模型名稱必須由 --model 傳入，不可寫死
- Ollama 僅綁定 127.0.0.1:11434，不可公開至 Internet
- 執行模型下載後，送出測試 prompt
- 所有操作要有清楚 log
- 發生錯誤時回傳非零 exit code
- 支援 --dry-run
- 可重複執行且不破壞既有環境
- 不得格式化硬碟、刪除 VPS 或刪除 Block Storage
- 不得將密碼、SSH key 或 API token 寫入 repository

docker-compose.yml 必須：
- 使用官方 Ollama container image
- 設定 restart policy
- 使用 named volume 儲存模型
- 只映射至 127.0.0.1:11434

最後加入基本 pytest 測試，並執行 lint 與測試。