
class Hand(object):
    def __init__(self, hand):
        self.cards = set(hand.split())

    def hasCard(self, card):
        return card in self.cards




