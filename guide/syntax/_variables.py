"""
Variables

* the name of the variable must not be any of Python's keywords

* Scalars variables are variables represented with just one value
* Collections variables are variables represented with some collections
  containing scalar values
"""


# Declaration
x = 1               # Integer
y = 'Hello world'   # String
avg = 3.5           # Float
cpx = 2j            # Complex
lst = [1, 2, 3]     # List
tpl = (1, 2, 3)     # Tuple


# Multiple variables in same line
x, y, z = 1, 2, 3
print(x, y, z, sep=', ')
# 1, 2, 3
print()


# One value for multiple variables
x = y = z = 'Orange'
print(x, y, z, sep=', ')
# Orange, Orange, Orange
print()


# Swap without auxiliary
# NOTE: Without using this sintax, a aux variable would need to be used
x = 10
y = 5
x, y = y, x
print(x, y, sep=', ')
# 5, 5


# Unpack a Collection
lst = [1, 2, 3]
x, y, z = lst
print(x, y, z, sep=', ')
# 1, 2, 3
print()


# Concat
x, y = 'Hello', 'world'
print(x + ' ' + y)
# Hello world


# Concat with other datatype
# * NOTE: Other datatypes need to be cast to str
x, y = 'The ', 7
print(x + str(y))
# The 7
