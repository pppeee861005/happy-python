import random


class Card:
    SUITES = {1: 'Club', 2: 'Diamond', 3: 'Heart', 4: 'Spade'}
    RANKS  = {11: 'Jack', 12: 'Queen', 13: 'King'}

    def __init__(self, suite, rank):
        self.suite = suite  # 1=Club, 2=Diamond, 3=Heart, 4=Spade
        self.rank  = rank   # 1~13

    def __str__(self):
        rank_str = self.RANKS.get(self.rank, str(self.rank))
        return f"{rank_str} of {self.SUITES[self.suite]}"

    def __gt__(self, other):
        if self.suite != other.suite:
            return self.suite > other.suite
        return self.rank > other.rank

    def __lt__(self, other):
        if self.suite != other.suite:
            return self.suite < other.suite
        return self.rank < other.rank

    def __eq__(self, other):
        return self.suite == other.suite and self.rank == other.rank


class Deck:
    def __init__(self):
        self.cards = [Card(suite, rank)
                      for suite in range(1, 5)
                      for rank  in range(1, 14)]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

    def is_empty(self):
        return len(self.cards) == 0


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def count(self):
        return len(self.cards)
