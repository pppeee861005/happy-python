import psutil
import os
import time
import platform
import subprocess
from datetime import datetime
from plyer import notification
def get_battery_info():
    """取得電池資訊，若沒有電池則回傳 None"""
    battery = psutil.sensors_battery()
    if battery is None:
        return None, None
    return battery.percent, battery.power_plugged

def show_notification(title, message):
    """顯示跨平台系統通知（優先使用 plyer，若失敗則 fallback）"""
    system = platform.system()
    try:
        # ✅ 首選：使用 plyer（簡單、穩定、跨平台）
        notification.notify(
            title=title,
            message=message,
            timeout=10  # 通知顯示 10 秒
        )
    except Exception as e:
        # 🔄 後備方案：依作業系統呼叫內建通知
        try:
            if system == "Windows":
                # Windows 備援方案（若 plyer 失敗）
                subprocess.run([
                    "powershell", "-Command",
                    f"[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]; "
                    f"$template = [Windows.UI.Notifications.ToastTemplateType]::ToastText02; "
                    f"$xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent($template); "
                    f"$xml.GetElementsByTagName('text')[0].AppendChild($xml.CreateTextNode('{title}')) | Out-Null; "
                    f"$xml.GetElementsByTagName('text')[1].AppendChild($xml.CreateTextNode('{message}')) | Out-Null; "
                    f"$toast = [Windows.UI.Notifications.ToastNotification]::new($xml); "
                    f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Python Script').Show($toast);"
                ], shell=True)
            elif system == "Darwin":
                os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")
            elif system == "Linux":
                os.system(f"notify-send '{title}' '{message}'")
            else:
                print(f"{title}: {message}")
        except Exception as inner_e:
            print(f"通知顯示失敗: {e}, 備援方案也失敗: {inner_e}")

# def show_notification(title, message):
#     """顯示跨平台系統通知"""
#     system = platform.system()
#     try:
#         if system == "Windows":
#             subprocess.run([
#                 "powershell", "-Command",
#                 f"New-BurntToastNotification -Text '{title}', '{message}'"
#             ], shell=True)
#         elif system == "Darwin":
#             os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")
#         elif system == "Linux":
#             os.system(f"notify-send '{title}' '{message}'")
#         else:
#             print(f"{title}: {message}")
#     except Exception as e:
#         print(f"通知顯示失敗: {e}")

def shutdown_computer():
    """執行關機指令"""
    system = platform.system()
    print("🛑 系統即將關機...")
    if system == "Windows":
        os.system("shutdown /s /t 10")
    elif system == "Darwin":
        os.system("osascript -e 'tell app \"System Events\" to shut down'")
    elif system == "Linux":
        os.system("shutdown -h now")
    else:
        print("❌ 無法識別的系統類型。")

def countdown_shutdown(hours=3):
    """無電池的桌機版本：三小時後自動關機"""
    total_seconds = hours * 3600
    print(f"🖥 檢測為桌上型電腦，將在 {hours} 小時後自動關機。")
    show_notification("💤 自動關機倒數", f"{hours} 小時後系統將自動關機。")

    while total_seconds > 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        print(f"⏳ 剩餘時間：{h:02d}:{m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1

    show_notification("🛑 時間到", "系統即將自動關機。")
    shutdown_computer()

def main():
    print("🚀 啟動智能電源管理程式")
    percent, plugged = get_battery_info()

    # 若無電池（桌機）
    if percent is None:
        countdown_shutdown(hours=3)
        return

    # 筆電模式
    while True:
        percent, plugged = get_battery_info()
        if percent is None:
            break

        print(f"🔋 電量：{percent:.1f}% | {'⚡ 插電中' if plugged else '🔋 使用電池中'}")

        if plugged and percent >= 98:
            #show_notification("🔋 電池已充飽", "電量96%，是否要關機？")
            #choice = input("⚡ 電量達96%，是否立即關機？(y/n): ").strip().lower()
            #if choice == "y":
                shutdown_computer()
                break
            #else:
                #print("⏸️ 已取消關機，繼續監控中。")

        time.sleep(60)

if __name__ == "__main__":
    main()
