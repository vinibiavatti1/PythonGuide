"""
Iterators

* An iterator is an object that contains a countable number of values, that can
  be iterated upon, like lists, tuples, dictionaries, strings and sets
* To define an object as an iterator, it must implement the `__iter__()` and
  `__next__()` methods from the iterator protocol
* To iterate over an iterator, you can use the for loop, or the methods below:

###############################################################################
Method                               Description
###############################################################################
iter(__iterable, __sentinel = None)  Return an iterator object
next(__i, __default = None)          Return the next item from iterator
###############################################################################
"""


###############################################################################
# Iter and Next
###############################################################################


# Creating an iterator
# * To create an iterator we can use the `iter()` function
# * The target object must implement the __iter__ and __next__ methods
# * The `iter()` function will perform the __iter__ method
x = [1, 2, 3]
x_iter = iter(x)


# Iterating over an iterator
# * To iterate over an iterator we can use the `next()` function
# * The `next()` function will perform the __next__ method
# * Note that the `next()` function will return a different value each time
#   that it is called
x = [1, 2, 3]
x_iter = iter(x)
print(next(x_iter))  # 1
print(next(x_iter))  # 2
print(next(x_iter))  # 3


# Iterating over an iterator (with exception)
# * When a iterator is over, the `next()` function will raise a StopIteration
#   exception
# * We can handle this case by using a try/except block
# * To avoid the exception, we can pass a default value to the `next()`
#   function (check the next example)
x = [1, 2, 3]
x_iter = iter(x)
try:
    print(next(x_iter))  # 1
    print(next(x_iter))  # 2
    print(next(x_iter))  # 3
    print(next(x_iter))  # <- This will raise a StopIteration exception
except StopIteration:
    print('StopIteration raised')
# StopIteration raised


# Iterating over an iterator (with default value)
# * When using a default value, the `next()` function will return the default
#   value when the iterator is over
x = [1, 2, 3]
x_iter = iter(x)
default = None
print(next(x_iter, default))  # 1
print(next(x_iter, default))  # 2
print(next(x_iter, default))  # 3
print(next(x_iter, default))  # None (default value)
print(next(x_iter, default))  # None (default value)


###############################################################################
# Iter and Next (Different Collections)
###############################################################################


# Iterating a list
# * The list is an iterable object, so we can iterate over it
x = [1, 2, 3]
x_iter = iter(x)
print(next(x_iter))  # 1
print(next(x_iter))  # 2
print(next(x_iter))  # 3


# Iterating a tuple
# * The tuple is an iterable object, so we can iterate over it
x = (1, 2, 3)
x_iter = iter(x)
print(next(x_iter))  # 1
print(next(x_iter))  # 2
print(next(x_iter))  # 3


# Iterating a set
# * The set is an iterable object, so we can iterate over it
# * Frozen sets are also iterable
# * NOTE: Sets are not ordered, so the iteration order is not guaranteed
x = {1, 2, 3}
x_iter = iter(x)
print(next(x_iter))  # 3
print(next(x_iter))  # 1
print(next(x_iter))  # 2


# Iterating a dictionary
# * for dictionaries, the iterator will return the keys of the dictionary
x = {'n1': 1, 'n2': 2, 'n3': 3}
x_iter = iter(x)
print(next(x_iter))  # n1
print(next(x_iter))  # n2
print(next(x_iter))  # n3


# Iterating a string
# * A string can be iterated, returning each character of the string
x = 'Hi!'
x_iter = iter(x)
print(next(x_iter))  # H
print(next(x_iter))  # i
print(next(x_iter))  # !


###############################################################################
# Iterator Sentinel
###############################################################################


# Defining a function
# * The `iter()` function can receive a sentinel parameter
# * The sentinel parameter is used to define a value that will stop the
#   iteration
# * For example, if we have a non-deterministic iterator (random numbers for
#   example), we can use the sentinel to stop the iteration when a specific
#   value is reached
# * When using the sentinel parameter, the first parameter must be a callable,
#   that will be called each time that the `next()` function is called
# * In this example, we will create a function that will return a random number
def random_number():
    from random import randint
    return randint(1, 3)


# Iterating with sentinel
# * Knowing that the number can be between 1 and 3, we can set the sentinel to
#   stop the iteration when the number 3 is reached
# * Note that the function reference is passed as the first parameter since the
#   iterator must be a callable when using the sentinel
# * The example below is not deterministic, so the result may vary
x_iter = iter(random_number, 3)
try:
    print(next(x_iter))  # 2
    print(next(x_iter))  # 1
    print(next(x_iter))  # <- This will raise a StopIteration exception
except StopIteration:
    print('StopIteration raised')
# StopIteration raised


###############################################################################
# Iterator Protocol
###############################################################################


# Implementing the iterator protocol
# * To implement the iterator protocol, we must implement the `__iter__()` and
#   `__next__()` methods
# * The `__iter__()` method must return the iterator object (a object that
#   implements the `__next__()` method)
# * The `__next__()` method must return the next value of the iterator
# * Note that the state of the iterator is stored in the object itself, so we
#   can have multiple iterators of the same object
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


# Iterating a custom object
# * Now we have a custom object that implements the iterator protocol, we can
#   iterate over it
x = CustomList(1, 2, 3)
x_iter = iter(x)
try:
    print(next(x_iter))  # 1
    print(next(x_iter))  # 2
    print(next(x_iter))  # 3
    print(next(x_iter))  # <- This will raise a StopIteration exception
except StopIteration:
    print('StopIteration raised')
# StopIteration raised
