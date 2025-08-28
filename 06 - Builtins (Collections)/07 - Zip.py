"""
Zip

* The zip operation is used to aggregate elements from two or more iterables
* The `zip()` builtin function can be used for this purpose
* The function accepts one or more iterables and returns an iterator that
  aggregates elements from each of the iterables.
* The function parameters are:
  * *iterables: One or more iterables to be aggregated
  * strict: If True, an exception is raised if a iterable is exhausted before
    the others (default False)
* Syntax: zip(*iterables, strict = False)
"""


###############################################################################
# Zip Object
###############################################################################


# The zip object
# * The result of the zip function is an iterator that aggregates elements from
#   each of the iterables
# * It is used when we need to iterate over two or more iterables at the same
#   time
# * When the iterables have different sizes, the zip will stop when the
#   smallest iterable is exhausted
# * The zip function accepts two parameters:
#   * *iterables: One or more iterables to be aggregated
#   * strict: If True, an exception is raised if a iterable is exhausted before
#     the others (default False)
# * Note that in this example, we needed to convert the result of the zip into
#   a list since it is a generator
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c']
x_zip = list(zip(x1, x2))
print(x_zip)
# [(1, 'a'), (2, 'b'), (3, 'c')]


# The zip object (with strict)
# * The `strict` parameter is used to define if an exception should be raised
#   when a iterable is exhausted before the others
# * Note that in the example below, an exception is raised since the second
#   iterable is exhausted before the first
"""
x1 = [1, 2, 3]
x2 = ['a', 'b']
y = list(zip(x1, x2, strict=True))

ValueError: zip() argument 2 is shorter than argument 1
"""


# The zip object (with multiple iterables)
# * The zip function can accept multiple iterables as parameters
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c']
x3 = ['I', 'II', 'III']
x_zip = list(zip(x1, x2, x3))
print(x_zip)
# [(1, 'a', 'I'), (2, 'b', 'II'), (3, 'c', 'III')]


# The zip object (with string)
# * The string is a collection of characters, so it can be used as a iterable
#   for the zip function
x1 = [1, 2, 3]
x2 = 'abc'
x_zip = list(zip(x1, x2))
print(x_zip)
# [(1, 'a'), (2, 'b'), (3, 'c')]


###############################################################################
# Zip Operations
###############################################################################


# Iterating over a zip (with for-each) (XXX recommended XXX)
# * We can use the for-each to iterate over the zip object
# * Since each item of the zip is a tuple, we can use tuple unpacking to get
#   the values of the current iteration
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c']
for e1, e2 in zip(x1, x2):
    print(e1, e2, sep=': ')
# 1: a
# 2: b
# 3: c


# Iterating over a zip (with comprehension)
# * The zip can be used in a comprehension
# * In the example below, we will not store the comprehension result into
#   memory since we don't need it
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c']
[print(e1, e2, sep=': ') for e1, e2 in zip(x1, x2)]
# 1: a
# 2: b
# 3: c


# Iterating over a zip (with next)
# * We can use the `next` function to iterate over the zip object
# * Note that the next function returns a tuple with the values of the current
#   iteration
# * When the zip is exhausted, the `next` function will raise a StopIteration
#   exception
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c']
x_zip = zip(x1, x2)
try:
    print(next(x_zip))  # (1, 'a')
    print(next(x_zip))  # (2, 'b')
    print(next(x_zip))  # (3, 'c')
    print(next(x_zip))  # <- This will raise a StopIteration exception
except StopIteration:
    print('StopIteration raised')


###############################################################################
# Zip To Dictionary
###############################################################################


# Zip to dictionary
# * Since the dict constructor accepts a iterable of tuples, we can use the zip
#   function to create a dictionary
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c']
x_dict = dict(zip(x1, x2))
print(x_dict)
# {1: 'a', 2: 'b', 3: 'c'}
