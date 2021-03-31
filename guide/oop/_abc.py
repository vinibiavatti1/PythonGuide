"""
ABC (Abstract Base Class)

* ABC the way to create abstract classes in Python
* abc is a module that has some resources to create abstract classes
* abc.ABC vs abc.ABCmeta is the same thing, the difference is that
  abc.ABCmeta needs to be defined as metaclass
"""
from abc import ABC, abstractmethod


###############################################################################
# ABC class
###############################################################################


# Define an abstract class
# * To define an ABC class you can pass the ABC class from abc module as
#   extension for the class
# * NOTE: ABC classes cannot be instantiated. They are used always as base
#   classes
class Vehicle(ABC):
    pass


# Implement the ABC class
# * To use the ABC class (Vehicle) as base class, you can just add this as
#   extension
class Car(Vehicle):
    pass


###############################################################################
# ABC method
###############################################################################


# Define abstract method
# * Abstract methods must create inside the ABC classes only
# * NOTE: The abstract method does not contains any implementation, and always
#   has the "pass" keyword as the body for the method
# * NOTE: This kind of method needs to be implemented in the child class
class Animal(ABC):
    @abstractmethod
    def say(self):
        pass


# Implement the ABC class with abstract method
# * When some ABC class containing an abstract method is inherited, this method
#   must be implemented as mandatory
class Duck(Animal):
    def say(self):
        print('quack!')


# Class abstract method
# * To call any abstract method it must be implemented in the concrete class
duck = Duck()
duck.say()
# quack!
