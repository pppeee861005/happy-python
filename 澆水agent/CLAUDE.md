# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 📋 項目概述

**澆水 Agent** - LLM 智能決策系統

一個基於 **Google Gemini LLM** 的植物澆水決策系統。系統接收土壤濕度 + 6 小時天氣預報數據，通過 LLM 推理做出澆水決策。

**設計哲學**：Agent-First（無硬編碼規則）、簡潔設計、易於測試、完整追蹤

---

## 🛠️ 開發環境設置

### 環境要求
- Python 3.12+（目前使用 3.12）
- pip 25.1.1+

### 初次環境建立

```bash
# 1. 建立虛擬環境
python -m venv venv

# 2. 激活虛擬環境（Windows）
venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 配置環境變數
# 編輯 .env 檔案：
# GOOGLE_API_KEY=your_api_key_here
```

### 虛擬環境狀態
- ✅ 已建立：`D:\gameplace\code\快樂寫程式\澆水agent\venv\`
- ✅ 依賴已安裝：google-genai 2.10.0 + python-dotenv 1.2.2

### 激活虛擬環境（後續使用）

```bash
# Windows 命令行
venv\Scripts\activate

# 退出虛擬環境
deactivate
```

---

## 🚀 常用開發命令

### 測試現有模塊

```bash
# 測試數據生成（Phase 1 ✅）
python data_generator.py

# 測試提示詞生成（Phase 2 ⚠️）
python prompts.py

# 測試 v0 版本（參考實現）
python v0/main.py
python v0/test_sensor.py
```

### 預期後續命令（Phase 3-5）

```bash
# 執行主程式（Phase 4 後）
python main.py

# 單元測試（Phase 3 後，若添加 pytest）
python -m pytest
```

---

## 📂 項目結構與架構

### 文件組織

```
澆水agent/
├── 📄 開發文檔
│   ├── readme.md                    # 項目簡介與快速開始
│   ├── 開發計劃.md                  # 完整 5-Phase 開發計劃
│   └── 開發進度表.md                # 進度追蹤（每個 Phase 詳細任務）
│
├── 🔧 依賴配置
│   ├── requirements.txt             # google-genai, python-dotenv
│   ├── .env                        # GOOGLE_API_KEY（已加入 .gitignore）
│   └── .gitignore                  # 標準 Python 配置
│
├── ✅ Phase 1: 基礎環境與數據層
│   └── data_generator.py           # 模擬數據生成
│
├── ⚠️ Phase 2: LLM 提示詞設計
│   └── prompts.py                  # 澆水決策規則與提示詞
│
├── ❌ Phase 3-5: 待實現
│   ├── water_agent.py              # Phase 3 - 核心決策邏輯
│   └── main.py                     # Phase 4 - 程式入口
│
├── 📚 參考實現
│   └── v0/                         # 舊版本（硬編碼邏輯）
│       ├── main.py
│       ├── watering_agent.py
│       ├── sensor.py
│       └── test_sensor.py
│
└── 🐍 虛擬環境
    └── venv/                       # Python 虛擬環境（已建立）
```

---

## 🔄 核心架構與工作流

### 系統設計流程

```
┌─────────────────────┐
│   輸入參數           │
│ • 土壤濕度 (%)      │
│ • 6小時天氣預報     │
└────────┬────────────┘
         │
         ▼
┌──────────────────────┐
│  LLM 智能推理        │
│  (Google Gemini)    │
│  • SYSTEM_PROMPT    │
│  • USER_PROMPT      │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│   決策輸出（JSON）    │
│ • decision           │
│ • confidence         │
│ • reasoning          │
│ • suggestion         │
└──────────────────────┘
```

### 核心模塊詳解

#### 1. `data_generator.py` (Phase 1 ✅)

**功能**：提供模擬數據

```python
get_mock_humidity() -> float
# 返回：0-100% 隨機濕度

get_mock_weather_6h() -> dict
# 返回：{
#   "precipitation_prob": int,  # 降雨機率 (%)
#   "temperature": float,       # 溫度 (°C)
#   "humidity": int,            # 空氣濕度 (%)
#   "wind_speed": float         # 風速 (km/h)
# }
```

#### 2. `prompts.py` (Phase 2 ⚠️)

**SYSTEM_PROMPT 設計**（澆水決策規則）：
- **5 級濕度等級**：極度乾燥 (< 20%) → 過度潮濕 (> 80%)
- **3 條邊界規則**：
  - 規則 A (濕度 < 30%)：傾向澆水
  - 規則 B (濕度 30-70%)：綜合判斷（降雨、溫度、風速）
  - 規則 C (濕度 > 70%)：不澆水
- **4 層優先級**：土壤濕度 > 溫度+降雨 > 風速 > 空氣濕度

**USER_PROMPT_TEMPLATE**（結構化輸入）：
- 输入：土壤濕度、降雨機率、溫度、空氣濕度、風速
- 輸出格式：JSON

```python
def get_system_prompt() -> str
def get_user_prompt(humidity, precipitation_prob, temperature,
                    humidity_air, wind_speed) -> str
```

#### 3. `water_agent.py` (Phase 3 待實現)

預期架構：
```python
class WaterAgent:
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash"):
        # 初始化 GenAI 客戶端

    def decide(self, humidity: float, weather_6h: dict) -> dict:
        # 返回決策結果 (decision, confidence, reasoning, suggestion)
