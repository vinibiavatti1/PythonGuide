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
# * NOTE: Check _set.py file for more details
# * Return a new set object, optionally with elements taken from iterable.
# * Used to cast some object
# * Syntax
#   * set([iterable])
st1 = set()
st2 = set([1, 2, 3])
print(st1, st2, sep=', ')
# set(), {1, 2, 3}


# dict()
# * NOTE: Check _dict.py file for more details
# * Create a new dictionary. The dict object is the dictionary class
# * Used to cast some object
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
# * NOTE: Check _bool.py file for more details
# * Return a Boolean value (True or False)
# * x is converted using the truth testing procedure
# * If x is false or omitted, this returns False; otherwise it returns True
# * The bool class is a subclass of int
# * Used to cast some object
# * Syntax
#   * bool([x])
b1 = bool()
b2 = bool(1)
b3 = bool((1, 2, 3))
print(b1, b2, b3, sep=', ')
# False, True, True


# int()
# * NOTE: Check _numbers.py file for more details
# * Return an integer object constructed from a number or string x, or return 0
#   if no arguments are given
# * Used to cast some object
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
# * NOTE: Check _string.py file for more details
# * Return a string version of object
# * If neither encoding nor errors is given, str(object) returns
#   object.__str__()
# * Used to cast some object
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
# * Used to cast some object
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
# * Used to cast some object
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
# * Return a floating point number constructed from a number or string x
# * Used to cast some object
# * Syntax
#   * float([x])
f0 = float()
f1 = float('+1.23')
f2 = float(5)
f3 = float('3e2')
f4 = float('Infinity')
print(f0, f1, f2, f3, f4, sep=', ')
# 0.0, 1.23, 5.0, 300.0, inf


# tuple()
# * NOTE: Check _tuple.py file for more details
# * Creates a empty tuple
# * Used to cast some object
# * Syntax
#   * tuple([iterable])
tpl1 = tuple()
tpl2 = tuple([1, 2, 3])
print(tpl1, tpl2, sep=', ')
# (), (1, 2, 3)


# type()
# * NOTE: Check _type.py file for more details
# * With one argument, return the type of an object. The return value is a type
#   object and generally the same object as returned by object.__class__
# * The isinstance() built-in function is recommended for testing the type of
#   an object, because it takes subclasses into account
# * With three arguments, return a new type object. This is essentially a
#   dynamic form of the class statement
# * Syntax
#   * type(object)
#   * type(name, bases, dict)
print(type(1))      # <class 'int'>
print(type('abc'))  # <class 'str'>
print(type((1,)))   # <class 'tuple'>
obj = type('Tower', (Building,), {'name': 'Trump tower'})
print(obj.__dict__)
# {'name': 'Trump tower', '__module__': '__main__', '__doc__': None}


# frozenset()
# * NOTE: Check _frozenset.py file for more details
# * Return a new frozenset object, optionally with elements taken from iterable
# * Syntax
#   * frozenset([iterable])
fs1 = frozenset()
fs2 = frozenset([1, 2, 3])
print(fs1, fs2, sep=', ')
# frozenset(), frozenset({1, 2, 3})


# list()
# * NOTE: Check _list.py file for more details
# * Return a new list object, optionally with elements taken from iterable
# * Syntax
#   * list([iterable])
lst1 = list()
lst2 = list((1, 2, 3))
print(lst1, lst2, sep=', ')
# [], [1, 2, 3]


# complex()
# * Return a complex number with the value real + imag*1j or convert a string
#   or number to a complex number
# * Used to cast some object
# * Syntax
#   * complex([real[, imag]])
c1 = complex()
c2 = complex(1)
c3 = complex('1+2j')
c4 = complex(1.0, 5.5)
print(c1, c2, c3, c4, sep=', ')
# 0j, (1+0j), (1+2j), (1.0+5.5j)


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
# * Return the hash value of the object
# * Syntax
#   * hash(object)
h1 = hash(1)
h2 = hash(Tower('Eiffel'))
print(h1, h2, sep=', ')
# 1, 79828552111


# memoryview()
# * Return a 'memory view' object created from the given argument
# * Syntax
#   * memoryview(bytes-like-object)
mv = memoryview(b'abc')
print(tuple(mv))
# (97, 98, 99)


# all()
# * Return True if all elements of the iterable are true (or if the iterable is
#   empty)
# * Syntax
#   * all(iterable)
a1 = all((1, 2, 3))
a2 = all([1, 2, 0])
a3 = all({True, False})
a4 = all([])
print(a1, a2, a3, a4, sep=', ')
# True, False, False, True


# help()
# * NOTE: Check _dir_and_help.py file for more details
# * Help is used to get help related to the object passed during the call
# * This is usually used for Python REPL
# * Syntax
#   * help([object])
txt = 'Hello'
help(txt.upper)
# upper() method of builtins.str instance
#     Return a copy of the string converted to uppercase.


# min()
# * Return the smallest item in an iterable or the smallest of two or more
#   arguments
# * Syntax
#   * min(iterable, *[, key, default])
#   * min(arg1, arg2, *args[, key])
m1 = min((3, 1, 2))
m2 = min(3, 1, 2)
m3 = min({'n': 2}, {'n': 5}, key=lambda el: el['n'])
print(m1, m2, m3, sep=', ')
# 1, 1, {'n': 2}


