#####################################################################
# Python x ChatGPT
# dict, file 字典與檔案應用
# [作業一]
# 檔案加密
# 使用字典為文字加密、解密
# 1)加密規則：
#     將每個字母向前旋轉3個次序，再對應原順序字元；
#     倒轉以上對照表，未來便可解密。
# 2)原字串(鍵)：
#     ASCII 可列印字元，去除最後3個轉義字元
#     即：string.printable[:-3]
# 3)編碼字典：
#     將每個字元母前轉3個次序，再與原字串對應。
#     (前移後字串 : 原字串) 即：
#     ' '對0, \t對1, \n對2 .. a對d, b對e .. y對B, z對C     
# 輸入：讀入檔案 zenofPython.txt (如附件)
# 輸出：
#      1)印出編碼字典
#      2)印出檔案內原始字串
#      3)印出新加密字串
#      4)印出解密後字串
# (提示：建立密碼字典 - 加密結果 : 原始字元)
#####################################################################
import string
def make_dict(encode=True):
    """
    使用【串列生成式】建立並傳回編碼(True) / 解碼字典(False)
    """
    orig_chars = string.printable[:-3]
    # 旋轉字串：將前 3 個字元移到最後面
    shifted_chars = orig_chars[3:] + orig_chars[:3]
    # 1. 嚴格使用串列生成式 (List Comprehension) 產生元組配對
    if encode:
        list_pair = [(orig, shifted) for orig, shifted in zip(orig_chars, shifted_chars)]
    else:
        list_pair = [(shifted, orig) for orig, shifted in zip(orig_chars, shifted_chars)]  
    # 2. 將串列轉換為字典回傳，方便後續加密查表
    return dict(list_pair)
def encrypt(text, encry_dict):
    """
    使用【串列生成式】依指定之密碼字典加密/解密文字並傳回結果
    """
    # 逐字查表，若字元不在字典中（防呆）則保留原字，最後用 join 拼回字串
    return "".join([encry_dict.get(char, char) for char in text])
# ==========================================
# 主程式執行流程 (4大輸出結果)
# ==========================================
if __name__ == "__main__":
    # 建立密碼字典
    encry_dict = make_dict(encode=True)
    decry_dict = make_dict(encode=False)
    # 輸出 1)：印出編碼字典 (前 15 個項目範例)
    print("1) 印出編碼字典 (部分顯示):")
    print({k: encry_dict[k] for k in list(encry_dict.keys())[:15]}) 
    print("-" * 60)
    # 讀入檔案 zenofPython.txt (若無檔案則模擬預設字串)
    try:
        with open("zenofPython.txt", "r", encoding="utf-8") as f:
            original_text = f.read()
    except FileNotFoundError:
        original_text = "Beautiful is better than ugly.\nExplicit is better than implicit."
    # 輸出 2)：印出檔案內原始字串
    print("2) 印出檔案內原始字串:")
    print(original_text)
    print("-" * 60)
    # 輸出 3)：印出新加密字串
    cipher_text = encrypt(original_text, encry_dict)
    print("3) 印出新加密字串:")
    print(cipher_text)
    print("-" * 60)
    # 輸出 4)：印出解密後字串
    decrypted_text = encrypt(cipher_text, decry_dict) 
    print("4) 印出解密後字串:")
    print(decrypted_text)
    print("-" * 60)
######################################################################
# Python x ChatGPT
# Function, list & dict 函數、串列與字典應用
# [作業二]
# 文字分析
# 輸入：
#    要求輸入檔名，並讀入一個歌詞檔案 (beatles.txt 如附)
# 輸出：
#    1)印出：歌詞共有幾個字？
#    2)印出：歌詞中不同的字數？
#    3)印出：歌詞中每個文字的出現頻率
#    4)印出：出現頻率最高前10名的字、及其出現次數
#####################################################################
import string
def find_words(text):
    """
    將字串改成小寫、移除標點符號，傳回以文字為元素的串列
    """
    text = text.lower()
    # 將所有英文標點符號替換為空格
    for p in string.punctuation:
        text = text.replace(p, " ")
    # split() 會自動忽略連續的多餘空格，精準切出單字
    return text.split()
def frequencies(words):
    """
    建立並傳回文字出現頻率的字典 {單字: 次數}
    """
    hist = {}
    for word in words:
        # 使用 .get() 語法：若無該單字則從 0 開始加 1
        hist[word] = hist.get(word, 0) + 1
    return hist
def ranking(hist):
    """
    傳回以出現頻率由大到小排序的 (頻率, 文字) 串列
    """
    # 轉換成 [(頻率, 文字), ...] 結構
    pairs = [(freq, word) for word, freq in hist.items()]
    # reverse=True 代表由大到小排序
    pairs.sort(reverse=True)
    return pairs
def print_ranking(hist, num=10):
    """
    印出前 num 名最常出現的文字與其出現頻率
    """
    sorted_pairs = ranking(hist)
    top_num = sorted_pairs[:num]
    for rank, (freq, word) in enumerate(top_num, 1):
        print(f"第 {rank:2d} 名：【{word}】出現了 {freq} 次")
def total_words(hist):
    """傳回歌詞總字數"""
    return sum(hist.values())
def different_words(hist):
    """傳回不重複的相異字數"""
    return len(hist)
# ==========================================
# 主程式執行流程
# ==========================================
if __name__ == "__main__":
    filename = input("請輸入歌詞檔名 (例如 beatles.txt): ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lyrics = f.read()
        # 資料處理
        word_list = find_words(lyrics)
        freq_dict = frequencies(word_list)
        # -------------------------------
        # 4 大作業標準輸出
        # -------------------------------
        print("\n" + "="*55)
        print("【文字分析結果】")
        print("="*55)
        # 1) 印出總字數
        print(f"1) 歌詞共有幾個字？\n   答：{total_words(freq_dict)} 個字")
        print("-" * 55)
        # 2) 印出不重複字數
        print(f"2) 歌詞中不同的字數？\n   答：{different_words(freq_dict)} 個字")
        print("-" * 55)
        # 3) 印出每個文字的出現頻率（網格完美對齊版）
        print("3) 歌詞中每個文字的出現頻率：")
        column_width = 16   # 每欄固定寬度
        columns_per_row = 4 # 一行顯示 4 欄
        for i, (word, count) in enumerate(freq_dict.items(), 0):
            item_str = f"{word}: {count}"
            # :<16 代表靠左對齊並補滿 16 格空間
            print(f"{item_str:<{column_width}}", end="")
            # 每 4 個單字換一次行
            if (i + 1) % columns_per_row == 0:
                print()
        print("\n" + "-" * 55)
        # 4) 印出前 10 名
        print("4) 出現頻率最高前 10 名的字、及其出現次數：")
        print_ranking(freq_dict, num=10)
        print("="*55)
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{filename}'，請確認檔案是否存在。")
