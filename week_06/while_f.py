i = 0
while i <= 100:
    if i == 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print("fizzeBuzz")
    elif i % 3 == 0:
        print("fizze")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1  # 每次循环加 1，防止死循环
    
#ey jti 再打一
i = 0
while i <= 100:
    if i == 0:
        print(i)