"""
Tic-tac-toe
"""
import random


# Constants
BOARD_SIZE = 3
MAX_PLAYS = 9
PLAYER_1 = 'X'
PLAYER_2 = 'O'


# Exception for invalid positions
class InvalidPositionError(Exception):
    pass


def create_board():
    """Create a 3x3 matrix with numbers from 1 to 9"""

    return [[x+y for x in range(BOARD_SIZE)] for y in range(1, 9, 3)]


def position_to_coords(position):
    """Convert position (1-9) to coordinates"""

    position -= 1
    y = position // BOARD_SIZE
    x = position % BOARD_SIZE
    return x, y


def display_board(board):
    """Print board into console"""

    for y in board:
        print('+---+---+---+')
        for x in y:
            print('|', x, end=' ')
        print('|')
    print('+---+---+---+')


def validate_position(position, plays):
    """Validates the position checking if the input is a number, if the input
    is in range 1-9 and if the position has already been marked
    """

    if not position.isdigit():
        raise InvalidPositionError('Invalid position')

    position = int(position)
    if position < 1 or position > 9:
        raise InvalidPositionError('Invalid position')

    if position in plays:
        raise InvalidPositionError('This position has already been marked')

    return True


def has_available_play(plays):
    """Check if there is available play"""
    return len(plays) != MAX_PLAYS


def random_position(plays):
    """Generates a random position checking the plays already did"""
    available_plays = {i for i in range(1, 10)}
    available_plays.difference_update(plays)
    position = random.choice(tuple(available_plays))
    return position


def check_victory(board, player):
    """Check if the player win the game validation the rows, columns and
    diagonals
    """
    # Lines
    for y in range(BOARD_SIZE):
        victory = True
        for x in range(BOARD_SIZE):
            victory &= board[y][x] == player
        if victory:
            return True

    # Columns
    for x in range(BOARD_SIZE):
        victory = True
        for y in range(BOARD_SIZE):
            victory &= board[y][x] == player
        if victory:
            return True

    # Main diagonal
    victory = True
    for x in range(BOARD_SIZE):
        victory &= board[x][x] == player
    if victory:
        return True

    # Inverse diagonal
    victory = True
    for x in range(BOARD_SIZE):
        victory &= board[x][(BOARD_SIZE - 1) - x] == player
    if victory:
        return True


# Variables
board = create_board()
plays = []
player = PLAYER_1

# Algorithm
while True:
    display_board(board)

    if player == PLAYER_1:
        print(f'Player {player} turn...')
        position = input('Type a position (1-9): ')
        try:
            validate_position(position, plays)
        except InvalidPositionError as e:
            print(e)
            continue
        position = int(position)
        x, y = position_to_coords(position)
    else:
        position = random_position(plays)
        x, y = position_to_coords(position)

    plays.append(position)

    board[y][x] = player

    if check_victory(board, player):
        display_board(board)
        print(f'Player {player} win!')
        break

    if not has_available_play(plays):
        display_board(board)
        print(f'TIC TAC TOE!')
        break

    player = PLAYER_1 if player != PLAYER_1 else PLAYER_2
