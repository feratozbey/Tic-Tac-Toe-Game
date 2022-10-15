import os  # To clean screen for better user experience

print('Welcome to TIC TAC TOE')  # Introduction
print('Player 1 is "X"\nPlayer 2 is "O"')  # Introduction
game = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Array for the game board/
game_on = True  # Boolean for while loop/


# Function to display most recent state of the game board.
def game_show():
    print(f' {game[0]} | {game[1]} | {game[2]}\n'
          f'-----------\n'
          f' {game[3]} | {game[4]} | {game[5]}\n'
          f'-----------\n'
          f' {game[6]} | {game[7]} | {game[8]}\n')


# Function to place "X"s and "O"s on the board. A little challenge added: if any player selects already occupied
# position they lose their turn to play.
def move(number, symbol):
    if type(game[number - 1]) == int:
        game[number - 1] = symbol
    else:
        print(f'Number {number} is already full. You lost your chance')


# Function to check either if there is a winner yet or all positions are occupied on the game board.
def is_won(player, symbol):
    global game_on

    # Checking if all positions are already filled with "X"s and "O"s.
    type_array = [type(n) == str for n in game]
    all_str = all(type_array)

    # Checking all possible winning scenarios.
    if game[0] == game[1] == game[2] == symbol or \
            game[3] == game[4] == game[5] == symbol or game[6] == game[7] == game[8] == symbol or \
            game[0] == game[4] == game[8] == symbol or game[0] == game[3] == game[6] == symbol or \
            game[1] == game[4] == game[7] == symbol or game[2] == game[5] == game[8] == symbol or \
            game[2] == game[4] == game[6] == symbol:
        game_show()
        print(f'!!! {player} Wins The Game !!!')
        game_on = False

    # If all positions are filled and game is not won, it is a draw.
    elif all_str:
        game_show()
        print('!!! It Is A Draw !!!')
        game_on = False


# While loop runs until one of the is_won() scenarios is fulfilled.
while game_on:
    try:
        game_show()
        player1 = int(input('Player 1, select a number for "X": '))
        os.system('cls')
        move(player1, 'X')
        is_won('Player 1', 'X')

        # If statement for user experience. If player1 won the game and is_won() func returned a False for
        # the game_on variable, it shouldn't ask player2's next move.
        if game_on:
            game_show()
            player2 = int(input('Player 2, select a number for "O": '))
            os.system('cls')
            move(player2, 'O')
            is_won('Player 2', 'O')

    # if user enters a number out of range:
    except IndexError:
        print('!!! Value must be between 1 to 9 !!!')

    # if user enters other than integer values:
    except ValueError:
        print('!!! Please use an integer between 1 to 9 !!!')