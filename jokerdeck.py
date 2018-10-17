#!/usr/bin/env python

from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _create_deck(self):
        super()._create_deck()
        joker = (None, 'Joker')
        self._cards.append(joker)
        self._cards.append(joker)

