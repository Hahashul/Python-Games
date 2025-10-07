# Blackjack Game
# The game is played with an infinite deck of cards.
# The cards in the deck have the following values:
# - 2-10 have their face value.
# - J, Q, K have a value of 10. 
# - A can count as 11 or 1.
# The deck is unlimited in size. There are no jokers.
# The cards have equal probability of being drawn.
# The computer is the dealer.
# The player can request additional cards (hit) until they decide to stop (stand) or exceed 21 (bust).
# If the player busts, they lose.
# If the player stands, the dealer reveals their hidden card and must hit until their total is 17 or higher.
# If the dealer busts, the player wins.
# If neither busts, the higher total wins. A tie results in a draw.

import random
from art import logo
# Function to deal a random card from the deck
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Function to calculate the score of a hand
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
# Check for an 11 (Ace). If the score is over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def ask_bet(user,bet):
    
    bet=int(input("Place your bet-: "))
    bet_loop= True
    while bet_loop:
        if user-bet<0:
            print("Insufficient Balance,Try Again")
            bet=int(input("Place your bet-: "))
        else:
            bet_loop=False
    return bet         

def win_bet(u_score, c_score):
    if u_score == c_score:
        return 0
    elif c_score == 0:
        return 1
    elif u_score == 0:
        return 2
    elif u_score > 21:
        return 1
    elif c_score > 21:
        return 2
    elif u_score > c_score:
        return 2
    else:
        return 1

def calculate_bet(win_bet,bet,user):
    if win_bet==1:
        user=user-bet
        return user
    elif win_bet==2:
        user=user+bet
        return user
    else:
        return user        


# Function to compare the final scores and determine the outcome
user_money=1000

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃" 
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱" 
    elif u_score == 0:
        return "Win with a Blackjack 😎" 
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Main function to play the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
# Deal two cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Current Balance -: {user_money}")
    bet=0
    bet=ask_bet(user_money,bet)
    
    
    while not is_game_over:
        user_score = calculate_score(user_cards)                         # Calculate the user's score
        computer_score = calculate_score(computer_cards)                  # Calculate the computer's score
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
# Check for a blackjack or if the user has exceeded 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
# Once the user is done, it's the computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
# Final results
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    check_win=win_bet(user_score,computer_score)
    user_money=calculate_bet(check_win,bet,user_money)
    print(f"\n\nCurrent Balance -: {user_money}")

    if user_money==0:
        print("You lost it all!!!")
        break
        

print("Thank you for playing!")     
# End of the game


