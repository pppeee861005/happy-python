# 社群媒體自動化發文工作流

## 📋 概述
使用 Claude computer use 工具自動化發佈貼文到 Facebook 和 X（Twitter）平台。此工作流已在 2025-04-14 驗證成功。

---

## 🚀 快速開始

### 工作流步驟
```
1. 初始化瀏覽器標籤 (tabs_context_mcp)
   ↓
2. 建立新標籤或切換至目標平台
   ↓
3. 導航至平台 URL (navigate)
   ↓
4. 等待頁面載入 (wait + screenshot)
   ↓
5. 確認已登入
   ↓
6. 尋找發文元素 (find)
   ↓
7. 點擊發文按鈕 (computer: left_click)
   ↓
8. 輸入內容 (computer: type)
   ↓
9. 檢查限制 (字數、媒體等)
   ↓
10. 點擊發佈按鈕 (computer: left_click)
   ↓
11. 驗證成功 (wait + screenshot)
```

---

## 📱 Facebook 發文流程

### 環境準備
- 平台 URL: `facebook.com`
- 需要登入狀態
- 發文框文字: 「在想些什麼？」

### 技術實現步驟

#### 1. 初始化標籤
```javascript
// 取得或建立標籤
await tabs_context_mcp({ createIfEmpty: true })
// 返回: { availableTabs: [...], tabGroupId: ... }
```

#### 2. 導航到 Facebook
```javascript
await navigate({
  tabId: <tab_id>,
  url: "facebook.com"
})
```

#### 3. 等待頁面載入
```javascript
await computer({
  action: "wait",
  tabId: <tab_id>,
  duration: 3
})
```

#### 4. 找發文框
```javascript
await find({
  query: "在想些什麼 發文框",
  tabId: <tab_id>
})
// 返回: ref_XXX (發文按鈕)
```

#### 5. 點擊開啟發文對話框
```javascript
await computer({
  action: "left_click",
  ref: "ref_XXX",  // 發文框按鈕
  tabId: <tab_id>
})
```

#### 6. 等待對話框打開
```javascript
await computer({
  action: "wait",
  tabId: <tab_id>,
  duration: 2
})
```

#### 7. 找文字輸入框
```javascript
await find({
  query: "文字輸入框 在想些什麼",
  tabId: <tab_id>
})
// 返回: ref_XXX (實際輸入框)
```

#### 8. 輸入內容
```javascript
await computer({
  action: "left_click",
  ref: "ref_XXX",
  tabId: <tab_id>
})

await computer({
  action: "type",
  tabId: <tab_id>,
  text: `同學們來學 opencli 吧！這是我的學習筆記庫，歡迎參考：
https://github.com/pppeee861005/opencli-learning`
})
```

#### 9. 找發佈按鈕
```javascript
await find({
  query: "發佈 按鈕",
  tabId: <tab_id>
})
// 返回: ref_XXX (發佈按鈕)
```

#### 10. 點擊發佈
```javascript
await computer({
  action: "left_click",
  ref: "ref_XXX",
  tabId: <tab_id>
})
```

#### 11. 驗證成功
```javascript
// 等待處理
await computer({
  action: "wait",
  tabId: <tab_id>,
  duration: 3
})

// 截圖確認
await computer({
  action: "screenshot",
  tabId: <tab_id>,
  save_to_disk: true
})
// 檢查是否看到新貼文
```

### Facebook 發文結果
✅ 貼文內容正確顯示
✅ GitHub URL 自動展開成卡片預覽
✅ 顯示發文者名稱、時間、互動按鈕

---

## 𝕏 X (Twitter) 發文流程

### 環境準備
- 平台 URL: `x.com`
- 需要登入狀態
- 字數限制: **280 字元**
- 發文按鈕位置: 左側導航欄

### 技術實現步驟

#### 1. 建立新標籤
```javascript
await tabs_create_mcp()
// 返回: { tabId: <new_tab_id> }
```

#### 2. 導航到 X
```javascript
await navigate({
  tabId: <tab_id>,
  url: "x.com"
})
```

#### 3. 等待頁面載入
```javascript
await computer({
  action: "wait",
  tabId: <tab_id>,
  duration: 3
})
```

#### 4. 找發文按鈕
```javascript
await find({
  query: "發文 按鈕 左側",
  tabId: <tab_id>
})
// 返回: ref_XXX (發佈按鈕連結)
```

#### 5. 點擊發文按鈕
```javascript
await computer({
  action: "left_click",
  ref: "ref_XXX",
  tabId: <tab_id>
})
// 導航至 /compose/post
```

#### 6. 等待發文對話框打開
```javascript
await computer({
  action: "wait",
  tabId: <tab_id>,
  duration: 2
})
```

#### 7. 找文字輸入框
```javascript
await find({
  query: "有什麼新鮮事 文字輸入框",
  tabId: <tab_id>
})
// 返回: ref_XXX (發文文字框)
```

#### 8. 輸入內容
```javascript
await computer({
  action: "left_click",
  ref: "ref_XXX",
  tabId: <tab_id>
})

