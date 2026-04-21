import random

# =====================================================
# 函數 1：讓使用者出拳
# =====================================================
def player_choice():
    """取得玩家輸入，回傳整數 1/2/3，輸入錯誤回傳 None"""
    print("1(剪刀)、2(石頭)、3(布)？")
    user_input = input("你出： ")
    
    # 檢查是否為合法輸入
    if user_input in ["1", "2", "3"]:
        return int(user_input)
    else:
        return None  # 來亂的


# =====================================================
# 函數 2：電腦隨機出拳
# =====================================================
def computer_choice():
    """電腦隨機出 1/2/3"""
    return random.randint(1, 3)


# =====================================================
# 函數 3：把數字轉成中文名稱
# =====================================================
def num_to_name(num):
    """1 → 剪刀, 2 → 石頭, 3 → 布"""
    names = ["", "剪刀", "石頭", "布"]  # 索引 0 不用
    return names[num]


# =====================================================
# 函數 4：顯示雙方出拳
# =====================================================
def show_result(player, computer):
    """顯示玩家和電腦的出拳"""
    print(f"你 出：{num_to_name(player)}")
    print(f"電腦出：{num_to_name(computer)}")


# =====================================================
# 函數 5：判斷勝負（核心邏輯）
# =====================================================
def judge(player, computer):
    """
    比較規則：
      剪刀(1) > 布(3)
      石頭(2) > 剪刀(1)
      布(3)   > 石頭(2)
    """
    if player == computer:
        return "平手!"
    
    # 玩家贏的三種情況
    if (player == 1 and computer == 3) or \
       (player == 2 and computer == 1) or \
       (player == 3 and computer == 2):
        return "你贏了!"
    else:
        return "你輸了!"


# =====================================================
# 函數 6：玩一輪遊戲
# =====================================================
def play_one_round():
    """完整玩一輪"""
    player = player_choice()
    
    # 輸入錯誤 → 直接結束這輪
    if player is None:
        print("嗶嗶嗶～只能輸入 剪刀 石頭 布 唷")
        return
    
    computer = computer_choice()
    show_result(player, computer)
    print(judge(player, computer))


# =====================================================
# 函數 7：主程式（遊戲循環）
# =====================================================
def main():
    while True:
        play_one_round()
        again = input("繼續下一盤嗎？(Y/N)： ")
        if again.upper() != "Y":
            print("遊戲結束，掰掰！")
            break


# 啟動遊戲
if __name__ == "__main__":
    main()