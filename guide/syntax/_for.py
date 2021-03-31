"""
For

* A for loop is used for iterating over a sequence (that is either a list, a
  tuple, a dictionary, a set, or a string)
"""


###############################################################################
# For range
###############################################################################


# For range(stop)
# * Arguments: range(0, stop, 1)
for i in range(5):
    print(i, end=', ')
print()
# 0, 1, 2, 3, 4,


# For range(start, stop)
# * Arguments: range(start, stop, 1)
for i in range(5, 10):
    print(i, end=', ')
print()
# 5, 6, 7, 8, 9,


# For range(start, stop, step)
# * Arguments: range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=', ')
print()
# 0, 2, 4, 6, 8,


# Unused index
# * Use the "_" when some variable is unused
for _ in range(10):
    pass


###############################################################################
# For each
###############################################################################


# For each string
# * String is cosidered collection too
txt = 'Hello world'
for char in txt:
    print(char, end='')
print()
# Hello world


# For each collection
# * Iterate a collection
tpl = (1, 2, 3)
for n in tpl:
    print(n, end=', ')
print()
# 1, 2, 3,


# For each collection with index
# * Iterate a collection with index
lst = ['a', 'b', 'c']
for i in range(len(lst)):
    print(f'{i}: {lst[i]}', end=', ')
print()
# 0: a, 1: b, 2: c,


# For each dict
# * As default, the for each in dict will return the key
dct = {'name': 'Vini', 'age': 26}
for key in dct:
    print(key, dct[key], end=', ')
print()
# name Vini, age 26, (keys)


# For each dict items()
# * Items returns the key and the value of the dictionary
for key, val in dct.items():
    print(f'{key}: {val}', end=', ')
print()
# name: Vini, age: 26


###############################################################################
# Break and continue
###############################################################################


# Break
# * Breaks the loop
for i in range(50):
    print(i, end=', ')
    if i == 5:
        break
print()
# 0, 1, 2, 3, 4, 5,


# Continue
# * Skips the rest of the loop code
for i in range(10):
    if i % 2 != 0:
        continue
    print(i, end=', ')
print()
# 0, 2, 4, 6, 8,


###############################################################################
# For else
###############################################################################


# For else
# * Else is executed after complete the loop
for i in range(5):
    print(i, end=', ')
else:
    print('end')
# 0, 1, 2, 3, 4, end
