# 📚 Claude Code + OpenCLI 新手學習計劃

**作者：Claude (虛擬CEO)**  
**目標受眾：豪力風神**  
**更新日期：2026-04-13**  
**時間投入：4 週，每週 3-5 小時**

---

## 📋 計劃概覽

| 週次 | 重點 | 時間 | 目標 |
|------|------|------|------|
| **Week 1** | 基礎熟悉 | 5-8 小時 | 安裝 OpenCLI，執行第一個命令 |
| **Week 2** | 核心平台 | 6-10 小時 | 學會 YouTube、Twitter、HackerNews |
| **Week 3** | 實戰應用 | 6-10 小時 | 創建數據蒐集腳本，自動化流程 |
| **Week 4** | 進階應用 | 5-8 小時 | 建立監控系統，數據分析 |

---

## 🎯 學習目標

完成本計劃後，你將能夠：

1. ✅ 熟練使用 Claude Code 的基本操作
2. ✅ 獨立安裝和配置 OpenCLI
3. ✅ 使用 OpenCLI 搜尋和蒐集來自 30+ 平台的數據
4. ✅ 解析 JSON 格式的數據
5. ✅ 創建自動化腳本定時蒐集數據
6. ✅ 用 Claude Code 進行數據分析
7. ✅ 為業務應用做準備

---

# 🔥 第 1 週：基礎熟悉

## 週目標
- 理解 Claude Code 的基本操作
- 安裝 OpenCLI
- 執行第一個 OpenCLI 命令

---

## Day 1-2：Claude Code 基礎操作

### Task 1.1：打開 Claude Code
```
【步驟】
1. 打開你的開發環境（VS Code / Cursor）
2. 確認 Claude Code 已安裝
3. 打開一個新項目或打開現有文件夾

【要點】
- 左側：文件樹（Files）
- 中間：代碼編輯器（Editor）
- 右側：終端（Terminal）
- 底部：面包屑（Breadcrumb）
```

### Task 1.2：創建第一個項目文件夾
```bash
# 在 Claude Code 終端中執行
mkdir ~/opencli-learning
cd ~/opencli-learning
pwd  # 確認當前位置
```

### Task 1.3：熟悉基本終端命令
```bash
# 列出文件
ls
ls -la

# 創建文件夾
mkdir test-folder

# 創建文件
touch test.txt

# 編輯文件（查看內容）
cat test.txt

# 刪除文件
rm test.txt

# 刪除文件夾
rmdir test-folder
```

### ✅ Day 1-2 檢查點
- [ ] Claude Code 能正常打開
- [ ] 能在終端中執行基本命令
- [ ] 理解文件樹和編輯器的用途

---

## Day 3-4：安裝 OpenCLI

### Task 1.4：檢查環境
```bash
# 檢查 Node.js 版本（應該 18+）
node --version

# 檢查 npm 版本（應該 9+）
npm --version

# 如果版本太舊，需要升級
# macOS：brew install node
# Windows：https://nodejs.org/
```

### Task 1.5：安裝 OpenCLI
```bash
# 全局安裝 OpenCLI
npm install -g @jackwener/opencli

# 安裝過程會輸出日誌，等待完成
# 看到 "added X packages" 表示成功
```

### Task 1.6：驗證安裝
```bash
# 檢查版本
opencli --version

# 查看所有可用命令
opencli list

# 應該看到 30+ 個平台的命令列表
# 包括：youtube、twitter、bilibili、zhihu 等
```

### ✅ Day 3-4 檢查點
- [ ] Node.js 版本 18+
- [ ] npm 版本 9+
- [ ] OpenCLI 安裝成功
- [ ] `opencli list` 能執行

---

## Day 5：第一個命令

### Task 1.7：執行最簡單的查詢
```bash
# HackerNews 是最簡單的（不需要瀏覽器登錄）
opencli hackernews top --limit 5

# 應該輸出表格格式的數據：
# ┌─────┬──────────────┬──────────┐
# │ id  │ title        │ score    │
# ├─────┼──────────────┼──────────┤
# │ 1   │ "Title..."   │ 1234     │
# ...
```

