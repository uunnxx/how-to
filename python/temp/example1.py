import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


beer_card = Card('7', 'diamonds')
print(beer_card)
print(len(beer_card))


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    @staticmethod
    def tt(self, a):
        return a


deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[1])
print(deck[2])
print(deck[3])
print(deck[4])
print(deck[5])
print(deck[6])
print(deck[7])
print(deck[8])
print(deck[9])
print(deck[10])
print(deck[11])
print(deck[12])

print(deck[13])


def main(a: int) -> int:
    return a

