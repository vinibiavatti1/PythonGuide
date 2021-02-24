"""
Collection storage type

* The name of an ordinary variable is the name of its content
* The name of a list is the name of a memory location where the list is stored

* NOTE: The assignment: list_2 = list_1 copies the name of the array, not its
        contents. In effect, the two names (list_1 and list_2) identify the
        same location in the computer memory. Modifying one of them affects the
        other, and vice versa
"""


# Variable assignment
x = 1
y = x
x = 2
print(y)
# 1


# Collection assignment
x = [1, 2, 3]
y = x
del x[1]
print(y)
# [1, 3]


# Slices create a copy of list
x = [1, 2, 3]
y = x[:]
z = x[1:2]
del x[1]
print(y, z, sep=', ')
# [1, 2, 3], [2]
