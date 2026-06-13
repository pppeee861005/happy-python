################################################################
# Python x ChatGPT
# lambda & function object 匿名函數與函數當作引數
# [練習一]
# 學校成績系統：
#   撰寫函數：grade(func, file)
#   '''讀檔、呼叫函數、傳回計算結果
#      func：函數名稱；file：檔案路徑'''
# 請另撰寫三個函數(參數 nums 為串列)：
#   1) average(nums)：計算所有學生分數的平均
#   2) best(nums)：找出最高分
#   3) failed(nums) ：統計不及格(<60)學生的數量
# 輸入：
#       學生分數檔案：allscores.txt (如附件)
#       (每行一位學生的分數)
# 輸出：
#       ****** 歡迎使用成績系統！******
#       1: 計算所有學生分數的平均：
#       2: 找出最高分：
#       3: 統計不及格(<60)學生的人數：
#       *******************************
#       使用 grade(func, file) 讀入檔案，
#       執行使用者所選擇的功能 (上列三種功能)。
#
#       例如 grade(best, filename)
#            傳回結果並印出：找出最高分： 100
# (提示)：讀取檔案全部資料，並建立以行為元素的串列
#        fin = open(filename)
#        all_scores = fin.readlines()
################################################################
def average(nums):
    """
    計算所有學生分數的平均
    :param (list) nums: scores of all students
    :return (float): average score
    """
    if not nums:
        return 0.0
    return sum(nums) / len(nums)
def best(nums):
    """
    找出最高分
    :param (list) nums: scores of all students
    :return the highest score
    """
    if not nums:
        return 0
    return max(nums)
def failed(nums):
    """
    統計不及格(<60)學生的數量
    :param (list) nums: scores of all students
    :return (int): number of those who don't pass
    """
    failed_students = [score for score in nums if score < 60]
    return len(failed_students)
def grade(func, file):
    """
    讀檔、呼叫函數、傳回計算結果
    :param (obj) func：函數名稱
    :param (str) file：檔案路徑
    """
    try:
        # 使用 utf-8 或是 cp950 (Windows 預設繁中編碼) 讀取檔案
        with open(file, 'r', encoding='utf-8') as fin:
            all_lines = fin.readlines()
            # 清理資料並轉為整數串列
            all_scores = [int(line.strip()) for line in all_lines if line.strip()]
            # 執行對應函數並回傳結果
            return func(all_scores)
    except FileNotFoundError:
        print(f"\n錯誤：找不到檔案！請確認路徑是否正確：\n{file}")
        return None
    except ValueError:
        print("\n錯誤：檔案內包含無法轉換為數字的字元，請檢查檔案內容。")
        return None
# --- 主程式：系統選單與功能執行 ---
if __name__ == "__main__":
    # 使用 r"" 確保 Windows 路徑中的反斜線不會造成轉義錯誤
    filename = r"E:\Python Project\Play Ground\week_10\allscores.txt"
    print("****** 歡迎使用成績系統！******")
    print(" 1: 計算所有學生分數的平均")
    print(" 2: 找出最高分")
    print(" 3: 統計不及格(<60)學生的人數")
    print("*******************************")
    choice = input("請選擇功能 (1/2/3): ").strip()
    if choice == "1":
        avg_score = grade(average, filename)
        if avg_score is not None:
            print(f"計算所有學生分數的平均： {avg_score:.2f}")
    elif choice == "2":
        highest_score = grade(best, filename)
        if highest_score is not None:
            print(f"找出最高分： {highest_score}")
    elif choice == "3":
        failed_count = grade(failed, filename)
        if failed_count is not None:
            print(f"統計不及格(<60)學生的人數： {failed_count}")
    else:
        print("無效的選擇，請輸入 1, 2 或 3。")
###############################################################
# Python x ChatGPT
# decorator & function object 修飾器與函數當作引數
# [練習二]
# 以修飾器增添除錯功能：
# 已知：
#     函數：mydiv(x, y)
#      '''x, y：float 數值；
#         傳回：float 除法結果 x/y'''
# 動作：
#     請設計修飾器 @errcheck 增加除數為 0 的檢查功能
# 輸出：
#     請印出 mydiv(6, 2)、mydiv(6, 0) 的結果
#     如：print(mydiv(6, 0) 時，印出以下
#        函數名稱：mydiv
#        函數參數：(6, 0)
#        執行結果：除數不可為 0
#        除數不可為 0
################################################################
def errcheck(func):
    """
    修飾器：用來檢查除數是否為 0，並印出詳細的偵錯訊息
    """
    def wrapper(*args, **kwargs):
        # 題目要求 mydiv(x, y)，這裡 args[1] 代表第二個參數 y (也就是除數)
        # 為了通用性，也可以檢查 kwargs 裡面的 'y'
        divisor = args[1] if len(args) > 1 else kwargs.get('y', None)
        if divisor == 0:
            print(f"函數名稱：{func.__name__}")
            # 印出位置引數 (args)，格式剛好會是 (6, 0) 這樣的元組 (tuple)
            print(f"函數參數：{args}")
            print("執行結果：除數不可為 0")
            return "除數不可為 0"
        # 如果除數不為 0，則正常執行原本的函數
        return func(*args, **kwargs)
    return wrapper
@errcheck
def mydiv(x, y):
    """
    執行除法運算
    """
    return x / y
# --- 測試輸出 ---
print("--- 測試一：mydiv(6, 2) ---")
result1 = mydiv(6, 2)
print(f"回傳結果：{result1}\n")

print("--- 測試二：mydiv(6, 0) ---")
result2 = mydiv(6, 0)
print(f"回傳結果：{result2}")

