"""
測試傳感器模塊
"""
from sensor import MoistureSensor, MockSensor


def test_random_sensor():
    """測試隨機濕度傳感器"""
    print("=== 隨機濕度傳感器測試 ===")
    sensor = MoistureSensor(min_humidity=20, max_humidity=80)

    for i in range(5):
        data = sensor.read()
        print(f"讀取 {i+1}: 濕度={data['humidity']}{data['unit']}, 時間={data['timestamp']}")


def test_mock_sensor():
    """測試模擬固定值傳感器"""
    print("\n=== 模擬傳感器測試 ===")

    # 測試濕度為 0
    sensor_zero = MockSensor(humidity=0)
    data = sensor_zero.read()
    print(f"濕度=0: {data}")

    # 測試濕度為 50
    sensor_mid = MockSensor(humidity=50)
    data = sensor_mid.read()
    print(f"濕度=50: {data}")

    # 測試濕度為 100
    sensor_full = MockSensor(humidity=100)
    data = sensor_full.read()
    print(f"濕度=100: {data}")


if __name__ == "__main__":
    test_random_sensor()
    test_mock_sensor()
