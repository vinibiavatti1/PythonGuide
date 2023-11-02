"""
Map

* The map process is used to apply a function to every item of iterable,
  transforming the values into another
* We can use comprehensions to do a map operation (recommended way), or use
  the `map()` builtin function
* Usually, the `map()` builtin function is used when a more complex operation
  is needed
* The `map()` builtin function returns a map object, that is a iterable
* Syntax: map(__func, *iterables)
"""


###############################################################################
# Map Object
###############################################################################


# The map object
# * The `map()` function will apply a action to every item of the iterable,
#   generating a new iterable
# * The function accepts two parameters:
#   * __func: The function that will be applied to every item of the iterable
#   * *iterables: One or multiple iterables that will be used to apply the
#     function
# * When using the map builtin function, we get a map object, that is a
#   iterable
x = [1, 2, 3]
x_map = map(lambda n: n + 1, x)
y = list(x_map)
print(y)
# [2, 3, 4]


# The map object (with multiple iterables)
# * Since the second argument "iterables" is arbitrary, we can pass multiple
#   iterables to the map function
# * When using multiple iterables, the `map()` must accept the same number of
#   arguments as the number of iterables, and the function will accept the same
#   number of arguments as the number of iterables, where each argument will be
#   the current value of the iterable
x1 = [1, 2, 3]
x2 = [4, 5, 6]
x_map = map(lambda n1, n2: n1 + n2, x1, x2)
y = list(x_map)
print(y)
# [5, 7, 9]


###############################################################################
# Map Operations
###############################################################################


# Map collection (with comprehension) (XXX recommended XXX)
# * The comprehension is the recommended way to do a map operation since
#   comprehensions are more readable
# * The `map()` function usually is used when a more complex operation is
#   needed
x = [1, 2, 3]
y = [n + 1 for n in x]
print(y)
# [2, 3, 4]


# Map collection (with map)
# * The `map()` function can be used to do a map operation
# * Note that the `map()` function returns a map object, that is a iterable.
#   Because of it, we need to convert the map object into a list to perform
#   and obtain the result
# * Check the example above to see how to using multiple iterables with map
x = [1, 2, 3]
x_map = map(lambda n: n + 1, x)
y = list(x_map)
print(y)
# [2, 3, 4]


# Map collection (with for-each)
# * The for-each can be used to do a map operation
# * Since comprehensions are more readable it is recommended to use them
x = [1, 2, 3]
y = []
for n in x:
    y.append(n + 1)
print(y)
# [2, 3, 4]
