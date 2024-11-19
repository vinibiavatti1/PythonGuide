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
