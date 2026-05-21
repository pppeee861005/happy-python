import time
import sys
import os
import random

# 初始化 Windows 終端機的 ANSI 顏色支援
if os.name == 'nt':
    os.system('')

# ANSI 顏色代碼
PINK = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'
CLEAR_LINE = '\033[K'

def print_title(title):
    print("\n" + "=" * 50)
    print(f"{BOLD}{PINK}★ {title} ★{RESET}")
    print("=" * 50)

def cat_and_fish_progress():
    """
    範例 1：小貓咪與小魚 (Cat and Fish)
    小貓咪一邊留下腳印，一邊朝著美味的小魚前進！
    """
    print_title("範例 1：小貓咪找小魚 🐈 🐾 🐟")
    total_steps = 20
    
    for i in range(101):
        # 計算小貓前進的步數 (0 到 20)
        step = int(i / (100 / total_steps))
        
        # 決定狀態文字
        if i == 0:
            status = "喵～小貓肚子餓了，出發找魚吃... 🐾"
        elif i < 30:
            status = "小貓聞到魚的味道了，踏著小碎步！ 🐱🐾"
        elif i < 60:
            status = "快到了！快到了！小魚等等我喵～ 🐈💨"
        elif i < 100:
            status = "只差一點點了！伸長肉球！ 🐾🐈"
        else:
            status = f"{GREEN}喵嗚！成功吃到小魚了！肚子飽飽好幸福～ 💖{RESET}"
            
        if i < 100:
            # 未完成時，畫出軌跡
            # 🐾 代表走過的路，🐈 是小貓的位置，. 代表還沒走的路，🐟 是終點
            track = "🐾" * step + "🐈" + "." * (total_steps - step - 1)
            # 使用 \r 讓游標回到行首，並用 \033[K 清除該行舊字元，避免殘留
            print(f"\r[{track}] 🐟 {BOLD}{BLUE}{i:3d}%{RESET} | {status}", end="", flush=True)
        else:
            # 完成時，小貓吃掉小魚，露出開心的表情
            track = "🐾" * total_steps + "😸❤️"
            print(f"\r[{track}] 🎉 {BOLD}{GREEN}{i:3d}%{RESET} | {status}{CLEAR_LINE}", flush=True)
            
        time.sleep(0.08) # 模擬進度條速度
    print()

def flower_growing_progress():
    """
    範例 2：種植美麗小花 (Planting a Flower)
    從播種、發芽、長葉到最後盛開滿滿的鮮花與蝴蝶！
    """
    print_title("範例 2：種植美麗小花 🌱 🌿 🌸")
    total_steps = 15
    
    for i in range(101):
        step = int(i / (100 / total_steps))
        
        if i < 20:
            icon = "🟤" # 種子
            status = "正在鬆土播種，注入愛心水滴... 💧"
        elif i < 50:
            icon = "🌱" # 發芽
            status = "小種子探出頭來囉！曬曬太陽 🌱☀️"
        elif i < 80:
            icon = "🌿" # 長葉
            status = "長出小葉子了，要快快長大喔 🌿✨"
        elif i < 100:
            icon = "🌷" # 花苞
            status = "結出小花苞了！期待綻放的瞬間 🌷✨"
        else:
            icon = "🌸"
            status = f"{YELLOW}哇！開出滿滿的花朵了！蝴蝶也飛來囉～ 🦋✨🌼{RESET}"
            
        if i < 100:
            # 用 🌿 代表生長的莖葉，🌱 代表未長成的土地
            bar = "🌿" * step + "🌱" * (total_steps - step)
            print(f"\r[{bar}] {icon} {BOLD}{CYAN}{i:3d}%{RESET} | {status}", end="", flush=True)
        else:
            # 滿開的花園！
            flowers = "🌸🌻🌷🌹🌼🌸🌻🌷🌹🌼"
            print(f"\r[{flowers}] {icon} {BOLD}{YELLOW}{i:3d}%{RESET} | {status}{CLEAR_LINE}", flush=True)
            
        time.sleep(0.1)
    print()

