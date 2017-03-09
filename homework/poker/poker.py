
class UnknownSuit(Exception):
	pass

class UnknownValue(Exception):
	pass


class Hand(object):
	_values = set(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

	def __init__(self, hand):
		self.cards = hand.split()

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
			if not (value in self._values):
				raise UnknownValue

		if self.cards[-1] == "AH":
			self._rank = "HIGH CARD: Ace of Hearts"
		elif self.cards[-1] == "AS":
			self._rank = "HIGH CARD: Ace of Spades"
		else:
			self._rank = "HIGH CARD: King of Clubs"

	def has_card(self, card):
		return card in self.cards

	def rank(self):
		return self._rank





