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

if __name__ == '__main__':
    unittest.main()


