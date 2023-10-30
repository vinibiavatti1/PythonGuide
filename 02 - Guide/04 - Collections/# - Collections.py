"""
Collections

* Collections are containers that are used to store collections of data, i.e. a
  single variable will hold multiple values at a time
* When choosing a collection type, it is useful to understand the properties of
  that type
* Choosing the right type for a particular data set could mean retention of
  meaning, and it could mean an increase in efficiency or security
* Python has 5 built-in types of collections:
###############################################################################
Collection      Description
###############################################################################
Tuple           Stores a sequence of immutable objects
List            Stores a list of objects
Set             Stores a set of unique objects
Frozenset       Stores a set of immutable objects
Dictionary      Stores Key-Value pairs
###############################################################################
"""


###############################################################################
# Collections
###############################################################################


# Tuple
# * Tuples are used to store multiple items in a single variable. Differently
#   from lists, tuples are immutable
# * Usually, tuples contain multiple data types, since each tuple position can
#   be assigned to a different data type. Lists in the other hand, are defined
#   to store a single data type
# * NOTE: When using type hints, each tuple index must be defined:
#   (tuple[type1, type2, ...])
"""
Properties:
(X) Ordered
( ) Mutable
(X) Allows Duplicate
(X) Indexed
"""
x = (1, 2.5, 'Python', True, None)


# List
# * Lists are the most used collections in Python. They are used to store an
#   amount of same type of data
# * NOTE: When using type hints, lists are defined with a single type that will
#   determine the type of all elements in the list (list[type])
"""
Properties:
(X) Ordered
(X) Mutable
(X) Allows Duplicate
(X) Indexed
"""
x = [1, 2, 3, 4]


# Set
# * Sets are group of unique elements. They are used to store an amount of data
#   without duplicates and without an order
# * It follows the same rules of a mathematical set
"""
Properties:
( ) Ordered
(X) Mutable
( ) Allows Duplicate
( ) Indexed
"""
x = {1, 2, 3, 4}


# Frozenset
# * A frozenset is equivalent to a set, but it is immutable
# * A frozenset cannot be created using a literal, only using a existent set
#   to transform it into a frozenset
"""
Properties:
( ) Ordered
( ) Mutable
( ) Allows Duplicate
( ) Indexed
"""
x = {1, 2, 3, 4}
y = frozenset(x)


# Dictionary
# * Dictionaries are used to store data values in key:value pairs
# * To access a dictionary value, you must refer to its key name instead of its
#   index number
"""
Properties:
(X) Ordered
(X) Mutable
( ) Allows Duplicate
(X) Indexed
"""
x = {
    'name': 'Python',
    'version': 3.12
}


###############################################################################
# Memory Usage Comparison
###############################################################################


# Memory usage comparison
# * The memory usage of each collection type is different, since some has
#   different properties from others
# * NOTE: Since some collections stores only pointers to the data itself, the
#   memory usage of a collection can be the same for different data types
x1 = 1, 2, 3
x2 = [1, 2, 3]
x3 = {1, 2, 3}
x4 = frozenset({1, 2, 3})
x5 = {'n1': 1}
print(x1.__sizeof__())  # 048 bytes - Tuple
print(x2.__sizeof__())  # 072 bytes - List
print(x3.__sizeof__())  # 200 bytes - Set
print(x4.__sizeof__())  # 200 bytes - Frozenset
print(x5.__sizeof__())  # 168 bytes - Dictionary