```

#### 4. `main.py` (Phase 4 待實現)

預期流程：
1. 載入 `.env`
2. 初始化 WaterAgent
3. 生成模擬數據
4. 執行決策
5. 格式化並輸出結果

---

## 🔌 技術棧詳解

### 核心依賴

| 套件 | 版本 | 用途 |
|------|------|------|
| **google-genai** | 2.10.0 | Google Gemini LLM API SDK |
| **python-dotenv** | 1.2.2 | 環境變數管理（API Key） |

### 子依賴（自動安裝）
- google-auth：API 認證
- httpx：HTTP 客戶端
- pydantic：數據驗證
- cryptography、websockets 等

### LLM 模型配置

- **模型**：`gemini-2.0-flash`
- **選擇原因**：快速、成本低、適合實時決策
- **API Key**：存儲在 `.env` 中（`GOOGLE_API_KEY=...`）

### 使用模式（基於 week_18/chat_bot_1.py）

```python
from google import genai
from dotenv import load_dotenv

load_dotenv()  # 自動讀取 GOOGLE_API_KEY
client = genai.Client()

response = client.interactions.create(
    model="gemini-2.0-flash",
    input=prompt_text
)
output = response.output_text
```

---

## 📊 開發進度與驗收標準

### 當前進度（2026-07-01）

```
Phase 1: 基礎環境與數據層    [████████████████████] 100% ✅
Phase 2: LLM 提示詞設計     [                    ] 0%
Phase 3: 核心決策邏輯       [                    ] 0%
Phase 4: 入口程式與集成     [                    ] 0%
Phase 5: 優化與部署         [                    ] 0%

總進度：20% ✅
```

### Phase 1 完成清單 ✅
- ✅ requirements.txt（依賴定義）
- ✅ .env（環境變數模板）
- ✅ .gitignore（Git 配置）
- ✅ data_generator.py（完整實現）
- ✅ 模擬數據測試通過
- ✅ Python venv 虛擬環境建立
- ✅ 依賴套件安裝

### Phase 2 進行中 ⚠️

**已完成**：
- ✅ SYSTEM_PROMPT 設計（1642 字元）
- ✅ USER_PROMPT_TEMPLATE 設計

**待完成**：
- [ ] 使用 Gemini 手工測試 Prompt 效果
- [ ] 驗證 LLM 輸出格式有效性
- [ ] 確認決策邏輯合理性

### Phase 3-5 待實現

| Phase | 目標 | 關鍵文件 |
|-------|------|---------|
| Phase 3 | 核心決策邏輯 | water_agent.py |
| Phase 4 | 程式入口與集成 | main.py |
| Phase 5 | 優化與部署 | scheduler.py（待實現） |

---

## ⚠️ 關鍵注意事項

### 決策輸出格式（必須 JSON）

```json
{
  "decision": "澆水" 或 "不澆水",
  "confidence": 0-100,
  "reasoning": "詳細推理過程",
  "suggestion": "用戶建議"
}
```

### 常見開發問題

1. **環境變數**：
   - 確保 `.env` 中設置了有效的 `GOOGLE_API_KEY`
   - `.env` 已加入 .gitignore，不會被提交

2. **LLM API 調用**：
   - 使用 `gemini-2.0-flash` 模型
   - 參考 week_18/chat_bot_1.py 的使用模式

3. **模擬數據測試**：
   - 使用 data_generator.py 測試邏輯，無需真實 Sensor
   - 支持快速迭代開發

4. **後續擴展**：
   - 天氣 API：OpenWeatherMap / 中央氣象局
   - 真實 Sensor：DHT11 / DS18B20
   - 定時執行：APScheduler（每天早上 6 點）

---

## 🔍 參考文檔與資源

### 項目文檔
- **readme.md** - 項目簡介與快速開始
- **開發計劃.md** - 完整 5-Phase 開發計劃
- **開發進度表.md** - 詳細進度追蹤

### 外部資源
- [Google GenAI SDK](https://pypi.org/project/google-genai/)
- [Week 18 Chat Bot 實現](../week_18/chat_bot_1.py) - SDK 使用參考

---

## 🎯 即時建議

### 下一步優先項目

1. **完成 Phase 2 驗證**（待進行）
   - 使用 Google Gemini 手工測試 Prompts
   - 檢查輸出 JSON 格式有效性

2. **修復已知問題**
   - prompts.py 中的"澳水"筆誤 → 改為"澆水"

3. **實現 Phase 3**（下一個主要任務）
   - 創建 water_agent.py
   - 實現 WaterAgent 類
   - 集成 Google GenAI SDK
   - 添加錯誤處理

4. **測試框架**（未來考量）
   - 添加 pytest 進行單元測試
   - 測試各濕度範圍的決策邏輯

---

## 🔄 Git 工作流

### 最近提交
```
dc94cb0 docs: update Phase 1 progress with venv setup
3ad7acc feat: complete Phase 1 - basic environment and data generation
```

### 提交規範
- 使用清晰的 commit message
- 每個 Phase 完成後更新 開發進度表.md
- 不提交敏感信息（.env 已在 .gitignore 中）

---

## 💡 設計原則

### 為什麼不用 LangGraph？

本項目採用**輕量 SDK 方案**而非 LangGraph，原因：
- 流程簡單：輸入 → LLM 推理（一次） → 決策輸出
- 無需複雜編排：不涉及多步驟、分支、循環
- 性能考量：LangGraph 內部複雜，不必要的開銷
- 維護簡潔：直接使用 Google GenAI SDK 足夠

**LangGraph 適用場景**（未來若需要）：
- 多步驟決策流程
- 多工具調用
- 複雜推理與驗證
- 多輪交互

---

## 📝 備註

- 此指南與 開發進度表.md 保持同步
- 每個 Phase 完成後更新此檔案和進度表
- 遇到技術問題，優先查看 開發計劃.md 的「風險與依賴」部分
