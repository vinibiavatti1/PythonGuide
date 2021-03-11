"""
Prototype design pattern

* Book: GOF
* Prototype is a creational design pattern that lets you copy existing objects
  without making your code dependent on their classes
* The Prototype pattern delegates the cloning process to the actual objects
  that are being cloned. The pattern declares a common interface for all
  objects that support cloning. This interface lets you clone an object without
  coupling your code to the class of that object. Usually, such an interface
  contains just a single clone method.
"""
from copy import copy


# Rectangle class
class Rectangle:

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __copy__(self):
        return Rectangle(self.size, self.color)


# Algorithm
rect = Rectangle(10, 'red')
clone = copy(rect)
print(rect.size, clone.color, sep=', ')  # red, red
print(id(rect), id(clone), sep=', ')      # 1931064524752, 1931064522832 (diff)
