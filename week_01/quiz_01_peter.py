name = input('你是什麼名字？')
age = input('你幾歲？')
f = input('來自哪裡？')
print(f'來自 {f}, {age} 歲的 {name}, 龍蝦歡迎您！')
print('####################################')
customer = 2000
rate = 0.05
money = 150
result = customer * rate * money
print(f'效果: {result}元')
print('####################################')
c = int(input('請輸入人數:'))
r = float(input('請輸入轉化率(%):'))
m = float(input('請輸入平均銷費:'))
result = c * (r/100) * m
print(f'效果: {result}錢')