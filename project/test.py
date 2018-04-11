#!/usr/bin/env python3

import pytest
from blackjack import Game

def test_start_returns_dict(game):
    # when
    state = game.start()

    # then
    assert type(state) is dict
    assert 'player_has_ace' in state
    assert 'player_score' in state
    assert 'dealer_score' in state

def test_start():
    # give
    deck = _create_deck([2, 4], [3])
    game = Game(deck)

    # when
    state = game.start()

    # then
    assert state['player_score'] == 6
    assert state['player_has_ace'] == False
    assert state['dealer_score'] == 3

def test_start_ace_high():
    # give
    deck = _create_deck([2, 1], [3])
    game = Game(deck)

    # when
    state = game.start()

    # then
    assert state['player_score'] == 13
    assert state['player_has_ace'] == True

def test_start_ace_low():
    # give
    deck = _create_deck([1, 1], [3])
    game = Game(deck)

    # when
    state = game.start()

    # then
    assert state['player_score'] == 12
    assert state['player_has_ace'] == True

def test_start_state2():
    # give
    deck = [2, 3, 4]
    game = Game(deck)

    # when
    state = game.start()

    # then
    assert state['player_score'] == 6
    assert state['player_has_ace'] == False
    assert state['dealer_score'] == 3

def test_hit():
    # give
    deck = _create_deck([2, 4, 5], [3])
    game = Game(deck)

    # when
    game.start()
    state = game.hit()

    # then
    assert state['player_score'] == 11
    assert state['player_has_ace'] == False
    assert state['dealer_score'] == 3

@pytest.fixture
def game():
  return Game()

def _create_deck(player_hand, dealer_hand):
    return [player_hand[0], dealer_hand[0]] + player_hand[1:]
