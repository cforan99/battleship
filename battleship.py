# -*- coding: utf-8 -*-
# TO DO: Add turn count and end the game if turn limit is reached or if position is guessed correctly.
# Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.
# Make your game a two-player game.

from random import randint

board = []
ALPHABET = { 'A': 1, 1: 'A', 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 
             10: 'J', 'J': 10, 2: 'B', 8: 'H', 3: 'C', 9: 'I', 7: 'G', 4: 'D', 6: 'F', 5: 'E' }

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
    return (randint(1, len(board)-1), randint(1, len(board)-1))

ship_row, ship_col = random_coordinates(board)

print "Row", ship_row
print "Col", ship_col

guess_row = None
guess_col = None

def get_guess(board):
    """Checks validity of guess from raw input and prints an error message, a hit, or a miss."""
    guess = raw_input("Enter the letter-number coordinate of your shot location (e.g., D-4):")
    if guess == "":
        get_guess(board)
        return
    elif "-" not in guess:
        print "Please type your coordinates as letter dash(-) number."
        get_guess(board)
        return
    
    guess_row_letter, guess_col = guess.split("-")

    if not guess_col.isdigit() or not guess_row_letter.isalpha():
        print "Please type your coordinates as letter dash(-) number."
        get_guess(board)
        return

    guess_row_letter = guess_row_letter.upper()
    guess_col = int(guess_col)

    if guess_row_letter not in ALPHABET or guess_col not in ALPHABET:
            print "Oops, that's not even in the ocean."
            get_guess(board)
            return

    guess_row_number = ALPHABET[guess_row_letter]
    print "Row", guess_row_letter

    if guess_row_number == ship_row and guess_col == ship_col:
        board[guess_row_number][guess_col] = 'X'
        print_board(board)
        print "Hit!"
    else:   
        if board[guess_row_number][guess_col] == 'X' or board[guess_row_number][guess_col] == 'O':
            print "You guessed that one already."
            get_guess(board)
        else:
            print "Miss!"
            board[guess_row_number][guess_col] = 'O'
            print_board(board)
            get_guess(board)

get_guess(board)