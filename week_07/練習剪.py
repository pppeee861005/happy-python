# =====================================================
# 函數 1：讓使用者出拳
# =====================================================
def player_choice():
    """取得玩家輸入，回傳整數 1/2/3，輸入錯誤回傳 None"""
    print("1(剪刀)、2(石頭)、3(布)？")
    user_input = input("你出： ")
    
    # 檢查是否為合法輸入
    if user_input in ["1", "2", "3"]:
        return int(user_input)
    else:
        return None  # 來亂的
    
def Player_choice():
    """取得玩家輸入，回傳整數 1/2/3，輸入錯誤回傳 None"""
    print("1(剪刀)、2(石頭)、3(布) ?")
    user_input = input("您出: ")
    
    # 檢查是否為合法輸入
    if user_input in ["1", "2", "3"]:
        return int(user_input)
    else:
        return None  # 來亂的

def player_choice():
    """取得玩家輸入，回傳整數 1/2/3，輸入錯誤回傳 None
    """
    print("1(剪刀)、2(石頭)、3(布)？")
    user_input = input("你出： ")
    
    # 檢查是否為合法輸入
    if user_input in ["1", "2", "3"]:
        return int(user_input)
    else:
        return None  # 來亂的
    
def player_choice():
    """取得玩家輸入，回傳整數 1/2/3，輸入錯誤回傳 None"""
    print("1剪刀、2石頭、3布 ?")
    user_input = input("你輸入 ?")
    
    # 檢查是否為合法輸入
    if user_input in ["1", "2", "3"]:
        return int(user_input)
    else:
        return None #來亂的 哈哈
    
def player_choice():
    """玩家輸入什麼123，並查檢，錯的話傳none
    """    
    print("1剪刀、2石頭、3布 ?")
    user_input = input(你出什麼 ?)
    
    #查有沒有輸錯
    if user_input in ["1","2","3"]
        return user_input
    else:
        return None #來亂的西西
    

def player_cgoice():
    """玩家輸入，去得123整數，查是不是錯的，錯了傳none"""
    print("1剪刀、2石、3布 :")
    user_input = input("你要出什麼 ?")
    

# =====================================================
# 函數 2：電腦隨機出拳
# =====================================================
import random

def computer_choice():
    """電腦隨機出123
    """
    
    return random.randint(1,3)

def computer_choice():
    """電腦123隨便出
    """
    
    return random.randint(1,3)