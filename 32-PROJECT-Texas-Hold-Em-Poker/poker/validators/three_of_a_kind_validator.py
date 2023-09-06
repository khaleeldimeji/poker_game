from poker.validators import RankValidator

class ThreeOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Three Of A Kind"

    def is_valid(self):
        rank_with_three_of_a_kind = self._ranks_with_count(3)
        return len(rank_with_three_of_a_kind) == 1

    def valid_cards(self):
        rank_with_pairs = self._ranks_with_count(3)
        cards = [card for card in self.cards if card.rank in rank_with_pairs.keys()]
        return cards