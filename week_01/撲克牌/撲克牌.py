#[隨堂練習]
# 撲克牌遊戲
# 以物件導向方式撰寫程式，制定類別 (Card, Deck, Hand) 存為模組 Card.py。
# 匯入類別模組，建立實體，以物件玩遊戲。
#
# 遊戲規則:
# 1)整副牌包含四個花色(Suites)：
#   4(Spade 黑桃)，3(Heart 紅心)，2(Diamond 方塊)，1(Club 梅花)
#   各花色有數字(Rank)：1~13 (11:Jack, 12:Queen, 13:King)
#   3,2 -「紅心2」、2,4 -「鑽石4」、4,7 -「黑桃7」、1,9 -「梅花9」..等
# 2)各玩家有自己的名字(name：字串)與 一手牌(hand of cards：串列).
# 3)遊戲開始時，會問兩個玩家的名字並安排就位.
# 4)每一回合，隨機發一張牌給每個玩家.
# 5)比較剛發的牌：先比花色大小 (黑桃 > 紅心 > 鑽石 > 梅花)；
#   如果花色相同，再比數字大小。
# 6)拿到較大牌的玩家，將此牌交給牌面較小的玩家.
# 7)當整副牌發完，比較兩位玩家手中牌數，擁有較少牌數的玩家贏得比賽！
#
# 模擬賽局，印出：
#
#      1 號玩家，請輸入你的名字：
#      2 號玩家，請輸入你的名字：
#      回合： 1 ---
#      Tony： 7 of Club
#      Ana： 2 of Heart
#      回合： 2 ---
#      Tony： 3 of Club
#      Ana： 2 of Club
#       ...
#      Game Over..整副牌已經發完
#      Tony 有 22 張牌
#      Ana 有 30 張牌
#      誰贏得比賽？
#      Tony 贏！
#
##########################################################################

from Card import Card, Deck, Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()


# ── 主程式 ────────────────────────────────────────────────
name1 = input("1 號玩家，請輸入你的名字：")
name2 = input("2 號玩家，請輸入你的名字：")

p1   = Player(name1)
p2   = Player(name2)
deck = Deck()

round_num = 0
while not deck.is_empty():
    card1 = deck.deal()
    card2 = deck.deal()
    if card1 is None or card2 is None:
        break

    round_num += 1
    print(f"回合： {round_num} ---")
    print(f"{p1.name}： {card1}")
    print(f"{p2.name}： {card2}")

    if card1 > card2:
        # p1 贏：把自己的牌（較大）交給 p2，p2 收兩張
        p2.hand.add_card(card1)
        p2.hand.add_card(card2)
    elif card2 > card1:
        # p2 贏：把自己的牌（較大）交給 p1，p1 收兩張
        p1.hand.add_card(card1)
        p1.hand.add_card(card2)
    else:
        # 平手：各自保留自己的牌
        p1.hand.add_card(card1)
        p2.hand.add_card(card2)

print("Game Over..整副牌已經發完")
count1 = p1.hand.count()
count2 = p2.hand.count()
print(f"{p1.name} 有 {count1} 張牌")
print(f"{p2.name} 有 {count2} 張牌")
print("誰贏得比賽？")

if count1 < count2:
    print(f"{p1.name} 贏！")
elif count2 < count1:
    print(f"{p2.name} 贏！")
else:
    print("平手！")
