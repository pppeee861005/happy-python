"""
澆水決策代理 v0 版本
硬編碼邏輯：濕度 = 0 → 澆水，濕度 ≠ 0 → 不澆水
"""
from sensor import MoistureSensor, MockSensor
from datetime import datetime


class WateringAgent:
    """澆水決策代理"""

    def __init__(self, sensor=None):
        """
        初始化澆水代理

        Args:
            sensor: 濕度傳感器對象，默認使用模擬傳感器
        """
        self.sensor = sensor or MockSensor()
        self.decision_history = []

    def make_decision(self) -> dict:
        """
        根據濕度讀數做決策

        Returns:
            dict: 包含決策結果、理由、時間等信息
        """
        # 讀取傳感器數據
        sensor_data = self.sensor.read()
        humidity = sensor_data["humidity"]

        # v0 硬編碼邏輯：濕度 = 0 → 澆水
        should_water = humidity == 0
        reasoning = (
            "土壤濕度為 0，需要澆水" if should_water
            else f"土壤濕度為 {humidity}%，暫不需要澆水"
        )

        decision = {
            "timestamp": datetime.now().isoformat(),
            "humidity": humidity,
            "should_water": should_water,
            "reasoning": reasoning,
            "version": "v0"
        }

        # 保存決策歷史
        self.decision_history.append(decision)

        return decision

    def display_decision(self, decision: dict) -> None:
        """
        顯示決策結果

        Args:
            decision: 決策字典
        """
        print("\n" + "="*50)
        print(f"⏰ 時間: {decision['timestamp']}")
        print(f"💧 濕度: {decision['humidity']}%")
        print(f"🚰 決策: {'澆水 ✓' if decision['should_water'] else '不澆水 ✗'}")
        print(f"💭 理由: {decision['reasoning']}")
        print("="*50)

    def get_history(self) -> list:
        """
        獲取決策歷史

        Returns:
            list: 所有決策記錄
        """
        return self.decision_history
