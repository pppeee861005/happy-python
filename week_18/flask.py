# flask_app.py

import os
from google import genai
from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# ✅ 讀取 .env 檔案
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

# ✅ 讀取金鑰與憑證
google_api_key = os.getenv('GOOGLE_API_KEY')
acc_code = os.getenv('LINE_TOKEN')
secr = os.getenv('LINE_SECRET')

# ✅ 初始化 LINE BOT 與 Google Gemini
line_bot_api = LineBotApi(acc_code)
handler = WebhookHandler(secr)
client = genai.Client(api_key=google_api_key)

# ✅ 初始化 Flask App
app = Flask(__name__)
application = app  # 提供給 WSGI 呼叫

# ✅ 全域變數
Model_ID = "gemini-2.0-flash"
users = {}
backtrace = 2

# ✅ 檢查使用者是否存在
def check_user(id, name):
    if id not in users or users[id] is None:
        users[id] = {
            'name': name,
            'hist': []
        }
        print('✅ 新增一名用戶：', id)
    else:
        print('👥 用戶已存在：', id)

# ✅ 與 Gemini 對話
def ask(id, question):
    greeting = ''
    my = users[id]
    name, chat_log = my['name'], my['hist']

    if not chat_log:
        greeting = f"{name} 你好！"

    chat = client.chats.create(model=Model_ID, history=chat_log)
    response = chat.send_message(question)
    my['hist'] = chat.get_history()[-2 * backtrace:]

    return greeting + response.text

# ✅ Flask 路由
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
    print('📩 捕捉到未知事件：', event)

# ✅ LINE 訊息處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    _id = event.source.user_id
    _name = profile.display_name
    _txt = event.message.text

    check_user(_id, _name)
    answer = ask(_id, _txt)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(answer))
