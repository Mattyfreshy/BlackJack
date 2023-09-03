from BlackJack import deal_card, calculate_score, create_deck, bcolors
import BlackJackAlgo as algo
from tqdm import tqdm
from pyspark import SparkContext



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
    """Simulate a number of games sequently and return the win rate."""
    wins = 0
    for i in tqdm(range(num_games)):
        deck = create_deck(num_decks)
        player_score, dealer_score = play_sim(deck)
        
        if player_score == 0 or (dealer_score > 21 or dealer_score < player_score):
            # Player wins or computer busts
             wins += 1
        
        # Progress bar using print
        # print(f" {(i / num_games) * 100:.2f}%", end='\r')

    win_rate = (wins / num_games) * 100
    return win_rate

def play_parallel(num_decks :int):
    deck = create_deck(num_decks)
    player_score, dealer_score = play_sim(deck)

    if player_score == 0 or (dealer_score > 21 or dealer_score < player_score):
        # Return 1 if player wins or computer busts
            return 1
    
    # Return 0 otherwise
    return 0

def simulate_games_parallel(num_games :int, num_decks :int) -> float:
    """Simulate a number of games in parallel and return the win rate."""
    # Initialize a SparkContext
    sc = SparkContext("local", "BlackjackSimulation")
    
    # Parallelize the game simulations using Spark
    games_rdd = sc.parallelize(range(num_games))

    wins = games_rdd.map(lambda _: play_parallel(num_decks)).reduce(lambda x, y: x + y)
    sc.stop()

    win_rate = (wins / num_games) * 100
    return win_rate

def main():
    num_decks = int(input("Enter the number of decks to use: "))
    num_games = int(input("Enter the number of games to simulate: "))
    
    # Simulate games
    accuracy = 100000
    if num_games < accuracy:
        print(f"{bcolors.WARNING}Warning: Simulating less than {accuracy} games may result in inaccurate results.{bcolors.ENDC}")
        print(f"{bcolors.CYAN}Simulating games sequentially...{bcolors.ENDC}")
        win_rate = simulate_games(num_games, num_decks)
    else:
        print(f"{bcolors.CYAN}Simulating games in parallel...{bcolors.ENDC}")
        win_rate = simulate_games_parallel(num_games, num_decks)

    print(f"{bcolors.GREEN}Simulated {num_games} games with {num_decks} deck(s).{bcolors.ENDC}")
    print(f"{bcolors.GREEN}Player win rate: {win_rate:.2f}%{bcolors.ENDC}")

if __name__ == "__main__":
    main()
