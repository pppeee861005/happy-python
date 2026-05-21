#############################################################
# Python x ChatGPT
# 迴圈與if敘述 Loop & Conditional
# [作業一]
# 1)已知串列如下，請撰寫程式刪除list中所有負數，
#   並印出結果串列。
#     x = [1, 3, 5, 0, -1, 3, -2]
# 2)已知串列如下，請撰寫程式計算並印出
#   list中負數的總個數。
#     y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
##############################################################
x = [1, 3, 5, 0, -1, 3, -2]
result = []  # 準備一個空籃子放正確的數字
for num in x:
    if num >= 0:      # 如果數字是大於等於 0 的正數或零
        result.append(num)  # 加入籃子中
x = result  # 把篩選好的結果回傳給 x
print(f"(1)刪除負數後的結果為：{x}")
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count = 0  # 用來計數的變數
# 第一層迴圈：取出 y 裡面的每個子串列
for sublist in y:
    # 第二層迴圈：取出子串列中的每個數字
    for num in sublist:
        if num < 0:    # 檢查是否為負數
            count += 1  # 是的話，計數器加 1

print(f"(2)串列中負數的總個數為：{count}")
##############################################################
# Python x ChatGPT
# Encription - slicing
# [作業二]
# 文件加密
# 最簡單的加密是將每個英文字元在 26 個英文字母
# (大、小寫各 26 個)中旋轉往前移，對應至不同字母；
# 記住所對應字母，未來便可解密。
# 如 加密方式：將每個字元前移 3 個在英文字母中的次序，
# 即：a對應到d；b對e； .. x對a；y對b；z對c
# 請撰寫程式加密以下輸入字串：
#   1) "abcdefghijklmnopqrstuvwxyz" 前移 3
#   2) "cheer" 前移 7
#   3) "melon" 後移 10
#   4) "sleep" 前移 9
# 印出：1)輸入字串 與 2)加密字串
# (如)：
# 輸入字串：cheer 移動位數 7
# 加密字串：jolly
# (提示)：化整為零，先寫個函數可以移動字元(字母)，
#         再在移動字串時呼叫此函數。
###############################################################
def encrypt_text(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text:
        if char in alphabet:
            # 1. 找出原字母在 alphabet 中的索引
            old_index = alphabet.find(char)
            # 2. 計算新索引 (加上位移量後對 26 取餘數，達成循環)
            new_index = (old_index + shift) % 26
            # 3. 取得新字母
            result += alphabet[new_index]
        else:
            # 如果不是小寫字母（如空白或符號），維持原狀
            result += char
    return result
# 測試資料
tasks = [
    ("abcdefghijklmnopqrstuvwxyz", 3),
    ("cheer", 7),
    ("melon", -10), # 後移可以用負數表示
    ("sleep", 9)
]

# 執行並印出結果
for original_str, move in tasks:
    encrypted_str = encrypt_text(original_str, move)
    print(f"輸入字串：{original_str} 移動位數 {move}")
    print(f"加密字串：{encrypted_str}")
###############################################################
# Python x ChatGPT
# String parse - 字串與迴圈
# [作業三]
# 文字檔解析
# 問題：撰寫程式仿照 UNIX 中 wc 公用程式解析文字檔
# 輸入：
#     讀入檔案：word_count.txt
# 輸出：
#     檔案中共有 {} 行，{} 個字，{} 個字元(不含標點符號)
# (請使用下列兩行敘述讀取檔案，因為還沒講到)
################################################################
# 自動產生測試檔案，確保程式能跑
content = """Python provides a complete set of control flow elements,
including while and for loops, and conditionals.
Python uses the level of indentation to group blocks
of code with control elements."""
with open('word_count.txt', 'w', encoding='utf-8') as f:
    f.write(content)
# --- 以下是你原本的作業程式碼 ---
infile = open('word_count.txt')      # 現在就不會報錯了
lines = infile.read().split("\n")
# 2. 初始化計數器
line_count = len(lines)  # 行數即為串列的長度
word_count = 0
char_count = 0
# 定義要排除的標點符號 (依作業要求不含標點符號)
punctuations = ",.[]:0123456789" 
# 3. 處理每一行
for line in lines:
    # --- 計算單字 ---
    # 使用 split() 會自動以空白切割字串，回傳單字串列
    words = line.split()
    word_count += len(words)
    # --- 計算字元 ---
    for char in line:
        # 檢查字元是否為字母或數字(若要更嚴格，可用 isalnum() 或比對排除表)
        # 這裡排除空白與定義的標點符號
        if char != " " and char not in punctuations:
            char_count += 1
# 4. 印出結果
print(f"檔案中共有 {line_count} 行，{word_count} 個字，{char_count} 個字元(不含標點符號)")


