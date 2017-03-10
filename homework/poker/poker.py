
class UnknownSuit(Exception):
	pass

class UnknownValue(Exception):
	pass


class Hand(object):
	_values = {'2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Right', '9':'Nine', '10':'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King', 'A':'Ace'}
	_suits = {'H':'Hearts', 'C':'Clubs', 'S':'Spades', 'D':'Diamonds'}

	def __init__(self, hand):
		self.cards = hand.split()

		for card in self.cards:
			ex_res = Hand.extract_value_suit(card)
			value = ex_res[0]
			suit = ex_res[1]

		high_card = self.cards[-1];
		self._rank = "HIGH CARD: " + Hand.card_string(high_card)

		#if self.cards[-1] == "AH":
			#self._rank = "HIGH CARD: Ace of Hearts"
		#elif self.cards[-1] == "AS":
			#self._rank = "HIGH CARD: Ace of Spades"
		#elif self.cards[-1] == "KC":
			#self._rank = "HIGH CARD: King of Clubs"
		#else:
			#self._rank = "HIGH CARD: Queen of Diamonds"

	def has_card(self, card):
		return card in self.cards

	@staticmethod
	def extract_value_suit(card):
		suit = None
		value = None
		if card[0] == '1' and card[1] == '0':
			value = '10'
			suit = card[2]
		else:
			value = card[0]
			suit = card[1]

		if not (suit in Hand._suits):
			raise UnknownSuit
		if not (value in Hand._values):
			raise UnknownValue

		return (value, suit)

	@staticmethod
	def card_string(card):
		temp = Hand.extract_value_suit(card)
		value = Hand._values[temp[0]]
		suit  =	Hand._suits[temp[1]]
		return value + " of " + suit

	def rank(self):
		return self._rank





