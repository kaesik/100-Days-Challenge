# Blackjack Project

# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from Blackjack_functions import *


game = True

print(logo)
while game:
    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player_hand = []
    dealer_hand = []
    starting_draw(player_hand, dealer_hand)
    if decision == "y":
        game_round = True
    elif decision == "n":
        game_round = False
        game = False
        print("Thank you for game!")
    else:
        print("Incorrect decision. Please repeat.")
        continue
    while game_round:
        show_player_hand(player_hand)
        print(f"Computer's first card:")
        print_hand(dealer_hand)
        print(f"With score: {sum_values(dealer_hand)}")
        print(f"─────────────────────")
        decision = input("Type 'y' to get another card, type 'n' to pass: ")
        clear()
        if decision == "y":
            draw_card(player_hand)
            if sum_values(player_hand) > 21:
                show_player_hand(player_hand)
                print(f"You went over. You lose.")
                game_round = False
        elif decision == "n":
            while sum_values(dealer_hand) < 16:
                draw_card(dealer_hand)
            show_player_hand(player_hand)
            show_dealer_hand(dealer_hand)
            if sum_values(dealer_hand) > 21:
                print(f"Dealer went over. You win.")
            elif sum_values(dealer_hand) > sum_values(player_hand):
                print(f"You lose.")
            elif sum_values(dealer_hand) < sum_values(player_hand):
                print(f"You win.")
            elif sum_values(dealer_hand) == sum_values(player_hand):
                print(f"It's a draw.")
            game_round = False
        else:
            print("Incorrect decision. Please repeat.")
            continue