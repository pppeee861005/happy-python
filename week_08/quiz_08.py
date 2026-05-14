##################################################################
# Python x ChatGPT
# 串列與迴圈 List & loop
# [練習一]
# 哪個第 k 大？ The kth Largest
# 問題：請參考以迴圈找最大值的方法，
#       撰寫函數找出參數 (數列) 中第 k 大數字
#       (不使用內建函數 sort/max)
# 已知：串列 nums 內含未排序的一串數字(如下)
#       k：任一正整數 (如：5)
# 輸出：印出串列中第 k (如：5) 大的數字為：
# (提示：以 k 個位置存放前 k 大的數字)
###################################################################

nums = [30, 3, 8, 20, 25, 21, 25, 10, 7, 18]

def find_kth(nums, k):
    """
    Return the kth largest number
    :param (list of float) nums: sequence of numbers
    :param (int) k: for the kth largest
    :return (float): the kth largest number
    """
    # 1) 建立一個長度為 k 的串列來存放目前看到的前 k 大數字
    # 初始化為極小值 (如負無窮大)
    k_largest = [float('-inf')] * k
    
    for n in nums:
        # 2) 如果目前的數字比排行榜中最小的 (最後一個) 還大
        if n > k_largest[k-1]:
            # 先取代最後一個位置
            k_largest[k-1] = n
            # 3) 模擬排序：將新進榜的數字往「前」移動到正確位置 (由大到小)
            # 就像氣泡排序的一小部分，確保排行榜有序
            for i in range(k-1, 0, -1):
                if k_largest[i] > k_largest[i-1]:
                    # 交換位置
                    k_largest[i], k_largest[i-1] = k_largest[i-1], k_largest[i]
                else:
                    # 已經找到位置，提早結束內部迴圈
                    break
    # 4) 排行榜的最後一個元素即為第 k 大
    return k_largest[k-1]

# 測試執行
k = 5
result = find_kth(nums, k)
print(f"串列中第 {k} 大的數字為：{result}")
####################################################################
# Python x ChatGPT
# Algorithm, loop, conditional - 演算法、迴圈、條件式
# [練習二]
# 問題：破解通關密碼
# 已知：
#  1) 正整數五位數的密碼 ABCDE
#  2) ABCDE * A = EEEEEE (每個字母代表一個數字)
#  3) 五個字母代表的數字之間互不相等
# 輸出：請印出密碼值 (ABCDE)
# (提示): 使用猜測與查驗法 (窮舉法) 
#####################################################################
def crack_password():
    # 窮舉所有的五位數 ABCDE (10000 到 99999)
    for abcde in range(10000, 100000):
        # 拆解每個位數
        s_abcde = str(abcde)
        a = int(s_abcde[0])
        b = int(s_abcde[1])
        c = int(s_abcde[2])
        d = int(s_abcde[3])
        e = int(s_abcde[4])
        # 條件 1：五個字母代表的數字互不相等
        # 利用 set (集合) 的特性來檢查是否有重複數字
        if len(set(s_abcde)) == 5:
            # 條件 2：計算 EEEEEE
            # EEEEEE = e * 111111 (例如 e=7, 則為 777777)
            eeeeee = e * 111111
            # 條件 3：驗證 ABCDE * A = EEEEEE
            if abcde * a == eeeeee:
                print(f"找到密碼了！")
                print(f"密碼 ABCDE 為：{abcde}")
                print(f"驗證：{abcde} * {a} = {eeeeee}")
                return # 找到後即可停止
# 執行程式
crack_password()
#####################################################################
# Python x ChatGPT
# loop, list & zip 迴圈與串列應用
# [練習三]
# 以天干、地支來排甲子
# 已知：
#   天干(tiangan)：'甲'~'癸' 計 10 個元素(如下)
#   地支(dizhi)：'子'~'亥' 計 12 個元素(如下)
# 輸出：
#   1)天干與地支配對排列，即：'甲子'、'乙丑' .. '癸酉'
#   2)然後是：'甲戌'、'乙亥'、'丙子' .. 接續排列
#   3)排列至 '癸亥'(下個'甲子'之前)為止，並印出結果(共 60 個配對)
# (提示)：使用 zip() 函數
######################################################################

tiangan = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
dizhi = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

# 1. 將天干重複 6 次，地支重複 5 次，使兩者長度都達到 60
full_tiangan = tiangan * 6
full_dizhi = dizhi * 5
# 2. 使用 zip() 將兩者配對
# 3. 使用列表推導式 (List Comprehension) 將元組組合成字串
jiazi_60 = [t + d for t, d in zip(full_tiangan, full_dizhi)]
# 輸出結果
print(f"六十甲子列表 (共 {len(jiazi_60)} 個)：")
# 為了方便閱讀，每 10 個換一行
for i in range(0, 60, 10):
    print(jiazi_60[i:i+10])
###########################################################################

