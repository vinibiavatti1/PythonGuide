"""
Class

* Python is an object oriented programming language.
* Almost everything in Python is an object, with its properties and methods.
* A Class is like an object constructor, or a "blueprint" for creating objects.
* To create a class, use the keyword class.
"""


# Define class
class Client1:
    pass


class Client2():  # Used for extensions
    pass


# Create instance
client = Client1()  # New object

# -----------------------------------------------------------------------------
# Class scope


# Class variables
# * Variables that will be shared with the instances of the class
class Client3:
    name = 'Vini'


# Access class variable
print(Client3.name)
# Vini


# Class methods
# * Usually used to define other constructors for the class, or create a
#   factory methods
# * Has the 'cls' as first parameters to reference the class itself
class Client4:
    @classmethod
    def create(cls):
        return cls()


# Access class methods
print(Client4.create())
# <__main__.Client4 object at 0x000002D75B713F70>

# -----------------------------------------------------------------------------
# Static scope


# Static methods
# * Usually used to create utility methods (like Math.sum())
# * Dont has any parameters as first mandatory
class Math:
    @staticmethod
    def sum(x, y):
        return x + y


# Access static methods
print(Math.sum(5, 5))
# 10

# -----------------------------------------------------------------------------
# Instance scope


# Init (Constructor)
class Client5:
    # Called when create new object of this class (aka Contructor)
    def __init__(self, name):
        self._name = name  # Used _ to define it is a private property


# Access init (constructor)
client = Client5('Vini')  # Constructor


# Instance variables (properties)
class Client6:
    # Self as first parameter always for constructor
    def __init__(self):
        self._name = 'Vini'  # Property. Unique for each instance of the class


# Instance Methods
class Client7:
    # Self as first parameter always for instance methods
    def set_name(self, name):
        self._name = name


c = Client7()
c.set_name('Vini')


# -----------------------------------------------------------------------------
# CAUTION


# NOTE: If you access the class variable from the instance to set a new value
#       using normal way, the class variable will not be changed, as
#       consequence a new variable will be create for that instance
class Car:
    whells = 4


car1 = Car()

# DO NOT changed the class variable. It created a new variable in instance
car1.whells = 3
print(car1.whells)            # 3 (new property)
print(car1.__class__.whells)  # 4 (kept)
print(Car.whells)             # 4 (kept)
