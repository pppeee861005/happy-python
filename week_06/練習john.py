data_list = []

while True:
    user_input = input(">>").split()
    
    user_input = input("請輸入資料 (或輸入 'q' 退出): ")
    if user_input.lower() == 'q':
        break