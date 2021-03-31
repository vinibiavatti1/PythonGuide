"""
Inheritance

* Inheritance allows us to define a class that inherits all the methods and
  properties from another class.
* Parent class is the class being inherited from, also called base class
* Child class is the class that inherits from another class, also called
  derived class.
* The base classes are defined in the () togueter the name of the class

Syntax: class Name(base_classes...):

* Reference:
  https://www.caelum.com.br/apostila-python-orientacao-a-objetos/heranca-multip
  la-e-interfaces#problema-do-diamante
"""


###############################################################################
# Base class
###############################################################################


# Define a class without base class
# * NOTE: If the class not has any class as the base, the object class will be
#   the base class implicit
class Person:  # base class: object
    pass


# Define a class with base class
# * To set the base class for some class, you have to set it inside the
#   parenthesis (bases tuple)
class Client(Person):
    pass


# Define more base classes
# * Python allows multi inheritance
class Employee():
    pass


class Worker(Person, Employee):
    pass


###############################################################################
# Base class context
###############################################################################


# Class context is not shered
# * The class context (class variables and methods) are not shared between the
#   child class
class File():
    version: 1


class CsvFile(File):
    pass  # CsvFile not contains version


# Instance context is shared
# * The instance context are shared between child class
class Car():
    def __init__(self, kind):
        self.kind = kind

    def honk(self):
        print('biiii!')


class Kombi(Car):
    pass


###############################################################################
# Inherited property/method
###############################################################################


# Access the inherited property and method
# * The child class will inherit the properties from base class
kombi = Kombi('car')  # (shared contructor)
print(kombi.kind)     # car (inherited)
kombi.honk()          # biiii! (inherited)


# Override constructor
# * You can override the base class constructor creating a new one constructor
#   in the child class
class Animal():
    def __init__(self, name):
        self.name = name


class Duck(Animal):
    def __init__(self):
        self.name = 'Donald'


animal = Duck()
print(animal.name)  # Donald


###############################################################################
# Base class constructor
###############################################################################


# Call the base class constructor (super())
# * There are two ways to call the constructor of the base class:
#   1. Using super() (Recommended) (Check _super.py file)
#   2. Using the base class name
# * Super uses the MRO (Method resolution order) to avoid inheritance problems
class Tower():
    def __init__(self, name):
        self.name = name


class Pisa(Tower):
    def __init__(self, name):
        super().__init__(name)


tower = Pisa('Pisa')
print(tower.name)  # Pisa


# Call the base class constructor (base class name)
# * This way is recommended just for multi inheritance, when the base classes
#   have different arguments in the constructor
# * NOTE: In this way, the MRO (Method resolution order) will not be executed
# * NOTE: This way you have to pass the self parameter to __init__ functions
class Building():
    def __init__(self, height):
        self.height = height


class Eiffel(Tower, Building):
    def __init__(self, name, height):
        Tower.__init__(self, name)
        Building.__init__(self, height)


eiffel = Eiffel('Eiffel', 300)
print(eiffel.name, eiffel.height, sep=', ')
# Eiffel, 300
