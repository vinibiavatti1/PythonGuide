"""
Sorted

* Return a new sorted list from the items in iterable
* key specifies a function of one argument that is used to extract a comparison
  key from each element in iterable
* reverse is a boolean value. If set to True, then the list elements are sorted
  as if each comparison were reversed

Syntax: sorted(iterable, *, key=None, reverse=False)
"""


# Sort collection
# tuple / list
lst = ['A', 'C', 'B']
lst = sorted(lst)
print(lst)


# Sort collection with dicts (key arg)
lst = [{'x': 1}, {'x': 3}, {'x': 2}]
lst = sorted(lst, key=lambda el: el['x'])
print(lst)
# [{'x': 1}, {'x': 2}, {'x': 3}]


# Sort collection reverse
lst = ['A', 'C', 'B']
lst = sorted(lst, reverse=True)
print(lst)
['C', 'B', 'A']
