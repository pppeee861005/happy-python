"""
澆水 Agent - Prompt 效果測試

手工測試 SYSTEM_PROMPT 和 USER_PROMPT 的效果
"""

import json
import os
from dotenv import load_dotenv
from google import genai
from prompts import get_system_prompt, get_user_prompt
from data_generator import get_mock_humidity, get_mock_weather_6h


def test_prompt_with_gemini(humidity: float, weather: dict, test_name: str) -> dict:
    """
    使用 Google Gemini 測試提示詞

    Args:
        humidity: 土壤濕度
        weather: 天氣數據字典
        test_name: 測試名稱

    Returns:
        dict: 解析後的決策結果
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("❌ 錯誤：未設置 GOOGLE_API_KEY")
        return None

    try:
        client = genai.Client(api_key=api_key)

        # 組合提示詞
        system_prompt = get_system_prompt()
        user_prompt = get_user_prompt(
            humidity=humidity,
            precipitation_prob=weather["precipitation_prob"],
            temperature=weather["temperature"],
            humidity_air=weather["humidity"],
            wind_speed=weather["wind_speed"]
        )

        print(f"\n{'='*60}")
        print(f"🧪 測試：{test_name}")
        print(f"{'='*60}")
        print(f"\n📊 輸入數據：")
        print(f"  • 土壤濕度：{humidity}%")
        print(f"  • 降雨機率：{weather['precipitation_prob']}%")
        print(f"  • 溫度：{weather['temperature']}°C")
        print(f"  • 空氣濕度：{weather['humidity']}%")
        print(f"  • 風速：{weather['wind_speed']} km/h")

        # 調用 Gemini API
        print(f"\n⏳ 調用 Gemini 模型...")
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": f"{system_prompt}\n\n{user_prompt}"
                        }
                    ]
                }
            ]
        )

        # 提取回應文本
        response_text = response.text.strip()
        print(f"\n📝 Gemini 原始回應：")
        print(response_text[:500])  # 只顯示前 500 字

        # 嘗試解析 JSON
        try:
            # 移除可能的 markdown 代碼塊標記
            if response_text.startswith("```"):
                json_str = response_text.split("```")[1]
                if json_str.startswith("json"):
                    json_str = json_str[4:]
            else:
                json_str = response_text

            decision = json.loads(json_str.strip())

            print(f"\n✅ JSON 解析成功！")
            print(f"\n🤖 決策結果：")
            print(f"  • 決策：{decision.get('decision', 'N/A')}")
            print(f"  • 信心度：{decision.get('confidence', 'N/A')}%")
            print(f"  • 推理過程：{decision.get('reasoning', 'N/A')[:100]}...")
            print(f"  • 建議：{decision.get('suggestion', 'N/A')[:100]}...")

            return decision

        except json.JSONDecodeError as e:
            print(f"\n❌ JSON 解析失敗：{e}")
            print(f"   原始回應：{response_text}")
            return None

    except Exception as e:
        print(f"\n❌ API 調用失敗：{e}")
        return None


def run_all_tests():
    """執行所有測試場景"""

    print("\n🌱 澆水 Agent - Prompt 效果測試\n")
    print("=" * 60)
    print("📋 開始執行 5 個典型測試場景")
    print("=" * 60)

    # 測試場景 1：低濕度（應該澆水）
    test_prompt_with_gemini(
        humidity=15.0,
        weather={
            "precipitation_prob": 10,
            "temperature": 30.0,
            "humidity": 40,
            "wind_speed": 5.0
        },
        test_name="低濕度 (15%) - 應該澆水"
    )

    # 測試場景 2：中濕度 + 高降雨（可能延遲澆水）
    test_prompt_with_gemini(
        humidity=50.0,
        weather={
            "precipitation_prob": 80,
            "temperature": 25.0,
            "humidity": 60,
            "wind_speed": 8.0
        },
        test_name="中濕度 (50%) + 高降雨 (80%) - 可能延遲"
    )

    # 測試場景 3：中濕度 + 高溫低降雨（應該澆水）
    test_prompt_with_gemini(
        humidity=45.0,
        weather={
            "precipitation_prob": 10,
            "temperature": 32.0,
            "humidity": 35,
            "wind_speed": 12.0
        },
        test_name="中濕度 (45%) + 高溫 (32°C) 低降雨 (10%) - 應該澆水"
    )

    # 測試場景 4：高濕度（不應該澆水）
    test_prompt_with_gemini(
        humidity=85.0,
        weather={
            "precipitation_prob": 50,
            "temperature": 22.0,
            "humidity": 75,
            "wind_speed": 3.0
        },
        test_name="高濕度 (85%) - 不應該澆水"
    )

    # 測試場景 5：邊界濕度 30%（規則 A 和 B 的分界）
    test_prompt_with_gemini(
        humidity=30.0,
        weather={
            "precipitation_prob": 20,
            "temperature": 28.0,
            "humidity": 55,
            "wind_speed": 6.0
        },
        test_name="邊界濕度 (30%) - 規則 A/B 分界"
    )

    print("\n" + "=" * 60)
    print("✅ 所有測試完成")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
