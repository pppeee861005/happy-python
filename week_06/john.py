while True:
    user_input = input(">> ").strip()
    
    # 檢查是否結束輸入
    if user_input.lower() == 'q':
        break
    
    try:
        # 以逗號分割字串並轉換為數值
        year, revenue, profit = user_input.split(',')
        year = year.strip()
        revenue = int(revenue.strip())
        profit = int(profit.strip())
        
        # 計算獲利率 (利潤 / 營業額)
        margin = (profit / revenue)
        
        # 存入列表
        data_list.append([year, revenue, profit, margin])
        
    except ValueError:
        print("格式錯誤！請確保輸入三個數值並以逗號隔開（例如：112,1550000,47895）")

# 輸出報表
print(f"\n{'年度':>6} {'營業額':>15} {'利潤':>15} {'獲利率':>10}")
print("=" * 50)

for item in data_list:
    year, rev, pro, mar = item
    # :> 代表靠右對齊，:, 代表加上千分位，:.2% 代表轉換為百分比並取兩位小數
    print(f"{year:>8} {rev:>18,d} {pro:>17,d} {mar:>12.2%}")
