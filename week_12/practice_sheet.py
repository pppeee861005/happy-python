#=========================
## ==========================================
# 資產負債表管理系統
# ==========================================
def input_assets():
    """輸入資產項目和金額"""
    assets = {}
    while True:
        item = input("輸入項目 (按 enter 結束):").strip()
        if not item:
            break
        try:
            amount = float(input(f"輪入 {item} 的金額: "))
            assets[item] = amount
        except ValueError:
            print("【錯誤】請輪入有效的數字!")
    return assets

def input_liabilities():
    """輸入負債項目和金額"""
    liabilities = {}
    while True:
        item = input("輸入負債項目 (按 enter 結束): ").strip()
        if not item:
            break
        try:
            amount = float(input(f"輪入 {item} 的金額: "))
            liabilities[item] = amount
        except ValueError:
            print("【錯誤】請輸入有效的數字!")
    return liabilities
                
def print_balance_sheet(assets, liabilities):
    """列印資產負債表"""
    # 計算總金額
    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())
    equity = total_assets - total_liabilities
    
    print("\n" + "=" * 60)
    print(" " * 16 + "資產負債表")
    print("=" * 66)
    
    #資產部分
    print("\n【資產】")
    print("-" * 88)
    for item, amount in assets.items():
        print(f" {item:<20} ${amount:>15,.2f}")
    print("-" * 50)
    print(f"  {'資產總計':<20} ${total_assets:>15,.2f}")
    
    # 負債部分
    print("\n【負債】")
    print("-" * 88)
    for item, amount in liabilities.items():
        print(f"  {item:<20} ${amount:>15,.2f}")
    print("-" * 88)
    print(f"  {'負債總數':<20} ${total_liabilities:>15,.2f}")
    
    #權益部分
    print("\n【權益】")
    print("-" * 88)
    print(f"  {'權東權益':<20} ${equity:>15,.2f}")
    
    # 驗證平衡
    print("\n【驗證】")
    print("-" * 88)
    print(f"  資產總計 (${total_assets:,.2f}) = 負債總計 (${total_liabilities:,.2f}) + 權益 (${equity:,.2f}))")
   
if __name__ == "__main__":
    print("-" * 50)
    print(" " * 12 + "資產負債表建立系統")
    print("-" * 50)
    
    # 輸入資產
    print("\n請輸入資產項目:")
    assets = input_assets()
    
    # 輸入負債
    print("\n請輸入負債項目:")
    liabilities = input_liabilities()
    
    # 列印資產負債表
    if assets or liabilities:
        print_balance_sheet(assets, liabilities)
    else:
        print("【警告】未輸入任何資料!")