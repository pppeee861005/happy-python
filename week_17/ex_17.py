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
import os
import asyncio
from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage,
    FollowEvent
)

app = Flask(__name__)
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# --- LINE 憑證 ---
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

# --- Google ADK 初始化 ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
APP_NAME = "line_chat_bot"
SYSTEM_PROMPT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "澆水agent",
    "watering_prompt.md",
)
with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as prompt_file:
    system_prompt = prompt_file.read().strip()

session_service = InMemorySessionService()
agent = LlmAgent(
    name="line_chat_agent",
    model="gemini-3.5-flash",
    instruction=system_prompt,
)
runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service,
)
user_sessions = {}


async def ask_google_adk(user_id, user_message):
    session_id = user_sessions.get(user_id)
    if session_id is None:
        session_id = f"line_{user_id}"
        await session_service.create_session(
            app_name=APP_NAME,
            user_id=user_id,
            session_id=session_id,
        )
        user_sessions[user_id] = session_id

    message = Content(role="user", parts=[Part(text=user_message)])
    reply_text = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            reply_text = event.content.parts[0].text or ""
    return reply_text.strip()

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 用一個全域變數來紀錄目前的模式 (預設為 AI 模式)
# 注意：在多人同時使用時此簡易寫法會共用狀態，但在單人測試交作業時非常方便實用
current_mode = "AI" 
CHAT_KEYWORD = "9527"

@app.route("/", methods=['GET'])
def index():
    return f"Welcome to Line Chat bot. Current Mode: {current_mode}"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理文字訊息 (包含 AI 聊天與純回音功能)
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    global current_mode
    user_message = event.message.text.strip()

    # 群組模式：只有以關鍵字開頭的訊息才交給機器人處理
    if not user_message.startswith(CHAT_KEYWORD):
        return

    # 移除關鍵字，留下真正要處理的內容
    user_message = user_message[len(CHAT_KEYWORD):].strip()
    if not user_message:
        return
    
    # 1. 檢查是否觸發模式切換指令
    if user_message == "切換回音":
        current_mode = "ECHO"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統提示：已切換至【純文字回音模式】。"))
        return
    elif user_message == "切換AI":
        current_mode = "AI"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="系統提示：已切換至【AI 智慧聊天模式】。"))
        return

    # 2. 根據目前模式決定回覆內容
    if current_mode == "AI":
        # --- AI 模式：由 Google ADK / Gemini 生成回覆 ---
        try:
            user_id = getattr(event.source, "user_id", "line_user")
            reply_text = asyncio.run(ask_google_adk(user_id, user_message))
        except Exception as e:
            print(f"Google ADK 錯誤: {e}")
            reply_text = f"【AI 出錯，自動轉回音】{user_message}"
    else:
        # --- 回音模式：學使用者說話 ---
        reply_text = user_message

    # 3. 發送文字回覆 + 作業要求的指定貼圖
    reply_messages = [
        TextSendMessage(text=reply_text),
        StickerSendMessage(package_id='3', sticker_id='233')
    ]
    line_bot_api.reply_message(event.reply_token, reply_messages)

# 處理貼圖訊息：一模一樣回應
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    user_package_id = str(event.message.package_id)
    user_sticker_id = str(event.message.sticker_id)
    
    reply_sticker = StickerSendMessage(
        package_id=user_package_id,
        sticker_id=user_sticker_id
    )
    try:
        line_bot_api.reply_message(event.reply_token, reply_sticker)
    except Exception as e:
        print(f"貼圖轉發失敗: {e}")
        
@handler.default()
def default(event):
    print("捕捉到事件:",event)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
