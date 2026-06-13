
####################################################################
# Python x ChatGPT
# random, loop, list & function 隨機數、迴圈、串列與函數
# [專題]
# 產生一副撲克牌
# 構想將撲克牌以數值編號，可以比大小
# - 花色(Suite)：4(Spade 黑桃)，3(Heart 紅心)，
#               2(Diamond 鑽石)，1(Club 梅花)
# - 數字(Rank)：2~14 (11:Jack, 12:Queen, 13:King, 14:Ace)
# - 花色 / 數字 與編號間的對照表 (tuple 元組型態) 如下
# 問題：
#   撰寫函數 card_name(card)：
#   1)參數 card：撲克牌數值編號，如：411
#   2)傳回：查核對照表得出牌名，如：SpadeJack
# 輸出：
#   1)印出整副牌的數值編號：
#     (為 402..~ 414, 302..~ 314, 202..~ 214, 102..~ 114)
#   2)印出洗牌後的整副牌
#   3)洗牌後隨機發一張牌，叫出牌名 
#     (如：隨機抽發一張牌 411 - SpadeJack)
# <加分題>
# 撰寫撲克牌遊戲(規則):
# 1)遊戲開始，問兩個玩家的名字並安排就位.
# 2)每一回合，隨機發一張牌給每個玩家.
# 3)比較剛發的牌：先比花色；如果相同，再比數字大小
# 4)拿到較大牌的玩家，將此牌交給牌面較小的玩家.
# 5)當整副牌發完，比較兩位玩家手中牌數，擁有較少牌數的玩家贏得比賽！  
#####################################################################
import random

# ==========================================
# 全域對照表定義 (Tuple 元組型態)
# ==========================================
suites = ((1, 'Club'), (2, 'Diamond'), (3, 'Heart'), (4, 'Spade'))
ranks = ((11, 'Jack'), (12, 'Queen'), (13, 'King'), (14, 'Ace'))

# ==========================================
# 核心函數實作
# ==========================================

def lookup(num, table):
    '''
    到指定的表格找出傳入數字所對應的字串並回傳
    若找不到（例如數字 2~10），則直接回傳該數字的字串
    :param int num
    :param tuple table
    :return str: the value against num
    '''
    for item in table:
        if item[0] == num:
            return item[1]
    return str(num)


def card_name(card):
    '''
    查出傳入之一張牌(數值編號)的牌名並回傳
    :param int card: 如 411
    :return str: name of the card, 如 SpadeJack
    '''
    suite_num = card // 100  # 取得百位數（花色）
    rank_num = card % 100    # 取得十位與個位數（數字）
    
    suite_str = lookup(suite_num, suites)
    rank_str = lookup(rank_num, ranks)
    
    return f"{suite_str}{rank_str}"


def cards_names(cards):
    '''
    查出傳入之整副牌(數值編號)的牌名並回傳
    :param list cards: number-coded cards
    :return list: card names
    '''
    return [card_name(c) for c in cards]


def whole_deck():
    '''
    產生整副牌(數值編號)並傳回
    :return list: the whole deck (402~414, 302~314, 202~214, 102~114)
    '''
    deck = []
    # 花色從 4 到 1 (Spade, Heart, Diamond, Club)
    for s in range(4, 0, -1):
        # 數字從 2 到 14 (14 代表 Ace)
        for r in range(2, 15):
            deck.append(s * 100 + r)
    return deck


def pop_card(cards, i=-1):
    '''
    傳入之整副牌(數值編號)於洗牌後抽出指定
    索引的牌並回傳；若未指定則為最後那張。
    :param list of int cards
    :param int i: index of the cards
    :return int: code of the card popped
    '''
    if not cards:
        return None
    return cards.pop(i)


# ==========================================
# <加分題> 撲克牌遊戲邏輯
# ==========================================

def play_game():
    print("\n" + "="*10 + " 撲克牌遊戲開始 " + "="*10)
    
    # 1) 遊戲開始，問兩個玩家的名字並安排就位
    player1 = input("請輸入玩家 1 的名字: ")
    player2 = input("請輸入玩家 2 的名字: ")
    
    p1_hand = []
    p2_hand = []
    
    # 準備一副全新的牌並洗牌
    game_deck = whole_deck()
    random.shuffle(game_deck)
    
    round_num = 1
    
    # 2) 每一回合，隨機發一張牌給每個玩家 (發完為止)
    while len(game_deck) >= 2:
        print(f"\n--- 回合 {round_num} ---")
        card1 = pop_card(game_deck)
        card2 = pop_card(game_deck)
        
        # 查詢兩張牌的牌名
        name1 = card_name(card1)
        name2 = card_name(card2)
        
        print(f"{player1} 抽到: {card1} ({name1})")
        print(f"{player2} 抽到: {card2} ({name2})")
        
        # 3) 比較剛發的牌：先比花色；如果相同，再比數字大小
        # (因為編號百位數是花色、低位數是數字，直接比大小即符合規則)
        if card1 > card2:
            print(f"結果: {player1} 的牌較大！")
            # 4) 拿到較大牌的玩家，將此牌交給牌面較小的玩家
            p2_hand.append(card1)
            print(f"★ {player1} 將 {name1} 交給了 {player2}")
        else:
            print(f"結果: {player2} 的牌較大！")
            p1_hand.append(card2)
            print(f"★ {player2} 將 {name2} 交給了 {player1}")
            
        round_num += 1

    # 5) 當整副牌發完，比較兩位玩家手中牌數，擁有較少牌數的玩家贏得比賽！
    print("\n" + "="*10 + " 遊戲結束 " + "="*10)
    print(f"{player1} 手中剩餘牌數: {len(p1_hand)} 張")
    print(f"{player2} 手中剩餘牌數: {len(p2_hand)} 張")
    
    if len(p1_hand) < len(p2_hand):
        print(f"🏆 恭喜 【{player1}】 贏得比賽！(牌數較少)")
    elif len(p2_hand) < len(p1_hand):
        print(f"🏆 恭喜 【{player2}】 贏得比賽！(牌數較少)")
    else:
        print("雙方牌數相同，平手！")


# ==========================================
# 主程式執行 (基礎題輸出 + 啟動遊戲)
# ==========================================
if __name__ == "__main__":
    # 1) 印出整副牌的數值編號
    deck = whole_deck()
    print("1) 整副牌的數值編號：")
    print(deck)
    print("-" * 50)
    
    # 2) 印出洗牌後的整副牌
    random.shuffle(deck)
    print("2) 洗牌後的整副牌：")
    print(deck)
    print("-" * 50)
    
    # 3) 洗牌後隨機發一張牌，叫出牌名 
    sampled_card = pop_card(deck)
    print("3) 隨機抽發一張牌：")
    print(f"{sampled_card} - {card_name(sampled_card)}")
    print("-" * 50)
    
    # 啟動加分題遊戲
    play_game()





