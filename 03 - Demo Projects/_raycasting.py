"""
Raycasting

* Ray casting is the methodological basis for 3-D CAD/CAM solid modeling and
  image rendering
* The world famous video game Wolfenstein 3D was built from a square based grid
  of uniform height walls meeting solid-colored floors and ceilings
"""
import os
import math
import time


###############################################################################
# Constants
###############################################################################


# Entities
EMPTY = ' '
WALL = '#'
SKY = ' '
FLOOR = '.'


###############################################################################
# Classes
###############################################################################


# RayCasting error
class RayCastingError(Exception):
    pass


# Raycasting Camera
class RayCastingCamera:
    def __init__(self, x, y, width, height, angle, fov=60):
        """
        Constructs a camera for RayCasting
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.fov = fov

    def add_angle(self, angle):
        """
        Adds angle parsing it to the angle range
        """
        self.angle += angle
        self.angle %= 360

    def sub_angle(self, angle):
        """
        Subtracts angle parsing it to the angle range
        """
        self.angle -= angle
        self.angle %= 360


# Raycasting Map
class RayCastingMap:
    def __init__(self, width, height):
        """
        Constructs a map for Raycasting
        """
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        """
        Resets map to the initial state
        """
        self.map = [
            [EMPTY for x in range(self.width)] for y in range(self.height)
        ]
        for x in range(self.width):
            self.set_entity(x, 0)
            self.set_entity(x, self.height - 1)
        for y in range(self.height):
            self.set_entity(0, y)
            self.set_entity(self.width - 1, y)

    def get_entity(self, x, y):
        """
        Gets the entity from the map by position
        """
        self._validate_coords(x, y)
        return self.map[y][x]

    def set_entity(self, x, y, entity=WALL):
        """
        Sets the entity from the map by position
        """
        self._validate_coords(x, y)
        self.map[y][x] = entity

    def print_map(self):
        """
        Prints the map into console
        """
        for y in self.map:
            for x in y:
                print(x, end='')
            print()

    def _validate_coords(self, x, y):
        """
        Validates coordinates
        """
        if x < 0 or x >= self.width:
            raise RayCastingError('Invalid x coordinate')
        if y < 0 or y >= self.height:
            raise RayCastingError('Invalid y coordinate')


# Raycasting
class RayCasting:
    def __init__(self, rc_map, rc_camera):
        """
        Constructs a Raycasting object
        """
        self.rc_map = rc_map
        self.rc_camera = rc_camera
        self.precision = 5
        self.reset_screen()

    def reset_screen(self):
        """
        Resets the screen for the initial position
        """
        self.screen = [
            [EMPTY for x in range(self.rc_camera.width)]
            for y in range(self.rc_camera.height)
        ]

    def raycasting(self):
        """
        Runs the raycasting algorithm and render the result
        """
        angle_step = self.rc_camera.fov / self.rc_camera.width
        angle = self.rc_camera.angle - self.rc_camera.fov / 2

        # Throw rays
        for ray in range(self.rc_camera.width):
            angle %= 360

            # Get vectors
            cos = math.cos(math.radians(angle)) / self.precision
            sin = math.sin(math.radians(angle)) / self.precision

            # Check distance to wall
            init_x, init_y = self.rc_camera.x, self.rc_camera.y
            x, y = init_x, init_y
            entity = None
            while entity != WALL:
                entity = self.rc_map.get_entity(round(x), round(y))
                x += cos
                y += sin
            distance = math.hypot(x - init_x, y - init_y)

            # Get adjacent side distance
            distance = math.cos(math.radians(angle - self.rc_camera.angle)) \
                * distance
            distance /= 1.5

            # Draw
            self.draw_strip(ray, distance)
            angle += angle_step

    def draw_strip(self, x, distance):
        """
        Draws a strip in the screen
        """
        if x < 0 or x > self.rc_camera.width:
            raise RayCastingError('Invalid x coord value')

        cheight = self.rc_camera.height

        strip_start = distance
        strip_end = self.rc_camera.height - distance
        strip_start = math.floor(strip_start)
        strip_end = math.floor(strip_end)
        if strip_start < 0:
            strip_start = 0
        if strip_end >= cheight:
            strip_end = cheight - 1

        for i in range(0, strip_start):
            self.screen[i][x] = SKY
        for i in range(strip_start, strip_end):
            self.screen[i][x] = WALL
        for i in range(strip_end, cheight):
            self.screen[i][x] = FLOOR

    def print_screen(self):
        """
        Prints the screen into console
        """
        print('+', end='')
        [print('-', end='') for _ in range(self.rc_camera.width)]
        print('+')
        for y in self.screen:
            print('|', end='')
            for x in y:
                print(x, end='')
            print('|')
        print('+', end='')
        [print('-', end='') for _ in range(self.rc_camera.width)]
        print('+')


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    os.system('@echo off')
    rc_mp = RayCastingMap(20, 20)
    angle = 0
    rc_camera = RayCastingCamera(10, 10, 80, 25, angle)
    raycasting = RayCasting(rc_mp, rc_camera)

    while True:
        os.system('cls')
        raycasting.raycasting()
        raycasting.print_screen()
        raycasting.rc_camera.add_angle(5)
        time.sleep(0.1)


# Init
if __name__ == '__main__':
    main()
