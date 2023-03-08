import os
import random
from Blackjack_arts import *

cards = {
    "Ace": [card_art["Ace"], 1],
    "2": [card_art["2"], 2],
    "3": [card_art["3"], 3],
    "4": [card_art["4"], 4],
    "5": [card_art["5"], 5],
    "6": [card_art["6"], 6],
    "7": [card_art["7"], 7],
    "8": [card_art["8"], 8],
    "9": [card_art["9"], 9],
    "10": [card_art["10"], 10],
    "J": [card_art["J"], 10],
    "Q": [card_art["Q"], 10],
    "K": [card_art["K"], 10],
}


def draw_card(hand):
    """Draws a card into hand"""
    random_card = random.choice(list(cards.keys()))
    return hand.append(random_card)


def print_hand(hand):
    """Prints a hand of cards"""
    for line in range(7):
        for card in hand:
            print(card_art.get(card)[line], end="")
        print()


def sum_values(hand):
    """Sums up the value of the cards in hand"""
    summary = 0
    for card in hand:
        if card == "Ace" and summary+11 <= 21:
            cards["Ace"][1] = 11
        summary += cards[card][1]
    return summary


def starting_draw(hand1, hand2):
    """At the beginning of the game, the player draws two cards and the dealer draws one"""
    draw_card(hand1)
    draw_card(hand1)
    draw_card(hand2)


def show_player_hand(hand):
    print(f"Your cards:")
    print_hand(hand)
    print(f"Current score: {sum_values(hand)}")
    print(f"──────────────────────")


def show_dealer_hand(hand):
    print(f"Dealer hand:")
    print_hand(hand)
    print(f"Final score: {sum_values(hand)}")
    print(f"──────────────────────")


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

