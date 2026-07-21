import os

from dotenv import load_dotenv
from openai import OpenAI


MODEL_NAME = "openai/gpt-oss-20b"
SYSTEM_PROMPT = "你是一位親切、實用的繁體中文聊天助理。"


def create_client() -> OpenAI:
    """建立使用 Groq OpenAI 相容 API 的客戶端。"""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "找不到 GROQ_API_KEY，請在 .env 中加入 GROQ_API_KEY=你的金鑰"
        )

    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )


def multi_turn_chat() -> None:
    """啟動會保留對話紀錄的終端機多輪聊天。"""
    try:
        client = create_client()
    except RuntimeError as error:
        print(f"❌ {error}")
        return

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("🤖 Groq 多輪聊天機器人已啟動")
    print("輸入 exit、quit 或 退出可結束聊天。")
    print("-" * 50)

    while True:
        try:
            user_input = input("\n👤 你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 再見！")
            break

        if user_input.lower() in {"exit", "quit", "退出"}:
            print("👋 再見！")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
            )
            assistant_reply = response.choices[0].message.content or ""
            messages.append({"role": "assistant", "content": assistant_reply})
            print(f"\n🤖 機器人：{assistant_reply}")
        except Exception as error:
            # 請求失敗時移除本輪問題，避免它污染下一次對話。
            messages.pop()
            print(f"\n❌ Groq API 呼叫失敗：{error}")


if __name__ == "__main__":
    multi_turn_chat()
