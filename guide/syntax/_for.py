"""
For (Loop Keyword)

* A for loop is used for iterating over a sequence (that is either a list, a
  tuple, a dictionary, a set, or a string)
* Syntax: for x in y:
"""


###############################################################################
# For Range (Iterate Ranges)
###############################################################################


# For range(stop)
# * Arguments: range(start=0, stop, step=1)
#   Stop: Specify the index to stop the range (x < stop)
for i in range(5):
    print(i, end=', ')
print()
# 0, 1, 2, 3, 4,


# For range(start, stop)
# * Arguments: range(start, stop, step=1)
#   Start: Specify the index to start the range (x >= start)
#   Stop: Specify the index to stop the range (x < stop)
for i in range(5, 10):
    print(i, end=', ')
print()
# 5, 6, 7, 8, 9,


# For range(start, stop, step)
# * Arguments: range(start, stop, step)
#   Start: Specify the index to start the range (x >= start)
#   Stop: Specify the index to stop the range (x < stop)
#   Step: Specify the increment to iterate over the range (x += step)
for i in range(0, 10, 2):
    print(i, end=', ')
print()
# 0, 2, 4, 6, 8,


# Unused index
# * Use the "_" when the variable is unused
for _ in range(10):
    pass


###############################################################################
# For Each (Iterate Collections: String, Tuple, List and Set)
###############################################################################


# For each string
# * String can be iterable as any collection
txt = 'Hello world'
for char in txt:
    print(char, end='')
print()
# Hello world


# For each tuple
# * Iterate a tuple
tpl = (1, 2, 3)
for n in tpl:
    print(n, end=', ')
print()
# 1, 2, 3,


# For each list
# * Iterate a list
lst = [1, 2, 3]
for n in tpl:
    print(n, end=', ')
print()
# 1, 2, 3,


# For each set
# * Iterate a set
# * NOTE: The set never has duplicated values. When the set is created, it
#   is performed to remove duplicate entries. Check the result of the
#   expression below for an example:
st = {1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1}
for n in st:
    print(n, end=', ')
print()
# 1, 2, 3,


###############################################################################
# For Each (Iterate Collections: Dictionary)
###############################################################################


# For each dict (default)
# * As default, the for each in a dict will return the key of each element
dct = {'name': 'Vini', 'level': 5}
for key in dct:
    print(key, end=', ')  # Uses dct[key] to access the value
print()
# name, level,


# For each dict (values)
# * Instead of the keys, values() returns the value of each element
for val in dct.values():
    print(val, end=', ')
print()
# Vini, 5


# For each dict (items)
# * Items returns the key and the value of the dictionary as a tuple
# * NOTE: You can unpack the returned tuple in the for
for key, val in dct.items():
    print(f'{key}: {val}', end=', ')
print()
# name: Vini, level: 5


###############################################################################
# For Each (Iterate Collections: Using Index)
###############################################################################


# For each collection with index
# * You can use the range to iterate a collection providing the length to
#   be able to access the index of all elements
lst = ['a', 'b', 'c']
for i in range(len(lst)):
    print(f'{i}: {lst[i]}', end=', ')
print()
# 0: a, 1: b, 2: c,


# For each collection with index and value
# * To have access to both data (index and value), you can use the built-in
#   function enumerate()
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(f'{index}: {value}', end=', ')
print()
# 0: a, 1: b, 2: c,


###############################################################################
# Break and Continue
###############################################################################


# Break
# * The break keyword stops the iteration
for i in range(50):
    print(i, end=', ')
    if i == 5:
        break  # Jump out of loop
print()
# 0, 1, 2, 3, 4, 5,


# Continue
# * The continue keyword skips the rest of the loop code
for i in range(10):
    if i % 2 != 0:
        continue  # Skip and process the next element
    print(i, end=', ')
print()
# 0, 2, 4, 6, 8,


###############################################################################
# For Else
###############################################################################


# For else
# * The else block in a for expression is always executed after complete the
#   loop
for i in range(5):
    print(i, end=', ')
else:
    print('end')
# 0, 1, 2, 3, 4, end