### Task 1.8：理解輸出結果
```
【表格說明】
- id：HackerNews 中的帖子 ID
- title：標題
- score：點贊數
- time：發佈時間
- comments：評論數

【重要概念】
這就是 OpenCLI 的核心工作方式：
1. 你給一個命令
2. OpenCLI 控制瀏覽器
3. 抓取數據
4. 返回結構化結果（表格或 JSON）
```

### ✅ Week 1 最終檢查點
- [ ] Claude Code 能正常打開和使用
- [ ] OpenCLI 安裝成功
- [ ] 能執行 `opencli list` 看到命令列表
- [ ] 能執行 `opencli hackernews top` 獲得結果
- [ ] 理解了命令的基本結構

---

# 🚀 第 2 週：核心平台操作

## 週目標
- 學會操作 3 個主要平台：YouTube、Twitter、HackerNews
- 理解 JSON 輸出格式
- 理解命令參數含義

---

## Day 1：HackerNews（最簡單）

### Task 2.1：查看 HackerNews 熱門
```bash
# 基礎命令
opencli hackernews top --limit 10

# 加上參數
opencli hackernews top --limit 20 --sort score
```

### Task 2.2：輸出為 JSON 格式
```bash
# JSON 輸出（更易於機器解析）
opencli hackernews top --limit 10 --format json

# 你應該看到類似這樣的結構：
# [
#   {
#     "id": 123,
#     "title": "...",
#     "score": 1234,
#     "time": "2026-04-13T10:00:00Z",
#     "url": "https://..."
#   },
#   ...
# ]
```

### Task 2.3：保存結果到文件
```bash
# 保存 JSON 結果
opencli hackernews top --limit 10 --format json > hn_top.json

# 檢查文件是否存在
ls -la hn_top.json

# 查看文件內容
cat hn_top.json
```

### Task 2.4：在 Claude Code 中打開文件
```
【操作】
1. 在 Claude Code 左側文件樹中找到 hn_top.json
2. 點擊打開
3. 觀察 JSON 結構

【理解 JSON】
JSON 是結構化數據格式：
- {} 表示對象（object）
- [] 表示數組（array）
- "key": "value" 是鍵值對

【字段含義】
- id：帖子 ID
- title：標題
- score：點贊數
- url：原始 URL
- time：發佈時間
- comments：評論數
```

### ✅ Day 1 檢查點
- [ ] 能查看 HackerNews 熱門
- [ ] 能輸出 JSON 格式
- [ ] 能保存到文件
- [ ] 理解 JSON 結構

---

## Day 2：Twitter/X（需要瀏覽器登錄）

### ⚠️ 前置條件
```
在開始前，確保：
1. 你的 Chrome 已經登錄 Twitter（twitter.com）
2. OpenCLI Browser Extension 已安裝
   - 從 GitHub Releases 下載 opencli-extension.zip
   - 解壓縮
   - chrome://extensions → 開發者模式 → 加載未打包的擴展
   - 選擇解壓縮後的文件夾
```

### Task 2.5：搜尋 Twitter
```bash
# 搜尋 tweets
opencli twitter search "AI voice agents" --limit 10

# 應該看到 tweets 列表
# 包括：作者、內容、點贊數、發佈時間等
```

### Task 2.6：查看 Timeline（你的首頁）
```bash
# 查看你的 Timeline
opencli twitter timeline --limit 20 --format json

# 這會返回你首頁的最新 tweets
```

### Task 2.7：保存結果
```bash
# 搜尋並保存為 JSON
opencli twitter search "Claude AI" --limit 20 --format json > twitter_search.json

# 查看結果
cat twitter_search.json
```

### Task 2.8：分析結果
```
【在 Claude Code 中提問】
我在 Claude Code 的終端中執行了：
opencli twitter search "Claude AI" --limit 5 --format json

結果保存在 twitter_search.json 中

問題：
1. 這個 JSON 代表什麼？
2. 最受歡迎的 tweet 是什麼？
3. 有多少個不同的發言人？
```

**Claude 會幫你解讀結果和提取關鍵信息。**

