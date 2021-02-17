"""
Builtin resources
* Builtin resources means classes and functions that are always available for
  usage in Python
* To check the builtins, you can print then using dir(__builtins__)
"""


# -----------------------------------------------------------------------------
# Classes


# set([iterable])
# * Return a new set object, optionally with elements taken from iterable.
# * Used to cast some object to a set
# * Syntax
#   * set([iterable])
st1 = set()
st2 = set([1, 2, 3])
print(st1, st2, sep=', ')
# set(), {1, 2, 3}


# dict()
# * Create a new dictionary. The dict object is the dictionary class
# * Used to cast some object to a dict
# * Syntax
#   * dict(**kwarg)
#   * dict(mapping, **kwarg)
#   * dict(iterable, **kwarg)
dct1 = dict()
dct2 = dict(name='Vini', age=26)
dct3 = dict({'name': 'Vini'}, age=26)
dct4 = dict((('age', 26), ), name='Vini')
print(dct1, dct2, dct3, dct4, sep=', ')
# {}, {'name': 'Vini', 'age': 26}, {'name': 'Vini', 'age': 26},
# {'age': 26, 'name': 'Vini'}


# slice()
# *


# object()
# *


# bool()
# *


# int()
# *


# str()
# *


# bytearray()
# *


# super()
# *


# bytes()
# *


# float()
# *


# tuple()
# *


# type()
# *


# frozenset()
# *


# list()
# *


# complex()
# *


# -----------------------------------------------------------------------------
# Decorators


# staticmethod()
# * Transform a method into a static method.
# * A static method does not receive an implicit first argument
class Math:
    @staticmethod
    def sum(x, y):
        return x + y


# classmethod()
# * Transform a method into a class method.
# * A class method receives the class as implicit first argument
class Car:
    @classmethod
    def create(cls):
        return cls()


# property()
# * Define a property in some class
# * Can be used as a function to define a property (old way)
class Person:
    @property
    def name(self):        # Get
        return self._name

    @name.setter
    def name(self, name):  # Set
        self._name = name

    @name.deleter
    def name(self):        # Deleter
        del self._name


# -----------------------------------------------------------------------------
# Functions


# abs()
# * Return the absolute value of a number. The argument may be an integer, a
#   floating point number, or an object implementing __abs__(). If the argument
#   is a complex number, its magnitude is returned
# * Syntax
#   * abs(n)
x = 10
y = -5
print(abs(x), abs(y), sep=', ')
# 10, 5


# delattr()
# * The string must be the name of one of the object’s attributes.
# * The function  deletes the named attribute, provided the object allows it.
# * delattr(x, 'foobar') is equivalent to del x.foobar
# * Syntax
#   * delattr(object, name)
class Client:
    def __init__(self):
        self.x = 5
        self.y = 10


c = Client()
delattr(c, 'x')
print(c.__dict__)
# {'y': 10}


# hash()
# *


# memoryview()
# *


# all()
# *


# help()
# *


# min()
# *


# setattr()
# *


# any()
# *


# dir()
# *


# hex()
# *


# next()
# *


# ascii()
# *


# divmod()
# *


# id()
# *


# sorted()
# *


# bin()
# *


# enumerate()
# *


# input()
# *


# oct()
# *


# eval()
# *


# open()
# *


# breakpoint()
# *


# exec()
# *


# isinstance()
# *


# ord()
# *


# sum()
# *


# filter()
# *


# issubclass()
# *


# pow()
# *


# iter()
# *


# print()
# *


# callable()
# *


# format()
# *


# len()
# *


# chr()
# *


# range()
# *


# vars()
# *


# getattr()
# *


# locals()
# *


# repr()
# *


# zip()
# *


# compile()
# *


# globals()
# *


# map()
# *


# reversed()
# *


# __import__()
# *


# hasattr()
# *


# max()
# *


# round()
# *
