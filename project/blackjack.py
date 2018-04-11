#!/usr/bin/python3
import functools

class Game:
    def __init__(self, deck=[1,1,1]):
        self._deck = deck
        self._player_hand = []
        self._dealer_hand = []

    def start(self):
        self._player_hit()
        self._dealer_hit()
        self._player_hit()
        return self._create_state()

    def hit(self):
        self._player_hit()
        return self._create_state()

    def _player_hit(self):
        card = self._deck.pop(0)
        self._player_hand.append(card)

    def _dealer_hit(self):
        self._dealer_hand.append(self._deck.pop(0))

    def _create_state(self):
        return {
            'player_has_ace': 1 in self._player_hand,
            'player_score': self._eval_hand(self._player_hand),
            'dealer_score': self._eval_hand(self._dealer_hand),
        }

    def _eval_hand(self, hand):
        score = sum(map(self._card_score, hand))
        number_of_aces = self._number_of_aces(hand)
        return self._calculate_score(number_of_aces, score)

    def _card_score(self, card):
        if card == 1:
            return 11
        return card

    def _number_of_aces(self, hand):
        return sum(card == 1 for card in hand)

    def _calculate_score(self, number_of_aces, score):
        if score > 21 and number_of_aces:
            return self._calculate_score(number_of_aces - 1, score - 10)
        return score