### ✅ Day 2 檢查點
- [ ] OpenCLI Browser Extension 已安裝
- [ ] Chrome 已登錄 Twitter
- [ ] 能搜尋 Twitter
- [ ] 能保存為 JSON
- [ ] 能用 Claude 分析結果

---

## Day 3：YouTube（需要瀏覽器登錄）

### ⚠️ 前置條件
```
確保：
1. Chrome 已登錄 YouTube（youtube.com）
2. OpenCLI Browser Extension 已安裝
```

### Task 2.9：搜尋 YouTube 視頻
```bash
# 搜尋視頻
opencli youtube search --query "AI tutorial" --limit 10

# 應該看到視頻列表
# 包括：標題、頻道、觀看數、上傳時間等
```

### Task 2.10：保存並分析結果
```bash
# 搜尋並保存
opencli youtube search --query "voice interface" --limit 20 --format json > youtube_search.json

# 查看結果
cat youtube_search.json
```

### Task 2.11：理解 YouTube 數據
```
【YouTube JSON 字段】
- videoId：視頻 ID（用於訪問視頻）
- title：視頻標題
- channel：頻道名稱
- views：觀看次數
- uploadedAt：上傳時間
- url：YouTube 鏈接

【分析要點】
1. 哪個視頻觀看次數最多？
2. 最近上傳的是哪個？
3. 有哪些不同的頻道？
```

### ✅ Day 3 檢查點
- [ ] Chrome 已登錄 YouTube
- [ ] 能搜尋 YouTube
- [ ] 能保存為 JSON
- [ ] 理解 YouTube 數據結構

---

## Day 4-5：多平台組合

### Task 2.12：一次性查詢多個平台
```bash
# 創建文件：multi_platform.sh
cat > multi_platform.sh << 'EOF'
#!/bin/bash

echo "查詢 HackerNews..."
opencli hackernews top --limit 5 --format json > hn_data.json

echo "查詢 Twitter..."
opencli twitter search "AI" --limit 5 --format json > tw_data.json

echo "查詢 YouTube..."
opencli youtube search --query "AI" --limit 5 --format json > yt_data.json

echo "完成！"
EOF

# 執行腳本
bash multi_platform.sh
```

### Task 2.13：用 Claude Code 對比分析
```
【提問】
我收集了 3 個平台的數據：
- hn_data.json（HackerNews 熱門）
- tw_data.json（Twitter 搜尋結果）
- yt_data.json（YouTube 搜尋結果）

問題：
1. 這 3 個平台上 AI 相關的內容熱度如何？
2. 哪個平台更關注 AI 技術？
3. 哪個平台更關注實際應用？
4. 用戶對哪個話題最感興趣？
```

**Claude 會幫你綜合分析多平台數據。**

### ✅ Week 2 最終檢查點
- [ ] 能搜尋 HackerNews、Twitter、YouTube
- [ ] 理解 JSON 格式
- [ ] 能保存結果到文件
- [ ] 能用 Claude 分析多平台數據
- [ ] 理解不同平台的數據特點

---

# 🎓 第 3 週：實戰應用

## 週目標
- 綜合運用多個命令
- 創建自己的數據蒐集腳本
- 用 Claude Code 進行數據分析

---

## Day 1-2：創建數據蒐集腳本

### Task 3.1：創建 Bash 腳本
```bash
# 創建文件：collect_data.sh
cat > collect_data.sh << 'EOF'
#!/bin/bash

# 顏色定義（便於閱讀輸出）
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}開始蒐集數據...${NC}"

# 創建輸出文件夾
mkdir -p data

echo -e "${GREEN}1. 蒐集 HackerNews 數據${NC}"
opencli hackernews top --limit 20 --format json > data/hn_data.json

echo -e "${GREEN}2. 蒐集 Twitter 數據${NC}"
opencli twitter search "AI" --limit 20 --format json > data/tw_data.json

echo -e "${GREEN}3. 蒐集 YouTube 數據${NC}"
opencli youtube search --query "artificial intelligence" --limit 20 --format json > data/yt_data.json

echo -e "${GREEN}4. 蒐集 Reddit 數據${NC}"
opencli reddit hot --subreddit MachineLearning --limit 20 --format json > data/reddit_data.json

echo -e "${YELLOW}數據蒐集完成！${NC}"
echo -e "${YELLOW}文件位置：data/ 文件夾${NC}"

# 顯示統計信息
echo ""
echo "統計信息："
echo "HackerNews 帖子數：$(grep -c '\"id\"' data/hn_data.json)"
echo "Twitter 推文數：$(grep -c '\"id\"' data/tw_data.json)"
echo "YouTube 視頻數：$(grep -c '\"videoId\"' data/yt_data.json)"
echo "Reddit 帖子數：$(grep -c '\"id\"' data/reddit_data.json)"
EOF

# 給腳本添加執行權限
chmod +x collect_data.sh
```

