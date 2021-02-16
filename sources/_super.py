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

Syntax: super(t, obj)
* t: The class that MRO will be followed
* obj: The parameters to share in MRO

* Guido Van Rossum topic: http://python-history.blogspot.com/2010/06/
                          method-resolution-order.html
* Super harmful: https://fuhm.net/super-harmful/
"""


# Method call with base class name
class Car:
    def __init__(self, name):
        self.name = name


class Kombi(Car):
    def __init__(self):
        # Without super (base class method call)
        Car.__init__(self, 'Kombi')


car = Kombi()
print(car.name)
# Kombi


# Method call with super()
class Car2:
    def __init__(self, name):
        self.name = name
        # NOTE: Even to object as base class the super has to be called!
        super().__init__()


class Kombi2(Car2):
    def __init__(self):
        # Same of super(Kombi2, self) (Implicit)
        super().__init__('Kombi')


car = Kombi2()
print(car.name)
# Kombi


# Super parameters
# NOTE: It is nor recommended to change the default parameters to super
#       the parametrization was allowed just to configure the MRO resolution in
#       Python 2. For Python 3 we can use super without parameters (super())
#       and change the default parameters can be indication of archicteture
#       problems
class Car3(object):
    def __init__(self, name):
        self.name = name
        # NOTE: Even to object as base class the super has to be called!
        super(Car3, self).__init__()


class Kombi3(Car3):
    def __init__(self):
        # Same of super(Kombi2, self) (Implicit)
        super(Kombi3, self).__init__('Kombi')


car = Kombi3()
print(car.name)
# Kombi


# Cooperative Super (super with different parameters)
# NOTE: To use different parameters to methods called with super and using
#       multi inheritance the *args and **kwargs must be used
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
