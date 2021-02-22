"""
Ordered Dict

* Used to create a ordered dict. Python 3.6+ defined dicts as ordered by
  default, but some standard operations do not consider ordering. The
  OrderedDict provides some funtions that consider the ordering

* Syntax
  * OrderedDict(dict)
"""
import collections


# Ordered dict
dct = {'name': 'Vini', 'age': 26}
dct_ordered = collections.OrderedDict(dct)
print(dct_ordered)
# OrderedDict([('name', 'Vini'), ('age', 26)])


# Move to end
dct = {'name': 'Vini', 'age': 26}
dct_ordered = collections.OrderedDict(dct)
dct_ordered.move_to_end('name')
print(dct_ordered)
# OrderedDict([('age', 26), ('name', 'Vini')])


# Comparing
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'age': 26, 'name': 'Vini'}
print(dct1 == dct2)  # True (Standart dict)
dct1 = collections.OrderedDict(dct1)
dct2 = collections.OrderedDict(dct2)
print(dct1 == dct2)  # False (Ordered dict)


# Reverse iteration
dct = {'name': 'Vini', 'age': 26}
dct_ordered = collections.OrderedDict(dct)
for key, value in reversed(dct_ordered.items()):
    print(f'{key}: {value}', end=', ')
    # age: 26, name: Vini,
print()
