# ========================
# 現金流量表管理系統
# ========================

def input_cash_flows(category_name):
    """輸入現金流項目和金額"""
    flows = {}
    print(f"\n請輪入 【{category_name}】項目： ")
    while True:
        item = input(f" 輸入項目 (按 Enter 結束): ").strip()
        if not item:
            break
        try:
            amount = float(input(f" 輸入 {item} 的金額: "))
            flows[item] = amount
        except ValueError:
            print(" 【錯誤】請輸入有效的數字!")
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
    print("=" * 55)
    if operating:
        for item, amount in operating.items():
            print(f" {item:<25} ${amount:>18,.2f}")
        print("-" * 55)
    print(f" {'營運活動淨現金流':<25} ${total_operating:>18,.2f}")
    