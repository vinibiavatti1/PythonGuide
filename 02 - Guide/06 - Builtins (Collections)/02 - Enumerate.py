"""
Enumerate

* The `enumerate()` function transforms an iterable into a generator of tuples,
  where each tuple contains the index and the value of the iterable
* It is used to iterate over a iterable and get the index of the current
  iteration
* Basically, when we iterate over a collection using for-each, we don't have
  the index of the current iteration, so we can use enumerate to get the index
  of the current iteration when it is needed
* Syntax: enumerate(iterable, start=0)
"""


###############################################################################
# Enumerate Result
###############################################################################


# Adding indexes to a collection
# * The result of the enumerate function is a generator of tuples, where each
#   tuple contains the index and the value of the iterable
# * Note that in this example, we needed to convert the result of the enumerate
#   into a list since it is a generator
x = ['a', 'b', 'c']
x_enumerate = enumerate(x)
y = list(x_enumerate)
print(y)
# [(0, 'a'), (1, 'b'), (2, 'c')]


# Adding indexes to a collection (with start)
# * The `start` parameter is used to define the start index of the enumerate
# * Note that in the example below, the index starts at 1 instead of 0
x = ['a', 'b', 'c']
x_enumerate = enumerate(x, start=1)
y = list(x_enumerate)
print(y)
# [(1, 'a'), (2, 'b'), (3, 'c')]


###############################################################################
# Iterating Over an Enumerate
###############################################################################


# Iterating over an enumerate (with for-each) (XXX recommended XXX)
# * When can use the for-each to iterate over the enumerate
# * Since each item of the enumerate is a tuple, we can use tuple unpacking to
#   get the index and the value of the current iteration
x = ['a', 'b', 'c']
for index, value in enumerate(x):
    print(index, value, sep=': ')
# 0: a
# 1: b
# 2: c


# Iterating over an enumerate (with comprehension)
# * The enumerate can be used in a comprehension
# * In the example below, we will not store the comprehension result into
#   memory since we don't need it
x = ['a', 'b', 'c']
[print(index, value, sep=': ') for index, value in enumerate(x)]
# 0: a
# 1: b
# 2: c


# Iterating over an enumerate (with next)
# * The `next()` function can be used to iterate over the enumerate
# * Note that we don't need to convert the enumerate into a iterator with
#   `iter()` since the enumerate is already an iterator
x = ['a', 'b', 'c']
x_enumerate = enumerate(x)
try:
    print(next(x_enumerate))  # (0, 'a')
    print(next(x_enumerate))  # (1, 'b')
    print(next(x_enumerate))  # (2, 'c')
    print(next(x_enumerate))  # <- This will raise a StopIteration exception
except StopIteration:
    print('StopIteration raised')
# StopIteration raised


###############################################################################
# Using Enumerate in a Custom Collection
###############################################################################


# Creating a custom collection
# * Any iterable object can be used with the enumerate function
# * An iterable object is an object that implements the iterator protocol
# * In the example below, we will create a custom collection that implements
#   the `__iter__()` and `__next__()` methods
class CustomList:

    def __init__(self, *args):
        self.__list = args

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__list):
            raise StopIteration
        current = self.__list[self.__index]
        self.__index += 1
        return current


# Getting the enumerate result of a custom collection
# * Knowing that the custom collection implements the iterator protocol, we can
#   use the enumerate function to iterate over it
x = CustomList('a', 'b', 'c')
x_enumerate = enumerate(x)
y = list(x_enumerate)
print(y)
# [(0, 'a'), (1, 'b'), (2, 'c')]


# Iterating over a custom collection
# * We can also iterate over the custom collection since it implements the
#   iterator protocol
x = CustomList('a', 'b', 'c')
for index, value in enumerate(x):
    print(index, value, sep=': ')
# 0: a
# 1: b
# 2: c


###############################################################################
# How Enumerate Works
###############################################################################


# Creating a custom enumerate function
# * The enumerate function can be implemented by using the `yield` keyword to
#   create a generator
# * In the example below, we will create a custom enumerate function that
#   returns a generator of tuples
def my_enumerate(iterable, start=0):
    index = start
    for value in iterable:
        yield index, value
        index += 1


# Using the custom enumerate function
# * We can now use the custom enumerate function to iterate over a collection
#   as we would do with the built-in enumerate function
x = ['a', 'b', 'c']
for index, value in my_enumerate(x):
    print(index, value, sep=': ')
# 0: a
# 1: b
# 2: c
