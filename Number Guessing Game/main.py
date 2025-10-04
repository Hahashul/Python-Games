# Number Guessing Game
# Guess a number between 1 and 100

from random import randint
from Art import logo

# Defficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}\n")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":       
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")
        return set_difficulty()

def game():
    print(logo)
   
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
   
    # Choose a difficulty level.
    turns = set_difficulty()
   
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        # If they run out of turns, they lose the game
        if turns == 0:
            print(f"The number was {answer}.")
            print("You've run out of guesses, you lose.\n")
            return
        elif guess != answer:
            print("Guess again.\n")
# Play the game again
loop = True
while loop:
    game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        loop = True
    else:
        loop = False
        print("Thanks for playing!")
# End of code