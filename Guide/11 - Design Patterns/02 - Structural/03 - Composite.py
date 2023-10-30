"""
Composite design pattern

* Book: GOF
* Composite is a structural design pattern that lets you compose objects into
  tree structures and then work with these structures as if they were
  individual objects
* Using the Composite pattern makes sense only when the core model of your app
  can be represented as a tree
* Can be used to draw GUI interfaces
"""
from abc import ABC, abstractmethod


# Graphic ABC
class Graphic(ABC):
    @abstractmethod
    def render(self):
        pass


# Circle graphic
class Circle(Graphic):
    def render(self):
        print('Circle')


# Square graphic
class Square(Graphic):
    def render(self):
        print('Square')


# Composite
# NOTE: This is a Graphic too
class CompositeGraphic(Graphic):
    def __init__(self):
        self._graphics = []

    def add(self, graphic):
        self._graphics.append(graphic)

    def remove(self, graphic):
        self._graphics.remove(graphic)

    def render(self):
        for g in self._graphics:
            g.render()


# Algorithm
c1 = Circle()
c2 = Circle()
s1 = Square()
s2 = Square()

group1 = CompositeGraphic()
group1.add(c1)
group1.add(s1)

group2 = CompositeGraphic()
group2.add(c2)
group2.add(s2)

root = CompositeGraphic()
root.add(group1)
root.add(group2)

root.render()
# Circle
# Square
# Circle
# Square
