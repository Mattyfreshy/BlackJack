from BlackJack import deal_card, calculate_score, create_deck

def black_jack_simple(deck :list[int], player_score :int, player_cards :list):
    """
    Simple strategy that hits until the player's score is 17 or greater.
    """
    """ 73% success rate """
    if player_score < 17:
        deal_card(deck, player_cards)
        return False
    else:
        return True
    
def black_jack_dHand(deck :list[int], player_score :int, player_cards :list, dealer_cards :list):
    """
    Strategy based on the dealer's first card.
        - if player hand < 11, always hit
        - if player hand > 11 and dealer first card < 7, hold
        - if player hand > 11 and dealer first card + 10 >= 17, hit
        - if above conditions not met, hold for now.
    """
    """ 78.4% success rate """
    dealer_first_card = dealer_cards[0]

    if player_score < 11:
        deal_card(deck, player_cards)
        return False
    elif player_score > 11 and dealer_first_card < 7:
        return True
    elif player_score > 11 and dealer_first_card + 10 >= 17:
        deal_card(deck, player_cards)
        return False

    return True

def black_jack_strategy(deck :list[int], player_score :int, player_cards :list, dealer_cards :list):
    """ Strategy to be used in simulate.py """
    
    # Simple
    # return black_jack_simple(deck, player_score, player_cards)

    # Dealer's Hand
    return black_jack_dHand(deck, player_score, player_cards, dealer_cards)
