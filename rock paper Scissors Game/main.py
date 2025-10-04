#Rock Paper Scissors Game
#chosse 0 for rock, 1 for paper or 2 for scissors
#user vs computer
import random 
from Art import rock, paper, scissors
user=0
computer=0
#function to display the game data
def game():
    print('Welcome to Rock, Paper, Scissors Game!')
    print(rock)
    print(paper)
    print(scissors)
    user=int(input('What do you wanna choose? Type 0 for rock, 1 for paper or 2 for scissors-: '))
    computer=random.randint(0,2)
    images=[rock,paper,scissors]

    #user data
    if user>=0 and user<=2:
        print('You choose:')
        print(images[user])

    #computer data
    print('\n \n \n Computer choose:')
    print(images[computer])
    
    return user,computer

#function to check the winner
def check_win(user,computer):            
    if user==0 and computer==2:
        print('You win!')
    elif computer==0 and user==2:
        print('You lose!')
    elif computer>user:
        print('You lose!')
    elif user>computer:
        print('You win!')
    elif computer==user:
        print('It is a draw!')
    else:
        print('You typed an invalid number, you lose!')

loop= True  
#loop to play the game again and again
while loop:
    user,computer=game()
    check_win(user,computer)
    play_again=input('Do you want to play again? Type y or n:-')
    if play_again=='y':
        loop=True
    else:
        loop=False
        print('Thanks for playing the game!')
#End of code