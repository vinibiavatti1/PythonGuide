"""
Reduce

* NOTE: The reduce() builtin function was removed from Python 3+. To use it you
  must import from functools module
* NOTE: Reduce function was removed because the Python Owner decided that this
  function is illegible, and 99% of times you can use a for loop to solve some
  reduce problem
* Reduce is used to reduce the iterable to a single value, manipulating the
  current value and the accumulator value
* Reduce has two parameters:
  * accumulator
  * current

* Syntax
  * reduce(function, iterable)
"""
from functools import reduce


# Sum values with def
def sum(accumulator, current):
    return accumulator + current


lst = [5, 2, 7, 8, 3, 5]
result = reduce(sum, lst)
print(result)
# 30


# Sum values with lambda
lst = [5, 2, 7, 8, 3, 5]
result = reduce(lambda a, c: a + c, lst)
print(result)
# 30


# Get the max
lst = [5, 2, 7, 8, 3, 5]
result = reduce(lambda a, c: c if c > a else a, lst)
print(result)
# 8
