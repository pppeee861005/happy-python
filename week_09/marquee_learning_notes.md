# 走馬燈程式學習筆記 📝

## 🎯 程式目標
創建一個模擬捷運站走馬燈效果的程式，讓文字「列車將進站 請勿靠近車門 以免夾傷」能夠優雅地滾動顯示。

## 🔧 核心技術概念

### 1. 字串切片 (String Slicing)
```python
text = "Hello World"
print(text[0:5])  # 輸出: "Hello"
print(text[6:11]) # 輸出: "World"
```

### 2. 無窮迴圈 (Infinite Loop)
```python
while True:
    # 這裡的程式碼會一直執行
    pass
```

### 3. 例外處理 (Exception Handling)
```python
try:
    # 可能出錯的程式碼
    pass
except KeyboardInterrupt:
    # 當使用者按 Ctrl+C 時執行
    print("程式結束")
```

## 🎨 走馬燈原理解析

### 步驟一：準備文字
```python
message = "列車將進站 請勿靠近車門 以免夾傷"
width = 40
full_text = " " * width + message + " " * width
```

**為什麼要加空格？**
- 讓文字從右邊「滑入」螢幕
- 讓文字完全「滑出」螢幕後再重新開始

### 步驟二：滾動效果
```python
position = 0
while True:
    display = full_text[position:position + width]
    print(f"\r[{display}]", end="", flush=True)
    position += 1
```

**關鍵技巧：**
- `\r`: 讓游標回到行首，覆蓋之前的文字
- `end=""`: 不換行
- `flush=True`: 立即顯示，不等緩衝區滿

### 步驟三：控制速度
```python
time.sleep(0.15)  # 暫停 0.15 秒
```

## 🌟 美感設計元素

### 1. 視覺框架
```python
print("🚇 捷運站走馬燈 🚇")
print("-" * (width + 2))
```

### 2. 優雅的結束
```python
except KeyboardInterrupt:
    print("\n\n🚇 走馬燈已停止，謝謝使用！")
```

## 🎓 學習重點

### 初學者版本 (simple_marquee.py)
- **簡潔明瞭**：每個步驟都很清楚
- **易於理解**：註解詳細，邏輯直觀
- **適合練習**：可以輕鬆修改參數實驗

### 進階版本 (marquee_train.py)
- **模組化設計**：使用函數分離功能
- **更多功能**：清除螢幕、更複雜的滾動邏輯
- **專業風格**：完整的文檔字串和錯誤處理

## 🔍 實驗建議

### 1. 調整參數
```python
width = 30        # 改變螢幕寬度
time.sleep(0.1)   # 改變滾動速度
```

### 2. 修改訊息
```python
message = "歡迎搭乘台北捷運 Welcome to Taipei MRT"
```

### 3. 添加顏色 (進階)
```python
# 需要安裝 colorama 套件
from colorama import Fore, Style
print(f"{Fore.GREEN}[{display}]{Style.RESET_ALL}")
```

## 💡 程式設計美學

這個走馬燈程式展現了程式設計的美感：
- **節奏感**：文字的流動如音樂般有韻律
- **視覺美**：簡潔的框架設計
- **互動美**：優雅的開始與結束
- **功能美**：簡單的程式碼實現複雜的效果

## 🚀 延伸挑戰

1. **雙向滾動**：讓文字可以左右來回滾動
2. **多行顯示**：同時顯示多條訊息
3. **彩色效果**：為不同的字加上不同顏色
4. **速度控制**：讓使用者可以調整滾動速度

記住：程式設計不只是邏輯，更是一種藝術創作！ ✨


這段程式碼用來實現跑馬燈（marquee）文字滾動的循環效果。當前顯示的位置 position 超過或等於 len(full_text) - width（也就是剩下的文字已經不足以填滿顯示寬度時），就會把 position 重設為 0，讓滾動從頭開始。這樣可以讓跑馬燈文字無限循環顯示，不會因為滾動到尾端就停止。這種寫法常見於動態顯示訊息或廣告欄位。

這行程式碼的作用是從完整的文字串 full_text 中，根據目前的位置 position，擷取出長度為 width 的子字串，並存到 display 變數。這樣可以讓跑馬燈每次只顯示一段固定寬度的內容，隨著 position 增加，顯示的內容就會往後「滾動」。這種寫法是實現文字跑馬燈效果的關鍵步驟。

假設    width = 20，   position 一開始是 0，
那第一次顯示的是    full_text[0:20]，
下一次    position 變成 1，就顯示    full_text[1:21]，
再下一次是    full_text[2:22]，以此類推。 也就是說，每次都往後移動一格，顯示的區間是「從 position 到 position+width」這一段，
這樣就能產生跑馬燈的滾動效果。

Ctrl+C 是在命令列（終端機）中用來中斷正在執行程式的標準快捷鍵。當你按下 Ctrl+C，Python 會產生一個    KeyboardInterrupt 例外，讓程式可以安全地結束。這種設計是為了讓使用者在無窮迴圈或長時間執行的程式（像跑馬燈）中，隨時可以用 Ctrl+C 來手動停止程式，而不需要強制關閉終端機或視窗。

在 Python 的 print() 函式中，   end 是一個參數，用來指定每次輸出結尾要加上的字串。預設值是換行字元 "\n"，所以每次 print() 都會自動換行。如果你想讓多次輸出在同一行，可以把    end 設成空字串（   end=""），或指定其他字元（例如    end=" " 讓輸出之間用空格分隔）。這個參數常用於需要動態更新同一行內容（如跑馬燈、進度條）或自訂輸出格式的情境。