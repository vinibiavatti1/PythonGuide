"""
Composite

* Composite is a structural design pattern that lets you compose objects into
  tree structures to represent part-whole hierarchies.
* Composite lets clients treat individual objects and compositions of objects
  uniformly.
* In other words, it allows you to create a tree structure where each node can
  be either a leaf or a composite.
"""


###############################################################################
# Composite
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Graphic
# * This interface defines the common operations for both leaf and composite
#   objects.
class Graphic(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


# Circle
# * This is a leaf node representing a circle.
class Circle(Graphic):
    def draw(self) -> None:
        print('()')


# Square
# * This is a leaf node representing a square.
class Square(Graphic):
    def draw(self) -> None:
        print('[]')


# Canvas
# * This is a composite node representing a drawing canvas.
# * Note that different from leafs, this class has a collection of child
#   components.
class Canvas(Graphic):
    def __init__(self) -> None:
        self.graphics: list[Graphic] = []

    def draw(self) -> None:
        for graphic in self.graphics:
            graphic.draw()


# Testing
# * Now, we will create a canvas and add some shapes to it.
# * Note that each leaf knows how to be drawn, and the composite knows how to
#   draw its children and itself.
canvas = Canvas()
canvas.graphics.append(Circle())
canvas.graphics.append(Square())
canvas.draw()
# ()[]
