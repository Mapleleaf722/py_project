import collections
import random

Card = collections.namedtuple("Card", ["rank", "suits"])
ranks = [str(i) for i in range(2, 11)] + list("JQKA")
suits = "黑桃 梅花 红心 方块".split()

cards = [Card(suit, rank) for rank in ranks for suit in suits]
print(cards)
# 洗牌
random.shuffle(cards)
print(random.choice(cards))
