"""
澆水代理 v0 主程序
演示硬編碼邏輯：濕度 = 0 → 澆水，濕度 ≠ 0 → 不澆水
"""
from sensor import MockSensor
from watering_agent import WateringAgent


def demo_v0():
    """演示 v0 版本的澆水邏輯"""
    print("🌱 澆水代理 v0 版本演示")
    print("規則：濕度 = 0 → 澆水 | 濕度 ≠ 0 → 不澆水\n")

    # 測試場景 1：濕度 = 0（應該澆水）
    print("📍 場景 1: 濕度 = 0")
    agent1 = WateringAgent(sensor=MockSensor(humidity=0))
    decision1 = agent1.make_decision()
    agent1.display_decision(decision1)

    # 測試場景 2：濕度 = 50（不應該澆水）
    print("\n📍 場景 2: 濕度 = 50%")
    agent2 = WateringAgent(sensor=MockSensor(humidity=50))
    decision2 = agent2.make_decision()
    agent2.display_decision(decision2)

    # 測試場景 3：濕度 = 25（不應該澆水）
    print("\n📍 場景 3: 濕度 = 25%")
    agent3 = WateringAgent(sensor=MockSensor(humidity=25))
    decision3 = agent3.make_decision()
    agent3.display_decision(decision3)

    # 測試場景 4：濕度 = 100（不應該澆水）
    print("\n📍 場景 4: 濕度 = 100%（土壤已飽和）")
    agent4 = WateringAgent(sensor=MockSensor(humidity=100))
    decision4 = agent4.make_decision()
    agent4.display_decision(decision4)

    # 演示連續決策
    print("\n\n📍 場景 5: 連續 5 次決策（濕度 = 0）")
    agent_continuous = WateringAgent(sensor=MockSensor(humidity=0))
    for i in range(5):
        decision = agent_continuous.make_decision()
        print(f"  決策 {i+1}: {'澆水 ✓' if decision['should_water'] else '不澆水 ✗'} - {decision['reasoning']}")

    # 顯示完整歷史
    print("\n\n📊 決策歷史摘要")
    print(f"總決策次數: {len(agent_continuous.get_history())}")
    water_count = sum(1 for d in agent_continuous.get_history() if d['should_water'])
    print(f"需要澆水的次數: {water_count}")


if __name__ == "__main__":
    demo_v0()
