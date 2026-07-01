"""
模擬土壤濕度傳感器
"""
import random
from datetime import datetime


class MoistureSensor:
    """模擬濕度傳感器"""

    def __init__(self, min_humidity: float = 0, max_humidity: float = 100):
        """
        初始化傳感器

        Args:
            min_humidity: 最小濕度值
            max_humidity: 最大濕度值
        """
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity

    def read(self) -> dict:
        """
        讀取傳感器數據

        Returns:
            dict: 包含濕度和時間戳的數據
        """
        humidity = random.uniform(self.min_humidity, self.max_humidity)
        return {
            "humidity": round(humidity, 2),
            "timestamp": datetime.now().isoformat(),
            "unit": "%"
        }


class MockSensor:
    """測試用的模擬傳感器 - 可以設置固定值"""

    def __init__(self, humidity: float = 0):
        """
        初始化模擬傳感器

        Args:
            humidity: 固定的濕度值
        """
        self.humidity = humidity

    def read(self) -> dict:
        """
        讀取固定濕度值

        Returns:
            dict: 包含濕度和時間戳的數據
        """
        return {
            "humidity": self.humidity,
            "timestamp": datetime.now().isoformat(),
            "unit": "%"
        }
