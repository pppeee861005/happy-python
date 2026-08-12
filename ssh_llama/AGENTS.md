# Repository Guidelines

## 專案結構與模組組織

本專案目前是 Vultr 上部署 Docker、Llama 與本地端 AI Agent 的學習紀錄。根目錄的 `readme.md` 說明實驗目標與主機環境；目前尚未加入程式碼、測試或資產目錄。

新增內容時請保持清楚的分層：

- `src/`：應用程式與 Agent 原始碼。
- `tests/`：與 `src/` 結構對應的自動化測試。
- `scripts/`：部署、下載模型及環境初始化腳本。
- `docs/`：操作步驟、架構說明與實驗紀錄。
- `config/`：可提交的設定範本，不得存放密鑰。

## 建置、測試與開發命令

目前沒有既定的建置或測試工具。新增可執行專案時，請在 `readme.md` 同步記錄完整指令與必要版本。Docker 相關變更應優先提供一致、可重現的入口，例如：

```bash
docker compose up -d       # 啟動本地服務
docker compose logs -f     # 追蹤容器日誌
docker compose down        # 停止並移除服務
```

若引入 Python，建議提供 `requirements.txt` 或 `pyproject.toml`，並以 `python -m pytest` 執行測試。

## 程式風格與命名慣例

Markdown 使用簡短標題、精簡段落及具語言標記的程式碼區塊。Shell 腳本採 2 空格縮排，檔名使用小寫 kebab-case，例如 `setup-ollama.sh`。Python 採 4 空格縮排、模組與函式使用 `snake_case`、類別使用 `PascalCase`；建議使用 Ruff 格式化與檢查。

## 測試指南

每項新功能至少涵蓋一個正常流程及一個失敗情境。Python 測試命名為 `tests/test_<module>.py`，測試函式命名為 `test_<behavior>()`。部署腳本需先在乾淨的 Ubuntu 22.04 環境驗證，並在 PR 中記錄實際執行結果。

## Commit 與 Pull Request 指南

近期提交多使用簡短、祈使式中文摘要，例如「新增 Groq 聊天機器人」；修正亦曾採 `fix:` 前綴。請維持單一目的提交，建議格式為 `feat: 新增模型啟動腳本` 或 `docs: 更新 Vultr 安裝步驟`。

PR 應說明目的、主要變更、驗證指令及結果，並連結相關 Issue。若變更 CLI 輸出或介面，附上截圖或終端輸出；涉及部署時，列出環境需求與回復方式。

## 安全與設定

不得提交 API 金鑰、SSH 私鑰、Token、`.env` 或雲端憑證。請提供 `.env.example`，使用假值標示必要變數，並在提交前檢查 staged diff。
