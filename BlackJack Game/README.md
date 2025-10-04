# Console Blackjack (Twenty-One)
A clean and simple implementation of the classic card game, Blackjack, designed to be played right in your terminal against a computer dealer. This project provides a quick and fun way to practice your hitting and standing strategy without needing a fancy GUI.

# Overview
This project is built purely in Python and simulates a game of Blackjack (also known as 21). We've ensured that the core rules are accurately followed, including the handling of a natural Blackjack and the crucial Ace adjustment mechanic, where an Ace can shift its value from 11 to 1 to prevent a player from busting. The computer dealer adheres to standard casino rules: they will always hit until their total score is 17 or higher.

The entire game logic is contained in modular functions for easy readability, making it straightforward for anyone to jump in and understand how the scoring or dealing works. It's a great example of a functional, text-based game built with fundamental Python concepts.

# Getting Started
Prerequisites
You only need Python 3 installed on your system to run this game.

Installation
Clone the Repository:

git clone [https://github.com/Hahashul/blackjack.git](https://github.com/Hahashul/blackjack.git)
cd BlackJack


# File Structure:
Ensure both the main game file (blackjack_game.py or your file name) and the visual asset file (art.py) are in the same folder.

# How to Play
Run the game directly from your terminal using the Python interpreter:

python blackjack_game.py


The game will prompt you to start, deal the initial hands, and display the first card of the computer dealer.

# In-Game Prompts:
To take another card (Hit): Type y

To keep your current hand (Stand): Type n

The game will automatically determine the winner based on the final scores.

# Game Rules & Scoring
| Card Value | Description |

| 2-10 | Face value (2 to 10) |

| J, Q, K | Count as 10 |

| Ace (A) |Counts as 11, unless the hand total exceeds 21, in which case it automatically counts as 1. |

Blackjack: A score of 21 achieved with only two cards (an Ace and a 10-value card).

Dealer Rules: The computer dealer must continue drawing cards until their score is 17 or more.

# Dependencies
This game uses only the following:

random: A built-in Python module for dealing cards randomly.

art: A local Python file (art.py) used to display the ASCII art logo at the start of the game.

Author:- HARSHUL ADWANI
# HOPE YOU ENJOY 
