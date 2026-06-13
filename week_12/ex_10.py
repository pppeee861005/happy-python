########################################################################
# Python x ChatGPT
# Capstone project - 字串、程式配置
# [作業一]
# 名字混搭 Name Mashup
# 要求使用者輸入兩組名與姓 (FIRST LAST)
# 程式重組兩個名(FIRST)及兩個姓(LAST)，並輸出兩組混搭的名與姓如下：
#   1)第一組名與姓的左半部 + 第二組名與姓的右半部
#   2)第二組名與姓的左半部 + 第一組名與姓的右半部
#   3)中間點的索引為字串長度除以2的商值。
#     (如：name 字串前半部為 name[:len(name) // 2]
# 舉例：使用者輸入兩組姓名： Aqua Man 與 Cat Woman，
#       輸出新的兩組混搭姓名： Aqat Mman 與 Cua Woan
########################################################################
# 讓使用者輸入兩組姓名 (格式：FIRST LAST)
name1 = input("請輸入第一組名與姓 (例如 Aqua Man): ")
name2 = input("請輸入第二組名與姓 (例如 Cat Woman): ")
# 使用 split() 將名與姓分開
first1, last1 = name1.split()
first2, last2 = name2.split()
# --- 處理「名 (First)」的混搭 ---
# 計算兩個名的中間點索引
mid_f1 = len(first1) // 2
mid_f2 = len(first2) // 2
# 混搭名：前半部 + 後半部
new_first1 = first1[:mid_f1] + first2[mid_f2:]
new_first2 = first2[:mid_f2] + first1[mid_f1:]
# --- 處理「姓 (Last)」的混搭 ---
# 計算兩個姓的中間點索引
mid_l1 = len(last1) // 2
mid_l2 = len(last2) // 2
# 混搭姓：前半部 + 後半部
new_last1 = last1[:mid_l1] + last2[mid_l2:]
new_last2 = last2[:mid_l2] + last1[mid_l1:]
# --- 輸出結果 ---
print("\n--- 混搭結果 ---")
print(f"第一組混搭姓名: {new_first1} {new_last1}")
print(f"第二組混搭姓名: {new_first2} {new_last2}")
########################################################################
# Python x ChatGPT
# Capstone project - String, Loop 字串、迴圈
# [作業二]
# 拼字遊戲 Scrabble
# 已知 (輸入)：
# 1) 藝術相關的有效詞庫 words：
#    儲存型態：長字串，每個詞一行 (如下)
# 2) 不定數量的字塊組(字母方塊組) tiles：
#    儲存型態：字串，每一字元為一個字塊 (如下)
# 輸出：找到詞庫內所有可以使用字塊組內的字元拼出來的詞。
#   - 有效詞庫為：
#   - 現有字塊為：
#   - 可以拼出的詞為：
# (此範例)：可以拼出的詞為：('ink',)
# (注意)：詞中若出現重複字母，必須有足夠數量的字塊來拚
#########################################################################
# 1. 定義有效詞庫與現有字塊
words = """
    art
    hue
    ink
    paint
    music
    poetry
    dance
    film
    skill
"""
tiles = "hijklmnosfp"
# 2. 資料清理：將長字串拆分成獨立單字的清單，並去除空白
# split() 預設會依據換行與空白字元進行拆分
word_list = words.split()
# 儲存符合條件的單字
valid_words = []
# 3. 使用迴圈檢查每個單字
for word in word_list:
    can_make = True  # 預設這個單字是可以拼出來的
    # 檢查單字中的每一個字母
    for char in word:
        # 如果單字中該字母需要的數量，大於字塊中現有的數量，就無法拼出
        if word.count(char) > tiles.count(char):
            can_make = False
            break  # 只要有一個字母不符合，就可以跳出內層迴圈
    # 如果檢查完所有字母都過關，就加入結果清單
    if can_make:
        valid_words.append(word)
# 4. 依照題目格式輸出結果
print(f"有效詞庫為：{word_list}")
print(f"現有字塊為：{tiles}")
# 題目範例要求以 tuple 格式輸出符合的詞
print(f"可以拼出的詞為：{tuple(valid_words)}")


