"""
Cellular Automata

* A cellular automaton is a discrete model of computation studied in automata
  theory
* A cellular automaton consists of a regular grid of cells, each in one of a
  finite number of states, such as on and off
* Rule 30 is an elementary cellular automaton introduced by Stephen Wolfram in
  1983. Using Wolfram's classification scheme, Rule 30 is a Class III rule,
  displaying aperiodic, chaotic behaviour
* This rule is of particular interest because it produces complex, seemingly
  random patterns from simple, well-defined rules. Because of this, Wolfram
  believes that Rule 30, and cellular automata in general, are the key to
  understanding how simple rules produce complex structures and behaviour in
  nature

Rule 30 example (Bin: 0011110 / Dec: 30)
###############################################################################
Dec     Bin     Result
###############################################################################
0       000     0
1       001     1
2       010     1
3       011     1
4       100     1
5       101     0
6       110     0
7       111     0
###############################################################################
"""


###############################################################################
# Constants
###############################################################################


# Cells states
ALIVE = 1
EMPTY = 0


###############################################################################
# Classes
###############################################################################


# Error module class
class CellularAutomataError(Exception):
    pass


# Cellular automata class
class CellularAutomata:
    def __init__(self, width=100):
        """
        Constructs Cellular Automata
        """
        self.width = width
        self.height = width // 2
        self.reset_grid()

    def make_rule_tuple(self, decimal: int):
        """
        Creates a rule tuple based on decimal number
        """
        if decimal < 0 or decimal > 255:
            raise CellularAutomataError('Decimal must be in range (0 ~ 255)')
        lst = []
        while decimal > 0:
            decimal, mod = divmod(decimal, 2)
            if mod > 0:
                lst.append(1)
            else:
                lst.append(0)

        while len(lst) < 8:
            lst.append(0)
        return tuple(reversed(lst))

    def reset_grid(self):
        """
        Resents the grid
        """
        self.grid = [
            [EMPTY for x in range(self.width)]
            for y in range(self.height)]
        self.grid[0][self.width // 2] = ALIVE

    def process_rule(self, rule_tuple):
        """
        Process the rule and generates the result
        """
        if len(rule_tuple) != 8:
            raise CellularAutomataError('Rule tuple must has 8 elements')
        for element in rule_tuple:
            if element != 0 and element != 1:
                msg = 'Rule tuple must contain binary values only (0 or 1)'
                raise CellularAutomataError(msg)
        rule = {
            '000': rule_tuple[7],
            '001': rule_tuple[6],
            '010': rule_tuple[5],
            '011': rule_tuple[4],
            '100': rule_tuple[3],
            '101': rule_tuple[2],
            '110': rule_tuple[1],
            '111': rule_tuple[0],
        }
        for y in range(1, self.height):
            for x in range(1, self.width - 1):
                c3 = self.grid[y - 1][x - 1]
                c2 = self.grid[y - 1][x]
                c1 = self.grid[y - 1][x + 1]
                pattern = f'{c3}{c2}{c1}'
                cell_state = rule[pattern]
                self.grid[y][x] = cell_state

    def print_grid(self, *, cell='1', empty=' '):
        """
        Prints the grid into console
        """
        for y in self.grid:
            for x in y:
                print(cell if x == 1 else empty, end='')
            print()


###############################################################################
# Algorithm
###############################################################################


# Main method
def main():
    cellular_automata = CellularAutomata()
    rule_tuple = cellular_automata.make_rule_tuple(30)
    cellular_automata.process_rule(rule_tuple)
    cellular_automata.print_grid()


# Init
if __name__ == '__main__':
    main()
