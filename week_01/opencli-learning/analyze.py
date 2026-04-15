import json

# 讀取 JSON 文件
with open('hn_data.json', 'r', encoding='utf-16') as f:
    data = json.load(f)

print("=" * 60)
print("HackerNews 數據分析報告")
print("=" * 60)

# 基本統計
print(f"\n📊 基本統計")
print(f"總帖子數：{len(data)}")

# 分數分析
scores = [item['score'] for item in data]
print(f"\n⭐ 分數分析")
print(f"平均分數：{sum(scores) / len(scores):.2f}")
print(f"最高分數：{max(scores)}")
print(f"最低分數：{min(scores)}")

# 評論分析
comments = [item['comments'] for item in data]
print(f"\n💬 評論分析")
print(f"平均評論數：{sum(comments) / len(comments):.2f}")
print(f"最多評論：{max(comments)}")
print(f"最少評論：{min(comments)}")

# 排名前 3 的帖子
print(f"\n🏆 排名前 3 的帖子（按分數）")
sorted_by_score = sorted(data, key=lambda x: x['score'], reverse=True)
for i, item in enumerate(sorted_by_score[:3], 1):
    print(f"{i}. {item['title']}")
    print(f"   分數：{item['score']} | 評論：{item['comments']}")

# 評論最多的帖子
print(f"\n💬 評論最多的帖子")
sorted_by_comments = sorted(data, key=lambda x: x['comments'], reverse=True)
for i, item in enumerate(sorted_by_comments[:3], 1):
    print(f"{i}. {item['title']}")
    print(f"   評論數：{item['comments']} | 分數：{item['score']}")

print("\n" + "=" * 60)