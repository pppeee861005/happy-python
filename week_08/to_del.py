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