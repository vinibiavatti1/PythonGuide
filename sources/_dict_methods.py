"""
Dictionary (dict) methods examples
"""
# items()
# Returns a list containing a tuple for each key value pair
dct = {'name': 'Vini', 'age': 26}
print(dct.items()) # dict_items([('name', 'Vini'), ('age', 26)])
for key, val in dct.items():
    print(f'{key}: {val}', end=', ') # name: Vini, age: 26, 
print()

# keys()
# Returns a list containing the dictionary's keys
dct = {'name': 'Vini', 'age': 26}
print(dct.keys()) # dict_keys(['name', 'age'])
for key in dct.keys():
    print(key, end=', ') # name, age, 
print()

# values()
# Returns a list of all the values in the dictionary
dct = {'name': 'Vini', 'age': 26}
print(dct.values()) # dict_values(['Vini', 26])
for val in dct.values():
    print(val, end=', ') # Vini, 26, 
print()

# clear()
# Removes all the elements from the dictionary
dct = {'name': 'Vini', 'age': 26}
dct.clear()
print(dct) # {}

# copy()
# Returns a copy of the dictionary
dct1 = {'name': 'Vini', 'age': 26}
dct2 = dct1.copy()
print(dct2) # {'name': 'Vini', 'age': 26}

# fromkeys(keys, [value])
# Returns a dictionary with the specified keys with the specified value or None if no value was informed
dct1 = {}
dct2 = dct1.fromkeys(('name', 'age'))
dct3 = dct1.fromkeys(('x', 'y'), 10)
print(dct2) # {'name': None, 'age': None}
print(dct3) # {'x': 10, 'y': 10}

# get(k, [default])
# Returns the value of the specified key
dct = {'name': 'Vini', 'age': 26}
print(dct.get('age')) # 26
print(dct.get('abc', 999)) # 999

# pop(k)
# Removes the element with the specified key
dct = {'name': 'Vini', 'age': 26}
dct.pop('name')
print(dct) # {'age': 26}

# popitem()
# Removes the last inserted key-value pair
dct = {'name': 'Vini', 'age': 26}
dct.popitem()
print(dct) # {'name': 'Vini'}

# setdefault(k, [default])
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
dct = {'name': 'Vini', 'age': 26}
val1 = dct.setdefault('name', 'Truta') # Already exists
val2 = dct.setdefault('skill', 'Python') # New
print(val1) # Vini
print(val2) # Python
print(dct) # {'name': 'Vini', 'age': 26, 'skill': 'Python'}

dct = {'name': 'Vini', 'age': 26}
val = dct.setdefault('skill') # No value
print(val) # None
print(dct) # {'name': 'Vini', 'age': 26, 'skill': None}

# update(m)
# Updates the dictionary with the specified key-value pairs
dct = {'name': 'Vini', 'age': 26}
dct.update({'skill': 'Python'})
print(dct) # {'name': 'Vini', 'age': 26, 'skill': 'Python'}

dct = {'name': 'Vini', 'age': 26}
dct.update(skill='Python')
print(dct) # {'name': 'Vini', 'age': 26, 'skill': 'Python'}