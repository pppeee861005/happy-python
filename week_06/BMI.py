# BMI(身體質量指數)是WHO認可的健康指數，計算方式：
# BMI = weight(公斤)/height(公尺) ** 2
#
# 體重過輕    BMI < 18.5
# 體重正常    18.5 <= BMI 而且 BMI < 24
# 超重        24 <= BMI 而且 BMI < 28
# 肥胖        BMI >= 28
#
# 寫支程式要求輸入身高(公分)、體重(公斤)
# 依上列公式與標準計算 BMI 指數(小數點2位)，
# 判斷並於螢幕印出 (print) 體重是否正常 如：
#
# BMI= 19.25，體重正常

height_cm = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

height_m = height_cm / 100
bmi = weight / height_m ** 2

if bmi < 18.5:
    status = "體重過輕"
elif bmi < 24:
    status = "體重正常"
elif bmi < 28:
    status = "超重"
else:
    status = "肥胖"

print(f"BMI= {bmi:.2f}，{status}")