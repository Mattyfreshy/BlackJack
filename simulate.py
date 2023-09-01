from BlackJack import deal_card, calculate_score, create_deck
import BlackJackAlgo as algo

def play_sim(deck :list[int]):
    """Simulate a game of blackjack."""
    player_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        deal_card(deck, player_cards)
        deal_card(deck, dealer_cards)

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            # Strategy Section
            is_game_over = algo.black_jack_strategy(deck, player_score, player_cards, dealer_cards)

    while dealer_score != 0 and dealer_score < 17:
        deal_card(deck, dealer_cards)
        dealer_score = calculate_score(dealer_cards)

    return player_score, dealer_score

def simulate_games(num_games :int, num_decks :int) -> float:
    """Simulate a number of games and return the win rate."""
    wins = 0
    for i in range(num_games):
        deck = create_deck(num_decks)
        player_score, dealer_score = play_sim(deck)
        
        if player_score == 0 or (dealer_score > 21 or dealer_score < player_score):
            # Player wins or computer busts
             wins += 1

        # Progress bar
        print(f" {(i / num_games) * 100:.2f}%", end='\r')

    win_rate = (wins / num_games) * 100
    return win_rate

def main():
    num_decks = int(input("Enter the number of decks to use: "))
    num_games = int(input("Enter the number of games to simulate: "))
    
    win_rate = simulate_games(num_games, num_decks)
    print(f"Simulated {num_games} games with {num_decks} deck(s).")
    print(f"Player win rate: {win_rate:.2f}%")

if __name__ == "__main__":
    main()
