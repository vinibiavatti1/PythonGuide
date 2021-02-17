"""
Builtin resources

* Builtin resources means classes and functions that are always available for
  usage in Python
* To check the builtins, you can print then using dir(__builtins__)
* The full documentations for Builtin resources is available at:
  https://docs.python.org/3/library/functions.html
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
# * Return a slice object representing the set of indices specified by
#   range(start, stop, step)
# * The start and step arguments default to None
# * Slice objects have read-only data attributes start, stop and step which
#   merely return the argument values (or their default)
# * Slice objects are also generated when extended indexing syntax is used. For
#   example: a[start:stop:step] or a[start:stop, i]
# * Syntax:
#   * slice(stop)
#   * slice(start, stop[, step])
lst = [1, 2, 3, 4]
sl1 = slice(1, len(lst), 2)
lst1 = lst[1::2]  # Slice way
lst2 = lst[sl1]   # Indexing syntax way (the same result)
print(lst1, lst2, sep=', ')
# [2, 4], [2, 4]


# object()
# * Return a new featureless object
# * Object is a base for all classes
# * It has the methods that are common to all instances of Python classes
# * This function does not accept any arguments
obj = object()
print(obj)
# <object object at 0x000002A99E4981A0>


# bool()
# * Return a Boolean value (True or False)
# * x is converted using the truth testing procedure
# * If x is false or omitted, this returns False; otherwise it returns True
# * The bool class is a subclass of int
# * Syntax
#   * bool([x])
b1 = bool()
b2 = bool(1)
b3 = bool((1, 2, 3))
print(b1, b2, b3, sep=', ')
# False, True, True


# int()
# * Return an integer object constructed from a number or string x, or return 0
#   if no arguments are given
# * If x defines __int__(), int(x) returns x.__int__()
# * If x defines __index__(), it returns x.__index__()
# * If x defines __trunc__(), it returns x.__trunc__()
#  * For floating point numbers, this truncates towards zero
# * Syntax
#   * int([x])
#   * int(x, base=10)
i1 = int()
i2 = int(5.5)
i3 = int('5')
i4 = int(True)
i5 = int('a', base=11)
print(i1, i2, i3, i4, i5, sep=', ')
# 0, 5, 5, 1, 10


# str()
# * Return a string version of object
# * If neither encoding nor errors is given, str(object) returns
#   object.__str__()
# * Syntax
#   * str(object='')
#   * str(object=b'', encoding='utf-8', errors='strict')
# * There are six types of errors:
#   * strict: default response which raises a UnicodeDecodeError exception on
#     failure
#   * ignore: ignores the unencodable Unicode from the result
#   * replace: replaces the unencodable Unicode to a question mark
#   * xmlcharrefreplace: inserts XML character reference instead of
#     unencodable Unicode
#   * backslashreplace: inserts a \uNNNN espace sequence instead of
#     unencodable Unicode
#   * namereplace: inserts a \N{...} escape sequence instead of unencodable
#     Unicode
s1 = str(1)
s2 = str(True)
s3 = str(b'@', encoding='utf-8', errors='ignore')
print(s1, s2, s3, sep=', ')
# 1, True, @


# bytearray()
# * Return a new array of bytes
# * The bytearray class is a mutable sequence of integers in the range
#   0 <= x < 256
# * The optional source parameter can be used as str, int, object or interable
# * Syntax
#   * bytearray()
#   * bytearray(ints: Iterable[int])
#   * bytearray(string: Text, encoding: Text, errors: Text=...)
#   * bytearray(length: int)
ba1 = bytearray()
ba2 = bytearray('abc', encoding='utf-8')
ba3 = bytearray(5)
ba4 = bytearray((1, 2, 3))
print(ba1, ba2, ba3, ba4, sep=', ')
# bytearray(b''), bytearray(b'abc'), bytearray(b'\x00\x00\x00\x00\x00'),
# bytearray(b'\x01\x02\x03')


# super()
# * NOTE: Check the _super.py file for more details
# * Determines the MRO (method resolution order) to be searched
# * Its is recommended to use super without parameters, like 'super().method'
# * Syntax:
#   * super(type: Any, obj: Any)
class Building:
    def __init__(self, name):
        self._name = name


class Tower(Building):
    def __init__(self, name):
        super(Tower, self).__init__(name)


tower = Tower('Trump tower')
print(tower._name)
# Trump tower


# bytes()
# * Return a new bytes object, which is an immutable sequence of integers in
#   the range 0 <= x < 256
# * bytes is an immutable version of bytearray
# * It has the same non-mutating methods and the same indexing and slicing
#   behavior
# * Accordingly, constructor arguments are interpreted as for bytearray()
# * Syntax
#   * bytes(string: str, encoding: str, errors: str=...)
#   * bytes(length: int)
#   * bytes()
#   * bytes(o: SupportsBytes)
#   * bytes(iterable_of_ints) -> bytes
#   * bytes(string, encoding[, errors]) -> bytes
#   * bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
#   * bytes(int) -> bytes object of size given by the parameter
ba1 = bytes()
ba2 = bytes('abc', encoding='utf-8')
ba3 = bytes(5)
ba4 = bytes((1, 2, 3))
print(ba1, ba2, ba3, ba4, sep=', ')
# b'', b'abc', b'\x00\x00\x00\x00\x00', b'\x01\x02\x03'


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
