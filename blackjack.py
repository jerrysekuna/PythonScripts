import random 

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """Returns the sum of a list of random cards"""
    if 10 in cards and 11 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score): 
    """Compares user scores to computer score to find winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21: 
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    """Continues the Blackjack game"""
    user_cards = []
    computer_cards = []
    game_end = False

    for item in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card) 

    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards) 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            user_deal = input("Type 'y' to get another card or 'n' to pass ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) 

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == 'yes':
    play_game()
