# Facebook 智慧發文 - 實作指南

## 完整工作流程

### 初始化階段（Pre-Automation）

```
用戶輸入
    ↓
判斷：用戶提供的是「完整文本」還是「主題」?
    ├─ 完整文本 → 跳到「內容確認」
    └─ 主題 → 進行「內容撰寫」
```

### 內容撰寫階段（如需要）

如果用戶只提供主題或大綱，按以下步驟撰寫：

1. **分析需求**
   - 確定文章類型（分享、介紹、新聞、個人心得）
   - 識別目標受眾
   - 確定發佈目的

2. **撰寫結構**
   ```
   開頭 (1-2 行)
       ↓ 使用表情符號吸引注意
   主要內容 (2-5 段)
       ↓ 清晰的段落分隔
   具體細節或例子 (1-3 段)
       ↓ 提供價值或有趣的資訊
   結尾/行動呼籲 (1-2 行)
       ↓ 個人簽名或相關說明
   ```

3. **內容優化**
   - 檢查表情符號的適當性
   - 確認段落長度（避免過長段落）
   - 驗證信息準確性
   - 確保語氣一致

### 內容確認階段

在自動化前，向用戶展示最終文本並確認：

```
「我準備發佈以下內容，請確認是否有任何更改：

[顯示完整文本]

是否要我繼續發佈？」
```

### 自動化操作階段

#### 步驟 1：驗證瀏覽器狀態

```python
# 使用 tabs_context_mcp 檢查可用標籤
tabs_context_mcp(createIfEmpty=True)

# 拍攝初始截圖
computer(action="screenshot", tabId=current_tab, save_to_disk=True)

# 驗證 Facebook 是否已加載
檢查頁面標題是否包含「Facebook」
```

**期望結果**：
- ✅ 標籤頁面打開且顯示「Facebook」
- ✅ 用戶已登入（能看到個人名稱）

**故障排除**：
- ❌ 若頁面顯示登入畫面 → 指示用戶登入
- ❌ 若頁面加載失敗 → 使用 navigate 重新加載

#### 步驟 2：定位發文輸入框

```python
# 使用 find 工具定位發文輸入框
find(
    query="post text input area what's on your mind",
    tabId=current_tab
)

# 預期返回
# ref_XXX: button/textbox "在想些什麼?" 或類似文本
```

**常見的按鈕標籤**（中文 Facebook）：
- 「在想些什麼?」（完整頻道）
- 「在想些什麼?」（個人頁面）

**可替代搜尋查詢**：
```
"發文框"
"新貼文"
"what's on your mind"
"text input for post"
```

#### 步驟 3：打開發文對話框

```python
# 點擊發文輸入框以打開發文對話
computer(
    action="left_click",
    ref=ref_328,  # 從 find 工具返回的參考 ID
    tabId=current_tab
)

# 等待對話框加載
computer(action="wait", duration=1, tabId=current_tab)

# 確認對話框已打開
computer(action="screenshot", tabId=current_tab, save_to_disk=True)
```

**期望結果**：
- ✅ 出現「建立貼文」對話框
- ✅ 文字輸入區域可見

#### 步驟 4：定位實際的文字輸入框

```python
# 在已打開的對話框中找到文字輸入框
find(
    query="text input field in post dialog",
    tabId=current_tab
)

# 返回應該是 textbox ref
# ref_XXX: textbox "在想些什麼?"
```

#### 步驟 5：輸入文章內容

```python
# 點擊文字輸入框確保焦點在那
computer(
    action="left_click",
    ref=ref_789,  # 文字輸入框的參考 ID
    tabId=current_tab
)

# 輸入完整文本
computer(
    action="type",
    tabId=current_tab,
    text="""🚀 OpenCLI：讓任何網站都成為命令行工具

你有沒有想過，如果能像用命令行一樣簡單地操作...
[完整文本]

💬 這是 Claude Code 發的文"""
)
```

**注意事項**：
- ✅ 文本可以包含換行符（保持格式）
- ✅ 表情符號完全支援
- ✅ 長文本會自動換行

#### 步驟 6：定位並點擊「發佈」按鈕

```python
# 找到發佈按鈕
find(
    query="publish post button",
    tabId=current_tab
)

# 返回應該是按鈕 ref
# ref_XXX: button "發佈"

# 點擊發佈按鈕
computer(
    action="left_click",
    ref=ref_809,  # 發佈按鈕的參考 ID
    tabId=current_tab
)
```

