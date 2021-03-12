"""
Collections

There are four collection data types:
* List is a collection which is ordered and changeable. Allows duplicate
  members
* Tuple is a collection which is ordered and unchangeable. Allows duplicate
  members
* Set is a collection which is unordered and unindexed. No duplicate members
* Frozenset is similar to set, but it cant be changed
* Dictionary is a collection which is unordered and changeable. No duplicate
  members
* When choosing a collection type, it is useful to understand the properties of
  that type
* Choosing the right type for a particular data set could mean retention of
  meaning, and it could mean an increase in efficiency or security
"""


###############################################################################
# Collections
###############################################################################


# List
# (V) Ordered
# (V) Changeable
# (V) Allow Duplicate
# (V) Indexed
lst = [1, 'two', None, True]


# Tuple
# (V) Ordered
# ( ) Changeable
# (V) Allow Duplicate
# (V) Indexed
tpl = (1, 'two', None, True)


# Set (unindexed)
# ( ) Ordered
# (V) Changeable
# ( ) Allow Duplicate
# ( ) Indexed
st = {1, 'two', None, True}


# Dict
# (V) Ordered (Sinse Python 3.7)
# (V) Changeable
# ( ) Allow Duplicate
# (V) Indexed
dct = {'name': 'Vini', 'age': 26}


# Frozenset
# ( ) Ordered
# ( ) Changeable
# ( ) Allow Duplicate
# ( ) Indexed
fst = frozenset({1, 2, 3, 4})


###############################################################################
# Builtin functions
###############################################################################


# Builtin functions for collections characteristics
# NOTE: Check _builtins.py file for more available functions
lst = [1, 5, 10, 15, 30]
print(sum(lst))  # 61    (The sum of elements)
print(min(lst))  # 1     (The min value)
print(max(lst))  # 30    (The max value)
print(len(lst))  # 5     (The length)
print(all(lst))  # True  (All values are True)
print(any(lst))  # True  (Any value is True)


# Builtin function to manupulate collections
# NOTE: Check _filter.py and _map.py for more details
lst = [1, 5, 10, 15, 30]
print(list(filter(lambda n: n > 10, lst)))  # [15, 30]
print(list(map(lambda n: n + 1, lst)))      # [2, 6, 11, 16, 31]


###############################################################################
# Memory
###############################################################################


# Memory comparison
tpl = (1, 2, 3)
lst = [1, 2, 3]
st = {1, 2, 3}
fst = frozenset({1, 2, 3})
dct = {'name': 'Vini', 'age': 26}
print(tpl.__sizeof__())  # 48
print(lst.__sizeof__())  # 104
print(st.__sizeof__())   # 200
print(fst.__sizeof__())  # 200
print(dct.__sizeof__())  # 216
