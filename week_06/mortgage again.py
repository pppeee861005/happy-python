loan_amount = float(input("請輸入貸款金額："))
loan_years = float(input("請輸入貸款年限："))
annual_rate = float(input("請輸入年利率(%) 百分之："))

# 計算月利率
monthly_rate = annual_rate / 100 / 12

# 計算總月數
total_months = loan_years * 12

# 計算每月還款金額（使用提供的公式）
# 分子 = 貸款金額 * 月利率
numerator = loan_amount * monthly_rate

# 分母 = 1 - 1/(1 + 月利率)^(貸款年限*12)
denominator = 1 - 1 / (1 + monthly_rate) ** total_months

# 每月還款金額 = 分子 / 分母
monthly_payment = numerator / denominator

# 計算總共還款金額
total_payment = monthly_payment * total_months

# 螢幕輸出
print("每月還款金額：")
print(int(monthly_payment))
print("總共還款金額：")
print(int(total_payment))
