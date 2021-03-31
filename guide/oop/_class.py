"""
Class

* Python is an object oriented programming language.
* Almost everything in Python is an object, with its properties and methods.
* A Class is like an object constructor, or a "blueprint" for creating objects.
* To create a class, use the keyword class.
* Class is a collection of related attributes and methods that try to
  represent a real-world situation. This idea of putting data and functions
  together in a class is central to the concept of object-oriented
  programming (OOP)

* Syntaxes to define a class:
  * class <name>:
  * class <name>():  # Same result of above
  * class <name>(<bases>)
  * class <name>(<bases>, metaclass=<meta>):
"""


###############################################################################
# Class
###############################################################################


# Define a class
# * To define some class, the "class" keyword must be used
class Client:
    pass


# Define a class with parenthesis
# * This works the same as the before example. This parenthesis are used to
#   define the base classes for this class.
class Person():
    pass


# Creating an instance
# * To create an instance of the class, just call the class
person = Person()
print(type(person))
# <class '__main__.Person'>


###############################################################################
# Class context
###############################################################################


# Class variables
# * These kind of variables will be shared between the instances of the class
# * If the value for this variable is changed, all of the classes will have the
#   value changed too
class Animal:
    name = 'Duck'


# Access class variable
# * To access a class variable, you access this from the class, not the
#   instance
print(Animal.name)
# Duck


# Class methods
# * Usually used to define other constructors for the class, or create a
#   factory methods
# * The decorator @classmethod is used to define this kind of method
# * Need to have as the first parameter the "cls", that represents the class
#   itself
class Vehicle:
    @classmethod
    def create(cls):
        return cls()


# Access class methods
# * To access a class method, you access this from the class, not the
#   instance
vehicle = Vehicle.create()
print(vehicle)
# <__main__.Vehicle object at 0x000002D75B713F70>


###############################################################################
# Static context
###############################################################################


# Static methods
# * Usually used to create utility methods (like Math.sum())
# * The decorator @staticmethod is used to define this kind of method
# * This kind of method does not have any reserved parameters as first
class Math:
    @staticmethod
    def sum(x, y):
        return x + y


# Access static methods
# * To access a class method, you access this from the class, not the
#   instance
print(Math.sum(5, 5))
# 10


###############################################################################
# Instance context
###############################################################################


# Define a class with constructor (__init__ method)
# * To define the constructor of the class you use the magic method __init__()
# * This constructor will be called when some instance of the class is being
#   created
# * NOTE: All the instance methods in the class must have the "self" parameter
#   as first
class House:
    def __init__(self, name):
        self.name = name


# Call constructor (__init__)
# * The constructor will be called during the instantiation of some object of
#   this class
home = House('My home')
print(home.name)
# My home


# Instance variables (properties)
# * Properties are variables for the instance, not the class
# * Each instance will have an own value for the instance variables
# * Properties are defined inside the constructor
class Lamp:
    def __init__(self):
        self.color = 'Yellow'


# Instance Methods
# * Methods are instance functions, that will use the properties to change the
#   state of the object
# * NOTE: All the instance methods in the class must have the "self" parameter
#   as first
class Light:
    def turn_on(self):
        self.__on = True


# Call instance method
# * To call the instance method, an instance of the class need to be created
#   first
light = Light()
light.turn_on()


# Class variable vs instance variable (CAUTION)
# * NOTE: If you access the class variable from the instance to set a new value
#   using normal way, the class variable will not be changed, as consequence a
#   new variable will be create for that instance
# * NOTE: DO NOT change the class variable from the instance, to avoid problems
fish = Animal()
fish.name = 'Fish'          # NOTE: It not changes the class variable
print(fish.name)            # Fish (new property)
print(fish.__class__.name)  # Duck (kept)
print(Animal.name)          # Duck (kept)
