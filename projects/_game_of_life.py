"""
Game of Life - Conway

* Cellular automaton devised by the British mathematician John Horton Conway
* It is Turing complete and can simulate a universal constructor or any other
  Turing machine
* Reference: https://www.conwaylife.com/wiki/Main_Page
"""
import os
import time
import copy


###############################################################################
# Constants
###############################################################################


# Rules Born/Survive
RULE_GOL = '3/23'
RULE_HIGH_LIFE = '23/36'
RULE_ASSIMILATION = '345/4567'
RULE_2X2 = '36/125'
RULE_DAY_AND_NIGHT = '3678/34578'
RULE_AMOEBA = '357/1358'
RULE_MOVE = '368/245'
RULE_PSEUDO_LIFE = '357/238'
RULE_DIAMOEBA = '35678/5678'
RULE_34 = '34/34'
RULE_LONG_LIFE = '345/5'
RULE_STAINS = '3678/235678'
RULE_SEEDS = '2/'
RULE_MAZE = '3/12345'
RULE_COAGULATIONS = '378/235678'
RULE_WALLED_CITIES = '45678/2345'
RULE_GNARL = '1/1'
RULE_REPLICATOR = '1357/1357'
RULE_MYSTERY = '3458/05678'


# Cell States
LIVE = '@'
DEAD = ' '


###############################################################################
# Classes
###############################################################################


# Exception
class GameOfLifeError(Exception):
    pass


# Game of life
class GameOfLife:
    def __init__(self, rule, width=70, height=50):
        """
        Constructs Game of Life
        """
        self.set_rule(rule)
        self.width = width
        self.height = height
        self.reset()
        self.reset_buffer()

    def set_rule(self, rule: str):
        """
        Sets the rule for the generation
        """
        msg = 'Rule must follow the format <born>/<survive>'
        if '/' not in rule:
            raise GameOfLifeError(msg)
        rule = rule.split('/')
        self.rule_survive = rule[1]
        self.rule_born = rule[0]
        self.rule = rule

    def reset(self):
        """
        Resets grid to empty
        """
        self.grid = [
            [DEAD for x in range(self.width)] for y in range(self.height)
        ]

    def reset_buffer(self):
        """
        Resets buffer to empty
        """
        self.buffer = [
            [DEAD for x in range(self.width)] for y in range(self.height)
        ]

    def set_cell_state(self, x, y, state=LIVE, buffer=False):
        """
        Sets a state for the cell in coordinates
        """
        self._validade_coords(x, y)
        if buffer:
            self.buffer[y][x] = state
        else:
            self.grid[y][x] = state

    def get_cell_state(self, x, y):
        """
        Gets the cell state from coordinates
        """
        try:
            self._validade_coords(x, y)
        except GameOfLifeError:
            return DEAD
        return self.grid[y][x]

    def get_adjacent_alives(self, x, y):
        """
        Gets the amount of alive cells adjacent of the coords cell
        """
        alives = 0
        alives += 1 if self.get_cell_state(x-1, y-1) == LIVE else 0
        alives += 1 if self.get_cell_state(x+0, y-1) == LIVE else 0
        alives += 1 if self.get_cell_state(x+1, y-1) == LIVE else 0
        alives += 1 if self.get_cell_state(x+1, y+0) == LIVE else 0
        alives += 1 if self.get_cell_state(x+1, y+1) == LIVE else 0
        alives += 1 if self.get_cell_state(x+0, y+1) == LIVE else 0
        alives += 1 if self.get_cell_state(x-1, y+1) == LIVE else 0
        alives += 1 if self.get_cell_state(x-1, y+0) == LIVE else 0
        return alives

    def print_grid_into_console(self):
        """
        Prints the grid to console
        """
        for y in self.grid:
            for x in y:
                print(x, end='')
            print()

    def next_generation(self):
        """
        Advances to the next generation
        """
        self.buffer = copy.deepcopy(self.grid)
        for y in range(self.height):
            for x in range(self.width):
                alives = self.get_adjacent_alives(x, y)
                if self.get_cell_state(x, y) == DEAD:
                    if str(alives) in self.rule_born:
                        self.set_cell_state(x, y, LIVE, True)
                else:
                    if str(alives) not in self.rule_survive:
                        self.set_cell_state(x, y, DEAD, True)
        self.grid = copy.deepcopy(self.buffer)

    def create_rule(self, born_tuple, survive_tuple):
        """
        Creates a rule based on born tuple and survive tuple
        """
        rule = ''.join(born_tuple)
        rule += '/'
        rule += ''.join(survive_tuple)
        return rule

    def _validade_coords(self, x, y):
        """
        Validate if coords are correct
        """
        if x < 0 or x >= self.width:
            raise GameOfLifeError('X must be in range (0 ~ width)')
        if y < 0 or y >= self.height:
            raise GameOfLifeError('Y must be in range (0 ~ height)')


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    game = GameOfLife(RULE_GOL)
    game.set_cell_state(35, 35)
    game.set_cell_state(36, 35)
    game.set_cell_state(36, 33)
    game.set_cell_state(38, 34)
    game.set_cell_state(39, 35)
    game.set_cell_state(40, 35)
    game.set_cell_state(41, 35)
    os.system('@echo off')
    game.print_grid_into_console()
    while True:
        os.system('cls')
        game.print_grid_into_console()
        game.next_generation()
        time.sleep(0.1)


# Init
if __name__ == '__main__':
    main()
