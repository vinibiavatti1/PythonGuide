"""
Default Dict

* Defines a default datatype of action for map, to be considered when some
  key that doesnt exist is accessed

* Syntax
  * defaultdict(default_factory [, map])
"""
import collections


# Default Dict
dct = {'name': 'Vini', 'age': 26}
dct_default = collections.defaultdict(int, dct)
print(dct_default)
# defaultdict(<class 'int'>, {'name': 'Vini', 'age': 26})


# Integer
dct = collections.defaultdict(int)
txt = 'mississippi'
for letter in txt:
    dct[letter] += 1
print(dct)
# defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})


# Function
dct = {'name': 'Vini', 'age': 26}
default_dct = collections.defaultdict(lambda: 'Not found', dct)
print(default_dct['invalid_key'])  # Not found
print(default_dct)
# defaultdict(<function <lambda> at 0x00000191275DAA60>,
# {'name': 'Vini', 'age': 26, 'invalid_key': 'Not found'})
