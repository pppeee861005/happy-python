# [練習一]
# 銀行(Banks)類別
# 問題：制定銀行類別 Banks，並對必要屬性與方法以私有變數撰寫
#
# 制定類別：
#    1)屬性：存戶姓名、存款金額、分行名稱、匯率、換匯手續費
#    2)分行名稱：Taipei Bank
#    3)存款方法：save_money(self, money)，同時印出：'存款 money 完成'
#    4)提款方法：withdraw_money(self, money)，印出：'提款 money 完成'
#    5)取得存款餘額：get_balance(self) - 印出：'存戶姓名 目前餘額: $$$$'
#    6)美金換匯：usd_to_ntd(self, usd)
#    7)結售匯率計算：__cal_rate(seld, usd) = 美金*匯率*(1-手續費)
#      假設：匯率 = 28.50；手續費 = 1%
#
# 實體化操作：
#    1)開戶只需姓名
#    2)印出開戶銀行名稱(開戶銀行：Taipei Bank)
#    3)存款 10000 元
#    4)提款 888 元
#    5)存款 1500 元
#    6)嘗試直接以點運算子更改剩餘金額 (如：mybank.__balance = 20000)
#    7)換匯 500 元美金為台幣，印出換到的台幣金額，並存入帳戶
#      (注意：銀行收取換匯手續費用 1%)
#    8)印出剩餘金額(如：Tony 您目前餘額： 22461)
#    請列出上述每次的執行結果帳單
############################################################################

class Banks:
    # 類別屬性：分行名稱
    branch_name = 'Taipei Bank'

    def __init__(self, name):
        self.__name = name          # 存戶姓名（私有）
        self.__balance = 0          # 存款金額（私有）
        self.__exchange_rate = 28.50  # 匯率（私有）
        self.__fee_rate = 0.01      # 換匯手續費 1%（私有）

    def save_money(self, money):
        self.__balance += money
        print(f'存款 {money} 完成')

    def withdraw_money(self, money):
        if money > self.__balance:
            print(f'餘額不足，無法提款 {money}')
        else:
            self.__balance -= money
            print(f'提款 {money} 完成')

    def get_balance(self):
        print(f'{self.__name} 您目前餘額： {self.__balance}')

    def __cal_rate(self, usd):
        # 結售匯率計算：美金 * 匯率 * (1 - 手續費)
        return usd * self.__exchange_rate * (1 - self.__fee_rate)

    def usd_to_ntd(self, usd):
        ntd = self.__cal_rate(usd)
        ntd = int(ntd)  # 取整數（銀行通常無條件捨去）
        print(f'{usd} 美金換得台幣 {ntd} 元')
        self.save_money(ntd)


# ── 實體化操作 ──────────────────────────────────────────
print('=' * 40)

# 1) 開戶只需姓名
mybank = Banks('Tony')

# 2) 印出開戶銀行名稱
print(f'開戶銀行：{Banks.branch_name}')

# 3) 存款 10000 元
mybank.save_money(10000)

# 4) 提款 888 元
mybank.withdraw_money(888)

# 5) 存款 1500 元
mybank.save_money(1500)

# 6) 嘗試直接以點運算子更改剩餘金額（私有變數保護，不會影響真正的 __balance）
mybank.__balance = 20000
print('嘗試直接修改 __balance = 20000（私有變數保護，實際餘額不受影響）')
mybank.get_balance()  # 仍顯示原本餘額

# 7) 換匯 500 元美金為台幣，存入帳戶
mybank.usd_to_ntd(500)

# 8) 印出剩餘金額
mybank.get_balance()

print('=' * 40)
