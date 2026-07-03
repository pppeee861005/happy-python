# 聊天機器人 (Chat Bot)

一個使用 Google Gemini AI 的簡單聊天機器人應用。

## 📋 專案描述

本專案實現了一個基於 Google Gemini 的聊天機器人，可以接收用戶輸入並通過 AI 模型生成回應。

## 🚀 功能

- ✅ 集成 Google Gemini API
- ✅ 支持自然語言交互
- ✅ 使用環境變數安全管理 API 金鑰

## 📁 檔案結構

```
聊天機器人/
├── README.md           # 本說明文件
├── chat_bot_1.py       # 主程式 - 聊天機器人實現
└── .env                # 環境變數配置 (包含 API 金鑰)
```

## 🔧 安裝與設置

### 1. 依賴項

```bash
pip install google-generativeai python-dotenv
```

### 2. 環境變數配置

在 `.env` 檔案中設置您的 Google API 金鑰：

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> 💡 如何獲取 Google API 金鑰？
> - 前往 [Google AI Studio](https://aistudio.google.com)
> - 點選「Create API Key」
> - 將金鑰複製到 `.env` 檔案中

## 💻 使用方法

### 基本運行

```bash
python chat_bot_1.py
```

### 自定義查詢

編輯 `chat_bot_1.py` 中的 main 部分：

```python
if __name__ == "__main__":
    content = "您的問題"              # 修改這裡的提問
    model = "gemini-3.5-flash"       # 選擇模型
    reply = chat_with_model(content, model)
    print("Model reply:", reply)
```

## 📚 API 說明

### `chat_with_model(prompt: str, model_name: str)`

與 Gemini 模型進行對話

**參數：**
- `prompt` (str): 用戶的提問內容
- `model_name` (str): 要使用的模型名稱 (例如: `gemini-3.5-flash`)

**返回值：**
- (str): 模型的回應文本

**使用範例：**
```python
from chat_bot_1 import chat_with_model

response = chat_with_model("什麼是機器學習？", "gemini-3.5-flash")
print(response)
```

## 🎯 支持的模型

- `gemini-3.5-flash` - 快速響應模型 (推薦用於實時應用)
- `gemini-2.0-flash` - 增強的閃電模型
- 其他 Google Gemini 模型

## ⚙️ 配置選項

| 選項 | 說明 |
|------|------|
| `model` | 使用的 AI 模型名稱 |
| `GOOGLE_API_KEY` | Google API 金鑰 (在 .env 中設置) |

## 🔐 安全提示

⚠️ **請勿將 `.env` 檔案提交到版本控制系統中**

建議在 `.gitignore` 中添加：
```
.env
*.key
```

## 🐛 常見問題

### Q: 如何換成其他 Gemini 模型？
A: 在 `chat_bot_1.py` 中修改 `model` 變數即可

```python
model = "gemini-2.0-flash"  # 改成想要的模型名稱
```

### Q: 提示「InvalidAPIKeyError」
A: 請檢查：
- `.env` 檔案是否存在
- `GOOGLE_API_KEY` 是否正確設置
- API 金鑰是否有效

### Q: 如何調整回應延遲？
A: 模型類型會影響回應速度，快速模型 (如 `gemini-3.5-flash`) 延遲較低

## 📖 相關資源

- [Google Generative AI Python SDK 文檔](https://ai.google.dev/tutorials/python_quickstart)
- [Gemini API 官方文檔](https://ai.google.dev/docs)
- [Gemini 3.5 最新 SDK 文檔](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=zh-tw) ⭐ **最新功能與更新**
- [Python dotenv 文檔](https://python-dotenv.readthedocs.io/)

## 📝 版本更新

| 版本 | 說明 |
|------|------|
| v1.0 | 初始版本 - 基本聊天功能 |

## 🤝 貢獻

如果您有改進建議或發現問題，歡迎提出！

## 📄 授權

本專案為學習用途，可自由使用和修改。

---

**最後修改日期：** 2026年1月
