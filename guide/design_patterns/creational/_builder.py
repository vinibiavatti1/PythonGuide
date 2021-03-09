"""
Builder design pattern

* Builder is a creational design pattern that lets you construct complex
  objects step by step. The pattern allows you to produce different types and
  representations of an object using the same construction code
* The Builder pattern suggests that you extract the object construction code
  out of its own class and move it to separate objects called builders
"""


# House class
class House:
    def __init__(self):
        self._color = None
        self._size = None
        self._floors = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def floors(self):
        return self._floors

    @floors.setter
    def floors(self, floors):
        self._floors = floors


# House builder class
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def with_color(self, color):
        self.house.color = color
        return self

    def with_size(self, size):
        self.house.size = size
        return self

    def with_floors(self, floors):
        self.house.floors = floors
        return self

    def build(self):
        return self.house


# Algorithm
house = HouseBuilder() \
    .with_color('red') \
    .with_size(120) \
    .with_floors(2) \
    .build()
print(house.color, house.size, house.floors, sep=', ')
# red, 120, 2
