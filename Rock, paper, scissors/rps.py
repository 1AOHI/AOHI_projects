#Rock, paper, scissors.
#Author: AOHI (P.Ah Sue)
#Email: pjae1882@gmail.com
#Game 2


import random

while True:

    player =  input('Select rock, paper, or scissors: ')
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)


#Results from the game
#Tie
    if player == computer:
        print('TIe! Both players selected:', player)

#If player selects rock
    elif player.lower() == 'rock':
        if computer.lower() == 'scissors':
            print('You win!')
#If computer selects paper
        else:
            print('You lose.')


#If player selects paper
    elif player.lower() == 'paper':
        if computer.lower() == 'rock':
            print('You win!')
#If computer selects scissors
        else:
            print('You lose.')

#If player selects scissors
    elif player.lower() == 'scissors':
        if computer.lower() == 'paper':
            print('You win!')
#If computer selects rock
        else:
            print('You lose.')
