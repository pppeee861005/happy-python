
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