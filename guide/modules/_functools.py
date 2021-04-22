"""
Functools
"""
import functools


# Reduce
# * Reduce is used to reduce the iterable to a single value, manipulating the
#   current value and the accumulator value
# * NOTE: Check the _reduce.py file for more details
def plus(accumulator, current):
    return accumulator + current


lst = [5, 2, 7, 8, 3, 5]
result = functools.reduce(plus, lst)
print(result)
# 30


# Partial
# * Freezes the positional args and kwargs of a function and return a new
#   function with these parameters already set
def add(x, y):
    return x + y


fn = functools.partial(add, 4, 6)
print(fn())
# 10
