"""
澆水 Agent - 模擬數據生成器

提供模擬的土壤濕度和天氣數據，用於測試決策邏輯
"""

import random


def get_mock_humidity() -> float:
    """
    生成模擬土壤濕度 (%)

    Returns:
        float: 0-100 範圍的隨機濕度值
    """
    return round(random.uniform(0, 100), 1)


def get_mock_weather_6h() -> dict:
    """
    生成未來 6 小時的模擬天氣預報

    Returns:
        dict: 包含以下鍵的字典
            - precipitation_prob (int): 降雨機率 0-100%
            - temperature (float): 溫度 15-35°C
            - humidity (int): 空氣濕度 30-90%
            - wind_speed (float): 風速 0-20 km/h
    """
    return {
        "precipitation_prob": random.randint(0, 100),
        "temperature": round(random.uniform(15, 35), 1),
        "humidity": random.randint(30, 90),
        "wind_speed": round(random.uniform(0, 20), 1),
    }


if __name__ == "__main__":
    # 測試數據生成
    print("🌱 澆水 Agent - 模擬數據生成器測試\n")

    print("📊 模擬土壤濕度：")
    for i in range(3):
        humidity = get_mock_humidity()
        print(f"  次數 {i+1}: {humidity}%")

    print("\n🌤️  模擬 6 小時天氣預報：")
    for i in range(3):
        weather = get_mock_weather_6h()
        print(f"  次數 {i+1}:")
        print(f"    • 降雨機率: {weather['precipitation_prob']}%")
        print(f"    • 溫度: {weather['temperature']}°C")
        print(f"    • 空氣濕度: {weather['humidity']}%")
        print(f"    • 風速: {weather['wind_speed']} km/h")
