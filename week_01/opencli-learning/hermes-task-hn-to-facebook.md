# 任務書：HackerNews 每日精選 → 自動發文到 Facebook

**給：Hermes Agent**
**建議模型：**
- 🥇 首選：`anthropic/claude-opus-4-6`（推理最強，agentic 任務最穩）
- 🥈 次選：`anthropic/claude-sonnet-4-6`（速度快，能力接近 Opus）
- 🥉 備選：`deepseek/deepseek-v3-2`（成本低，適合測試）
- ❌ 避免：`google/gemini-3-flash-preview`（Flash 系列不適合複雜多步驟任務）
**日期：2026-04-14**

---

## 任務

從 HackerNews 抓取今日熱門文章 Top 1，整理成貼文，自動發到 Facebook，並設定每日定時執行。

---

## 環境

- 系統：Windows，Shell 為 bash
- 工作目錄：`D:\gameplace\code第三學期初階\week_01\opencli-learning\`
- `opencli` 已全域安裝
- Chrome 已登入 facebook.com，介面語言為中文

---

## 成功標準

- [ ] Facebook 動態牆出現今日 HN Top 5 貼文
- [ ] 每天 09:00 自動執行
- [ ] 有執行記錄可查

---

## 限制

- 不翻譯英文標題，保留原文
- 失敗超過 2 次請停止並回報原因
- 不關閉 Chrome 其他分頁
