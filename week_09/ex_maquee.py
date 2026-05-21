import time
msg = '列車將進站 請勿靠近車門 以免夾傷 '
print("按 Ctrl+C 可終止程式\n")
try:
    while True:
        # \r (Carriage Return) 會讓游標回到行首，達成原地更新的效果
        # end="" 則避免 print 自動換行
        print(f"\r{msg}", end="", flush=True)
        # 走馬燈邏輯：將第一個字搬到最後面
        msg = msg[1:] + msg[0]
        time.sleep(0.2)  # 暫停 0.2 秒
except KeyboardInterrupt:
    print("\n走馬燈已停止。")