#########################################################################
# Python x ChatGPT
# Flask, Linebot, deployment - 網站伺服器串聯LINE服務
#
# [作業]
# LINE AI Bot 升級為 AI 聊天機器人
#
# 問題：請依照本週課程所述，撰寫程式並於串聯LINE頻道後測試。
#       測試完成後遷移寄存佈署至伺服器 (PythonAnywhere)
#
# 輸出：
#       1)使用者加入好友後於 LINE 所發文字訊息，機器人會連結
#         Google Gemini，由 AI 生成回覆內容後再轉發回去給發送者。
#       2)回應使用者的內容須有聊天脈絡，具備一定的對話記憶。
#       3)每次聊天時擁有的對話記憶維持在2個回合(即問與答共4段內容)。
#       4)加入機器人為好友的眾多使用者之個別聊天內容必須保密。
#       5)聊天機器人應24小時服務用戶。
#
# 加分題：增加 Line Bot 網路搜尋功能以排除 AI 幻覺，並提供即時訊息。
#       1)當使用者訊息最前面2字為 "搜尋" 時，進行網蒐任務。
#       2)安裝並匯入套件：googlesearch-python
#         from googlesearch import search
#         response = search(question) ...
#
##########################################################################

import os
from google import genai
from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

env_path = 'path/to/your/.env'
load_dotenv(env_path)

google_api_key = os.getenv('GOOGLE_API_KEY')
acc_code = os.getenv('LINE_TOKEN')
secr = os.getenv('LINE_SECRET')

line_bot_api = LineBotApi(acc_code)  # 你的LINE存取代碼
handler = WebhookHandler(secr)  # 你的LINE頻道密鑰

client = genai.Client(api_key=google_api_key)  # 你的Google API密鑰

app = Flask(__name__)

Model_ID = "gemini-2.0-flash"
users = {}
backtrace = 2

def check_user(id, name):
    global users

    if id not in users or users[id] is None:
        users[id] = {    # 初始化此使用者物件
            'name': name,
            'hist': []
        }
        print('新增一名用戶：', id)
    else:
        print('用戶已經存在，id：', id)
        print('目前用戶數：', len(users))

def ask(id, question):
    global users
    greeting = ''
    my = users[id]
    name, chat_log = my['name'], my['hist']

    if not chat_log:
        greeting = f"{name} 你好！"

    chat = client.chats.create(
        model=Model_ID,
        history=chat_log,
        config=genai.types.GenerateContentConfig(
            system_instruction='你是 棉羊豬歐巴馬 愛吃愛打架'
        )
    )
    response = chat.send_message(question)
    my['hist'] = chat.get_history()[-2 * backtrace:]

    return greeting + response.text

@app.route('/')
def index():
    return 'Welcome to Line Bot!'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.default()
def default(event):
    print('捕捉到事件：', event)

# 接收文字訊息的事件處理程式
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    # 紀錄用戶資料
    _id = event.source.user_id
    _name = profile.display_name
    _txt = event.message.text

    check_user(_id, _name)
    answer = ask(_id, _txt)

    msg = TextSendMessage(answer)

    line_bot_api.reply_message(event.reply_token, msg)


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=80)
    app.run(debug=True, port=80)
