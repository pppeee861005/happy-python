# 快樂寫程式 - Python 初階學習筆記

第三學期 Python 初階課程的練習作業與專案集合。

## 目錄結構

```
快樂寫程式/
├── week_01/          # 第一週：基礎語法、輸入輸出、物件導向
└── week_06/          # 第六週：迴圈、函式、資料分析
```

---

## Week 01 - 基礎語法與物件導向

| 檔案 | 說明 |
|------|------|
| `quiz_01_peter.py` | 使用者輸入與變數計算練習（姓名、年齡、行銷效益公式） |
| `quiz_01_2再練習一次.py` | 再次練習輸入輸出與計算 |
| `calculate_stats.py` | 統計計算練習 |
| `TEST.py` | 測試練習檔 |

### 銀行系統 (`銀行/`)

練習 Python 物件導向（OOP）的私有變數與封裝概念：

- **`銀行.py`** — `Banks` 類別實作
  - 私有屬性：姓名、餘額、匯率、手續費
  - 存款、提款、換匯（美金 → 台幣）功能
  - 示範私有變數保護（`__balance` 無法從外部直接修改）
- **`quiz_01.py`** — 銀行類別練習題

### 撲克牌遊戲 (`撲克牌/`)

練習多個類別互相協作：

- **`Card.py`** — 三個類別：
  - `Card`：單張牌，支援比較運算子（`>`, `<`, `==`）
  - `Deck`：一副 52 張牌，支援洗牌與發牌
  - `Hand`：手牌管理
- **`撲克牌.py`** — 遊戲主程式
- 附有完整解說文件（`1 Card.py 完整解說.MD`、`2克牌遊戲完整解說.md`）

---

## Week 06 - 迴圈、函式與資料分析

| 檔案 | 說明 |
|------|------|
| `fizze.py` | FizzBuzz — 用 `for` 迴圈與 `while` 迴圈各寫一次 |
| `lacy.py` | FizzBuzz 一行版（list comprehension） |
| `heart_bar.py` | 動態愛心進度條動畫（`❤️` / `🤍`） |
| `ninja.py` | 忍者丟手裡劍動畫（`for` 迴圈 + `time.sleep`） |
| `ninja_while.py` | 忍者動畫 while 版 |
| `pig.py` | 跨平台音效（Windows / macOS / Linux） |
| `moon_travel_time.py` | 計算音速飛行到月球所需天數 |
| `moon_again.py` | 月球旅行時間再練習 |
| `while_f.py` | while 迴圈練習 |
| `Mortgage calculator.py` | 房屋貸款每月還款金額計算器 |
| `mortgage again.py` | 房貸計算再練習 |
| `nfl.py` | NFL 進攻資料統計分析（pandas + matplotlib） |

### NFL 資料分析 (`nfl.py`)

使用 Python x ChatGPT 提示工程協作完成：

- 讀取 2019–2022 NFL 進攻統計 CSV
- 計算 Aaron Rodgers 總傳球碼數
- 排名所有四分衛（QB）傳球碼數
- 繪製 > 4000 碼球員的水平長條圖

---

## 執行環境

- Python 3.x
- NFL 分析需額外安裝：`pip install pandas matplotlib`

---

## 學習重點

- 變數、輸入輸出、格式化字串（f-string）
- 物件導向：類別、私有變數、繼承、運算子多載
- 迴圈：`for`、`while`
- 函式與模組
- 資料分析：pandas、matplotlib
- AI 輔助程式開發（提示工程）
