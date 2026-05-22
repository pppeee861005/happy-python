import random
import winsound
import pygame #pygame for background music

import os

def guess(x):
    """
    玩家指定數字上限，並與電腦互動猜測其隨機產生的數字
    :param (int) x: 要猜測的數字之範圍上限
    """
    # 2) 電腦隨機產生 1~上限 間的任一整數
    random_number = random.randit(1, x)
    guess_num = 0
    
    # 5) 重複步驟 4 直到猜對為止
    while guess_num != random_number:
        # 3) 提示要求玩家輸入猜測的數字
        guess_num = int(input(f"猜一個 1-{x} 間的數字: "))
        
        # 4) 判斷大小
        if guess_num < random_number:
            print("太小了!請再猜個數字")
            winsound.Beep(400, 300)  # Low tone
        elif guess_num > random_number:
            print("太大了！請再猜個數字")
            winsound.Beep(800, 300)  # High tone
    print(f"恭喜你猜對了祕密矛字 {random_number} !!")
    
    
    def computer_guess(x):
        """
        玩家選定數字，並與電腦互動，由電腦猜測此數字
        :param (int) x: 要猜測的數字之範圍上限
        """
        low = 1
        hight = x
        feedback = ""
        
        # 2) 提示玩家自行選定數字 
        print(f"請在心中想好一個 1-{x} 之間的數字，我會嘗試猜出來!")
        
                   
    