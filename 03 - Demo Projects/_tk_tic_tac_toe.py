"""
Impossible TK Tic Tac Toe
"""
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox


###############################################################################
# Constants
###############################################################################


PLAYER = 'X'
COMPUTER = 'O'
EMPTY = ' '


###############################################################################
# Classes
###############################################################################


# Game
class TicTacToe:
    def __init__(self):
        self.reset_data()
        self.current_player = PLAYER
        self.play_count = 0

    def create_window(self):
        self.window = tk.Tk()

        font = tkfont.Font(size=20)
        label = tk.Label(
            self.window,
            text='Welcome back, Headstrong!',
            anchor=tk.CENTER,
            font=font
        )
        label.grid(row=0, column=0, columnspan=3)

        for y in range(3):
            for x in range(3):
                btn = tk.Button(
                    self.window,
                    text=EMPTY,
                    command=lambda x=x, y=y: self.play(
                        self.current_player, x, y
                    ),
                    width=10,
                    height=5,
                    anchor=tk.CENTER,
                    font=font
                )
                btn.grid(row=x + 1, column=y)
                self.btngrid[y][x] = btn
        self.window.mainloop()

    def start(self):
        self.create_window()

    def reset_data(self):
        self.grid = [[EMPTY for _ in range(3)] for __ in range(3)]
        self.btngrid = [[None for _ in range(3)] for __ in range(3)]
        self.play_count = 0

    def reset(self):
        self.reset_data()
        self.window.destroy()
        self.start()

    def play(self, player, x, y):
        if self.grid[y][x] != EMPTY:
            messagebox.showerror('Error', 'Cannot play in this position')
            return
        self.btngrid[y][x].configure(text=player)
        self.set(x, y, player)
        if player == PLAYER:
            self.play_computer()
            self.play_count += 1
        if self.check_tictactoe():
            messagebox.showinfo('Info', 'TIC TAC TOE!')
            self.reset()

    def set(self, x, y, player):
        self.grid[y][x] = player

    def get(self, x, y):
        return self.grid[y][x]

    def count_player_in_row(self, player, row):
        count = 0
        for pos in range(3):
            if self.get(row, pos) == player:
                count += 1
        return count

    def count_player_in_col(self, player, col):
        count = 0
        for pos in range(3):
            if self.get(pos, col) == player:
                count += 1
        return count

    def count_player_in_diag(self, player):
        count = 0
        for pos in range(3):
            if self.get(pos, pos) == player:
                count += 1
        return count

    def count_player_in_inv_diag(self, player):
        count = 0
        for pos in range(3):
            if self.get(pos, 2 - pos) == player:
                count += 1
        return count

    def play_in_available_position_in_row(self, row):
        for pos in range(3):
            if self.get(row, pos) == EMPTY:
                self.play(COMPUTER, row, pos)
                return True
        return False

    def play_in_available_position_in_col(self, col):
        for pos in range(3):
            if self.get(pos, col) == EMPTY:
                self.play(COMPUTER, pos, col)
                return True
        return False

    def play_in_available_position_in_diag(self):
        for pos in range(3):
            if self.get(pos, pos) == EMPTY:
                self.play(COMPUTER, pos, pos)
                return True
        return False

    def play_in_available_position_in_inv_diag(self):
        for pos in range(3):
            if self.get(pos, 2 - pos) == EMPTY:
                self.play(COMPUTER, pos, 2 - pos)
                return True
        return False

    def check_tictactoe(self):
        for y in range(3):
            for x in range(3):
                if self.get(x, y) == EMPTY:
                    return False
        return True

    def win(self):
        messagebox.showinfo('Info', 'Computer won!')
        self.reset()

    def play_by_search(self):

        #######################################################################
        # Check to win
        #######################################################################

        # Row
        for row in range(3):
            if (self.count_player_in_row(COMPUTER, row) == 2 and
                    self.count_player_in_row(PLAYER, row) == 0):
                res = self.play_in_available_position_in_row(row)
                if res:
                    self.win()
                    return

        # Col
        for col in range(3):
            if (self.count_player_in_col(COMPUTER, col) == 2 and
                    self.count_player_in_col(PLAYER, col) == 0):
                res = self.play_in_available_position_in_col(col)
                if res:
                    self.win()
                    return

        # Diag
        if (self.count_player_in_diag(COMPUTER) == 2 and
                self.count_player_in_diag(PLAYER) == 0):
            res = self.play_in_available_position_in_diag()
            if res:
                self.win()
                return

        # Inv Diag
        if (self.count_player_in_inv_diag(COMPUTER) == 2 and
                self.count_player_in_inv_diag(PLAYER) == 0):
            res = self.play_in_available_position_in_inv_diag()
            if res:
                self.win()
                return

        #######################################################################
        # Check to block
        #######################################################################

        # Row
        for row in range(3):
            if (self.count_player_in_row(PLAYER, row) == 2 and
                    self.count_player_in_row(COMPUTER, row) == 0):
                res = self.play_in_available_position_in_row(row)
                if res:
                    return

        # Col
        for col in range(3):
            if (self.count_player_in_col(PLAYER, col) == 2 and
                    self.count_player_in_col(COMPUTER, col) == 0):
                res = self.play_in_available_position_in_col(col)
                if res:
                    return

        # Diag
        if (self.count_player_in_diag(PLAYER) == 2 and
                self.count_player_in_diag(COMPUTER) == 0):
            res = self.play_in_available_position_in_diag()
            if res:
                return

        # Inv Diag
        if (self.count_player_in_inv_diag(PLAYER) == 2 and
                self.count_player_in_inv_diag(COMPUTER) == 0):
            res = self.play_in_available_position_in_inv_diag()
            if res:
                return

        #######################################################################
        # Random
        #######################################################################

        for y in range(3):
            for x in range(3):
                if self.get(x, y) == EMPTY:
                    self.play(COMPUTER, x, y)
                    return

    def play_computer(self):
        if self.play_count == 0:
            # Corner
            positions = []
            positions.append(self.get(0, 0))
            positions.append(self.get(0, 2))
            positions.append(self.get(2, 0))
            positions.append(self.get(2, 2))
            if PLAYER in positions:
                self.play(COMPUTER, 1, 1)
                return

            # Middle
            positions = []
            positions.append(self.get(0, 1))
            positions.append(self.get(1, 0))
            positions.append(self.get(1, 2))
            positions.append(self.get(2, 1))
            if PLAYER in positions:
                self.play(COMPUTER, 0, 0)
                return

            # Center
            self.play(COMPUTER, 0, 0)
            return
        elif self.play_count == 1:
            positions = []
            positions.append(self.get(0, 0))
            positions.append(self.get(2, 2))
            if ((self.get(0, 0) == PLAYER and self.get(2, 2) == PLAYER) or
                    (self.get(0, 2) == PLAYER and self.get(2, 0) == PLAYER)):
                self.play(COMPUTER, 0, 1)
                return
            elif self.get(1, 1) == PLAYER and self.get(2, 2) == PLAYER:
                self.play(COMPUTER, 0, 2)
            else:
                self.play_by_search()
                return
        else:
            self.play_by_search()
            return


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    game = TicTacToe()
    game.start()


# Init
if __name__ == '__main__':
    main()
