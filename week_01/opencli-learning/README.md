# 🚀 OpenCLI 學習計劃

> **OpenCLI 是什麼？** 一個 AI 原生的命令行工具，可以把 Bilibili、知乎、Twitter、Reddit、HackerNews 等 70+ 個網站變成命令行界面。

這是一份**系統化的 4 週學習計劃**，帶你從零開始掌握 OpenCLI，最終能夠獨立構建數據蒐集和監控系統。

---

## 📊 學習概覽

| 週次 | 重點 | 時間 | 目標 |
|------|------|------|------|
| **Week 1** | 基礎熟悉 | 5-8 小時 | 安裝 OpenCLI，執行第一個命令 |
| **Week 2** | 核心平台 | 6-10 小時 | 學會 YouTube、Twitter、HackerNews |
| **Week 3** | 實戰應用 | 6-10 小時 | 創建數據蒐集腳本，自動化流程 |
| **Week 4** | 進階應用 | 5-8 小時 | 建立監控系統，數據分析 |

**總投入時間：** 4 週，每週 3-5 小時

---

## 🎯 完成後你能做什麼？

✅ 熟練使用 Claude Code 的基本操作  
✅ 獨立安裝和配置 OpenCLI  
✅ 使用 OpenCLI 搜尋和蒐集來自 30+ 平台的數據  
✅ 解析 JSON 格式的數據  
✅ 創建自動化腳本定時蒐集數據  
✅ 用 Claude Code 進行數據分析  
✅ 為業務應用做準備  

---

## 📖 計劃結構

### 第 1 週：基礎熟悉 🔥

**目標：** 安裝 OpenCLI，執行第一個命令

**內容：**
- Day 1-2：Claude Code 基礎操作
- Day 3-4：安裝 OpenCLI
- Day 5：執行第一個 HackerNews 命令

**關鍵成果：**
- 能正常打開 Claude Code
- OpenCLI 安裝成功
- 能執行 `opencli list` 看到命令列表
- 能執行 `opencli hackernews top` 獲得結果

---

### 第 2 週：核心平台操作 🚀

**目標：** 學會操作 3 個主要平台

**內容：**
- Day 1：HackerNews（最簡單，不需要登錄）
- Day 2：Twitter/X（需要瀏覽器登錄 + 安裝 Browser Extension）
- Day 3：YouTube（需要瀏覽器登錄 + 安裝 Browser Extension）
- Day 4-5：多平台組合查詢

**關鍵命令：**
```bash
# HackerNews
opencli hackernews top --limit 10 --format json

# Twitter
opencli twitter search "AI voice agents" --limit 10

# YouTube
opencli youtube search --query "AI tutorial" --limit 10
```

**關鍵成果：**
- 能搜尋 HackerNews、Twitter、YouTube
- 理解 JSON 格式
- 能保存結果到文件
- 能用 Claude 分析多平台數據

---

### 第 3 週：實戰應用 🎓

**目標：** 綜合運用多個命令，創建自動化系統

**內容：**
- Day 1-2：創建 Bash 數據蒐集腳本
- Day 3：用 Claude Code 進行數據分析
- Day 4-5：設置定時自動執行（crontab）

**關鍵腳本：**
```bash
# 一次性蒐集多個平台數據
bash collect_data.sh

# 分析蒐集的數據
python3 analyze_data.py

# 設置定時任務
crontab -e
```

**關鍵成果：**
- 能創建和執行 Bash 腳本
- 從 4 個平台自動蒐集數據
- 用 Claude Code 分析 JSON 數據
- 能生成數據報告
- 設置了定時自動執行

---

### 第 4 週：進階應用 🏆

**目標：** 建立行業監控系統，為業務應用做準備

**內容：**
- Day 1-2：定義監控主題，創建監控腳本
- Day 3：Python 數據分析和報告生成
- Day 4-5：總結與規劃業務應用

**關鍵應用：**
- 市場趨勢監控
- 競爭對手分析
- 客戶需求研究
- 實時數據驅動決策

**關鍵成果：**
- 能清楚解釋什麼是 OpenCLI
- 理解了完整的數據流程
- 有明確的業務應用計劃
- 建立了可重用的知識庫

---

## 🔧 前置要求

