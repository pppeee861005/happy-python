import html
import random
import time
from itertools import cycle
from tkinter import BROWSE
from httpx import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from sympy import sequence
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 定義可用的按鍵方向
KEY_INPUTS = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)


def play_2048(random_input=False):
    """
    This function launches and plays a game of 2048 with either sequential
    (up, right, down, left) or random inputs. Once the game is over,
    the browser exits and the final score is displayed.
    :param bool random_input: True for random moves, False for sequential.
    """
    # 啟動 Chrome 瀏覽器
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")  
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])  
    BROWSE = webdriver.Chrome(service=service, options=options)

    try:
        # 開啟 2048 遊戲網頁
        BROWSE.get("https://play2048.co/")
        # 取得可接收鍵盤事件的元素
        game_status = BROWSE.find_element(By.CSS_SELECTOR, ".text-4xl")
        html_element = BROWSE.find_element(By.CSS_SELECTOR, 'html')

        # 設定輸入序列
        if random_input:
            sequence = KEY_INPUTS
            game_input = lambda seq: random.choice(seq)
        else:
            sequence = cycle(KEY_INPUTS)
            game_input = lambda seq: next(seq)

        # 主迴圈：持續送出按鍵，直到偵測到遊戲結束
        while game_status.text != "Game Over":
            html_element.send_keys(game_input(sequence))
            time.sleep(0.1)  # 添加短暫延遲
            game_status = BROWSE.find_element(By.CSS_SELECTOR, ".text-4xl")

        try:
            # 等待分數元素載入並取得分數
            score_elem = WebDriverWait(BROWSE, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shrink-1.truncate"))
            )
            score_text = score_elem.text.strip()
            
            # 處理可能包含加號的分數
            if '+' in score_text:
                score = int(score_text.split('+')[0].strip())
            else:
                score = int(score_text) if score_text else 0
                
            print(f"{'Randomized' if random_input else 'Sequential':<10} input:"
                  f"\tGame over - your score: {score:6,d}!")
                  
        except Exception as e:
            print(f"分數處理錯誤: {e}")
            print(f"原始分數文字: {score_text if 'score_text' in locals() else '無法取得'}")
            
    except Exception as e:
        print(f"遊戲執行錯誤: {e}")
        
    finally:
        # 關閉瀏覽器
        BROWSE.quit()

if __name__ == '__main__':
    KEY_INPUTS = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
    play_2048()  # 執行一次，使用循序輸入
    play_2048(random_input=True)  # 執行一次，使用隨機輸入
    print("Game Over")
