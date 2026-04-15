import time
import os
import sys

time.sleep(10)
print("🐷 哼哼哼！～")

if sys.platform == "darwin":
    os.system("say '哼哼哼'")
elif sys.platform == "win32":
    import winsound
    winsound.Beep(400, 500)
else:
    print("\a")