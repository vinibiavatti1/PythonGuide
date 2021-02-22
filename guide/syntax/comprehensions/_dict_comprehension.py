"""
Dict comprehension

* Dict comprehension offers a shorter syntax when you want to create a new dict
  based on the key and values of an existing dict.

Syntax: {value: value for value in iterable if condition == True}
        {key: value for key, value in dict.items() if condition == True}
"""


# Clone dict
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {k: v for k, v in dct1.items()}
print(dct2)
# {'name': 'Vini', 'age': 26}


# Create dict from matrix
lst = (('name', 'Vini'), ('age', 26))
dct = {v[0]: v[1] for v in lst}
print(dct)
# {'name': 'Vini', 'age': 26}


# Static value
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {k: 1 for k, vl in dct1.items()}
print(dct2)
# {'name': 1, 'age': 1}


# Transform element
dct1 = {'name': 'Vini', 'age': 'twenty-six'}
dct2 = {k: v.upper() for k, v in dct1.items()}
print(dct2)
# {'name': 'VINI', 'age': 'TWENTY-SIX'}


# Condition in element
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {k: v.upper() if isinstance(v, str) else v for k, v in dct1.items()}
print(dct2)
# {'name': 'VINI', 'age': 26}


# Condition in for
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {k: v for k, v in dct1.items() if k == 'name'}
print(dct2)
# {'name': 'Vini'}


# Condition (in) in for
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {k: v for k, v in dct1.items() if isinstance(v, int)}
print(dct2)
# {'age': 26}
