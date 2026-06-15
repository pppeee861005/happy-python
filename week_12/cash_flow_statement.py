# ==========================================
# 現金流量表管理系統
# ==========================================

def input_cash_flows(category_name):
    """輸入現金流項目和金額"""
    flows = {}
    print(f"\n請輸入【{category_name}】項目:")
    while True:
        item = input(f"  輸入項目 (按 Enter 結束): ").strip()
        if not item:
            break
        try:
            amount = float(input(f"  輸入 {item} 的金額: "))
            flows[item] = amount
        except ValueError:
            print("  【錯誤】請輸入有效的數字!")
    return flows

def print_cash_flow_statement(operating, investing, financing):
    """列印現金流量表"""
    # 計算各類別小計
    total_operating = sum(operating.values())
    total_investing = sum(investing.values())
    total_financing = sum(financing.values())

    # 計算淨現金流
    net_cash_flow = total_operating + total_investing + total_financing

    print("\n" + "=" * 55)
    print(" " * 18 + "現金流量表")
    print("=" * 55)

    # 營運活動現金流
    print("\n【營運活動現金流】")
    print("-" * 55)
    if operating:
        for item, amount in operating.items():
            print(f"  {item:<25} ${amount:>18,.2f}")
        print("-" * 55)
    print(f"  {'營運活動淨現金流':<25} ${total_operating:>18,.2f}")

    # 投資活動現金流
    print("\n【投資活動現金流】")
    print("-" * 55)
    if investing:
        for item, amount in investing.items():
            print(f"  {item:<25} ${amount:>18,.2f}")
        print("-" * 55)
    print(f"  {'投資活動淨現金流':<25} ${total_investing:>18,.2f}")

    # 融資活動現金流
    print("\n【融資活動現金流】")
    print("-" * 55)
    if financing:
        for item, amount in financing.items():
            print(f"  {item:<25} ${amount:>18,.2f}")
        print("-" * 55)
    print(f"  {'融資活動淨現金流':<25} ${total_financing:>18,.2f}")

    # 淨現金流及期末現金餘額
    print("\n【淨現金流】")
    print("-" * 55)
    print(f"  {'本期淨現金流增減':<25} ${net_cash_flow:>18,.2f}")
    print("=" * 55)

    # 現金流量分析
    print("\n【現金流量分析】")
    print("-" * 55)
    print(f"  營運活動現金流: ${total_operating:>15,.2f}")
    print(f"  投資活動現金流: ${total_investing:>15,.2f}")
    print(f"  融資活動現金流: ${total_financing:>15,.2f}")
    print(f"  {'─' * 45}")
    print(f"  本期淨現金流增減: ${net_cash_flow:>15,.2f}")
    print("=" * 55 + "\n")

if __name__ == "__main__":
    print("-" * 55)
    print(" " * 15 + "現金流量表建立系統")
    print("-" * 55)

    # 輸入各類現金流
    operating = input_cash_flows("營運活動現金流")
    investing = input_cash_flows("投資活動現金流")
    financing = input_cash_flows("融資活動現金流")

    # 列印現金流量表
    if operating or investing or financing:
        print_cash_flow_statement(operating, investing, financing)
    else:
        print("【警告】未輸入任何資料!")
