####################################################################
# Python x ChatGPT
# Flask, Linebot, deployment - 網站伺服器串聯LINE服務
# [作業]
# LINE Echo Bot 回音機器人
# 問題：請依照本週課程所述，撰寫程式並佈署至伺服器
#       於串聯LINE頻道後測試。
# 輸出：
#       1)使用者加入好友後於 LINE 所發文字訊息，機器人會如鸚鵡般
#         轉發回去給發送者(學使用者說話)，
#         並加上貼圖 (如：package_id=3, sticker_id=233)。
#       2)使用者所傳的貼圖 (限 Line 所支援的)，機器人也會相同回應。
# 加分題：升級 Line Bot 為 AI 聊天機器人
#####################################################################
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
    FollowEvent
)

import os
from openai import OpenAI

app = Flask(__name__)

# --- LINE 憑證設定 (使用環境變數) ---
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# --- [加分題] ChatGPT API 設定 (使用環境變數) ---
USE_AI = os.getenv('USE_AI', 'False').lower() == 'true'
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


# 1. 建立 LINE Webhook 接收端點
@app.route("/callback", methods=['POST'])
def callback():
    # 取得 LINE 傳來的標頭驗證碼
    signature = request.headers['X-Line-Signature']

    # 取得請求內容
    body = request.get_data(as_text=True)

    # 驗證訊息是否來自 LINE 官方伺服器
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 2. 處理文字訊息 (作業要求 1 + 加分題)
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    user_message = event.message.text
    
    # 【加分題：AI 聊天機器人模式】
    if globals().get('USE_AI', False):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "你是一個友善的中文助手。"},
                    {"role": "user", "content": user_message}
                ]
            )
            ai_reply = response.choices[0].message.content
            
            reply_messages = [
                TextSendMessage(text=ai_reply),
                StickerSendMessage(package_id='3', sticker_id='233')
            ]
        except Exception as e:
            reply_messages = TextSendMessage(text=f"AI 連線錯誤：{str(e)}")
            
    # 【標準題：鸚鵡學舌模式】
    else:
        reply_messages = [
            TextSendMessage(text=user_message),  # 學使用者說話
            StickerSendMessage(package_id='3', sticker_id='233')  # 加上指定貼圖
        ]
    
    # 回覆訊息給使用者
    line_bot_api.reply_message(event.reply_token, reply_messages)


# 3. 處理貼圖訊息 (作業要求 2)
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # 取得使用者發送的貼圖 ID 與套圖 ID
    user_package_id = event.message.package_id
    user_sticker_id = event.message.sticker_id
    
    # 回傳一模一樣的貼圖給使用者
    reply_sticker = StickerSendMessage(
        package_id=user_package_id,
        sticker_id=user_sticker_id
    )
    
    line_bot_api.reply_message(event.reply_token, reply_sticker)


# 啟動伺服器
if __name__ == "__main__":
    # 這裡固定使用 5000 埠口進行測試
    app.run(host='0.0.0.0', port=5000)
