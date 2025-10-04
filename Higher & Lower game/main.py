# Higher & Lower Game
# In this game, you are to guess which of the two accounts has more followers.
# You will be shown two accounts, and you have to type 'A' or 'B' to guess which has more followers.
# The game continues until you make a wrong guess. Your score is the number of correct guesses you make in a row.
# The game uses a predefined list of accounts with their follower counts, descriptions, and countries.

from art import logo, vs
from game_data import data
import random


def format_data(account):
#   Takes the account data and returns the printable format.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

 
def check_answer(user_guess, a_followers, b_followers):
#   Take a user's guess and the follower counts and returns if they got it right.
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Display art
print(logo)
#game function
def game():
    score = 0
    game_should_continue = True
    # Generate a random account from the game data
    account_a =account_b = random.choice(data)
    repeated_account = []
    # Make the game repeatable.
    while game_should_continue:
        #check if account_a and account_b are the same or have been used before
        repeated_account.append(account_a)
        
        account_b = random.choice(data)
        while account_a == account_b or account_b in repeated_account:
            account_b = random.choice(data)
        
        repeated_account.append(account_b)
        # Format the account data into printable format.
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the screen
        print("\n" * 20)
        print(logo)

        # - Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        print(is_correct)
        # Give user feedback on their guess.
        # score keeping.
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}")
            if guess == "b":
                account_a = account_b
            else:
                account_a = account_a
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False

game()
# Ask user if they want to restart the game.
while input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    print(logo)
    game()
#End of the game    