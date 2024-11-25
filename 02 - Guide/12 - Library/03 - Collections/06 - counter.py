"""
Counter

* A Counter is a dict subclass for counting hashable objects. It can be used
  to count every element individually.
* The Counter class is available in the collections module.
* The Counter is ordered by the elements and their counts. The most common
  elements are at the beginning.
* Syntax: Counter([iterable-or-mapping])
"""


###############################################################################
# Importing Resource
###############################################################################


# Importing the resource
# * We can import the resource using the import statement below
from collections import Counter


###############################################################################
# Creating Counters
###############################################################################


# Creating an empty Counter
# * We can create an empty counter using the Counter class
x = Counter()
print(x)
# Counter()


# Creating a Counter (with list)
# * We can create a counter using a list as a parameter
x = Counter(['a', 'b', 'b'])
print(x)
# Counter({'b': 2, 'a': 1})


# Creating a Counter (with string)
# * Since a string is an iterable, we can use it as a parameter
# * This will result in the same counter as the previous example
x = Counter('abb')
print(x)
# Counter({'b': 2, 'a': 1})


# Creating a Counter (with dict)
# * We can create a counter using a dict as a parameter
# * In this way, the keys will be the elements and the values will be the
#   counts
x = Counter({'a': 1, 'b': 2})
print(x)
# Counter({'b': 2, 'a': 1})


###############################################################################
# Counter Methods
###############################################################################


# Elements
# * The `elements()` method is used to get an iterator with the elements
x = Counter('aaabbc')
y = x.elements()
print(list(y))
# ['a', 'a', 'a', 'b', 'b', 'c']


# Most Common
# * The `most_common()` method is used to get the most common elements
# * It returns a list of tuples with the elements and their counts
x = Counter('aaabbc')
print(x.most_common())
# [('a', 3), ('b', 2), ('c', 1)]


# Most Common (with `n` set)
# * The `n` parameter is used to set the number of most common elements to
#   return. In the case below, the function will return the two most common
#   elements
x = Counter('aaabbc')
print(x.most_common(2))
# [('a', 3), ('b', 2)]


# Subtract
# * The `subtract()` method is used to subtract elements from another iterable
# * It accepts any iterable as a parameter
x = Counter('aaabbc')
x.subtract('abc')
print(x)
# Counter({'a': 2, 'b': 1, 'c': 0})


# Total
# * The `total()` method is used to get the total of all counts
x = Counter('aaabbc')
y = x.total()
print(y)
# 6


# From Keys
# * The `fromkeys()` method is used to create a new Counter from the keys of a
#   dictionary
x = Counter()
y = x.fromkeys({'a': 1, 'b': 2})
print(y)
# Counter({'a': 0, 'b': 0})


# Update
# * The `update()` method is used to update the counter with another iterable
x = Counter('aaabbc')
x.update('abc')
print(x)
# Counter({'a': 4, 'b': 3, 'c': 2})
