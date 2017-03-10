import unittest
from poker import Hand
from poker import UnknownSuit
from poker import UnknownValue

class PokerTests(unittest.TestCase):

	def test_has_card_return_true_if_hand_has_ace_of_spades(self):
		hand = Hand("2C 3H 4S 8C AS")

		res = hand.has_card("AS")

		self.assertEqual(res, True)

	def test_hand_raise_exception_unknown_suit_if_input_has_suit_is_non_c_h_s_d(self):
		res = False
		try:
			Hand("2C 3W 4S 8C AS")
		except UnknownSuit:
			res = True

		self.assertEqual(res, True)

	def test_hand_raise_exception_unknown_value_if_input_has_value_is_non_poker_deck(self):
		res = False
		try:
			Hand("2C YH 4S 8C AS")
		except UnknownValue:
			res = True

		self.assertEqual(res, True)


	def test_method_hand_rank_return_high_card_rank_if_hand_contain_2C_3H_4S_8C_AS(self):
		hand = Hand("2C 3H 4S 8C AS")

		res = hand.rank()

		self.assertEqual(res, "HIGH CARD: Ace of Spades")


	def test_method_hand_rank_return_high_card_rank_if_hand_contain_2C_3H_4S_8C_AH(self):
		hand = Hand("2C 3H 4S 8C AH")

		res = hand.rank()

		self.assertEqual(res, "HIGH CARD: Ace of Hearts")

	def test_method_hand_rank_return_high_card_rank_if_hand_contain_2C_3H_4S_8C_KC(self):
		hand = Hand("2C 3H 4S 8C KC")

		res = hand.rank()

		self.assertEqual(res, "HIGH CARD: King of Clubs")

	def test_method_hand_rank_return_high_card_rank_if_hand_contain_2C_3H_4S_8C_QD(self):
		hand = Hand("2C 3H 4S 8C QD")

		res = hand.rank()

		self.assertEqual(res, "HIGH CARD: Queen of Diamonds")

	def test_method_hand_rank_return_high_card_rank_if_hand_contain_2C_3H_4S_8C_JS(self):
		hand = Hand("2C 3H 4S 8C JS")

		res = hand.rank()

		self.assertEqual(res, "HIGH CARD: Jack of Spades")

	def test_method_hand_rank_return_pair_rank_if_hand_contain_2C_2S_4S_8C_JS(self):
		hand = Hand("2C 2S 4S 8C JS")

		res = hand.rank()

		self.assertEqual(res, "PAIR: 2C 2S")

	def test_method_hand_rank_return_pair_rank_if_hand_contain_2C_3S_8S_8C_JS(self):
		hand = Hand("2C 3S 8S 8C JS")

		res = hand.rank()

		self.assertEqual(res, "PAIR: 8S 8C")

	def test_method_hand_rank_return_pair_rank_if_hand_contain_2C_3S_8C_8S_JS(self):
		hand = Hand("2C 3S 8C 8S JS")

		res = hand.rank()

		self.assertEqual(res, "PAIR: 8C 8S")

if __name__ == '__main__':
    unittest.main()


