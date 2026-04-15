這個檔案定義了三個類別，是整個撲克牌遊戲的核心模組。

  ---
  一、Card 類別（一張牌）

  class Card:
      SUITES = {1: 'Club', 2: 'Diamond', 3: 'Heart', 4: 'Spade'}
      RANKS  = {11: 'Jack', 12: 'Queen', 13: 'King'}
  - 類別變數（所有牌共用）
  - 花色和特殊點數的對照表

  ---
  __init__ — 建立一張牌

  def __init__(self, suite, rank):
      self.suite = suite  # 1=Club, 2=Diamond, 3=Heart, 4=Spade
      self.rank  = rank   # 1~13
  - suite：花色（1~4，數字越大花色越大）
  - rank：點數（1~13）

  ---
  __str__ — 印出牌的名稱

  def __str__(self):
      rank_str = self.RANKS.get(self.rank, str(self.rank))
      return f"{rank_str} of {self.SUITES[self.suite]}"

  ┌──────┬────────────────────┬──────────────────┐
  │ 點數 │  RANKS.get() 結果  │       輸出       │
  ├──────┼────────────────────┼──────────────────┤
  │ 7    │ 找不到 → 用 str(7) │ "7 of Club"      │
  ├──────┼────────────────────┼──────────────────┤
  │ 11   │ 找到 → "Jack"      │ "Jack of Spade"  │
  ├──────┼────────────────────┼──────────────────┤
  │ 12   │ 找到 → "Queen"     │ "Queen of Heart" │
  └──────┴────────────────────┴──────────────────┘

  ---
  比較方法

  def __gt__(self, other):          # card1 > card2
      if self.suite != other.suite:
          return self.suite > other.suite
      return self.rank > other.rank

  def __lt__(self, other):          # card1 < card2
      if self.suite != other.suite:
          return self.suite < other.suite
      return self.rank < other.rank

  def __eq__(self, other):          # card1 == card2
      return self.suite == other.suite and self.rank == other.rank

  比較邏輯：先比花色，花色相同再比點數

  花色大小：Club(1) < Diamond(2) < Heart(3) < Spade(4)
  點數大小：1 < 2 < 3 < ... < 13

  ---
  二、Deck 類別（整副牌）

  class Deck:
      def __init__(self):
          self.cards = [Card(suite, rank)
                        for suite in range(1, 5)
                        for rank  in range(1, 14)]
          random.shuffle(self.cards)

  用雙層迴圈產生 52 張牌，然後洗牌：

  suite=1, rank=1~13  →  13張梅花
  suite=2, rank=1~13  →  13張方塊
  suite=3, rank=1~13  →  13張紅心
  suite=4, rank=1~13  →  13張黑桃
                          ────────
                          共 52 張

  ---
  deal() — 發牌

  def deal(self):
      return self.cards.pop() if self.cards else None
  - 有牌 → pop() 取出最上面一張（同時從牌堆移除）
  - 沒牌 → 回傳 None

  ---
  is_empty() — 檢查是否發完

  def is_empty(self):
      return len(self.cards) == 0
  - 牌堆空了回傳 True，否則 False

  ---
  三、Hand 類別（玩家手牌）

  class Hand:
      def __init__(self):
          self.cards = []

      def add_card(self, card):
          self.cards.append(card)

      def count(self):
          return len(self.cards)

  ┌────────────────┬──────────────────┐
  │      方法      │       功能       │
  ├────────────────┼──────────────────┤
  │ __init__       │ 建立空的手牌串列 │
  ├────────────────┼──────────────────┤
  │ add_card(card) │ 把一張牌加入手牌 │
  ├────────────────┼──────────────────┤
  │ count()        │ 回傳目前手牌張數 │
  └────────────────┴──────────────────┘

  ---
  三個類別的關係

  Deck（牌堆）
    │  deal() 發牌
    ▼
  Card（一張牌）  ──比較大小──►  Card
    │  add_card()
    ▼
  Hand（手牌）
    │  count()
    ▼
   張數（決定勝負）