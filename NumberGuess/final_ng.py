#Number guess game.
#Author: AOHI (P.Ah Sue)
#Email: pjae1882@gmail.com
#Game1

import random

unknown = random.randint(1,100)
guess = 0
attempt = 0

#Greetings
print('Welcom to AOHIs Number Guessing Game')
print('Pick any number from 1 to 100. You only have 6 guesses. Good luck!')

#Guess until player has no more returns
while guess != unknown and attempt < 6:

    number = input('Make your guess!')

    try:
        guess = int(number)

    except:
        print('Invalid Entry')
        quit()

    if guess < unknown:
        print ('Too low. Aim higher buddy')

    if guess > unknown:
        print ('Too high. Try something lower.')

    attempt = attempt + 1

#Make sure the value entered is only an integer

#Win or lose. End of game.
if guess == unknown:
    print ('Yaaaay! You guessed the correct number.')
else:
    print('Sorry, you have used all of your guesses.')
    print('The secret number was:', unknown)
