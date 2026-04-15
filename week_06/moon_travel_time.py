# 計算地球航行到月球所需時間

# 定義常數
MACH_SPEED = 1225  # 一馬赫 = 每小時1225公里
DISTANCE_TO_MOON = 384400  # 地球到月球距離（公里）

# 計算所需的總小時數
total_hours = DISTANCE_TO_MOON / MACH_SPEED

# 轉換為天數和小時數
days = int(total_hours // 24)  # 整數除法得到天數
hours = int(total_hours % 24)   # 取餘數得到剩餘小時數

# 螢幕輸出
print("總共需要天數")
print(days)
print("小時數")
print(hours)