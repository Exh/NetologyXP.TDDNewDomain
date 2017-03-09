
class UnknownSuit(Exception):
	pass

class UnknownValue(Exception):
	pass


class Hand(object):
	def __init__(self, hand):
		self.cards = set(hand.split())

		for card in self.cards:
			suit = None
			value = None
			if card[0] == '1' and card[1] == '0':
				value = '10'
				suit = card[2]
			else:
				value = card[0]
				suit = card[1]
			if suit != 'S' and suit != 'H' and suit != 'D' and suit != 'C':
				raise UnknownSuit
			if value != '2' and value != '3' and value != '4' and value != '8' and value != 'A':
				raise UnknownValue


	def has_card(self, card):
		return card in self.cards




