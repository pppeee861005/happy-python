import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv()  # 載入根目錄下的 .env 環境變數

# 設置 API 金鑰
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def multi_turn_chat(model_name: str):
    model = genai.GenerativeModel(model_name)
    chat = model.start_chat()
    
    print("聊天機器人已啟動(輸入 'exit' 退出)")
    print("-" * 50)
    
    while True:
        user_input = input("\n 你說: ").strip()
        
        if user_input.lower() in ['exit', 'quit', '退出']:
            print(" 881 再見囉~see you") 
            break
        if not user_input:
            continue
        
        try:
            response = chat.send_message(user_input)
            print(f"\n 機器人說: {response.text}")
            # 添加延遲避免超過每分鐘的請求限制
            time.sleep(1)
        except Exception as e:
            if "quota" in str(e).lower():
                print("\n 塞車了，請等一分鐘後再試")
                print(" 建議：請付錢再試")
            else:
                print(f"\n XX 錯誤: {e}")
                
if __name__ == "__main__":
    # 使用 gemini-3.5-flash 模型
    model = "gemini-3.5-flash"
    multi_turn_chat(model)
