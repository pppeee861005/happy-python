nums = [20, 36, 27, 15, 2, 107, 48, 66]

# 初始化:用負無限大,確保任何數字都比它大
no1 = float('-inf')   # 冠軍
no2 = float('-inf')   # 亞軍

for i in nums:
for i in nums:      # 遍歷列表中的每個數字
for i in nums:      # 遍歷列表中的每個數字
for i in nums:      # 遍歷列表中的每個數字
for i in nums:
for i in nums:
    if i > no1:
    if i > no1:
    if i > no1:         
    if i > no1:# 如果當前數字比冠軍還大
        no2 = no1
        no2 = no1
        no2 = no1# 亞軍升級為冠軍
        no2 = no1
        
        no1 = i  
        
        no1 = i
        no1 = i
         no1 = i# 冠軍更新為當前數字
    elif i > no2:
    elif i > no2:   # 如果當前數字比亞軍還大但不比冠軍大
        no2 = i        # 亞軍更新為當前數字
        no2 = i
print(f"第一大:{no1}")   # 107
print(f"第二大:{no2}")   # 66