### 必需的軟件
- **Node.js** 18+ （[下載](https://nodejs.org/)）
- **npm** 9+ （通常隨 Node.js 一起安裝）
- **Chrome 瀏覽器**（用於 OpenCLI）
- **開發環境**：VS Code、Cursor 或 Claude Code

### 必需的帳戶（Week 2+）
- **Twitter/X** 帳號（並已登錄 Chrome）
- **YouTube** 帳號（並已登錄 Chrome）
- **Chrome 開發者工具** 基礎知識

---

## 🚀 快速開始

### 1️⃣ 安裝 OpenCLI

```bash
# 檢查環境
node --version   # 應該 18+
npm --version    # 應該 9+

# 全局安裝 OpenCLI
npm install -g @jackwener/opencli

# 驗證安裝
opencli --version
opencli list
```

### 2️⃣ 執行第一個命令

```bash
# HackerNews（最簡單，不需要登錄）
opencli hackernews top --limit 5

# 應該看到表格格式的數據
```

### 3️⃣ 輸出為 JSON

```bash
opencli hackernews top --limit 5 --format json

# 保存到文件
opencli hackernews top --limit 10 --format json > data.json
```

---

## 📚 文件結構

```
opencli-learning/
├── README.md                    # 本文件
├── LEARNING_PLAN.md             # 完整學習計劃
├── Week1/                       # 第 1 週筆記
│   ├── Day1-2-setup.md
│   └── Day5-first-command.md
├── Week2/                       # 第 2 週筆記
│   ├── hackernews.md
│   ├── twitter.md
│   └── youtube.md
├── Week3/                       # 第 3 週筆記
│   ├── collect_data.sh
│   ├── analyze_data.py
│   └── automation.md
├── Week4/                       # 第 4 週筆記
│   ├── monitor.sh
│   ├── business-application.md
│   └── knowledge-base.md
└── data/                        # 蒐集的數據
    ├── hn_data.json
    ├── tw_data.json
    └── yt_data.json
```

---

## 🎯 每週目標

### Week 1：基礎熟悉 ✅
- [ ] Claude Code 能正常打開和使用
- [ ] OpenCLI 安裝成功
- [ ] 能執行 `opencli list` 看到命令列表
- [ ] 能執行 `opencli hackernews top` 獲得結果
- [ ] 理解了命令的基本結構

### Week 2：核心平台 🚀
- [ ] 能搜尋 HackerNews、Twitter、YouTube
- [ ] 理解 JSON 格式
- [ ] 能保存結果到文件
- [ ] 能用 Claude 分析多平台數據
- [ ] 理解不同平台的數據特點

### Week 3：實戰應用 🎓
- [ ] 能創建和執行 Bash 腳本
- [ ] 從 4 個平台自動蒐集數據
- [ ] 用 Claude Code 分析 JSON 數據
- [ ] 能生成數據報告
- [ ] 設置了定時自動執行

### Week 4：進階應用 🏆
- [ ] 能清楚解釋什麼是 OpenCLI
- [ ] 理解了完整的數據流程
- [ ] 有明確的業務應用計劃
- [ ] 建立了可重用的知識庫

---

## 🔗 OpenCLI 官方資源

- **GitHub：** https://github.com/jackwener/opencli
- **官方命令參考：** https://github.com/jackwener/opencli/blob/main/SKILL.md
- **Node.js 官方文檔：** https://nodejs.org/
- **Chrome Developer Tools：** https://developer.chrome.com/docs/devtools/

---

## 📚 推薦學習資源

### CLI 相關
- Bash 腳本基礎教程
- 命令行工具最佳實踐
- Shell 編程指南

### 數據相關
- JSON 格式介紹
- Python 數據分析基礎
- 數據可視化入門

### 自動化相關
- Cron 定時任務使用
- 系統監控和告警
- 日誌管理最佳實踐

---

## 🤝 貢獻

如果你在學習過程中有改進建議、發現錯誤或想分享你的學習筆記，歡迎提交 Pull Request！

**貢獻方式：**
1. Fork 本倉庫
2. 創建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改動 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

---

## 💡 常見問題

### Q1：OpenCLI Browser Extension 安裝不成功？
A：確認已解壓縮到文件夾，在 `chrome://extensions` 確認開發者模式已啟用，Chrome 版本最新，或嘗試禁用其他擴展重新安裝。

### Q2：`opencli youtube search` 沒有結果？
A：檢查清單：Chrome 已登錄 YouTube、Browser Extension 已啟用、Chrome 開發者工具沒有錯誤、嘗試簡化搜尋詞。

### Q3：JSON 文件很大，怎麼處理？
A：用 `head -100 large_file.json` 只顯示前 100 行，或用 Claude 分析，Claude 能有效處理大型 JSON 文件。

### Q4：定時任務沒有運行？
A：檢查 `crontab -l` 是否設置正確，檢查日誌（macOS：`log stream --predicate 'process == "cron"'`），手動測試腳本。

---

## 📝 學習建議

✅ **每天都要動手實踐**（不要只看）  
✅ **遇到問題時詢問 Claude 或查文檔**  
✅ **記錄你的學習進度和發現**  
✅ **定期回顧和總結**  
✅ **分享你的成果和經驗**  

---

## 📄 許可證

本項目採用 MIT 許可證。詳見 [LICENSE](LICENSE) 文件。

---

## 👨‍💻 作者

**Created by:** Claude (Virtual CEO)  
**For:** 豪力風神  
**Updated:** 2026-04-14

---

## 🙏 致謝

感謝 OpenCLI 的開發者 [@jackwener](https://github.com/jackwener)  
感謝 Claude 提供的虛擬 CEO 服務  
感謝所有貢獻者和學習者的反饋

---

## 📞 聯繫方式

有問題或建議？
- 📧 提交 GitHub Issue
- 💬 發起 Discussion
- 🤝 歡迎 Pull Request

---

**祝你學習順利！** 🚀

如果這個計劃對你有幫助，請給個 ⭐ Star 支持一下！
