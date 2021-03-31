"""
Super

* Used to solve the diamond problem, when using multi inheritance
* This will call the constructors using Method Resolution Order (MRO) __mro__
* NOTE: The parameterless call to is recommended and sufficient for most use
  cases, and needing to change the search hierarchy regularly could be
  indicative of a larger design problem
* NOTE: if you are passing different parameters to a method being called via
  super, all the implementations of that method going up the MRO towards
  object() need to have compatible signatures
* NOTE: People omit calls to super(...).__init__ if the only superclass is
  'object', as, after all, object.__init__ doesn't do anything! However, this
  is very incorrect. Doing so will cause other classes' __init__ methods to not
  be called.
* NOTE: To use super() with different parameters between classes the arbitraty
  parameters will be needed to use as arguments (*args, **kwargs)

Example:
* If __mro__ of object-or-type is D -> B -> C -> A -> object and the value of
  type is B, then super() searches C -> A -> object.

Syntax: super(type, object-or-type)
* type: The search starts from the class right after the type
* object-or-type: The object-or-type determines the method resolution order to
  be searched

* Guido Van Rossum topic: http://python-history.blogspot.com/2010/06/
                          method-resolution-order.html
* Super harmful: https://fuhm.net/super-harmful/
"""


###############################################################################
# Base class call vs Super
###############################################################################


# Method call with base class name
# * In this, the method will be called by the base class name
class Car:
    def __init__(self, name):
        self.name = name


class Kombi(Car):
    def __init__(self):
        Car.__init__(self, 'Kombi')


car = Kombi()
print(car.name)
# Kombi


# Method call with super()
# * In this, the method will be called by the super() keyword
# * NOTE: To use super(), even the root class need to call super to object!
class Tower:
    def __init__(self, name):
        self.name = name
        # NOTE: Even to object as base class the super has to be called!
        super().__init__()


class Pisa(Tower):
    def __init__(self):
        # Same of super(Tower, self) (Implicit)
        super().__init__('Pisa')


tower = Pisa()
print(tower.name)
# Pisa


###############################################################################
# Super parameters
###############################################################################


# Super parameters
# * NOTE: It is nor recommended to change the default parameters to super the
#   parametrization was allowed just to configure the MRO resolution in Python
#   2. For Python 3 we can use super without parameters (super()) and change
#   the default parameters can be indication of archicteture problems
class Building(object):
    def __init__(self, name):
        self.name = name
        # NOTE: Even to object as base class the super has to be called!
        super(Building, self).__init__()


class Castle(Building):
    def __init__(self):
        # Same of super(Castle, self) (Implicit)
        super(Castle, self).__init__('Castle')


building = Castle()
print(building.name)
# Castle


###############################################################################
# Dynamic super
###############################################################################


# Dynamic Super (super methods with different parameters)
# * NOTE: To use different parameters to methods called with super and using
#   multi inheritance the *args and **kwargs must be used
# * This situation is common when multi-inheritance is being used, and the base
#   classes have different parameters to the methods
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


bus = TourismBus(id='Vehicle', version=1, name='Tourism Bus')
print(bus.name, bus.id, bus.version, sep=', ')
# Tourism Bus, Vehicle, 1
