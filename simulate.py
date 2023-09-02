from BlackJack import deal_card, calculate_score, create_deck
import BlackJackAlgo as algo
import multiprocessing as mp

PARALLEL_PROGRESS = 0

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

def play_parallel(num_games :int, num_decks :int):
    deck = create_deck(num_decks)
    player_score, dealer_score = play_sim(deck)

    # Progress bar #!FIXME: Progress bar is inaccurate
    global PARALLEL_PROGRESS
    PARALLEL_PROGRESS += 1
    print(f" {(PARALLEL_PROGRESS / num_games) * 100:.2f}%", end='\r')

    if player_score == 0 or (dealer_score > 21 or dealer_score < player_score):
        # Return 1 if player wins or computer busts
            return 1
    
    # Return 0 otherwise
    return 0

def simulate_games_parallel(num_games :int, num_decks :int) -> float:
    """Simulate a number of games in parallel and return the win rate."""
    # Parallel processing
    with mp.Pool(mp.cpu_count()) as p:
        # Result is a list of 1s and 0s (1 if player wins, 0 otherwise)
        result = p.starmap(play_parallel, [(num_games, num_decks) for _ in range(num_games)])

    wins = sum(result)
    win_rate = (wins / num_games) * 100
    return win_rate

def main():
    num_decks = int(input("Enter the number of decks to use: "))
    num_games = int(input("Enter the number of games to simulate: "))
    
    # Simulate games
    accuracy = 100000
    if num_games < accuracy:
        print(f"Warning: Simulating less than {accuracy} games may result in inaccurate results.")
        print("Simulating games sequentially...")
        win_rate = simulate_games(num_games, num_decks)
    else:
        print("Simulating games in parallel...")
        win_rate = simulate_games_parallel(num_games, num_decks)

    print(f"Simulated {num_games} games with {num_decks} deck(s).")
    print(f"Player win rate: {win_rate:.2f}%")

if __name__ == "__main__":
    main()
