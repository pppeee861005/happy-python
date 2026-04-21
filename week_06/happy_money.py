def computepay(hours, rate):
    """
    計算總工資：
    - 40 小時以內按標準時薪計算
    - 超過 40 小時的加班部分，按 1.5 倍時薪計算
    """
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate
    return pay

def main():
    while True:
        try:
            # 獲取工作時數
            hours_str = input("請輸入工作時數：").strip()
            if not hours_str:
                print("時數不能為空，請重新輸入。")
                continue
            hours = float(hours_str)

            # 獲取標準時薪 (提供預設值 300)
            rate_str = input("請輸入標準時薪 [預設 300，直接按 Enter]：").strip()
            if rate_str == "":
                rate = 300.0
            else:
                rate = float(rate_str)

            # 執行計算
            total_pay = computepay(hours, rate)

            # 格式化輸出 (含千分位整數)
            print("-" * 30)
            print(f"工作時數：{hours:g} 小時")
            print(f"標準時薪：${rate:,.0f}")
            print(f"總工資：${total_pay:,.0f}")
            print("-" * 30)
            break

        except ValueError:
            print(">> 錯誤：請輸入有效的數字格式！")

if __name__ == "__main__":
    main()
