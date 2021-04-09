"""
Super

* Used to solve the diamond problem, when using multi inheritance
* This will call the constructors using Method Resolution Order (MRO)
* NOTE: The parameterless call to is recommended and sufficient for most use
  cases, and needing to change the search hierarchy regularly could be
  indicative of a larger design problem
* NOTE: if you are passing different parameters to a method being called via
  super, all the implementations of that method going up the MRO towards
  object() need to have compatible signatures
* NOTE: People omit calls to super(...).__init__ if the only superclass is
  'object', as, after all, object.__init__ doesn't do anything! However, this
  is very incorrect. Doing so will cause other classes' __init__ methods to not
  be called!
* NOTE: To use super() with different parameters between classes, the arbitraty
  parameters will be needed to use as arguments (*args, **kwargs)

Example:
* If __mro__ of object-or-type is D -> B -> C -> A -> object and the value of
  type is B, then super() searches C -> A -> object.

Syntax: super(type, object-or-type)
* type: The search starts from the class right after the type
* object-or-type: The object-or-type determines the method resolution order to
  be searched
* NOTE: It is recommended to use super() with parameterless

* Guido Van Rossum topic: http://python-history.blogspot.com/2010/06/
                          method-resolution-order.html
* Super harmful: https://fuhm.net/super-harmful/
"""


###############################################################################
# Base class call vs super()
###############################################################################


# Define inheritance without super()
# * In this, the method will be called by the base class name
# * This way will not fix the diamond problem (Check _mro.py)
class Car:
    def __init__(self, name):
        self.name = name


class Kombi(Car):
    def __init__(self):
        Car.__init__(self, 'Kombi')


# Create an instance of inheritance without super()
# * This will work correctly, but for multi inheritance, its is not recommended
car = Kombi()
print(car.name)
# Kombi


# Define inheritance with super()
# * In this situation, the method will be called by the super() keyword
class Tower:
    def __init__(self, name):
        self.name = name


class Pisa(Tower):
    def __init__(self):
        super().__init__('Pisa')  # Same of super(Tower, self) (Implicit)


# Create an instance of inheritance with super()
# * This is recommended because super() with follow the MRO
tower = Pisa()
print(tower.name)
# Pisa


###############################################################################
# Super parameters
###############################################################################


# Super parameters
# * NOTE: It is recommended to user super() with parameterless to prevent
#   architectural problems
# * In bellow versions of Python, the parameters of super were required
# * In this example, we used parameters just to show how it works
class Building(object):
    def __init__(self, name):
        self.name = name


class Castle(Building):
    def __init__(self):
        super(Castle, self).__init__('Castle')


# Create an instance of inheritance with super(parameters)
# * Using parameters in super() is not recommended
building = Castle()
print(building.name)
# Castle


###############################################################################
# Different methods signatures
###############################################################################


# Define an inheritance of different methods signatures
# * NOTE: To use different parameters to methods called with super and using
#   multi inheritance the *args and **kwargs must be used
# * This situation is common when multi-inheritance is being used, and the base
#   classes have different parameters in the methods
# * To solve this situation, the unique way is using the arbitrary parameters
class Auto:
    def __init__(self):
        super().__init__()


class Vehicle(Auto):
    def __init__(self, id, version, **kwargs):
        self.id = id
        self.version = version
        super().__init__(**kwargs)


class Bus(Auto):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)


class TourismBus(Vehicle, Bus):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Create an instance of inheritance witg different method signatures
# * To solve this problem, the parameters must be set using keyword arguments
bus = TourismBus(id='Vehicle', version=1, name='Tourism Bus')
print(bus.name, bus.id, bus.version, sep=', ')
# Tourism Bus, Vehicle, 1
