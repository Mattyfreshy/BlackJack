"""
Blackjack game.
"""

import random

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def create_deck(num_decks :int) -> list[int]:
    """
    Create a deck consisting of multiple decks.
    - Face cards are worth 10.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck = cards * 4 * num_decks
    random.shuffle(deck)
    return deck

def deal_card(deck :list[int], hand :list):
    """Deal a card from the deck to a hand."""
    card = deck.pop()
    hand.append(card)

def calculate_score(cards):
    """Calculate the score of a list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def play_blackjack(num_decks :int) -> None:
    """Play a game of blackjack."""
    deck = create_deck(num_decks)
    player_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        deal_card(deck, player_cards)
        deal_card(deck, dealer_cards)

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass: ").lower()

            if should_continue == 'y':
                deal_card(deck, player_cards)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        deal_card(deck, dealer_cards)
        dealer_score = calculate_score(dealer_cards)

    print(f"{bcolors.CYAN}Your final hand: {player_cards}, final score: {player_score}{bcolors.ENDC}")
    print(f"{bcolors.CYAN}Computer's final hand: {dealer_cards}, final score: {dealer_score}{bcolors.ENDC}")


    if player_score > 21:
        print(bcolors.WARNING + "You went over 21. You lose!" + bcolors.ENDC)
    elif dealer_score > 21:
        print(bcolors.GREEN + "Computer went over 21. You win!" + bcolors.ENDC)
    elif player_score == 0:
        print(bcolors.GREEN + "Blackjack! You win!" + bcolors.ENDC)
    elif dealer_score == 0:
        print(bcolors.WARNING + "Computer got a blackjack. You lose!" + bcolors.ENDC)
    elif player_score > dealer_score:
        print(bcolors.GREEN + "You win!" + bcolors.ENDC)
    elif player_score == dealer_score:
        print(bcolors.GREEN + "No Loss" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "You lose!" + bcolors.ENDC)

def play_real():
    """Play a game of blackjack."""
    # Run the game
    num_decks = int(input("Enter the number of decks to use: "))
    try:
        while True:
            print("-----------------------------------")
            play_blackjack(num_decks)
    except KeyboardInterrupt:
        print("Game interrupted by user.")

def main():
    play_real()

if __name__ == "__main__":
    main()






