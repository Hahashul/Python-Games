# Hangman Game-A classic word guessing game.
# The player tries to guess a word by suggesting letters within a certain number of guesses.
# If the player suggests a letter that is in the word, the letter is revealed in its correct position(s).
# If the player suggests a letter that is not in the word, they lose a life.
# The game continues until the player either guesses the word or runs out of lives.
import random
from Hangman_words import words
from Hangman_art import stages, logo

lives = 6  #life count
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(words)
placeholder = ""

# Create a placeholder for the chosen word with underscores
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder +f" ({word_length} letters)")

# Initialize game variables
game_over = False
correct_letters = []
used_letters = []

# Game loop
while not game_over:    
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

# If the letter has already been guessed, prompt the user to try again    
    while guess in used_letters:
        print(f"You have already guessed the letter {guess}, try again.")
        guess = input("Guess a letter: ").lower()
# Check if the letter has already been guessed
    if guess not in used_letters:
        used_letters += guess
# Create a display string to show the current state of the word    
    display = ""
# Update the display string based on the guessed letter
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    print(f"Used letters: {used_letters}")
# If the guessed letter is not in the chosen word, reduce the number of lives
    if guess not in chosen_word:
        lives -= 1
# If the player runs out of lives, end the game and reveal the word
        if lives == 0:
            game_over = True
            print(f"The word was {chosen_word}.")
            print(f"***********************YOU LOSE**********************")
            

# Check if the player has guessed all the letters in the word
    if "_" not in display:
        game_over = True
        print("congratulations, you guessed the word!")
        print("****************************YOU WIN****************************")      
    
    print(stages[lives])
# End of game loop
# End of code