await computer({
  action: "type",
  tabId: <tab_id>,
  text: `同學們來學 opencli 吧！這是我的學習筆記庫，歡迎參考：
https://github.com/pppeee861005/opencli-learning`
})
```

#### 9. 檢查字數 ⭐ 重要
```javascript
// 使用 JavaScript 檢查實際字數
await javascript_tool({
  action: "javascript_exec",
  tabId: <tab_id>,
  text: `
const textElement = document.querySelector('[data-testid="tweetTextarea_0"]');
if (textElement) {
  const text = textElement.innerText || textElement.textContent;
  const charCount = text.length;
  charCount <= 280 ? '✅ 字數 OK: ' + charCount : '❌ 超過限制: ' + charCount;
} else {
  const allDivs = document.querySelectorAll('div[contenteditable="true"]');
  if (allDivs.length > 0) {
    const text = allDivs[0].innerText;
    text.length + ' 字元';
  } else {
    '找不到文字框';
  }
}
  `
})
```

**本次測試結果:** 80 字元 ✅ (遠低於 280 字元)

#### 10. 找發佈按鈕
```javascript
await find({
  query: "發佈 按鈕",
  tabId: <tab_id>
})
// 對於 X，通常在對話框右下方
```

#### 11. 點擊發佈
```javascript
await computer({
  action: "left_click",
  ref: "ref_XXX",
  tabId: <tab_id>
})
```

#### 12. 驗證成功
```javascript
// 等待處理
await computer({
  action: "wait",
  tabId: <tab_id>,
  duration: 3
})

// 頁面應回到首頁，看到「已發佈」提示
await computer({
  action: "screenshot",
  tabId: <tab_id>,
  save_to_disk: true
})

// 向上滾動找新貼文
await computer({
  action: "scroll",
  coordinate: [465, 400],
  scroll_direction: "up",
  scroll_amount: 5,
  tabId: <tab_id>
})
```

### X 發文結果
✅ 貼文內容正確顯示
✅ 發文者 @huang23999
✅ GitHub URL 自動展開成卡片預覽
✅ 字數驗證: 80/280 ✅

---

## 🔑 核心工具參考

### tabs_context_mcp
```javascript
{
  createIfEmpty: true  // 若無標籤群組，自動建立新視窗
}
// 返回: { availableTabs: [...], tabGroupId: ... }
```

### find
```javascript
{
  query: string,       // 自然語言描述
  tabId: number       // 標籤 ID
}
// 返回: { ref_XXX: "Element description" }
```

### computer
```javascript
{
  action: "left_click" | "type" | "screenshot" | "wait" | "scroll" | ...,
  tabId: number,
  ref?: string,        // 從 find 或 read_page 取得
  coordinate?: [x, y], // 絕對座標
  text?: string,       // type 或 key 時使用
  duration?: number    // wait 時使用 (秒)
}
```

### navigate
```javascript
{
  tabId: number,
  url: string  // 不需要 https://, 自動補上
}
```

---

## ⚠️ 常見問題 & 解決方案

### 問題 1: 找不到發文框
**原因:** 頁面尚未完全載入
**解決:** 增加 wait 時間 (3-5 秒)
```javascript
await computer({ action: "wait", duration: 5, tabId })
```

### 問題 2: 字數超過限制 (X 平台)
**原因:** 貼文內容過長
**解決:** 在發佈前檢查字數
```javascript
// 建議使用上述 JavaScript 檢查方案
// 若超過 280，則縮短內容或移除換行
```

### 問題 3: 貼文框未激活 (contenteditable 元素)
**原因:** X 使用 div[contenteditable=true]，不是標準 textarea
**解決:** 使用 triple_click 或 key ctrl+a 後重新輸入
```javascript
await computer({
  action: "triple_click",
  ref: "ref_XXX",
  tabId
})
await computer({
  action: "type",
  text: "新內容",
  tabId
})
```

### 問題 4: 多標籤管理
**原因:** 開啟多個標籤時容易混淆
**解決:** 使用 tabId 變數追蹤
```javascript
const facebookTabId = 44578543;
const xTabId = 44578557;
// 明確指定每個操作的 tabId
```

---

## 📊 成功指標

### Facebook 成功標誌
- ✅ 貼文出現在首頁時間軸
- ✅ 顯示正確的發文者名稱
- ✅ GitHub 連結自動展開為卡片
- ✅ 可見完整的互動按鈕 (讚、留言、分享)

### X 成功標誌
- ✅ 回到首頁，看到「已發佈」提示
- ✅ 向上滾動可看到新貼文
- ✅ 字數檢查: ≤ 280 字元
- ✅ GitHub 連結自動展開為卡片
- ✅ 發文者顯示為登入帳號

---

## 🔄 批量發文策略

### 多平台同時發佈
```javascript
// 1. 同時建立兩個標籤
const facebookTab = await tabs_create_mcp();
const xTab = await tabs_create_mcp();

