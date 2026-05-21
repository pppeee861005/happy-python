
x = [1, 3, 5, 0, -1, 3, -2]
# 方法一：使用 list comprehension（推薦）  
result = [num for num in x if num >= 0]
print(result)  # [1, 3, 5, 0, 3]
  
# 方法二：使用 for 循環
result = []  for num in x:
if num >= 0:
result.append(num)
print(result)  # [1, 3, 5, 0, 3]

# 方法三：filter() 函數
result = list(filter(lambda num: num >= 0, x))  
print(result)  # [1, 3, 5, 0, 3]