import unittest
from poker import Hand


class PokerTests(unittest.TestCase):


    def test_has_card_return_true_if_hand_has_ace_of_spades(self):
        hand = Hand("2C 3H 4S 8C AS")

        res = hand.hasCard("AS")

        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()




