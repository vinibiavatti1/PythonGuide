"""
Variables
"""


# Declaration
x = 1               # Integer
y = 'Hello world'   # String
avg = 3.5           # Float
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
