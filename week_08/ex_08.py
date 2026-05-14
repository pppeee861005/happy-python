############################################################
# Python x ChatGPT
# import, loop, conditionals - 條件式、迴圈與隨機數
# [作業一]
# 遊戲：猜數字
# A)玩家猜數字：
#   1)提示要求輸入猜測數字的範圍上限
#   2)電腦隨機產生 1~上限 間的任一整數
#   3)提示要求玩家輸入猜測的數字
#     "猜一個 1-{上限} 間的數字: "
#   4)如果所猜數字 < 電腦隨機數：
#       輸出："太小了！請再猜個數字"
#     如果所猜數字 > 電腦隨機數：
#       輸出："太大了！請再猜個數字"
#   5)重複步驟 4) 直到猜對為止，並輸出：
#     "恭喜你猜對了秘密數字 {隨機數} !!"
# B)電腦猜數字：
#   1)提示要求輸入猜測數字的上限
#   2)提示玩家自行選定 1~上限 間的任一整數並記住
#   3)電腦輸出 (提示要求玩家比較並輸入正確與否)：
#     "我猜 {隨機數字}，太高(H)/太低(L) 或 正確(C)?? "
#   4)電腦依據玩家輸入的線索縮小猜測範圍，
#     並重複步驟 3) 直到猜對為止
#   5)輸出：
#     "耶~ 電腦猜對了你的秘密 {正確數字} !!"
############################################################
import random

def guess(x):
    """
    玩家指定數字上限，並與電腦互動猜測其隨機產生的數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    # 2) 電腦隨機產生 1~上限 間的任一整數
    random_number = random.randint(1, x)
    guess_num = 0
    
    # 5) 重複步驟 4 直到猜對為止
    while guess_num != random_number:
        # 3) 提示要求玩家輸入猜測的數字
        guess_num = int(input(f"猜一個 1-{x} 間的數字: "))
        
        # 4) 判斷大小
        if guess_num < random_number:
            print("太小了！請再猜個數字")
        elif guess_num > random_number:
            print("太大了！請再猜個數字")
            
    print(f"恭喜你猜對了秘密數字 {random_number} !!")


def computer_guess(x):
    """
    玩家選定數字，並與電腦互動，由電腦猜測此數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    low = 1
    high = x
    feedback = ""
    
    # 2) 提示玩家自行選定數字
    print(f"請在心中想好一個 1-{x} 之間的數字，我會嘗試猜出來！")
    
    # 4) 電腦依據線索縮小範圍，重複直到猜對
    while feedback != 'c':
        if low != high:
            # 電腦隨機從目前範圍內挑選一個數字
            guess_num = random.randint(low, high)
        else:
            # 如果範圍縮小到只剩下一個點，那肯定就是它了
            guess_num = low 
            
        # 3) 電腦輸出並要求玩家輸入線索
        feedback = input(f"我猜 {guess_num}，太高(H)/太低(L) 或 正確(C)?? ").lower()
        
        if feedback == 'h':
            high = guess_num - 1
        elif feedback == 'l':
            low = guess_num + 1
            
    # 5) 輸出結果
    print(f"耶~ 電腦猜對了你的秘密 {guess_num} !!")

# 測試執行
limit = int(input("請輸入猜測數字的上限: "))
guess(limit)
computer_guess(limit)
###########################################################
# Python x ChatGPT
# Datetime & loop 日期模組與迴圈應用
# [作業二]
# 選擇性刪減檔案
# 問題：針對每天永無止境的資料檔，儲存空間實在不足，決定
# 對超過30天的檔案，僅保留星期二收到的檔案，其餘刪除。
# 已知：
#       1)串列 archive 如下，內存所有檔案的名稱
#       2)檔案名稱為字串(是以接收日期命名的壓縮檔)
# 輸出：
#       印出串列，內含：
#       超過30天、且不是星期二收到的檔案名稱明細
#
# (提示)：datetime物件.weekday() 會取得接收日是星期幾
#         (週一是0，週日是6)
############################################################
from datetime import datetime, timedelta

archive = [
    '2024-07-05.zip', '2024-07-16.zip', '2024-07-24.zip',
    '2024-08-06.zip', '2024-08-14.zip', '2024-08-20.zip',
    '2024-09-04.zip', '2024-09-12.zip', '2024-09-24.zip',
    '2024-10-01.zip', '2024-10-15.zip', '2024-10-25.zip'
]

# 假設今天的日期（為了配合範例資料，我們設在 2024-10-31）
# 實際使用時可以用 datetime.now()
today = datetime(2024, 10, 31)
to_delete = []

for file_name in archive:
    # 1. 取得日期字串 (去掉 .zip) 並轉換成 datetime 物件
    # strptime 可以將字串轉換為日期物件
    date_str = file_name.replace('.zip', '')
    file_date = datetime.strptime(date_str, '%Y-%m-%d')    
    # 2. 計算天數差距
    days_diff = (today - file_date).days
    # 3. 判斷星期幾 (週二在 weekday() 中是 1)
    day_of_week = file_date.weekday()
    # 4. 條件判斷：超過 30 天 且 不是星期二
    if days_diff > 30 and day_of_week != 1:
        to_delete.append(file_name)
# 輸出結果
print("待刪除檔案明細：")
print(to_delete)


