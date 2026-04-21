"""
剪刀、石頭、布遊戲
使用問題分解方式撰寫函數組合
"""

import random


def get_player_choice():
    """
    功能：取得玩家出拳，並驗證輸入是否有效
    返回：玩家的選擇 (1, 2, 3) 或 None（輸入錯誤）
    """
    print("\n1(剪刀)、2(石頭)、3(布)？")
    player_input = input("你出： ").strip()
    
    # 驗證輸入
    if player_input in ['1', '2', '3']:
        return int(player_input)
    else:
        return None


def get_computer_choice():
    """
    功能：電腦隨機出拳
    返回：電腦的選擇 (1, 2, 3)
    """
    return random.randint(1, 3)


def choice_to_name(choice):
    """
    功能：將數字轉換為中文名稱
    參數：choice - 1(剪刀), 2(石頭), 3(布)
    返回：中文字串
    """
    choices = {
        1: "剪刀",
        2: "石頭",
        3: "布"
    }
    return choices.get(choice, "未知")


def display_choices(player, computer):
    """
    功能：顯示雙方的出拳結果
    """
    player_name = choice_to_name(player)
    computer_name = choice_to_name(computer)
    
    print(f"你　　出：{player_name}")
    print(f"電腦出：{computer_name}")


def determine_winner(player, computer):
    """
    功能：根據遊戲規則判斷輸贏
    規則：
      - 剪刀(1) 勝 布(3)
      - 石頭(2) 勝 剪刀(1)
      - 布(3)   勝 石頭(2)
    
    返回：
      "平手" - 平手
      "你贏了" - 玩家勝利
      "你輸了" - 玩家失敗
    """
    # 檢查是否平手
    if player == computer:
        return "平手"
    
    # 檢查玩家勝利的情況
    win_conditions = [
        (1, 3),  # 剪刀勝布
        (2, 1),  # 石頭勝剪刀
        (3, 2)   # 布勝石頭
    ]
    
    if (player, computer) in win_conditions:
        return "你贏了"
    else:
        return "你輸了"


def play_again():
    """
    功能：詢問是否繼續遊戲
    返回：True 表示繼續，False 表示結束
    """
    answer = input("\n繼續下一盤嗎？(Y/N)： ").strip().upper()
    return answer == 'Y'


def play_game():
    """
    功能：主遊戲流程 - 組合所有函數
    """
    print("="*30)
    print("歡迎來到 剪刀、石頭、布 遊戲！")
    print("="*30)
    
    while True:
        # 1. 取得玩家輸入
        player_choice = get_player_choice()
        
        # 5. 驗證輸入
        if player_choice is None:
            print("嗶嗶嗶～只能輸入 剪刀 石頭 布 唷")
            continue
        
        # 2. 生成電腦出拳
        computer_choice = get_computer_choice()
        
        # 3. 顯示雙方出拳
        display_choices(player_choice, computer_choice)
        
        # 4. 判斷輸贏並顯示結果
        result = determine_winner(player_choice, computer_choice)
        print(result + "!")
        
        # 6. 詢問是否繼續
        if not play_again():
            print("\n感謝遊玩！再見！")
            break


if __name__ == "__main__":
    play_game()
