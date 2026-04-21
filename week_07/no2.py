nums = [20, 36, 27, 15, 2, 107, 48, 66]

# 初始化:用負無限大,確保任何數字都比它大
no1 = float('-inf')   # 冠軍
no2 = float('-inf')   # 亞軍

for i in nums:
    if i > no1:
        no2 = no1    # 原本的冠軍被擠下來當亞軍
        no1 = i      # 挑戰者登基
    if i > no2:
        no2 = i      # 只夠資格當亞軍

print(f"第一大:{no1}")   # 107
print(f"第二大:{no2}")   # 66