### Task 3.2：執行腳本
```bash
# 運行腳本
bash collect_data.sh

# 你應該看到彩色輸出，顯示進度
# 完成後會顯示統計信息
```

### Task 3.3：檢查生成的文件
```bash
# 查看 data 文件夾中的文件
ls -la data/

# 檢查文件大小（文件越大 = 數據越多）
du -h data/

# 查看某個文件的內容
cat data/hn_data.json | head -20
```

### ✅ Day 1-2 檢查點
- [ ] 能創建 Bash 腳本
- [ ] 腳本能正常執行
- [ ] 生成了 4 個 JSON 文件
- [ ] 理解腳本的邏輯

---

## Day 3：用 Claude Code 分析數據

### Task 3.4：在 Claude Code 中打開文件
```
【操作】
1. 在 Claude Code 左側文件樹中打開 data/ 文件夾
2. 逐個打開 json 文件
3. 觀察各平台數據的結構
```

### Task 3.5：要求 Claude 進行深度分析
```
【提問示例 1：趨勢分析】
我從 4 個平台蒐集了最新數據：
- HackerNews：科技新聞論壇
- Twitter：實時社交媒體
- YouTube：視頻平台
- Reddit：社區討論

問題：
1. 哪些話題在多個平台都很熱？
2. 不同平台的用戶關注點有什麼區別？
3. 如果我要進行市場研究，應該從哪個平台優先獲取信息？

【提問示例 2：競爭分析】
基於這些數據，如果我要宣傳一個 AI 語音產品，應該：
1. 在哪個平台最有效果？
2. 什麼樣的內容最容易獲得關注？
3. 目標受眾是誰？

【提問示例 3：數據質量】
1. 不同平台的數據有什麼特點？
2. 哪些數據可靠性最高？
3. 如何綜合這些數據做決策？
```

### Task 3.6：優化數據和生成報告
```
【讓 Claude 幫你】
1. 提取最重要的 10 個話題
2. 按熱度排序
3. 生成一份簡潔的報告

【報告應該包含】
- 話題排名
- 熱度評分
- 數據來源
- 洞察和建議
```

### ✅ Day 3 檢查點
- [ ] 能在 Claude Code 中打開多個 JSON 文件
- [ ] 能用 Claude 進行數據分析
- [ ] 理解不同平台數據的特點
- [ ] 能生成數據報告

---

## Day 4-5：創建自動化流程

### Task 3.7：設置定時任務（Cron）

**對於 macOS / Linux：**
```bash
# 打開 crontab 編輯器
crontab -e

# 添加以下行：
# 每天早上 9 點運行
0 9 * * * cd ~/opencli-learning && bash collect_data.sh

# 每周一下午 2 點運行
0 14 * * 1 cd ~/opencli-learning && bash collect_data.sh

# 保存並退出（:wq）
```

**對於 Windows：**
```
使用 Task Scheduler：
1. 搜索"任務計劃程序"
2. 創建基本任務
3. 設置觸發器（每天 9 點）
4. 設置操作：執行程序 bash，參數 collect_data.sh
5. 保存
```

### Task 3.8：驗證自動化
```bash
# 檢查 crontab 是否已設置
crontab -l

# 檢查最新的數據文件時間戳
ls -la data/

# 比較文件修改時間，確認是否自動更新
```

### ✅ Week 3 最終檢查點
- [ ] 能創建和執行 Bash 腳本
- [ ] 從 4 個平台自動蒐集數據
- [ ] 用 Claude Code 分析 JSON 數據
- [ ] 能生成數據報告
- [ ] 設置了定時自動執行

