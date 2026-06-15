contacts = {
    '王大牛': '忠孝東路四段168號',
    '張小花': '內湖路三段18號',
    '趙石頭': '美村路二段37巷7號', 
    '孫小丁': '堤頂大道文化街9號'
}

def add(contacts):
    """要求輸入並添加新的朋友姓名與地址"""
    name = input("新增姓名:")
    address = input("住址:")
    # 字典新增資料：直接指定 contacts[key] = value
    contacts[name] = address
    print("已增加")
    
def modify(contacts):
    """要求輸入並以朋友姓名刪除整筆記錄"""
    name = input("要修改誰的住址？请输入姓名：")
    # 先檢查這個人是不是在通訊錄內
    if name in contacts:
        new_address = input(f"請輸入 {name} 的新地址:")
        # 字典修改資料:與新增相同，若 key 存在就會直接覆蓋舊值
        cintacts[name] = new_address
        print("地址已修改")
    else:
        print(f"【錯誤】通訊錄中找不到姓名為 {name} 的朋友。")

def delete(contacts):
    """要求輪入並以朋友姓名刪除整筆紀錄"""
    name = input("姓名(請勿寫錯)")
    if name in contacts:
        # 彈出確認警告
        confim = input(f"【警告】需要刪除姓名為 {name} 的記錄嗎?\n 回答 Y 或 y(yes)確認")
        if confirm.lower() == 'y':
        # 字典刪除資料:使用 del 關鍵字
            del contacts[name]
            print("記錄已刪除")
        else:
            print("已取消刪除")
    else:
        print(f"【錯誤】通訊錄中找不到名為「{name}」的朋友。")
# ==========================================
# 主程式執行流程 (無窮迴圈選單)
# ==========================================
if __name__ == "__main__":
    while True:
        print("-" * 15 + "我的通訊錄" + "-" * 15)
        print(f"通訊明細:{contacts}")
        # 讓使用者選擇功能
        choice = input("請選擇要做的操作:【1】添加；【2】修改；【3】刪除；【0】退出\n")
        if choice == "1":
            add(contacts)
        elif choice == "2":
            modify(contacts)
        elif choice == "3":
            delete(contacts)
        elif choice == "0":
            # 退出系統
            print(f"通訊明細:{contacts}")
            print("-" * 18 + "已退出" + "-" * 18)
            break # 強制中斷 while 迴圈
        else:
            print("【輸入錯誤】請輸入 1, 2, 3 或 0!\n")