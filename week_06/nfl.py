######################################################################
# Python x ChatGPT
# 提示工程 Prompt Engineering
# [專案]
# 美式足球聯盟(NFL)進攻資料統計分析
# www.kaggle.com/datasets/dtrade84/nfl-offensive-stats-2019-2022
# 問題：
# - 與 AI 助手 (Windsurf, GitHub Copilot, Gemini) 協作編寫程式
# - 程式碼須加入註解，並且包含你對 AI 所下的「提示詞」
# a) 讀取附件檔案：美式足球聯盟(NFL)進攻資料統計表
#    CSV 檔案："nfl_offensive_stats.csv"
# b) 加總資料集中球員 "Aaron Rogers" 所有的傳球碼數。
# c) 將他的數據與那段期間所有四分衛 (QB) 進行比較，
#    依傳球總碼數排序 (由大到小) 後，
#    印出每個四分衛的 "名字：傳球總碼數"。
# d) 將傳球總碼數 (大於 4000 碼者) 統計資料繪製成圖表 (球員：碼數)
#######################################################################
import pandas as pd
import matplotlib.pyplot as plt
import os
# [提示詞]：自動獲取當前檔案所在目錄，確保 read_csv 能正確讀取檔案 (解決 FileNotFoundError)
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "nfl_offensive_stats.csv")
# [提示詞]：讀取 NFL 進攻資料 CSV，並清除欄位名稱前後的空白 (例如將 'position ' 轉為 'position')
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
# --- 任務 (b): Aaron Rodgers 資料統計 ---
# [提示詞]：篩選球員姓名為 "Aaron Rodgers" 的資料，並計算其傳球碼數 (pass_yds) 的總和
aaron_rodgers_data = df[df['player'] == 'Aaron Rodgers']
total_pass_yds_aaron = aaron_rodgers_data['pass_yds'].sum()
print(f"--- 專案分析結果 ---")
print(f"1. Aaron Rodgers 在 2019-2022 間的總傳球碼數為：{total_pass_yds_aaron} 碼")
print("-" * 50)
# --- 任務 (c): QB 比較與排序 ---
# [提示詞]：
# 1. 篩選守備位置 (position) 為 "QB" 的所有資料
# 2. 以球員 (player) 分組並加總傳球碼數
# 3. 依碼數由大到小排序，並印出「名字：碼數」
qb_stats = df[df['position'] == 'QB'].groupby('player')['pass_yds'].sum().reset_index()
qb_stats_sorted = qb_stats.sort_values(by='pass_yds', ascending=False)
print("2. 所有四分衛 (QB) 傳球總碼數排名：")
for index, row in qb_stats_sorted.iterrows():
    print(f"   {row['player']}: {row['pass_yds']} 碼")
# --- 任務 (d): 繪製統計圖表 ---
# [提示詞]：
# 1. 篩選出總傳球碼數大於 4000 碼的頂尖球員
# 2. 繪製水平長條圖 (Horizontal Bar)，設定標題為 "Top NFL QBs (>4000 yds)"
# 3. 圖表顏色設為 'skyblue'，並自動調整版面配置後顯示
top_qbs = qb_stats_sorted[qb_stats_sorted['pass_yds'] > 4000].sort_values(by='pass_yds')
plt.figure(figsize=(10, 8))
plt.barh(top_qbs['player'], top_qbs['pass_yds'], color='skyblue')
plt.xlabel('Total Passing Yards')
plt.ylabel('Quarterback')
plt.title('NFL Quarterbacks with > 4000 Passing Yards (2019-2022)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
# [提示詞]：優化圖表間距並顯示圖表
plt.tight_layout()
plt.show()
