"""
ABC (Abstract Base Class)

* The Abstract Base Class (ABC) in Python is a class that cannot be
  instantiated, and is used as a super class for classes that is considered
  abstract
* In other words, the ABC is the way to create abstract classes in Python
* The ABC class is located at "abc" module
* The "abc" module contains resources and utilities to handle abstract classes
* The ABC class uses the ABCMeta metaclass to handle the abstract classes
* An abstract class can be defined using the ways below:
  * class AbstractClass(ABC):  # Same behavior as below but simpler
  * class AbstractClass(metaclass=ABCMeta):
"""


###############################################################################
# Defining an abstract class
###############################################################################


# Importing the ABC class
# * First, we need to import the ABC class we can use the "abc" module
# * The ABCMeta class is used for the same purpose of the ABC class. Both are
#   imported in the example below but usually only the ABC class is used
from abc import ABC, ABCMeta


# Defining an abstract class (using ABC)
# * To define an abstract class we can simple inherit the ABC class
class AbstractClass(ABC):
    ...


# Defining an abstract class (using ABCMeta)
# * We can also use the ABCMeta to define an abstract class, however, using ABC
#   is simpler and less verbose
class AbstractClass(metaclass=ABCMeta):
    ...


###############################################################################
# Abstract methods/properties
###############################################################################


# Importing the abstractmethod decorator
# * To define an abstract method inside an abstract class, we need first to
#   import the `abstractmethod` decorator
from abc import abstractmethod


# Defining an abstract method
# * To define an abstract method we can use the `abstractmethod` decorator
# * Abstract methods are methods that must be implemented in the child class,
#   and doesn't have any implementation in the super class
# * NOTE: Note that the first argument is `self` since it is a method that
#   belongs to the class
class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        ...


# Defining an abstract class method
# * Abstract class methods is defined using the `classmethod` and
#   `abstractmethod` decorators
# * NOTE: Note that the first argument is `cls` since it is a class method
class AbstractClass(ABC):

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        ...


# Defining an abstract static method
# * Abstract static methods are defined using the `staticmethod` and
#   `abstractmethod` decorators
# * NOTE: Note that there is no first required argument since it is a static
#   method
class AbstractClass(ABC):

    @staticmethod
    @abstractmethod
    def abstract_static_method():
        ...


# Defining an abstract property
# * Abstract properties are defined using the `property` and
#   `abstractmethod` decorators
# * All property methods can be annotated as abstract methods (getter, setter
#   and deleter)
class AbstractClass(ABC):

    @property
    @abstractmethod
    def property(self):
        ...

    @property.setter
    @abstractmethod
    def property(self, x):
        ...

    @property.deleter
    @abstractmethod
    def property(self):
        ...


###############################################################################
# Instantiating an Abstract Class
###############################################################################


# Instantiating an Abstract Class
# * An abstract class that contains abstract methods cannot be instantiated
# * An abstract class is used only as a base class for other classes, providing
#   abstract methods that must be implemented in the child class
"""
x = AbstractClass()

Traceback (most recent call last):
  File "c:/.../_abc.py", line 73, in <module>
    x = AbstractClass()
        ^^^^^^^^^^^^^^^
TypeError: Can't instantiate abstract class AbstractClass with abstract method
abstract_method
"""


###############################################################################
# Use Case
###############################################################################


# Defining an abstract class
# * Here we are going to define an abstract class using the ABC class
# * Also, we will define a abstract method that must be implemented by the
#   child class
class Animal(ABC):

    @abstractmethod
    def say(self):
        pass


# Defining a child class and implement the abstract method
# * Here, we defined a class that inherits the abstract class we created above,
#   and implements the abstract method
class Duck(Animal):

    def say(self):
        print('Quack!')


# Testing
# * To test the use case, we can simple instantiate the child class and call
#   the implemented method
animal = Duck()
animal.say()
# Quack!
