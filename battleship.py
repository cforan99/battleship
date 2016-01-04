#TO DO: Add turn count and end the game if turn limit is reached or if position is guessed correctly.
# Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.
# Make your game a two-player game.

from random import randint

board = []
ALPHABET = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def initialize_board(n):
    """Creates a nxn board with column and row labels."""
    row = ["/"]
    for i in range(1, n+1):
        row.append(str(i))
    board.append(row)
    # print " ".join(row)
    for num in range(1, n+1):
        row = [ALPHABET[num]]
        row = row + ["-"] * n
        board.append(row)
        # print " ".join(row)
    return board

board = initialize_board(10)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_coordinates(board):
    return (randint(1, len(board)), randint(1, len(board)))

ship_row, ship_col = random_coordinates(board)

print ship_row
print ship_col

guess_row = None
guess_col = None

def get_guess(board):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == 'X':
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = 'X'
            print_board(board)
        get_guess(board)

get_guess(board)