#### 步驟 7：確認發佈成功

```python
# 等待發佈完成（發送到服務器需要 1-2 秒）
computer(action="wait", duration=2, tabId=current_tab)

# 截圖確認文章已出現在時間線上
computer(action="screenshot", tabId=current_tab, save_to_disk=True)

# 驗證成功的指標：
# ✅ 發文對話框已關閉
# ✅ 回到主時間線
# ✅ 新文章出現在頁面頂部
# ✅ 文章包含正確的內容和用戶名
```

### 結果反饋階段

向用戶展示：

```
✨ 發佈成功！

你的文章已發佈到 Facebook 上：

[顯示最終截圖]

文章內容：
🚀 OpenCLI：讓任何網站都成為命令行工具
...

用戶可以在 Facebook 上看到：
- 有多少人可以看到（公開、朋友、指定人員）
- 文章的贊數和留言數
- 分享選項
```

## 常見問題排查表

| 問題 | 症狀 | 解決方案 |
|------|------|--------|
| Chrome 擴展未連接 | 「Chrome extension is not connected」 | 確保 Chrome 已打開並切換到 Claude 標籤 |
| 找不到發文框 | find 工具返回 0 個結果 | 使用 read_page 查看完整結構，或重新整理頁面 |
| 文本未輸入 | 輸入後文框為空 | 等待 1 秒確保焦點在輸入框，重試 type 操作 |
| 發佈按鈕失效 | 按鈕點擊後無反應 | 確認文本框內容完整，檢查是否有驗證錯誤 |
| 發佈超時 | 等待 5 秒後文章未出現 | 手動刷新頁面，檢查是否已發佈，重試發佈 |
| 權限被拒 | 「Permission denied by user」 | 在 Chrome 擴展彈窗中點擊允許或授予權限 |

## 性能最佳實踐

### 優化操作序列

✅ **推薦的操作順序**：
```
1. find() - 定位所有必要元素（快速）
2. computer(wait) - 等待頁面穩定
3. computer(left_click) - 點擊元素
4. computer(wait) - 等待操作完成
5. computer(type) - 輸入文本
6. computer(screenshot) - 驗證結果
```

❌ **避免的操作模式**：
```
- 過多的 screenshot() 呼叫（耗時）
- 連續快速點擊後立即輸入（可能失敗）
- 不等待頁面加載就進行操作
```

### 時序建議

| 操作 | 建議等待時間 | 說明 |
|------|-----------|------|
| 點擊發文框後 | 1 秒 | 讓對話框加載和渲染 |
| 輸入文本後 | 0.5 秒 | 確保所有字符已輸入 |
| 點擊發佈後 | 2 秒 | 讓服務器處理並返回 |
| 讀取頁面前 | 0.5 秒 | 確保 DOM 穩定 |

## 進階技巧

### 處理多語言環境

Facebook 支持多種語言，查詢詞應該適應：

```python
# 中文環境
find(query="在想些什麼", tabId=current_tab)

# 英文環境
find(query="What's on your mind", tabId=current_tab)

# 備用通用查詢
find(query="post text input", tabId=current_tab)
```

### 處理特殊字符

```python
# 正確的方式：直接在 type() 中使用 Unicode
computer(action="type", text="🚀 這是表情符號")

# 長文本的換行處理
text = """第一行
第二行
第三行"""

computer(action="type", text=text)
```

### 錯誤恢復

```python
# 如果某個操作失敗，嘗試重新整理後重試
try:
    # 嘗試原始操作
    find(query="publish button", tabId=current_tab)
except:
    # 重新整理頁面
    navigate(url="https://www.facebook.com/", tabId=current_tab)
    computer(action="wait", duration=2, tabId=current_tab)
    # 重試
    find(query="publish button", tabId=current_tab)
```

## 測試檢查清單

實施前應驗證：

- [ ] Chrome 瀏覽器已安裝 Claude in Chrome 擴展
- [ ] 能夠使用 find 工具定位 Facebook 元素
- [ ] computer 工具能夠執行 left_click 和 type 操作
- [ ] 文本輸入支持表情符號和換行符
- [ ] 發佈流程完整（打開 → 輸入 → 發佈 → 確認）
- [ ] 錯誤情況下有適當的恢復機制

---

**最後更新**：2026 年 4 月  
**文檔版本**：1.0
