#!/usr/bin/env python
import random

class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer_name):
        self.dealer = dealer_name
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer_name):
        if isinstance(dealer_name, str):
            self._dealer = dealer_name
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)


    def draw(self):
        return self._cards.pop()
