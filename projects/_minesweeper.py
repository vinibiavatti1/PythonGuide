"""
Minesweeper Game.

This game was based on Windows 98 Mineweeper game, and contains the same rule
logics of that.
"""
import random
import tkinter as tk
from tkinter import messagebox
from typing import Final


###############################################################################
# Constants
###############################################################################


WIDTH: Final[int] = 15
HEIGHT: Final[int] = 10
MINES_AMOUNT: Final[int] = 20


###############################################################################
# Classes
###############################################################################


class Mine:
    """
    Mine object class.
    """

    ###########################################################################
    # Magic Methods
    ###########################################################################

    def __init__(self, mine_camp: 'MineCamp', x, y) -> None:
        """
        Construct a new mine object.
        """
        self.__mine_camp = mine_camp
        self.__x = x
        self.__y = y
        self.__is_bomb = False
        self.__width = 2
        self.__height = 0
        self.__button = None
        self.__clicked = False
        self.__bomb_char = '*'
        self.__bomb_bg_color = '#FF0000'
        self.__bg = '#C0C0C0'
        self.__colors = {
            '1': '#0000FF',
            '2': '#008000',
            '3': '#FF0000',
            '4': '#000080',
            '5': '#800000',
            '6': '#008080',
            '7': '#000000',
            '8': '#808080',
        }

    ###########################################################################
    # Public Methods
    ###########################################################################

    def create_ui(self, window: tk.Tk) -> tk.Button:
        """
        Create button UI to window.
        """
        button = tk.Button(
            master=window,
            text='',
            width=self.__width,
            height=self.__height,
            relief=tk.RAISED,
            font='Courier 12 bold',
            bg=self.__bg,
            borderwidth=1,
            command=self.click_event
        )
        button.grid(row=self.__y, column=self.__x)
        self.__button = button

    ###########################################################################
    # Public Methods
    ###########################################################################

    def click_event(self) -> None:
        """
        Click event handler.
        """
        if self.__clicked:
            return
        self.__clicked = True
        self.__button['relief'] = tk.SUNKEN
        if self.__is_bomb:
            self.__button['text'] = self.__bomb_char
            self.__button['bg'] = self.__bomb_bg_color
            messagebox.showwarning(title='Dead', message='You died!')
            self.__mine_camp.reset()
            return
        neighbors = self.__mine_camp.get_neighbors(
            self.__x, self.__y,
        )
        bomb_neighbors = [mine for mine in neighbors if mine.is_bomb]
        bomb_amount = len(bomb_neighbors)
        if bomb_amount > 0:
            bomb_amount_str = str(bomb_amount)
            self.__button['text'] = bomb_amount_str
            self.__button['fg'] = self.__colors[bomb_amount_str]
            self.__button['bg'] = self.__bg
        else:
            for mine in neighbors:
                if not mine.clicked:
                    mine.click_event()
        self.__mine_camp.inc_selection_amount()
        if self.__mine_camp.is_won():
            messagebox.showinfo(title='Success', message='You won!')
            self.__mine_camp.reset()
            return

    def destroy_ui(self) -> None:
        """
        Destroy button ui.
        """
        self.__button.destroy()

    ###########################################################################
    # Properties
    ###########################################################################

    @property
    def mine_camp(self) -> 'MineCamp':
        return self.__mine_camp

    @property
    def clicked(self) -> bool:
        return self.__clicked

    @property
    def colors(self) -> dict[str, str]:
        return self.__colors

    @colors.setter
    def colors(self, colors: dict[str, str]) -> None:
        self.__colors = colors

    @property
    def bomb_bg_color(self) -> str:
        return self.__bomb_bg_color

    @bomb_bg_color.setter
    def bomb_bg_color(self, bomb_bg_color: str) -> None:
        self.__bomb_bg_color = bomb_bg_color

    @property
    def is_bomb(self) -> bool:
        return self.__is_bomb

    @property
    def button(self) -> tk.Button:
        return self.__button

    @is_bomb.setter
    def is_bomb(self, is_bomb: bool) -> None:
        self.__is_bomb = is_bomb

    @property
    def bg(self) -> str:
        return self.__bg

    @bg.setter
    def bg(self, bg: str) -> None:
        self.__bg = bg

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def bomb_char(self) -> str:
        return self.__bomb_char

    @bomb_char.setter
    def bomb_char(self, bomb_char) -> None:
        self.__bomb_char = bomb_char


