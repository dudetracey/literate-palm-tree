# Exercise 9:
# Write a game that makes the user guess a random number
# Tell the user if they guessed too low, too high, or exactly right
# Extra 1: Keep the game going until the user types "exit"
# Extra 2: Keep track of how many guesses the user has taken, and when the game ends, tell them
#
# HERE TO TRY TO MAKE b THE QUIT VARIABLE AND GET RID OF c
#
#
import random
# variables a and b are for the secret number and the guess
# c is for checking if we are closing the program
# first I set up these variables to start the game's first run
a = random.randint(1, 6)
b = -1
count = 0
player = input('Tell me your name: ')
# count is to keep track of number of attempts
print('Hey ' + player + ', I\'m thinking of a random number. Can you guess what it is?')

while a != b:
    b = input('Take a guess: ')
    if b == 'exit':
        break
    else:
        b = int(b)
    count = count + 1
    if a == b:
        count = str(count)
        print('Congratulations, ' + player + ', you won! It took you ' + count + ' guesses to find the correct '
                                                                                 'number!')
        b = input('Do you want to play again? Type "exit" to quit. ').lower()
# This is where I reset the variables so the game can run in the loop
        a = random.randint(1, 6)
        if b == 'exit':
            break
        else:
            b = -1
        count = 0
        continue
    elif a > b:
        print('Too low, guess again!')
    elif a < b:
        print('Too high, guess again!')

print('Thanks for playing! Have an amazing day!')




