"""
Sin wave

* ASCII representation for a sin wave
"""
import math
import time
import os


###############################################################################
# Constants
###############################################################################


# Screen representation
WAVE_SIN_REPR = '#'
WAVE_COS_REPR = '$'
EMPTY = ' '

# Wave types
WAVE_SIN = 'sin'
WAVE_COS = 'cos'


###############################################################################
# Classes
###############################################################################


# Sin Wave generator class
class PolarWave:
    def __init__(self, width, height):
        """
        Constructs a Polar Wave Generator
        """
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        """
        Resets the grid
        """
        self.grid = [EMPTY for _ in range(self.width * self.height)]

    def process(self, angle, step, wave_type):
        """
        Generates a kind of wave by angle and step
        The wave type needs to be WAVE_SIN or WAVE_COS
        """
        if angle < 0 or angle > 360:
            raise ValueError('Angle must be in range (0 ~ 360)')
        for x in range(self.width):
            angle += step
            angle %= 360
            rad = angle * math.pi / 180
            if wave_type == 'sin':
                polar = math.sin(rad) + 1
            else:
                polar = math.cos(rad) + 1
            y = round((polar * (self.height - 1) / 2))
            rep = WAVE_SIN_REPR if wave_type == WAVE_SIN else WAVE_COS_REPR
            self.grid[y * self.width + x] = rep

    def process_sin(self, angle=0, step=1):
        """
        Generates the SIN wave by angle and step
        """
        self.process(angle, step, WAVE_SIN)

    def process_cos(self, angle=0, step=1):
        """
        Generates the COS wave by angle and step
        """
        self.process(angle, step, WAVE_COS)

    def render(self, bordered=True):
        """
        Renders grid in the console
        Set bordered to False to hide the border
        """
        if bordered:
            print('+', end='')
            [print('-', end='') for x in range(1, self.width + 1)]
            print('+')
        for y in range(self.height):
            if bordered:
                print('|', end='')
            for x in range(self.width):
                pos = y * self.width + x
                print(self.grid[pos], end='')
            if bordered:
                print('|')
            else:
                print()
        if bordered:
            print('+', end='')
            [print('-', end='') for x in range(1, self.width + 1)]
            print('+')


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    os.system('@echo off')
    wave = PolarWave(100, 10)
    angle = 10
    step = 10
    while True:
        wave.reset()
        wave.process_sin(angle, step)
        # wave.process_cos(angle, step)
        os.system('cls')
        wave.render()
        time.sleep(0.05)
        angle += step
        angle %= 360


# Init
if __name__ == '__main__':
    main()
