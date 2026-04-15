import time
import sys

def heart_progress_bar(total=20):
    for i in range(total + 1):
        # 使用紅心與白心作為進度填充
        filled = "❤️" * i
        empty = "🤍" * (total - i)
        percent = (i / total) * 100
        
        # \r 回到行首，並使用 flush 確保即時印出
        sys.stdout.write(f"\r進度: |{filled}{empty}| {percent:3.0f}% ")
        sys.stdout.flush()
        
        time.sleep(0.15)  # 設定動畫速度
    print("\n\n載入完成！ ❤️❤️❤️")

if __name__ == "__main__":
    heart_progress_bar()
