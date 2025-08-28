"""
Tic Tac Toe

* Tic Tac Toe is a paper-and-pencil game for two players, X and O, who take
  turns marking the spaces in a 3×3 grid. The player who succeeds in placing
  three of their marks in a diagonal, horizontal, or vertical row is the winner
"""
import random


###############################################################################
# Constants
###############################################################################


# Players
PLAYER_X = 'X'
PLAYER_O = 'O'


###############################################################################
# Classes
###############################################################################


# Tic Tac Toe Exception
class TicTacToeError(Exception):
    pass


# Tic Tac Toe class
class TicTacToe:
    def __init__(self):
        """
        Constructs a Tic Tac Toe game
        """
        self.board = [i for i in range(1, 10)]
        self.current_player = PLAYER_X

    def play(self, position):
        """
        Chooses a position in the board for the current player
        """
        if not str(position).isdigit():
            raise TicTacToeError('The position must be a number')
        position = int(position)
        if position < 1 or position > 9:
            raise TicTacToeError('Invalid position')
        if not self.is_valid_position(position):
            raise TicTacToeError('The position must be empty')
        self.board[position - 1] = self.current_player
        self.swap_player()

    def is_valid_position(self, position):
        """
        Checks if the position is valid
        """
        if position < 1 or position > 9:
            raise TicTacToeError('Invalid position')
        return str(self.board[position - 1]).isdigit()

    def is_player_in_positions(self, player, *positions):
        """
        Checks if the player is in a list of positions
        """
        for pos in positions:
            if self.board[pos - 1] != player:
                return False
        return True

    def swap_player(self):
        """
        Swaps the current player
        """
        if self.current_player == PLAYER_X:
            self.current_player = PLAYER_O
        else:
            self.current_player = PLAYER_X

    def is_player_winner(self, player):
        """
        Checks if the player is the winner
        """
        h1 = self.is_player_in_positions(player, 1, 2, 3)
        h2 = self.is_player_in_positions(player, 4, 5, 6)
        h3 = self.is_player_in_positions(player, 7, 8, 9)
        v1 = self.is_player_in_positions(player, 1, 4, 7)
        v2 = self.is_player_in_positions(player, 2, 5, 8)
        v3 = self.is_player_in_positions(player, 3, 6, 9)
        d1 = self.is_player_in_positions(player, 1, 5, 9)
        d2 = self.is_player_in_positions(player, 3, 5, 7)
        return h1 or h2 or h3 or v1 or v2 or v3 or d1 or d2

    def get_winner(self):
        """
        Gets the winner. If there is no winner, returns None
        """
        px = self.is_player_winner(PLAYER_X)
        if px:
            return PLAYER_X
        po = self.is_player_winner(PLAYER_O)
        if po:
            return PLAYER_O
        return None

    def is_tictactoe(self):
        """
        Checks if there is no possible play to do
        """
        for pos in self.board:
            if str(pos).isdigit():
                return False
        return True

    def print_board(self):
        """
        Prints the board into console
        """
        b = self.board
        print('+', '+', '+', '+', sep='-----')
        print('| ', b[0], ' | ', b[1], ' | ', b[2], ' |')
        print('+', '+', '+', '+', sep='-----')
        print('| ', b[3], ' | ', b[4], ' | ', b[5], ' |')
        print('+', '+', '+', '+', sep='-----')
        print('| ', b[6], ' | ', b[7], ' | ', b[8], ' |')
        print('+', '+', '+', '+', sep='-----')


# Computer
class Computer:
    @staticmethod
    def choose_position(game):
        """
        Choose a random position in the board
        """
        available_positions = list(
            filter(lambda p: str(p).isdigit(), game.board)
        )
        return random.choice(available_positions)


# User interation class
class Interaction:
    @staticmethod
    def welcome():
        """
        Prints the welcome message
        """
        print('Welcome to Python Tic Tac Toe!')
        print('By: Vini')
        print()
        print('** Type enter to start! **')
        input()

    @staticmethod
    def play(game):
        """
        Ask for a position and make the play
        """
        while True:
            position = input('Choose a position (1 - 9): ')
            try:
                game.play(position)
                break
            except TicTacToeError as err:
                print(err)
                continue


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    """
    Main method
    """
    Interaction.welcome()
    game = TicTacToe()
    player = random.choice((PLAYER_X, PLAYER_O))
    winner = None
    game.print_board()
    while True:
        print(f'Player {game.current_player} turn...')
        if game.current_player == player:
            Interaction.play(game)
        else:
            position = Computer.choose_position(game)
            game.play(position)
        game.print_board()
        winner = game.get_winner()
        if winner is not None:
            print(f'The player {winner} won this game!')
            break
        if game.is_tictactoe():
            print(f'TIC TAC TOE!')
            break


# Init
if __name__ == '__main__':
    main()