# setattr()
# * The string must be the name of one of the object's attributes
# * The function set the named attribute, provided the object allows it
# * setattr(x, 'foobar', 1) is equivalent to x.foobar = 1
# * Syntax
#   * setattr(object, name, value)
class Tree:
    def __init__(self):
        self.x = 5
        self.y = 10


t = Tree()
setattr(t, 'x', 500)
print(t.__dict__)
# {'x': 500, 'y': 10}


# any()
# * Return True if any element of the iterable is true. If the iterable is
#   empty, return False
# * Syntax
#   * any(iterable)
a1 = any((1, 2, 3))
a2 = any([1, 2, 0])
a3 = any({True, False})
a4 = any([])
a5 = any([0, False])
print(a1, a2, a3, a4, a5, sep=', ')
# True, True, True, False, False


# dir()
# * NOTE: Check _dir_and_help.py file for more details
# * Dir returns list of the attributes and methods of any object (functions,
#   modules, strings, lists, dictionaries etc.)
# * If no argument is passed, dir will return the attributes and methods of the
#   current scope, not for the specified object
# * Syntax:
#   * dir([object])
lst = dir()
print(lst)
# ['Building', 'Car', 'Client', 'Math', 'Person', 'Tower', 'Tree',
# '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', ...]


# hex()
# * Convert an integer number to a lowercase hexadecimal string prefixed with
#   '0x'
# * If x is not a Python int object, it has to define an __index__() method
#   that returns an integer
# * Syntax
#   * hex(x)
h1 = hex(255)
h2 = hex(0)
h3 = hex(-255)
print(h1, h2, h3, sep=', ')
# 0xff, 0x0, -0xff


# next()
# * NOTE: Check _iterator.py file for more details
# * Retrieve the next item from the iterator by calling its __next__() method.
#   If default is given, it is returned if the iterator is exhausted, otherwise
#   StopIteration is raised
# * If default is given and the iterator is exhausted, it is returned instead
#   of raising StopIteration
# * Syntax
#   * next(iterator[, default])
lst = ['a', 'b', 'c']
lst_iter = iter(lst)
print(next(lst_iter))    # a
print(next(lst_iter))    # b
print(next(lst_iter))    # c
# print(next(lst_iter))  # StopIteration


# ascii()
# * As repr(), return a string containing a printable representation of an
#   object, but escape the non-ASCII characters in the string returned by
#   repr() using \x, \u or \U escapes
# * Syntax
#   * ascii(object)
asc = ascii({'name': 'Vini'})
print(asc)
# {'name': 'Vini'}


# divmod()
# * The divmod() method takes two numbers and returns a pair of numbers
#   (a tuple) consisting of their quotient and remainder
# * Syntax
#   * divmod(a, b)
res = divmod(9, 2)
print(res)
# (4, 1)


# id()
# * Return the 'identity' of an object
# * This is the address of the object in memory
# * Syntax
#   * id(object)
x = 5
print(id(x))
# 2433823304112 (can be other value)


# sorted()
# * NOTE: Check _sorted.py file for more details
# * Return a new sorted list from the items in iterable
# * Syntax
#   * sorted(iterable, *, key=None, reverse=False)
lst = ['C', 'B', 'A']
print(sorted(lst))
# ['A', 'B', 'C']


# bin()
# * Convert an integer number to a binary string prefixed with '0b'
# * Syntax
#   * bin(number)
txt = bin(10)
print(txt)
# 0b1010


# enumerate()
# * NOTE: Check the _enumerate.py file for more details
# * When you use enumerate(), the function gives you back two loop variables
#   * The index of the current iteration
#   * The value of the item at the current iteration
# * Syntax
#   * enumerate(iterable [, start])
tpl = ('a', 'b', 'c')
for index, value in enumerate(tpl):
    print(f'{index}: {value}', end=', ')
    # 0: a, 1: b, 2: c,
print()


# input()
# * NOTE: Check the _input.py file for more details
# * The input() function allows user input
# * Syntax
#   * input(prompt)
# * NOTE: The example will be commented to prevent interation in execution
#
# user_answer = input('Type your answer:')


# oct()
# * Convert an integer number to an octal string prefixed with '0o'
# * If x is not a Python int object, it has to define an __index__() method
#   that returns an integer
# * Syntax
#   * oct(x)
oc = oct(8)
print(oc)
# 0o10


# eval()
# * NOTE: Check the _eval.py file for more details
# * Evaluates some Python expression and return the new context value
# * The arguments are a string and optional globals and locals. If provided,
#   globals must be a dictionary. If provided, locals can be any mapping object
# * Syntax
#   * eval(expression[, globals[, locals]])
x = 2
x = eval('x ** 3')
print(x)
# 8


# open()
# * NOTE: Check the _open.py file for more details
# * Open file and return a corresponding file object.
# * If the file cannot be opened, an OSError is raised
# * Syntax
#   * open(file, mode='r', buffering=-1, encoding=None, errors=None,
#     newline=None, closefd=True, opener=None)
import os
import sys
f = open(os.path.join(sys.path[0], '../resources/file_read.txt'), 'r')
print(f.read())
# Lorem ipsum dolor sit amet...


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
