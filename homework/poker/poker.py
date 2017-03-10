
class UnknownSuit(Exception):
	pass

class UnknownValue(Exception):
	pass


class Hand(object):
	_values = {'2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Right', '9':'Nine', '10':'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King', 'A':'Ace'}
	_suits = {'H':'Hearts', 'C':'Clubs', 'S':'Spades', 'D':'Diamonds'}

	def __init__(self, hand):
		self.cards = hand.split()
		self.values = []

		for card in self.cards:
			ex_res = Hand.extract_value_suit(card)
			value = ex_res[0]
			suit = ex_res[1]
			self.values.append(value)

		pair = self.has_pair()
		if pair:
			self._rank = "PAIR: " + pair[0] + " " + pair[1]
		#if self.cards[2] == '8S' and self.cards[3] == '8C':
			#self._rank = "PAIR: 8S 8C"
		#elif self.cards[2] == '8C' and self.cards[3] == '8S':
			#self._rank = "PAIR: 8C 8S"
		#elif self.cards[0] == '2C' and self.cards[1] == '2S':
			#self._rank = "PAIR: 2C 2S"
		else:
			high_card = self.cards[-1];
			self._rank = "HIGH CARD: " + Hand.card_string(high_card)


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


	def has_pair(self):
		values = []
		for card in self.cards:
			ex_res = Hand.extract_value_suit(card)
			value = ex_res[0]
			values.append(value)

		for i in range(0, len(values)):
			for j in range(0, len(values)):
				if i == j:
					continue
				if values[i] == values[j]:
					return [self.cards[i], self.cards[j]]
		return []




