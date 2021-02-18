"""
Collections

There are four collection data types:
* List is a collection which is ordered and changeable. Allows duplicate
  members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate
  members.
* Set is a collection which is unordered and unindexed. No duplicate members.
* Dictionary is a collection which is unordered and changeable. No duplicate
  members.
* When choosing a collection type, it is useful to understand the properties of
  that type.
* Choosing the right type for a particular data set could mean retention of
  meaning, and it could mean an increase in efficiency or security.
"""


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
# ( ) Ordered
# (V) Changeable
# ( ) Allow Duplicate
# (V) Indexed
dct = {'name': 'Vini', 'age': 26}


# Memory comparison
tpl = (1, 2, 3)
lst = [1, 2, 3]
st = {1, 2, 3}
dct = {'name': 'Vini', 'age': 26}
print(tpl.__sizeof__())  # 48
print(lst.__sizeof__())  # 104
print(st.__sizeof__())   # 200
print(dct.__sizeof__())  # 216
