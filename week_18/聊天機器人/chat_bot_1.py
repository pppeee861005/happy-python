from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入根目錄下的 .env 環境變數

def chat_with_model(prompt: str, model_name: str):
    client = genai.Client()
    interaction = client.interactions.create(
        model=model_name,
        input=prompt
    )
    return interaction.output_text

if __name__ == "__main__":
    content = "幫我買可樂?"
    model = "gemini-3.5-flash"
    reply = chat_with_model(content, model)
    print("Model reply:", reply)