---

# 🏆 第 4 週：進階應用

## 週目標
- 建立行業監控系統
- 用 Python 進行數據分析
- 為業務應用做準備

---

## Day 1-2：建立監控系統

### Task 4.1：定義監控主題
```bash
# 創建配置文件：monitor_keywords.txt
cat > monitor_keywords.txt << 'EOF'
# VoiceFlow.ai 相關話題
AI voice agents
conversational AI
speech interface
voice AI
virtual assistant

# 競爭對手相關
Retell AI
voice API
voice interface platform

# 市場趨勢
generative AI
large language model
voice technology
EOF
```

### Task 4.2：創建監控腳本
```bash
# 創建文件：monitor.sh
cat > monitor.sh << 'EOF'
#!/bin/bash

KEYWORDS="AI voice agents|conversational AI|speech interface|voice AI"

mkdir -p monitoring_results

echo "開始監控多個話題..."
echo "監控時間：$(date)"

# 讀取配置文件
while IFS= read -r keyword; do
    # 跳過註釋行
    [[ "$keyword" == "#"* ]] && continue
    [[ -z "$keyword" ]] && continue
    
    echo "監控：$keyword"
    
    # YouTube
    opencli youtube search --query "$keyword" --limit 10 --format json > "monitoring_results/youtube_${keyword// /_}.json"
    
    # Twitter
    opencli twitter search "$keyword" --limit 20 --format json > "monitoring_results/twitter_${keyword// /_}.json"
    
    # HackerNews
    opencli hackernews top --limit 10 --format json >> "monitoring_results/hn_combined.json"
    
done < monitor_keywords.txt

echo "監控完成！結果保存在 monitoring_results/ 文件夾"
EOF

chmod +x monitor.sh
```

### Task 4.3：運行監控
```bash
# 執行監控腳本
bash monitor.sh

# 查看結果
ls -la monitoring_results/

# 檢查某個結果
cat monitoring_results/youtube_AI_voice_agents.json | head -30
```

### ✅ Day 1-2 檢查點
- [ ] 定義了監控關鍵詞
- [ ] 創建了監控腳本
- [ ] 能執行監控並生成結果
- [ ] 結果保存到文件

---

## Day 3：數據存儲和管理

### Task 4.4：創建 Python 分析腳本
```python
# 創建文件：analyze_data.py
import json
import os
from datetime import datetime
from collections import Counter

def load_json_file(filepath):
    """加載 JSON 文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加載 {filepath} 失敗：{e}")
        return []

def analyze_hackernews(data):
    """分析 HackerNews 數據"""
    if not isinstance(data, list):
        data = [data] if data else []
    
    print("\n=== HackerNews 分析 ===")
    print(f"總帖子數：{len(data)}")
    
    if data:
        scores = [item.get('score', 0) for item in data if isinstance(item, dict)]
        print(f"平均分數：{sum(scores) / len(scores) if scores else 0:.2f}")
        print(f"最高分數：{max(scores) if scores else 0}")
        
        # 顯示前 5 個最受歡迎的帖子
        sorted_data = sorted(data, key=lambda x: x.get('score', 0), reverse=True)
        print("\n前 5 個最受歡迎的帖子：")
        for i, item in enumerate(sorted_data[:5], 1):
            print(f"  {i}. {item.get('title', 'N/A')} - 分數：{item.get('score', 0)}")

def analyze_twitter(data):
    """分析 Twitter 數據"""
    if not isinstance(data, list):
        data = [data] if data else []
    
    print("\n=== Twitter 分析 ===")
    print(f"總推文數：{len(data)}")
    
    if data:
        likes = [item.get('likes', 0) for item in data if isinstance(item, dict)]
        print(f"平均點贊數：{sum(likes) / len(likes) if likes else 0:.2f}")
        print(f"最多點贊：{max(likes) if likes else 0}")

def analyze_youtube(data):
    """分析 YouTube 數據"""
    if not isinstance(data, list):
        data = [data] if data else []
    
    print("\n=== YouTube 分析 ===")
    print(f"總視頻數：{len(data)}")
    
    if data:
        channels = [item.get('channel', 'Unknown') for item in data if isinstance(item, dict)]
        print(f"不同頻道數：{len(set(channels))}")
        
        # 頻道熱度排名
        channel_counts = Counter(channels)
        print("\n最活躍的頻道（Top 5）：")
        for channel, count in channel_counts.most_common(5):
            print(f"  - {channel}：{count} 個視頻")

def generate_report():
    """生成綜合報告"""
    print("\n" + "="*50)
    print("數據分析報告")
    print(f"生成時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    
    # 分析 data 文件夾中的所有文件
    data_dir = "data"
    
    if os.path.exists(f"{data_dir}/hn_data.json"):
        hn_data = load_json_file(f"{data_dir}/hn_data.json")
        analyze_hackernews(hn_data)
    
    if os.path.exists(f"{data_dir}/tw_data.json"):
        tw_data = load_json_file(f"{data_dir}/tw_data.json")
        analyze_twitter(tw_data)
    
    if os.path.exists(f"{data_dir}/yt_data.json"):
        yt_data = load_json_file(f"{data_dir}/yt_data.json")
        analyze_youtube(yt_data)
    
    print("\n" + "="*50)
    print("報告完成")
    print("="*50)

if __name__ == "__main__":
    generate_report()
EOF
```

