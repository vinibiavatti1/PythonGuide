"""
Dictionary (dict)

* Dictionaries are used to store data values in key:value pairs.
* A dictionary is a collection which is ordered, changeable and does not allow
  duplicates.
* Dictionaries are written with curly brackets, and have keys and values:
(V) Ordered
(V) Changeable
( ) Allow Duplicate
(V) Indexed
"""


# -----------------------------------------------------------------------------
# Intro


# Create dict
dct = {}  # empty
dct = {'name': 'Vini', 'age': 26}


# Nested dicts and lists inside
dct = {
    'name': 'Vini',
    'skills': ('Programming', 'Gamer'),
    'phones': {
        'primary': 123456789,
        'secondary': 987654321
    }
}


# Create dict using named arguments
dct = dict(name='Vini', age=26)
print(dct)
# {'name': 'Vini', 'age': 26}


# Copy dict
dct1 = {'name': 'Vini', 'age': 26}
dct2 = dict(dct1)
print(dct2)
# {'name': 'Vini', 'age': 26}


# Join dicts
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'skill': 'Python'}
print(dct1 | dct2)
# {'name': 'Vini', 'age': 26, 'skill': 'Python'}


dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'skill': 'Python'}
dct1.update(dct2)
print(dct1)
# {'name': 'Vini', 'age': 26, 'skill': 'Python'}


# Ordered
dct = {'name': 'Vini', 'age': 26}
print(dct)
# {'name': 'Vini', 'age': 26}


# Changeable
dct = {'name': 'Vini', 'age': 26}
dct['name'] = 'Truta'
print(dct['name'])
# Truta


# NOT Allow Duplicate
dct = {'name': 'Vini', 'age': 26, 'name': 'Truta'}
print(dct)
# {'name': 'Truta', 'age': 26}


# Length
dct = {'name': 'Vini', 'age': 26}
length = len(dct)
print(length)
# 2


# Umpack
dct = {'name': 'Vini', 'age': 26}
name, age = dct.values()
print(name, age)
# Vini 26


# -----------------------------------------------------------------------------
# Umpack
# NOTE: This is different then lists. The operator ** is used to umpack the key
#       and values from dict to use in other dict or to use as function
#       arguments


# Umpack in dict
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {**dct1, 'skill': 'Python'}
print(dct2)
# {'name': 'Vini', 'age': 26, 'skill': 'Python programmer'}


# Umpack as arguments
def sum(x, y):
    return x + y


dct = {'x': 4, 'y': 6}
val = sum(**dct)
print(val)
# 10


# -----------------------------------------------------------------------------
# Data access


# Index
dct = {'name': 'Vini', 'age': 26}
print(dct['name'])      # Vini
print(dct['age'])       # 26
print(dct.get('name'))  # Vini


# Check if key exists
dct = {'name': 'Vini', 'age': 26}
if 'name' in dct:
    print('"name" is present')


# For each keys
dct = {'name': 'Vini', 'age': 26}
for el in dct:
    print(el, end=', ')
    # name, age,
print()


# For each values
dct = {'name': 'Vini', 'age': 26}
for el in dct:
    print(dct[el], end=', ')
    # Vini, 26,
print()


# For each items
dct = {'name': 'Vini', 'age': 26}
for key, val in dct.items():
    print(f'{key}: {val}', end=', ')
    # name: Vini, age: 26
print()


# Print with dict comprehension
dct1 = {'name': 'Vini', 'age': 26}
{print(f'{key}: {val}', end=', ') for (key, val) in dct.items()}
# name: Vini, age: 26
print()


# Items
dct = {'name': 'Vini', 'age': 26}
items = dct.items()
for item in items:
    print(item, end=', ')
    # ('name', 'Vini'), ('age', 26),
print()


# Keys
dct = {'name': 'Vini', 'age': 26}
keys = dct.keys()
for key in keys:
    print(key, end=', ')
    # name, age,
print()

# Values
dct = {'name': 'Vini', 'age': 26}
values = dct.values()
for val in values:
    print(val, end=', ')
    # Vini, 26,
print()


# -----------------------------------------------------------------------------
# Change data


# Change by index
dct = {'name': 'Vini', 'age': 26}
dct['name'] = 'Truta'
print(dct)
# {'name': 'Truta', 'age': 26}


# Remove index with del
dct = {'name': 'Vini', 'age': 26}
del dct['name']
print(dct)
# {'age': 26}