// 2. 平行導航
await navigate({ tabId: facebookTab, url: "facebook.com" });
await navigate({ tabId: xTab, url: "x.com" });

// 3. 等待兩者載入
await Promise.all([
  computer({ action: "wait", duration: 3, tabId: facebookTab }),
  computer({ action: "wait", duration: 3, tabId: xTab })
]);

// 4. 分別發佈
// ... Facebook 流程 ...
// ... X 流程 ...
```

### 內容自適應
```javascript
// Facebook: 無字數限制，支援完整內容
const facebookContent = "同學們來學 opencli 吧！...(完整)";

// X: 需檢查 280 字限制，可能需要縮短
const xContent = "同學們來學 opencli 吧！這是我的學習筆記庫，歡迎參考：\nhttps://github.com/pppeee861005/opencli-learning";
// 字數: 80 ✅
```

---

## 📈 未來優化方向

1. **自動化排程發佈** - 使用時間戳記排程貼文
2. **內容管理庫** - 建立預設模板庫 (行銷、產品、企業新聞等)
3. **跨平台統計** - 記錄發佈數據、互動率
4. **多語言支援** - 自動轉譯內容為不同語言
5. **媒體上傳** - 自動上傳圖片、影片、GIF
6. **主題標籤智能生成** - 根據內容自動建議相關主題標籤

---

## 📝 測試紀錄

### 2025-04-14 驗證
- ✅ Facebook 貼文發佈成功
- ✅ X (Twitter) 貼文發佈成功  
- ✅ GitHub URL 自動展開
- ✅ 字數檢查: 80/280 ✅
- ✅ 多標籤管理: 正常運作

---

## 🎯 快速複製範本

### 發佈到 Facebook
```javascript
// 初始化
const ctx = await tabs_context_mcp({ createIfEmpty: true });
const tabId = ctx.availableTabs[0].tabId;

// 導航
await navigate({ tabId, url: "facebook.com" });
await computer({ action: "wait", duration: 3, tabId });

// 發文
const postBtn = await find({ query: "在想些什麼", tabId });
await computer({ action: "left_click", ref: postBtn, tabId });
await computer({ action: "wait", duration: 2, tabId });

const textBox = await find({ query: "文字輸入框", tabId });
await computer({ action: "left_click", ref: textBox, tabId });
await computer({ action: "type", text: "貼文內容", tabId });

const publishBtn = await find({ query: "發佈", tabId });
await computer({ action: "left_click", ref: publishBtn, tabId });
await computer({ action: "wait", duration: 3, tabId });

// 驗證
await computer({ action: "screenshot", tabId, save_to_disk: true });
```

### 發佈到 X (Twitter)
```javascript
// 建立新標籤
const newTab = await tabs_create_mcp();

// 導航
await navigate({ tabId: newTab, url: "x.com" });
await computer({ action: "wait", duration: 3, tabId: newTab });

// 發文
const postBtn = await find({ query: "發文", tabId: newTab });
await computer({ action: "left_click", ref: postBtn, tabId: newTab });
await computer({ action: "wait", duration: 2, tabId: newTab });

const textBox = await find({ query: "有什麼新鮮事", tabId: newTab });
await computer({ action: "left_click", ref: textBox, tabId: newTab });
await computer({ action: "type", text: "貼文內容", tabId: newTab });

// 檢查字數 (280 限制)
const charCheck = await javascript_tool({
  action: "javascript_exec",
  tabId: newTab,
  text: "document.querySelector('[data-testid=\"tweetTextarea_0\"]').textContent.length"
});

const publishBtn = await find({ query: "發佈", tabId: newTab });
await computer({ action: "left_click", ref: publishBtn, tabId: newTab });
await computer({ action: "wait", duration: 3, tabId: newTab });

// 驗證
await computer({ action: "scroll", coordinate: [465, 400], scroll_direction: "up", scroll_amount: 5, tabId: newTab });
await computer({ action: "screenshot", tabId: newTab, save_to_disk: true });
```

---

**最後更新:** 2025-04-14
**驗證狀態:** ✅ 已驗證兩平台成功發佈
**維護者:** Claude AI + 豪力風神
