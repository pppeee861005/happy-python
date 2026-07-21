
from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
    model="openai/gpt-oss-20b",
)
print(response.output_text)

網止：https://console.groq.com/docs/overview

model=openai/gpt-oss-20b

先在 .env 加入：

  GROQ_API_KEY=你的_Groq_API_Key

  安裝套件：

  pip install -r "D:\gameplace\code\快樂寫程式\week_18\聊天機器人\requirements.txt"

  執行：

  python "D:\gameplace\code\快樂寫程式\week_18\聊天機器人\chat_bot_groq.py"

  程式會保存本次執行期間的對話上下文；輸入 exit、quit 或 退出 即可結束。