"""
Reduce

* The reduce is a process of generating a single value from an iterable, for
  example, sum all values from a list
* We can use the `functools.reduce()` function to reduce an iterable to a
  single value, but as the Python Community decided that this function is
  illegible, its is recommended to use the builtin functions or a normal for
  loop
* To use the `reduce()` function it must be imported from the `functools`
  module
* For simple operations, we can use the builtin reduce functions: `sum()`,
  `max()`, `min()`, `all()` and `any()`
* A comprehension cannot be used to reduce an iterable to a single value since
  it returns always a collection
* The `functools.reduce()` function has the parameters below:
  * function: The function that will be applied to every item of the iterable
  * iterable: The iterable that will be used to apply the function
  * initial: The initial value of the accumulator
* Syntax: reduce(function, iterable, initial = None)
"""


###############################################################################
# Functools Reduce
###############################################################################


# Importing the reduce function
# * To start using the reduce function, we need to import it from the functools
from functools import reduce


# The reduce function
# * The reduce function is used to reduce an iterable to a single value
# * The reduce function has the parameters `function`, `iterable` and `initial`
# * The `function` parameter is the function that will be applied to every item
#   of the iterable. This function must have two parameters:
#   * accumulator (a): The value that will be used to accumulate the result
#   * current (c): The current value of the iterable
# * In the example below, we will use a lambda function to sum all values of a
#   list
x = [1, 2, 3]
y = reduce(lambda a, c: a + c, x)
print(y)
# 6


# The reduce function (with initial value)
# * We can set an initial value to the accumulator using the `initial`
#   parameter
x = [1, 2, 3]
y = reduce(lambda a, c: a + c, x, 10)
print(y)
# 16


###############################################################################
# Builtin Reduce Functions
###############################################################################


# Sum
# * The `sum()` function is used to reduce an iterable to a single value by
#   summing all values
# * The second parameter is the initial value of the accumulator
x = [1, 2, 3]
y1 = sum(x)
y2 = sum(x, 10)
print(y1, y2)
# 6 16


# Max
# * The `max()` function is used to reduce an iterable to a single value by
#   getting the max value
# * The second parameter is the key function, used to determine how to get the
#   element from the iterable
# * Note that the second collection is a dictionary, in which we must set the
#   key function to define that the value of the dictionary will be used to
#   compare the values
x1 = [1, 2, 3]
x2 = {'n1': 1, 'n2': 3, 'n3': 2}
y1 = max(x1)
y2 = max(x2, key=lambda k: x2[k])
print(y1, y2)
# 3 n2


# Min
# * The same as the `max()` function, but it gets the min value
x1 = [1, 2, 3]
x2 = {'n1': 1, 'n2': 3, 'n3': 2}
y1 = min(x1)
y2 = min(x2, key=lambda k: x2[k])
print(y1, y2)
# 1 n1


# All
# * The `all()` function is used to reduce an iterable to a single value by
#   checking if all values are True
# * For each element the "truth test procedure" is applied
# * If all elements in the collection is considered True, the result will be
#   True, otherwise, the result will be False
# * Note that in the example below, the "x2" collection has a 0 value, that is
#   considered False
x1 = [1, 2, 3]
x2 = [1, 2, 0]
y1 = all(x1)
y2 = all(x2)
print(y1, y2)
# True False


# Any
# * Same as the `all()` function, but it checks if any value is True, i.e. if
#   at least one value is True
# * If all values are False, the result will be False, otherwise, the result
#   will be True
# * Note that in the example below, the "x2" collection has the 1 value, that
#   is considered True
x1 = [0, 0, 0]
x2 = [0, 0, 1]
y1 = any(x1)
y2 = any(x2)
print(y1, y2)
# False True


###############################################################################
# Reduce Operations
###############################################################################


# Reduce a collection (with builtin functions) (XXX recommended XXX)
# * Using the builtin functions is the recommended way to do a reduce operation
#   since they are more readable
# * In the example below, we are reducing the collection by summing all values
#   of the collection
x = [1, 2, 3]
y = sum(x)
print(y)
# 6


# Reduce a collection (with for-each)
# * We can use a for-each to reduce a collection when the builtin functions
#   cannot be used
# * It is recommended instead of using the `reduce()` function since it is
#   more readable
# * In the example below, we are reducing the collection by summing all values
#   using a for-each loop
x = [1, 2, 3]
y = 0
for n in x:
    y += n
print(y)
# 6


# Reduce a collection (with functools reduce)
# * We can use the `reduce()` function from the `functools` module to reduce a
#   collection
x = [1, 2, 3]
y = reduce(lambda a, c: a + c, x)
print(y)
# 6