def bunny_carrot_progress():
    """
    範例 3：貪吃小兔子與胡蘿蔔 (Hungry Bunny and Carrot)
    小兔子在草地上快樂蹦蹦跳，奔向胡蘿蔔！
    """
    print_title("範例 3：小兔子奔向胡蘿蔔 🐇 🍀 🥕")
    total_steps = 20
    
    for i in range(101):
        step = int(i / (100 / total_steps))
        
        # 讓兔子在跳動時有動態效果（奇數偶數步切換表情/動作）
        bunny = "🐰" if (i // 5) % 2 == 0 else "🐇"
        
        if i == 0:
            status = "小兔子蹦蹦跳跳地出發囉！ 🐇🐾"
        elif i < 35:
            status = "胡蘿蔔！好大一根胡蘿蔔！ 🥕👀"
        elif i < 70:
            status = "用力跳！一步兩步，跳得很高！ 🐰💨"
        elif i < 100:
            status = "馬上就要咬到胡蘿蔔囉！加油！ 🥕🐇"
        else:
            status = f"{PINK}嚼嚼嚼！胡蘿蔔真甜！小兔子開心地轉圈圈～ 🥕🐰💖{RESET}"
            
        if i < 100:
            # 🍀 代表滿地綠草，. 代表前方的路
            track = "🍀" * step + bunny + "." * (total_steps - step - 1)
            print(f"\r[{track}] 🥕 {BOLD}{PINK}{i:3d}%{RESET} | {status}", end="", flush=True)
        else:
            # 吃掉胡蘿蔔後開心的模樣
            track = "🍀" * total_steps + "🐰✨"
            print(f"\r[{track}] 🎉 {BOLD}{GREEN}{i:3d}%{RESET} | {status}{CLEAR_LINE}", flush=True)
            
        time.sleep(0.08)
    print()

def magic_heart_progress():
    """
    範例 4：愛心魔法能量條 (Love & Magic Heart Bar)
    魔法棒施放魔法，將一顆顆空心愛心填滿粉紅能量，最後發射愛心光束！
    """
    print_title("範例 4：愛心魔法能量條 🪄 💖 ✨")
    total_steps = 10  # 愛心條比較寬，用10格即可
    
    for i in range(101):
        step = int(i / (100 / total_steps))
        
        # 魔法星光閃爍效果
        sparkles = "✨" if i % 2 == 0 else "⭐"
        
        if i < 30:
            status = "🪄 魔法少女變身！注入粉紅能量... ✨"
        elif i < 60:
            status = "🪄 奇幻咒語：嗶哩嗶哩，愛心滿載！ 💗"
        elif i < 90:
            status = "🪄 魔法能量正在急遽上升中！ 🌟"
        elif i < 100:
            status = "🪄 能量即將臨界！準備發射愛心光束！ ⚡🎀"
        else:
            status = f"{RED}魔法愛心光束發射！(。･ω･)ﾉﾞ 💖✨🎀🌈{RESET}"
            
        if i < 100:
            # 💖 代表填滿的愛心，🤍 代表未填滿的空心
            bar = "💖" * step + "🤍" * (total_steps - step)
            print(f"\r🪄 {sparkles} [{bar}] {BOLD}{RED}{i:3d}%{RESET} | {status}", end="", flush=True)
        else:
            # 能量大爆發！
            bar = "💖" * total_steps
            print(f"\r🪄✨ [{bar}] 🎉 {BOLD}{RED}{i:3d}%{RESET} | {status}{CLEAR_LINE}", flush=True)
            
        time.sleep(0.09)
    print()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{BOLD}{CYAN}🎀 歡迎來到可愛風格進度條動畫示範 🎀{RESET}")
        print("+" + "-" * 48 + "+")
        print(f"| {YELLOW}1.{RESET} 🐈 小貓咪找小魚進度條                        |")
        print(f"| {YELLOW}2.{RESET} 🌱 栽培美麗小花進度條                        |")
        print(f"| {YELLOW}3.{RESET} 🐇 小兔子奔向胡蘿蔔進度條                    |")
        print(f"| {YELLOW}4.{RESET} 🪄 愛心魔法能量條                           |")
        print(f"| {YELLOW}5.{RESET} 🌟 一次播放全部範例                           |")
        print(f"| {YELLOW}0.{RESET} 🚪 離開程式                                 |")
        print("+" + "-" * 48 + "+")
        
        try:
            choice = input(f"請選擇想觀看的動畫 (0-5): ").strip()
            
            if choice == '1':
                cat_and_fish_progress()
                input(f"\n{BLUE}[按 Enter 鍵返回主選單]{RESET}")
            elif choice == '2':
                flower_growing_progress()
                input(f"\n{BLUE}[按 Enter 鍵返回主選單]{RESET}")
            elif choice == '3':
                bunny_carrot_progress()
                input(f"\n{BLUE}[按 Enter 鍵返回主選單]{RESET}")
            elif choice == '4':
                magic_heart_progress()
                input(f"\n{BLUE}[按 Enter 鍵返回主選單]{RESET}")
            elif choice == '5':
                cat_and_fish_progress()
                time.sleep(1)
                flower_growing_progress()
                time.sleep(1)
                bunny_carrot_progress()
                time.sleep(1)
                magic_heart_progress()
                print(f"\n{BOLD}{GREEN}恭喜！所有可愛進度條均已播放完畢！✨🎉{RESET}")
                input(f"\n{BLUE}[按 Enter 鍵返回主選單]{RESET}")
            elif choice == '0':
                print(f"\n{BOLD}{PINK}感謝您的使用，祝您天天快樂寫程式！Bye Bye~ 👋💖{RESET}\n")
                break
            else:
                print(f"\n{RED}輸入錯誤！請輸入 0 到 5 之間的數字。{RESET}")
                time.sleep(1.5)
        except KeyboardInterrupt:
            print(f"\n\n{RED}程式已被使用者中斷。Bye Bye~ 👋{RESET}\n")
            break

if __name__ == '__main__':
    main()
