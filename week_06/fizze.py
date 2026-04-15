for i in range(1, 101):  # 从 1 开始可以避开 0 的余数问题
    if i % 3 == 0 and i % 5 == 0:
        print("fizzeBuzz")
    elif i % 3 == 0:
        print("fizze")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
#我要再打一次
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzeBuzz")
    elif i % 3 == 0:
        print("fizze")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) #原數打出來

# nqj 用while loop

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