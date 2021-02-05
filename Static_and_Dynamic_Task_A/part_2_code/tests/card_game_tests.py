import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game1 = CardGame()
        self.card1 = Card("spades", 1)
        self.card2 = Card("hearts", 10)

    def test_for_ace(self):
        self.assertEqual(True, self.game1.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.game1.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        cards_list = []
        cards_list.append(self.card1)
        cards_list.append(self.card2)
        self.assertEqual("You have a total of 11", self.game1.cards_total(cards_list))