class MineCamp:
    """
    MineCamp object class.
    """

    ###########################################################################
    # Magic Methods
    ###########################################################################

    def __init__(self, width: int, height: int, bomb_amount: int) -> None:
        """
        Construct a minecamp object.
        """
        if width < 0:
            raise ValueError(f'Invalid width: {width}')
        if height < 0:
            raise ValueError(f'Invalid height: {height}')
        if bomb_amount < 0 or bomb_amount > (width * height):
            raise ValueError(f'Invalid bomb amount: {bomb_amount}')
        self.__width = width
        self.__height = height
        self.__slot_amount = self.__width * self.__height
        self.__bomb_amount = bomb_amount
        self.__window = None
        self.__selection_amount = 0
        self.__create_mines()
        self.__create_bombs()

    ###########################################################################
    # Public Methods
    ###########################################################################

    def render(self, title: str) -> None:
        """
        Create and render minecamp GUI.
        """
        window = tk.Tk()
        window.title(title)
        for mine in self.__mines.values():
            mine.create_ui(window)
        self.__window = window
        window.mainloop()

    def reset(self) -> None:
        self.__selection_amount = 0
        for mine in self.__mines.values():
            mine.destroy_ui()
        self.__create_mines()
        self.__create_bombs()
        for mine in self.__mines.values():
            mine.create_ui(self.__window)

    def get_neighbors(self, x: int, y: int) -> list[Mine]:
        """
        Return the mine neighbors.
        """
        neighbors = list()
        for neighbor_y in range(y - 1, y + 2):
            if neighbor_y < 0 or neighbor_y > self.__height - 1:
                continue
            for neighbor_x in range(x - 1, x + 2):
                if neighbor_x < 0 or neighbor_x > self.__width - 1:
                    continue
                key = f'x{neighbor_x}y{neighbor_y}'
                neighbors.append(self.__mines[key])
        return neighbors

    def inc_selection_amount(self) -> None:
        """
        Increment selection amount.
        """
        self.__selection_amount += 1

    def is_won(self) -> bool:
        """
        Return True if the mine camp was won.
        """
        return \
            self.__selection_amount == self.__slot_amount - self.__bomb_amount

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __create_mines(self) -> None:
        """
        Create mines field.
        """
        self.__mines: dict[str, Mine] = dict()
        for y in range(self.__height):
            for x in range(self.__width):
                key = f'x{x}y{y}'
                mine = Mine(self, x, y)
                self.__mines[key] = mine

    def __create_bombs(self) -> None:
        """
        Set bombs into minecamp.
        """
        keys: list[str] = []
        for y in range(self.__height):
            for x in range(self.__width):
                keys.append(f'x{x}y{y}')
        random.shuffle(keys)
        amount = self.__bomb_amount
        if self.__bomb_amount > len(keys):
            amount = len(keys)
        for i in range(amount):
            self.__mines[keys[i]].is_bomb = True

    ###########################################################################
    # Properties
    ###########################################################################

    @property
    def selection_amount(self) -> int:
        return self.__selection_amount

    @property
    def mines_amount(self) -> int:
        return self.__bomb_amount

###############################################################################
# Functions
###############################################################################


def main() -> None:
    """
    Main method.
    """
    mine_camp = MineCamp(WIDTH, HEIGHT, MINES_AMOUNT)
    mine_camp.render('Minesweeper (By Vini)')


if __name__ == '__main__':
    main()
