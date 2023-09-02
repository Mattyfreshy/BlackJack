"""
Blackjack game.
"""

import random

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
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

def play_blackjack(num_decks :int) -> int:
    """
    Play a game of blackjack.
    Return: 1 if player wins, 0 otherwise.
    """
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

        print(f"Your cards: {player_cards}, current score: {player_score if player_score != 0 else 21}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass: ").lower()

            # Quit the game
            if should_continue == 'q' or should_continue == 'quit':
                raise KeyboardInterrupt
            
            if should_continue == 'y':
                deal_card(deck, player_cards)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        deal_card(deck, dealer_cards)
        dealer_score = calculate_score(dealer_cards)

    print() # Newline
    print(f"{bcolors.CYAN}Your final hand: {player_cards}, final score: {player_score if player_score != 0 else 21}{bcolors.ENDC}")
    print(f"{bcolors.CYAN}Dealer's final hand: {dealer_cards}, final score: {dealer_score if dealer_score != 0 else 21}{bcolors.ENDC}")


    
    if player_score == 0:
        print(bcolors.GREEN + "Blackjack! You win!" + bcolors.ENDC)
        return 1
    elif dealer_score == 0:
        print(bcolors.RED + "Dealer got a blackjack. You lose!" + bcolors.ENDC)
    elif player_score > 21:
        print(bcolors.RED + "You went over 21. You lose!" + bcolors.ENDC)
    elif dealer_score > 21:
        print(bcolors.GREEN + "Dealer went over 21. You win!" + bcolors.ENDC)
        return 1
    elif player_score > dealer_score:
        print(bcolors.GREEN + "You win!" + bcolors.ENDC)
        return 1
    elif player_score == dealer_score:
        print(bcolors.GREEN + "No Loss" + bcolors.ENDC)
    else:
        print(bcolors.RED + "You lose!" + bcolors.ENDC)
    
    # return 0 if player loses
    return 0

def play_real():
    """Play a game of blackjack."""
    # Game counter and win counter
    game_count = 0
    win_count = 0

    # Run the game
    try:
        # Print the welcome message
        print("Welcome to Blackjack!")
        print("To end the game, type 'q' or 'quit'.")

        num_decks = int(input("Enter the number of decks to use: "))
        while True:
            print("-----------------------------------")
            win_count += play_blackjack(num_decks)
            game_count += 1
    except KeyboardInterrupt:
        print("\n")
        print(f"{bcolors.CYAN} # of games: {str(game_count)}{bcolors.ENDC}")
        print(f"{bcolors.CYAN} # of wins: {str(win_count)}{bcolors.ENDC}")
        print(f"{bcolors.CYAN} Win rate: {(win_count / game_count)*100 if game_count != 0 else 0.00:.2f}%{bcolors.ENDC}")

def main():
    play_real()

if __name__ == "__main__":
    main()






