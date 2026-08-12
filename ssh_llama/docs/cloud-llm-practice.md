# Vultr 連接雲端 LLM 練習

## 本次選擇

- 供應商：Groq
- 模型：`llama-3.3-70b-versatile`
- API：OpenAI 相容的 Chat Completions
- 程式內費率：輸入 US$0.59／百萬 token，輸出 US$0.79／百萬 token

> 費率會變動，正式實驗前請核對 Groq 官方 pricing 頁面，並同步更新程式常數。

## 1. 建立並保存 API Key

1. 在 Groq Console 的 API Keys 頁面建立 Key。
2. 不要把 Key 貼到程式、Markdown、終端截圖或 Git commit。
3. 在 Vultr Ubuntu 終端中輸入：

```bash
read -rsp "Groq API Key: " GROQ_API_KEY
echo
export GROQ_API_KEY
```

`read -s` 不會把 Key 顯示在螢幕上；這項設定只在當前 shell 有效。先不寫入 shell history 或永久設定檔，比較適合第一次練習。

## 2. 用 curl 發送第一個請求

```bash
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.3-70b-versatile",
    "messages": [
      {"role": "system", "content": "你是一位使用繁體中文的 Linux 教練。"},
      {"role": "user", "content": "請用三句話解釋 API 是什麼。"}
    ]
  }'
```

回應中應看到 `choices[0].message.content` 與 `usage`。若回傳 `401`，通常是 Key 未設定或無效；`429` 則通常是超過配額或速率限制。

## 3. 執行 Python 互動聊天

程式只使用 Python 標準庫，不需要安裝套件。

```bash
cd ~/ssh_llama
python3 src/cloud-chat.py
```

程式會：

- 以 `system` 設定助手風格。
- 把終端輸入加成 `user` 訊息。
- 把模型回答放回對話歷史作為 `assistant` 訊息。
- 顯示耗時、輸入／輸出 token 與估計費用。
- 將指標寫入 `results/cloud-chat-metrics.csv`（Git 會忽略此檔）。

## 4. 比較 Groq 與 Gemma 4

在兩個模型使用完全相同的三個題目，每題各執行三次：

1. 知識：「用 150 字解釋 Docker volume 與 bind mount 的差異。」
2. 推理：「一台 8 GB RAM 的 VPS 要執行 27B 模型，會遇到哪些問題？」
3. 程式：「寫一個有超時與錯誤處理的 Python HTTP GET 範例。」

手動把結果填入：

| 模型 | 題目 | 總耗時（秒） | 回答正確性 1–5 | 指令遵循 1–5 | 可讀性 1–5 | 費用 USD | 備註 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Groq Llama 3.3 70B | 知識 |  |  |  |  |  |  |
| Gemma 4 | 知識 |  |  |  |  | 0 |  |

Gemma 4 自架不代表完全沒有成本；表格的 API 費用可寫 0，但備註要記錄 Vultr 主機時間成本。

## 5. 安全檢查

```bash
git status --short
git check-ignore -v .env
git diff --cached
```

確認 `.env` 會被忽略，且 staged diff 沒有 `GROQ_API_KEY` 的真實值後，才可提交。

