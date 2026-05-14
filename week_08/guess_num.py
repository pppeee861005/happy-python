import random

def guess(x):
    """
    玩家指定數字上限，並與電腦互動猜測其隨機產生的數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    # 2) 電腦隨機產生 1~上限 間的任一整數
    random_number = random.randint(1, x)
    guess_num = 0
    
    # 5) 重複步驟 4 直到猜對為止
    while guess_num != random_number:
        # 3) 提示要求玩家輸入猜測的數字
        guess_num = int(input(f"猜一個 1-{x} 間的數字: "))
        
        # 4) 判斷大小
        if guess_num < random_number:
            print("太小了！請再猜個數字")
        elif guess_num > random_number:
            print("太大了！請再猜個數字")
            
    print(f"恭喜你猜對了秘密數字 {random_number} !!")


def computer_guess(x):
    """
    玩家選定數字，並與電腦互動，由電腦猜測此數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    low = 1
    high = x
    feedback = ""
    
    # 2) 提示玩家自行選定數字
    print(f"請在心中想好一個 1-{x} 之間的數字，我會嘗試猜出來！")
    
    # 4) 電腦依據線索縮小範圍，重複直到猜對
    while feedback != 'c':
        if low != high:
            # 電腦隨機從目前範圍內挑選一個數字
            guess_num = random.randint(low, high)
        else:
            # 如果範圍縮小到只剩下一個點，那肯定就是它了
            guess_num = low 
            
        # 3) 電腦輸出並要求玩家輸入線索
        feedback = input(f"我猜 {guess_num}，太高(H)/太低(L) 或 正確(C)?? ").lower()
        
        if feedback == 'h':
            high = guess_num - 1
        elif feedback == 'l':
            low = guess_num + 1
            
    # 5) 輸出結果
    print(f"耶~ 電腦猜對了你的秘密 {guess_num} !!")
    
# 測試執行
limit = int(input("請輸入猜測數字的上限: "))
guess(limit)
computer_guess(limit)