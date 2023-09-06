import unittest

from poker.card import Card
from poker.hand import Hand
from poker.validators import NoCardsValidator

class NoCardsValidatorTest(unittest.TestCase):
    def test_validates_that_no_cards_present(self):
        validator = NoCardsValidator(cards = [])

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_no_valid_cards(self):
        validator = NoCardsValidator(cards = [])

        self.assertEqual(
            validator.valid_cards(),
            []
        )