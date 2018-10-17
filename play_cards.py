#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck


d1 = CardDeck("Bob")

print(d1)
print(d1.dealer)

d1.shuffle()
print(d1.cards)

hand = []

for i in range(5):
    hand.append(d1.draw())

print(hand)

d2 = CardDeck("Linda")

j1 = JokerDeck("Beth")

j1.shuffle()

print(j1.cards)

