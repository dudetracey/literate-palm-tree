# Exercise 8:
# Two Player Rock-Paper-Scissors
# Get input from the player, compare the inputs, and declare a winner. Ask if the players want to play again.
def rock_paper_scissors():
    player1 = input('Player 1 Name: ')
    player2 = input('Player 2 Name: ')
    quit = input('Do you want to play Rock, Paper Scissors? ')
    while quit != 'no':
        if quit == 'no':
            break
        x = input((player1 + ', Rock, Paper, or Scissors? ')).lower()
        y = input((player2 + ', Rock, Paper, or Scissors? ')).lower()
        if x == y:
            print('You are tied')
        elif x == 'rock' and y == 'paper':
            print(player2 + ' wins!!!')
        elif x == 'rock' and y == 'scissors':
            print(player1 + ' wins!!!')
        elif x == 'paper' and y == 'scissors':
            print(player2 + ' wins!!!')
        elif x == 'paper' and y == 'rock':
            print(player1 + ' wins!!!')
        elif x == 'scissors' and y == 'rock':
            print(player2 + ' wins!!!')
        elif x == 'scissors' and y == 'paper':
            print(player1 + ' wins!!!')
        else:
            print('Please type a correct choice for the game.')
        quit = input('Do you want to play again? ').lower()
    print('Have an amazing day! ')
