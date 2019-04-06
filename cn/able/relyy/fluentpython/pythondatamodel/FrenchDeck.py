import collections

# 生成一张牌
Card = collections.namedtuple('Card',['rank','suit'])

## 生成一副扑克牌
class FrenchDeck:

    ranks = [str(n) for n in range(2,11)] + list('JQKA')

    # 扑克牌花色 spades:黑桃 diamonds 方块 clubs 梅花 hearts 红桃
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7','diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[4])

## 随机抽取一张
from random import choice
print(choice(deck))

# 集合没有实现__contains__方法，可以使用in进行一次迭代搜索检查是否包含指定元素
print(Card('Q','hearts') in deck)
print(Card('q','hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_values = FrenchDeck.ranks.index(card.rank)
    return rank_values * len(suit_values) + suit_values[card.suit]
for card in sorted(deck, key=spades_high):
    print(card)