### Task 4.5：執行分析
```bash
# 需要先有數據
bash collect_data.sh

# 然後運行 Python 分析
python3 analyze_data.py

# 你應該看到詳細的分析報告
```

### Task 4.6：查看報告
```
【報告內容包括】
- 每個平台的數據統計
- 熱度排名
- 頻道/作者分析
- 趨勢洞察
```

### ✅ Day 3 檢查點
- [ ] 能創建 Python 分析腳本
- [ ] 腳本能讀取 JSON 文件
- [ ] 能生成統計報告
- [ ] 理解數據分析的基本邏輯

---

## Day 4-5：回顧和計劃

### Task 4.7：總結所學
```markdown
# 創建文件：README.md

# OpenCLI 學習總結

## 什麼是 OpenCLI？
OpenCLI 是一個 AI 原生的命令行工具...

## 我能做什麼？
- 蒐集來自 30+ 平台的數據
- 定時自動監控市場趨勢
- 分析用戶行為和熱點話題
- 為業務決策提供數據支持

## 主要命令
- `opencli hackernews top`：查看科技新聞
- `opencli twitter search`：搜尋推文
- `opencli youtube search`：搜尋視頻

## 文件結構
```
opencli-learning/
├── collect_data.sh      # 數據蒐集腳本
├── monitor.sh          # 監控腳本
├── analyze_data.py     # 分析腳本
├── monitor_keywords.txt # 監控關鍵詞
├── data/               # 蒐集的數據
└── monitoring_results/ # 監控結果
```

## 下一步計劃
- 集成到 n8n 自動化系統
- 連接到 VoiceFlow.ai 儀表板
- 為企業客戶提供實時監控服務
```

### Task 4.8：規劃業務應用
```
【反思問題】
1. OpenCLI 如何幫助 VoiceFlow.ai？
   - 市場監控
   - 競爭分析
   - 客戶需求研究

2. 需要什麼功能？
   - 實時監控
   - 自動報告生成
   - 數據可視化

3. 如何與現有系統集成？
   - n8n 工作流
   - 數據庫存儲
   - API 連接

4. 短期（1 個月）的目標？
   - 建立基本監控系統
   - 生成周報告
   - 識別市場機會

5. 長期（3 個月）的願景？
   - 完整的數據驅動系統
   - 為客戶提供監控服務
   - AI 驅動的洞察引擎
```

### Task 4.9：建立知識庫
```bash
# 將所有文件保存到輸出文件夾
mkdir -p ~/opencli-learning/docs

# 保存你的筆記
# 保存成功案例
# 保存命令參考
# 保存遇到的問題和解決方案

# 最終目錄結構
opencli-learning/
├── Week1/              # 第 1 週筆記
├── Week2/              # 第 2 週筆記
├── Week3/              # 第 3 週筆記
├── Week4/              # 第 4 週筆記
├── scripts/            # 所有腳本文件
├── docs/               # 文檔和參考
└── README.md           # 總結
```

