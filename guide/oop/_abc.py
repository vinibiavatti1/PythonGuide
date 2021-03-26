"""
ABC (Abstract Base Class)

* ABC the way to create abstract classes in Python
* abc is a module that has some resources to create abstract classes
* abc.ABC vs abc.ABCmeta is the same thing, the difference is that
  abc.ABCmeta needs to be defined as metaclass
"""
import abc


# Abstract Class
class Vehicle(abc.ABC):
    pass


# Abstract methods
class Vehicle2(abc.ABC):
    @abc.abstractmethod
    def run(self):
        pass


# Inheritance
class Car(Vehicle2):
    def __init__(self):
        self.speed = 0

    def run(self):
        self.speed += 1


car = Car()
car.run()
