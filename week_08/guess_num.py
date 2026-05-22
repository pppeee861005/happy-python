import random
import winsound
import pygame
import os
from pathlib import Path

# pygame 初始化（用於背景音樂）
pygame.mixer.init()

# 音效頻率和持續時間參數
CORRECT_SOUND_FREQ = 1000
CORRECT_SOUND_DURATION = 500
TOO_SMALL_FREQ = 400
TOO_SMALL_DURATION = 200
TOO_LARGE_FREQ = 600
TOO_LARGE_DURATION = 200

def play_background_music(music_path=None):
    """
    播放背景音樂
    :param music_path: 音樂文件路徑（支援 .mp3, .wav 等格式）
    """
    if music_path and os.path.exists(music_path):
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)  # -1 表示無限循環
            print(f"🎵 背景音樂已開始播放：{os.path.basename(music_path)}")
        except Exception as e:
            print(f"無法加載音樂：{e}")
    else:
        print("提示：如要播放背景音樂，請在遊戲目錄放置 'bg_music.mp3'")

def stop_background_music():
    """停止背景音樂"""
    pygame.mixer.music.stop()

def play_too_small_sound():
    """太小的音效"""
    winsound.Beep(TOO_SMALL_FREQ, TOO_SMALL_DURATION)

def play_too_large_sound():
    """太大的音效"""
    winsound.Beep(TOO_LARGE_FREQ, TOO_LARGE_DURATION)

def play_correct_sound():
    """猜對的音效"""
    winsound.Beep(CORRECT_SOUND_FREQ, CORRECT_SOUND_DURATION)
    winsound.Beep(CORRECT_SOUND_FREQ, CORRECT_SOUND_DURATION)

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
            play_too_small_sound()
        elif guess_num > random_number:
            print("太大了！請再猜個數字")
            play_too_large_sound()
    print(f"恭喜你猜對了秘密數字 {random_number} !!")
    play_correct_sound()


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
            print("往下猜...")
            high = guess_num - 1
            play_too_large_sound()
        elif feedback == 'l':
            print("往上猜...")
            low = guess_num + 1
            play_too_small_sound()

    # 5) 輸出結果
    print(f"耶~ 電腦猜對了你的秘密 {guess_num} !!")
    play_correct_sound()
    
# 測試執行
if __name__ == "__main__":
    # 播放背景音樂
    music_path = Path(__file__).parent / "One_Final_Life_Remaining.mp3"
    play_background_music(str(music_path))

    try:
        limit = int(input("請輸入猜測數字的上限: "))

        print("\n===== 遊戲開始：玩家猜電腦的數字 =====")
        guess(limit)

        print("\n===== 遊戲開始：電腦猜玩家的數字 =====")
        computer_guess(limit)

        print("\n遊戲結束，感謝遊玩！")

    finally:
        # 停止背景音樂
        stop_background_music()
        pygame.mixer.quit()