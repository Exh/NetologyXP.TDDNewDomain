
class UnknownSuit(Exception):
    pass


class Hand(object):
    def __init__(self, hand):
        self.cards = set(hand.split())

        for card in self.cards:
            if card[1] != 'S' and card[1] != 'H' and card[1] != 'D' and card[1] != 'C':
                raise UnknownSuit

    def has_card(self, card):
        return card in self.cards




