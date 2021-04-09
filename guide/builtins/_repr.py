"""
Repr (Representation)

* The repr function calls the __repr__ method inside the object
* By default, the __repr__ is implemented to show the memory position of the
  object created from object as base class
* To change the default implementation, just implement the __repr__ magic
  method inside the object class
"""


###############################################################################
# Repr
###############################################################################


# Define a class
# * This class will not implement the __repr__ method
class Person:
    def __init__(self, name):
        self.name = name


# Check the representation of the object
person = Person('Vini')
print(repr(person))  # <__main__.Person object at 0x000002E1FE1DCE80>
print(person)        # <__main__.Person object at 0x000002E1FE1DCE80> (same)


# Define a class with __repr__ implemented
# * In this case, we will re-implement the repr class to represent our object
#   in a better way
class Guy:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


# Check the representation of the object
guy = Guy('Vini')
print(repr(guy))  # Vini
print(guy)        # Vini (same)
