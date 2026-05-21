# Week 09 - 列表與字串操作進階

## 📚 本週學習重點

這一週主要深入學習 **迴圈控制**、**列表推導式** 和 **字串操作**，透過實務練習掌握 Python 的核心技能。

---

## 🎯 核心概念

### 1️⃣ 列表推導式 (List Comprehension)

列表推導式是 Python 中簡潔且高效的列表創建方式。

**基本語法：**
```python
[expression for item in iterable if condition]
```

**優勢：**
- ✅ 簡潔易讀，代碼量少
- ✅ 執行效率高
- ✅ 支持嵌套條件

**實例：**
```python
# 刪除列表中的所有負數
x = [1, 3, 5, 0, -1, 3, -2]
result = [num for num in x if num >= 0]  # [1, 3, 5, 0, 3]
```

---

### 2️⃣ 嵌套列表與雙層迴圈

處理嵌套列表時，需要使用雙層迴圈遍歷所有元素。

**三種常見方法：**

| 方法 | 說明 | 適用場景 |
|------|------|---------|
| **雙層 for 迴圈** | 最直觀，容易理解 | 需要細粒度控制 |
| **sum() + 生成器表達式** | 高效簡潔 | 計數和統計操作 |
| **先展平再處理** | 邏輯清晰 | 複雜處理邏輯 |

**實例：計算嵌套列表中負數的個數**
```python
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]

# 方法一：雙層迴圈
count = 0
for row in y:
    for num in row:
        if num < 0:
            count += 1

# 方法二：sum() + 生成器表達式（推薦）
count = sum(1 for row in y for num in row if num < 0)
```

---

### 3️⃣ 字串切片與旋轉

Python 支持強大的字串操作，包括索引、切片和循環旋轉。

**常用操作：**

| 操作 | 語法 | 說明 |
|------|------|------|
| **索引** | `str[i]` | 取得第 i 個字符 |
| **切片** | `str[a:b]` | 取得從 a 到 b-1 的字符 |
| **旋轉** | `str[1:] + str[0]` | 字符循環左移 |
| **迴圈匹配** | `(old_index + shift) % 26` | 字母迴圈位移 |

**實例：走馬燈效果**
```python
msg = '列車將進站 請勿靠近車門 '
while True:
    print(f"\r{msg}", end="", flush=True)
    msg = msg[1:] + msg[0]  # 字符循環左移
    time.sleep(0.2)
```

---

### 4️⃣ 字串搜尋與解析

掌握字串搜尋和提取的多種方法，處理文本數據。

**常用方法：**

| 方法 | 說明 | 返回值 |
|------|------|--------|
| **`str.find()`** | 找出子字串首次出現的位置 | 索引 (int) |
| **`str.split()`** | 按分隔符分割字串 | 列表 (list) |
| **`str.count()`** | 計算子字串出現次數 | 計數 (int) |
| **`str.replace()`** | 替換字串中的子字串 | 新字串 (str) |

**實例：擷取網域名稱**
```python
data = 'From stephen.marquard@uct.ac.za steve@apple.com brian@ibm.com'
words = data.split()
domains = []
for word in words:
    if '@' in word:
        domain = word.split('@')[1]
        domains.append(domain)
# 結果：['uct.ac.za', 'apple.com', 'ibm.com']
```

---

### 5️⃣ 加密演算法 - Caesar Cipher

瞭解簡單的文本加密方式，理解迴圈與條件的應用。

**原理：**
- 將每個字母在字母表中移動固定位數
- 使用模運算 (%) 實現循環

**實例：**
```python
def encrypt_text(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text:
        if char in alphabet:
            old_index = alphabet.find(char)
            new_index = (old_index + shift) % 26  # 循環位移
            result += alphabet[new_index]
        else:
            result += char
    return result

# "cheer" 前移 7 → "jolly"
encrypt_text("cheer", 7)
```

---

### 6️⃣ 檔案讀寫與數據解析

讀取文本文件並進行數據統計和分析。

**關鍵技能：**
- 📖 使用 `open()` 和 `read()` 讀取文件
- 🔄 使用 `split()` 按行或空白分割內容
- 📊 計算行數、單詞數、字符數
- 🔍 使用條件篩選出特定數據

**實例：計算文件統計**
```python
# 讀取文件
with open('word_count.txt') as f:
    lines = f.read().split("\n")

# 統計
line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len([c for c in line if c.isalpha()]) for line in lines)

print(f"檔案中共有 {line_count} 行，{word_count} 個字，{char_count} 個字元")
```

---

## 📁 本週檔案說明

| 檔案 | 內容 |
|------|------|
| `ex_09.py` | **作業練習**：迴圈與 if 敘述、加密、檔案解析 |
| `quiz_09.py` | **複習測驗**：走馬燈、字串搜尋、網域提取 |
| `ex_091.py` | 補充練習 |
| `ex_09_02.py` | 進階練習 |
| `ex_09_022.py` | 進階練習 2 |
| `peter_ex09.md` | 核心概念詳解 |
| `README.md` | 本檔案 - 完整學習指南 |

---

## ✨ 學習要點速記

### 三個必會技能

1. **列表推導式** → 快速篩選和轉換列表
   ```python
   [x for x in list if condition]
   ```

2. **字串切片與操作** → 靈活處理文本數據
   ```python
   str[start:end]  # 切片
   str.split(sep)  # 分割
   ```

3. **迴圈 + 條件** → 解決複雜的數據問題
   ```python
   for item in iterable:
       if condition:
           # 執行操作
   ```

---

## 🎓 進階學習建議

- 🔹 練習列表推導式的各種變形（嵌套、多條件）
- 🔹 熟悉字串的所有常用方法（find, split, replace, count）
- 🔹 理解 `%` 運算符在循環中的應用
- 🔹 嘗試結合迴圈與條件解決實際問題
- 🔹 讀寫檔案並進行數據統計

---

## 📝 自我評估

完成本週學習後，確認你能夠：

- [ ] 編寫列表推導式篩選數據
- [ ] 處理嵌套列表並進行統計
- [ ] 使用字串切片實現旋轉效果
- [ ] 用多種方法搜尋和提取字串內容
- [ ] 實現簡單的加密演算法
- [ ] 讀取檔案並統計文本數據

---

**祝學習愉快！** 🎉
