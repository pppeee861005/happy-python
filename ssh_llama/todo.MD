# Vultr、Ollama 與 Hermes Agent 練習計畫

## 1. Docker、Ollama 與 Gemma 4 基礎（已完成）

- [x] 在 Vultr Ubuntu 主機安裝 Docker Engine。
- [x] 驗證 `docker run hello-world`。
- [x] 建立 Ollama Docker 容器。
- [x] 使用 Docker Volume 保存模型。
- [x] 下載並執行 `gemma4:e2b`。
- [x] 透過終端與 Gemma 4 對話。
- [x] 理解 Docker、映像、容器、Ollama 與 LLM 的關係。

完成標準：Gemma 4 能正常回答問題，重新啟動容器後模型仍然存在。

## 2. 使用 Vultr 連接雲端 LLM（已完成）

目標：理解 Vultr 上的程式如何透過 API 使用雲端模型。

- [x] 選擇一個雲端 LLM 供應商與模型：Groq `llama-3.3-70b-versatile`。
- [x] 建立 API Key，且沒有把金鑰寫入 Git 或筆記。
- [x] 使用 `GROQ_API_KEY` 環境變數保存 API Key。
- [x] 用 `curl` 發送第一個聊天 API 請求。
- [x] 寫一個簡單的 Python 聊天程式 `src/cloud-chat.py`。
- [x] 練習 system、user、assistant 三種訊息角色。
- [x] 記錄 token 用量、回應時間與費用。
- [x] 比較雲端模型與 Gemma 4 的回答品質及速度。

### 2026-08-01 實驗紀錄

- 從 Windows 以 `scp` 上傳 `src/cloud-chat.py` 到 Vultr。
- 驗證 Groq Models API 回傳 HTTP 200，API Key 與 Vultr 網路正常。
- Python `urllib` 請求曾被 Cloudflare 以 `403 / error code 1010` 拒絕；加入應用程式 `User-Agent` 後解決。
- 成功與 `llama-3.3-70b-versatile` 進行多輪對話。
- 成功用 `curl` 呼叫 Groq Chat Completions API，傳送 system 與 user 訊息並取得模型回應。
- 四次請求總計 554 tokens（輸入 436、輸出 118）。
- 平均回應時間 0.341 秒，最快 0.301 秒，最慢 0.383 秒。
- 四次請求估計總費用 US$0.00035046。
- 指標保存於 Vultr 的 `results/cloud-chat-metrics.csv`，此檔已由 `.gitignore` 排除。
- 以同一題「8 GB RAM、無 GPU 的 VPS 執行 27B 模型」比較 Groq 與 Gemma 4。
- Groq Llama 3.3 70B：1.15 秒，343 tokens（輸入 100、輸出 243），估計 US$0.00025097。
- Gemma 4：76.570 秒，API token 費用 US$0，但會使用 Vultr 的 CPU、RAM 與租用時間。
- Groq 本次約快 66.6 倍，回答精簡且遵守三點格式；但第三點將「執行」誤讀為「訓練」，與推理情境不完全相符。
- Gemma 4 的回答較詳細，並更聚焦於量化、CPU 推理與上下文限制；但「從磁碟逐層載入」會進一步拖慢推理，實用性有限。
- 本次結論：Groq 在速度、精簡度與本機資源負擔上明顯領先；Gemma 4 在此題的推理情境貼合度略佳，且不產生 API token 費用。

完成標準：Vultr 能安全呼叫雲端 LLM，程式碼與 Git 紀錄中沒有 API Key。

## 3. Hermes Agent 使用雲端 LLM

目標：先用能力較完整的雲端模型理解 Agent 的工作流程。

- [ ] 在 Vultr 主機安裝 Hermes Agent。
- [ ] 完成 Hermes 的基本設定與診斷。
- [ ] 將雲端模型設為主要模型。
- [ ] 練習一般聊天與跨工作階段記憶。
- [ ] 練習檔案讀取、終端及網路搜尋等基礎工具。
- [ ] 觀察「使用者要求 → 模型判斷 → 工具執行 → 模型回答」流程。
- [ ] 設定工具權限，避免不必要的破壞性操作。

完成標準：Hermes 能使用雲端模型完成一個包含工具呼叫的簡單任務。

## 4. Hermes Agent 使用自架 LLM

目標：讓 Hermes 經由本機 API 使用 Ollama 容器中的模型。

- [ ] 確認 Ollama API `http://127.0.0.1:11434` 正常。
- [ ] 理解 Ollama 的 OpenAI 相容端點 `/v1`。
- [ ] 將 Hermes provider 設為 Ollama。
- [ ] 將 `gemma4:e2b` 設為練習模型。
- [ ] 先以少量工具測試聊天與工具呼叫。
- [ ] 測量 RAM、Swap、CPU 使用率與回應時間。
- [ ] 測試重新啟動後，模型、Hermes 設定及記憶是否保留。
- [ ] 比較 Hermes 使用雲端 LLM 與自架 LLM 的差異。

完成標準：Hermes 不使用第三方模型 API，也能透過 Ollama 完成至少一個工具任務。

## 5. 模型與硬體實驗

目標：理解模型大小、量化、上下文及硬體之間的關係。

- [ ] 比較 2B、4B、9B 等不同大小模型。
- [ ] 理解參數量、模型檔案大小、RAM、VRAM 與量化。
- [ ] 調整上下文長度，觀察記憶體與速度變化。
- [ ] 使用 `docker stats` 觀察 Ollama 容器資源。
- [ ] 使用 `ollama ps` 與 `ollama list` 檢查模型狀態。
- [ ] 下載 `qwen3.6:27b` 作為模型管理練習（約 17 GB）。
- [ ] 不在目前 8 GB RAM、無 GPU 的主機強行執行 27B 模型。
- [ ] 若升級 GPU 主機，再測試 27B 模型與 Hermes Agent。

完成標準：能根據模型大小，估算所需 RAM、VRAM、磁碟與合理的上下文長度。

## 6. 整理成可重現的專案

目標：把手動操作整理成可以安全重建的部署方式。

- [ ] 在 `compose.yaml` 定義 Ollama 服務與 Volume。
- [ ] 建立 `.env.example`，只放變數名稱及假值。
- [ ] 確認 `.env` 已被 `.gitignore` 排除。
- [ ] 將安裝、啟動、停止、備份及復原方式寫入 `readme.md`。
- [ ] 記錄常見錯誤與排查指令。
- [ ] 執行一次停止、移除及重新建立容器的演練。
- [ ] 確認重建後模型資料仍然存在。

完成標準：只閱讀專案文件，就能在乾淨的 Ubuntu 主機重新建立環境。

## 建議練習順序

```text
Docker／Ollama 基礎（完成）
  → 雲端 LLM API
  → Hermes + 雲端 LLM
  → Hermes + Ollama 自架 LLM
  → 模型與硬體比較
  → Docker Compose 與完整文件
```

## 目前下一步

1. 選擇第 2 階段要使用的雲端 LLM 供應商。
2. 或直接安裝 Hermes Agent，以 `gemma4:e2b` 進行有限度的自架模型練習。

> 注意：目前 Vultr 主機約有 7.2 GiB RAM、8 GiB Swap，且沒有 GPU。適合學習小模型與整合流程，不適合實際執行 `qwen3.6:27b`。
