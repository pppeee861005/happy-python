# LINE Echo Bot - 回音機器人

一個使用 Flask 和 LINE Bot SDK 開發的回音機器人，具備文字和貼圖互動功能，並支援升級為 AI 聊天機器人。

## 功能特性

### 基礎功能
- **文字回音**：使用者發送文字訊息，機器人會原樣回覆
- **貼圖互動**：使用者發送貼圖，機器人會回應相同的貼圖
- **自動問候**：新使用者加入好友時自動回應

### 加分題功能
- **AI 聊天**：整合 ChatGPT API，機器人可進行智能對話（需啟用）

## 系統需求

- Python 3.8+
- Flask 3.0.0
- line-bot-sdk 3.11.1
- openai 1.54.1
- python-dotenv 1.0.1

## 安裝步驟

### 1. 建立虛擬環境
```bash
python -m venv venv
```

### 2. 啟動虛擬環境

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. 安裝依賴套件
```bash
pip install -r requirements.txt
```

## 配置設定

### 設置環境變數

在專案根目錄建立 `.env` 檔案，並填入以下內容：

```env
LINE_CHANNEL_ACCESS_TOKEN=你的LINE頻道存取令牌
LINE_CHANNEL_SECRET=你的LINE頻道祕密
OPENAI_API_KEY=你的OpenAI API金鑰（可選）
```

### 取得 LINE 憑證

1. 前往 [LINE Developers](https://developers.line.biz/zh-hant/)
2. 建立 Provider 和 Channel
3. 在 Channel Settings > Basic settings 中找到：
   - **Channel access token**
   - **Channel secret**

### 取得 OpenAI API 金鑰（選用）

1. 前往 [OpenAI Platform](https://platform.openai.com/)
2. 申請 API 帳號
3. 在 API Keys 頁面建立新的 API 金鑰

## 使用方法

### 執行機器人

```bash
python ex_16.py
```

預設在 `http://0.0.0.0:5000` 啟動服務

### 基礎測試（鸚鵡學舌模式）

程式碼預設 `USE_AI = False`，機器人運作如下：

1. **文字訊息**：使用者發「哈囉」→ 機器人回「哈囉」+ 貼圖
2. **貼圖訊息**：使用者發貼圖 → 機器人回相同貼圖

### 啟用 AI 聊天模式

將 `ex_16.py` 第 36 行改為：

```python
USE_AI = True
```

機器人將透過 ChatGPT 進行智能對話。

## 部署到伺服器

### 使用 Gunicorn（推薦）

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 ex_16.py:app
```

### 配置 LINE 官方 Webhook

1. 登入 LINE Developers Console
2. 在 Channel Settings > Messaging settings 中：
   - 設定 **Webhook URL**：`https://你的伺服器域名/callback`
   - 啟用 **Use webhooks**

## 程式碼結構

```
ex_16.py
├── 初始化配置
│   ├── Flask 應用
│   ├── LINE Bot API 設置
│   └── OpenAI 客戶端
├── Webhook 端點 (/callback)
│   └── 驗證 LINE 簽章
├── 文字訊息處理器
│   ├── 標準模式（鸚鵡學舌）
│   └── AI 模式（ChatGPT）
└── 貼圖訊息處理器
    └── 回應相同貼圖
```

## 常見問題排查

### 1. 簽章驗證失敗 (400 Error)

**原因**：Channel Secret 不正確或 Webhook URL 設置錯誤

**解決**：
- 確認 Channel Secret 已正確填入
- 檢查 Webhook URL 是否可公開存取
- 確認使用 HTTPS（若在網路上）

### 2. 機器人無法回覆訊息

**原因**：Channel Access Token 無效或權限不足

**解決**：
- 重新複製 Channel Access Token
- 確認 Channel 已啟用 Webhook

### 3. AI 模式無回應

**原因**：OpenAI API 金鑰無效或額度用盡

**解決**：
- 確認 API 金鑰正確
- 檢查 OpenAI 帳號額度
- 查看 API 使用狀態

### 4. ImportError: No module named 'flask'

**原因**：虛擬環境未啟動或依賴未安裝

**解決**：
```bash
# 確保虛擬環境已啟動
source venv/bin/activate  # Mac/Linux
# 或
venv\Scripts\activate  # Windows

# 重新安裝依賴
pip install -r requirements.txt
```

## 貼圖 ID 參考

預設使用的貼圖：
- **Package ID**: 3
- **Sticker ID**: 233

更多貼圖 ID 可在 [LINE Emoji GIF](https://line.me/emoji) 中查詢。

## 開發提示

- **調試模式**：修改最後一行為 `app.run(debug=True)` 以啟用 Flask 調試
- **自訂 AI 提示詞**：修改 `system` 角色的內容可改變 AI 行為
- **錯誤日誌**：生產環境建議導入日誌系統記錄所有訊息互動

## 安全建議

⚠️ **重要**：不要在程式碼中硬編碼敏感資訊

- 使用 `.env` 檔案存儲密鑰
- 確保 `.env` 在 `.gitignore` 中
- 定期更新 API 金鑰
- 不要將密鑰提交到版本控制系統

## 授權

本專案為教學用途

## 相關資源

- [LINE Developers](https://developers.line.biz/zh-hant/)
- [line-bot-sdk 文檔](https://github.com/line/line-bot-sdk-python)
- [Flask 官方文檔](https://flask.palletsprojects.com/)
- [OpenAI API 文檔](https://platform.openai.com/docs)
