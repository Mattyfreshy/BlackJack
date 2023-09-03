# BlackJack Game Simulator
## Introduction
This is a simple BlackJack game simulator written in python. The goal was to not only create a blackjack program in python, but to also develop algorithms that can play the game with a high success rate. A successful turn is when the player/program makes a gain. 

## How to Play
The game is played with a standard 52 card deck. The goal is to get as close to 21 as possible without going over. The player is dealt two cards and can choose to hit or stay. If the player hits, they are dealt another card. If the player stays, they are dealt no more cards. The player can hit as many times as they want until they either go over 21 or choose to stay. If the player goes over 21, they bust and lose the game. If the player stays, the dealer is dealt cards until they either beat the player or bust. If the dealer busts, the player wins. If the dealer beats the player, the player loses. If the dealer and player tie, the game is a push and the player neither wins nor loses.

## Rules
- The player can hit as many times as they want until they either go over 21 or choose to stay.
- The dealer must hit if their hand is less than 17.
- The dealer must stay if their hand is greater than or equal to 17.

## How to Run
To run the program, simply run the following command in the terminal:
```
python3 blackjack.py
```

## Python Files: Description + arguments (if applicable) + Examples
### BlackJack.py
Description: 
- Play a game of blackjack against the dealer (computer).

Arguments:
- Num of decks.
- y to hit, n to stay.
- q or quit to exit game.

```
# Example
Enter the number of decks to use: 8
Type 'y' to get another card, or 'n' to pass: y

```

### simulate.py
Description: 
- Simulate n games of blackjack against the dealer (computer). Status percentage is displayed to show progress during simulation. Can be run sequentially or in parallel depending on number of games to simulate. Uses pyspark to run in parallel.

Arguments:
- Num of decks.
- num of games to simulate.

```
# Example
Enter the number of decks to use: 8
Enter the number of games to simulate: 1000000
Simulated 1000000 games with 8 deck(s).
Player win rate: 48%
```

### BlackJackAlgo.py
Description:
- Where the algorithms are stored. The algorithms are used to play the game of blackjack and called in simulate.py to determine success rate.

Algorithms:
- Simple (73% win rate):
    - Simple strategy that hits until the player's score is 17 or greater.
- dHand (81.4% win rate):
    - Strategy based on the dealer's first card.
        - if player hand < 11, always hit
        - if player hand > 11 and dealer first card < 7, hold
        - if player hand > 11 and dealer first card + 10 >= 17, hit
        - if above conditions not met, hold for now.