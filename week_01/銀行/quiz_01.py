##################################################################
# 隨堂練習
##################################################################
# Python x ChatGPT
#
# [練習一]
# 設計程式可以：
#   1) 要求使用者輸入下列三行資料
#   2) 印出所取得的這三樣資料
#
# (螢幕輸入)
#   你的大名： (name)
#   你的年紀： (age)
#   來自哪裡： (city)
#
# (螢幕輸出)
#   來自 (city), (age) 歲的 (name), Python 歡迎您！
##################################################################

name = input("請輸入您的大名：")
age  = input("請輸入您的年齡：")
city = input("請輸入您來自哪裡：")

print(f"來自 {city}, {age} 歲的 {name}, Python 歡迎您！")

print("=" * 50)

##################################################################
# Python x ChatGPT
#
# [練習二]
#   1) 開了咖啡店，我們在 Facebook 投放廣告，要給兩千人曝光。
#      假設轉化率為 5%，轉化後的平均消費為 150 元，
#      來算算看廣告成效吧！
#   2) 改動各種數字組合看看會有甚麼變化？
#
# (螢幕輸出)
#   廣告成效：$$$$ (計算結果)
##################################################################

# --- (1) 固定數值示範 ---
impressions     = 2000   # 曝光人數
conversion_rate = 0.05   # 轉化率 (5%)
average_spend   = 150    # 平均消費額（元）

total_revenue = impressions * conversion_rate * average_spend
print(f"(1) 廣告成效：{total_revenue} 元")

print("=" * 50)

# --- (2) 互動式輸入 ---
impressions        = int(input("請輸入曝光人數："))
conv_rate_percent  = float(input("請輸入預期轉化率（例如 5 代表 5%）："))
average_spend      = float(input("請輸入顧客平均消費額（元）："))

total_revenue = impressions * (conv_rate_percent / 100) * average_spend
print(f"(2) 預估廣告成效：{total_revenue} 元")