### ✅ Week 4 最終檢查點
- [ ] 能清楚解釋什麼是 OpenCLI
- [ ] 理解了完整的數據流程
- [ ] 有明確的業務應用計劃
- [ ] 建立了可重用的知識庫

---

# 📊 完整學習進度檢查表

## Week 1：基礎熟悉
- [ ] Day 1-2：熟悉 Claude Code 操作
- [ ] Day 3-4：安裝 OpenCLI
- [ ] Day 5：執行第一個命令
- [ ] ✅ 完成度：____%

## Week 2：核心平台
- [ ] Day 1：HackerNews 操作
- [ ] Day 2：Twitter 操作
- [ ] Day 3：YouTube 操作
- [ ] Day 4-5：多平台組合
- [ ] ✅ 完成度：____%

## Week 3：實戰應用
- [ ] Day 1-2：創建蒐集腳本
- [ ] Day 3：數據分析
- [ ] Day 4-5：自動化流程
- [ ] ✅ 完成度：____%

## Week 4：進階應用
- [ ] Day 1-2：建立監控系統
- [ ] Day 3：Python 分析
- [ ] Day 4-5：總結和規劃
- [ ] ✅ 完成度：____%

---

# 🚨 常見問題和解決方案

## Q1：OpenCLI Browser Extension 安裝不成功？
```
【解決方案】
1. 確認已解壓縮到文件夾
2. chrome://extensions 確認開發者模式已啟用
3. 確認 Chrome 版本最新
4. 嘗試禁用其他擴展重新安裝
```

## Q2：`opencli youtube search` 沒有結果？
```
【檢查清單】
1. Chrome 已登錄 YouTube？
2. Browser Extension 已啟用？
3. Chrome 開發者工具沒有錯誤？
4. 嘗試簡化搜尋詞（例如 "AI" 而不是複雜短語）
```

## Q3：JSON 文件很大，怎麼處理？
```
【解決方案】
# 只顯示前 100 行
head -100 large_file.json

# 用 Claude 分析，而不是手動查看
# Claude 能有效處理大型 JSON 文件
```

## Q4：定時任務沒有運行？
```
【調試步驟】
# 檢查 crontab 是否設置正確
crontab -l

# 檢查日誌（macOS）
log stream --predicate 'process == "cron"'

# 手動測試腳本
bash /full/path/to/script.sh
```

---

# 📚 學習資源清單

## 官方文檔
- **OpenCLI GitHub：** https://github.com/jackwener/opencli
- **OpenCLI 命令參考：** https://github.com/jackwener/opencli/blob/main/SKILL.md

## 工具和環境
- **Node.js：** https://nodejs.org/
- **Claude Code：** 在你的編輯器中安裝
- **Chrome：** 需要最新版本

## 學習資源
- Claude Code 官方文檔
- Bash 腳本教程
- JSON 格式介紹
- Python 數據分析基礎

---

# 🎓 完成後的期望成果

完成這 4 週的學習後，你應該能夠：

1. ✅ **獨立操作 OpenCLI**
   - 熟練使用 Claude Code
   - 理解 30+ 平台的命令
   - 解析和分析 JSON 數據

2. ✅ **創建自動化系統**
   - 編寫和執行 Bash 腳本
   - 設置定時任務
   - 監控多個數據源

3. ✅ **數據驅動決策**
   - 用 Python 進行分析
   - 生成數據報告
   - 提取商業洞察

4. ✅ **為業務應用做準備**
   - 理解數據流程
   - 有明確的集成方案
   - 能為客戶提供監控服務

---

# 📝 最後的話

這個計劃設計來幫助你**系統地掌握 Claude Code 和 OpenCLI**。

關鍵是：
- ✅ 每天都要動手實踐（不要只看）
- ✅ 遇到問題時詢問 Claude
- ✅ 記錄你的學習進度和發現
- ✅ 定期回顧和總結

**祝你學習順利！** 🚀

---

**文件生成日期：2026-04-13**  
**作者：Claude (Virtual CEO)**  
**為：豪力風神**
