"""
    >>> card = Card('7', 'cats')
    >>> print(card)
    Card(rank='7', suit='cats')

"""


import collections
from itertools import product
from random import choice

# Create a class and its attributes
Card = collections.namedtuple('Card', ['rank', 'suit'])

"""
Instead of using the function "namedtuple", you can create your own class as below: 

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f'Carta(valor={self.valor}, naipe={self.naipe})'
"""


class FrenchDeck:
    _ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    _suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank, suit in product(self._ranks, self._suits)]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value


if __name__ == '__main__':
    for card in FrenchDeck():
        print(card)

    print()
    deck = FrenchDeck()

    print("Length of deck")
    print(len(deck))

    print("\nSlicing...")
    print(deck[0])

    print("\nRandom choice using the library random")
    print(choice(deck))
