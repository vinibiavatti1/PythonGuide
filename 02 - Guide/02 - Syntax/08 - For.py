"""
For

* A for loop is used to iterate over a sequence (that is either a list, a
  tuple, a dictionary, a set, or a string)
* The difference of the "while" loop is that the "for" instruction will give
  the element of the collection, and the "while" does not set any variable
* Syntax: for x in y:
"""


###############################################################################
# For Range (Iterate Ranges)
###############################################################################


# Create a for loop to iterate a range (start)
# * The "for" loop can be used to iterate a range
# * In this example, we will show the range only set with the stop argument
# * Arguments: range(start=0, stop=<defined>, step=1)
#   stop: Specifies the index to stop the range (x < stop)
for i in range(5):
    print(i, end=' ')
print()
# 0 1 2 3 4


# Create a for loop to iterate a range (start, stop)
# * In this example, we will show the range set with the start and stop
#   arguments
# * Arguments: range(start=<defined>, stop=<defined>, step=1)
#   start: Specifies the index to start the range (x >= start)
#   stop: Specifies the index to stop the range (x < stop)
for i in range(5, 10):
    print(i, end=' ')
print()
# 5 6 7 8 9


# Create a for loop to iterate a range (start, stop, step)
# * In this example, we will show the range set with the start, stop and step
#   arguments
# * Arguments: range(start=<defined>, stop=<defined>, step=<defined>)
#   start: Specifies the index to start the range (x >= start)
#   stop: Specifies the index to stop the range (x < stop)
#   step: Specifies the increment to iterate over the range (x += step)
for i in range(0, 10, 2):
    print(i, end=' ')
print()
# 0 2 4 6 8


###############################################################################
# For Each (Iterate Collections)
###############################################################################


# Create a for loop to iterate a string
# * The "for" instruction can be used to iterate a collection
# * Each element of the collection will be given to the "for" variable
# * Strings can be iterated as any collection, since it is also a collection
txt = 'Hello World'
for char in txt:
    print(char, end='')
print()
# Hello World


# Create a for loop to iterate a tuple
# * The same way as above can be used to iterate a tuple
collection = (1, 2, 3)
for n in collection:
    print(n, end=' ')
print()
# 1 2 3


# Create a for loop to iterate a list
# * The same way as above can be used to iterate a list
collection = [1, 2, 3]
for n in collection:
    print(n, end=' ')
print()
# 1 2 3


# Create a for loop to iterate a set
# * The same way as above can be used to iterate a set
# * NOTE: The set never has duplicated values. When the set is created, it
#   is performed to remove duplicate entries. Check the result of the
#   expression below for an example:
collection = {1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1}
for n in collection:
    print(n, end=' ')
print()
# 1 2 3


# Create a for loop to iterate a frozenset
# * The same way as above can be used to iterate a frozenset
collection = frozenset({1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1})
for n in collection:
    print(n, end=' ')
print()
# 1 2 3


# Create a for loop to iterate a dictionary (by key)
# * The "for" instruction can also be used to iterate a dictionary
# * As default, the "for" will iterate each key of the dictionary
dictionary = {'name': 'Vini', 'level': 5}
for key in dictionary:
    print(key, end=' ')  # Uses dct[key] to access the value
print()
# name level


# Create a for loop to iterate a dictionary (by value)
# * Instead of the keys, the "values()" function from the dict can be used to
#   return the values of the dictionary that will be used to iterate
for val in dct.values():
    print(val, end=' ')
print()
# Vini 5


# Create a for loop to iterate a dictionary (by key and value)
# * The "items()" function returns the key and the value of the dictionary as a
#   tuple
# * We can unpack the returned tuple in the for as separated variables, like
#   the example below
for key, val in dct.items():
    print(f'{key}: {val}', end=', ')
print()
# name: Vini, level: 5,


###############################################################################
# For Each (Iterate Collections by Index)
###############################################################################


# Create a for loop to iterate a collection by index
# * We can use the "range()" function to provide the length of the collection,
#   and to iterate each index of the collection
# * The "len()" function returns the size of the list
collection = ['A', 'B', 'C']
for i in range(len(collection)):
    print(f'{i}: {collection[i]}', end=', ')
print()
# 0: A, 1: B, 2: C,


# Create a for loop to iterate a collection by index and value
# * To have access to both data (index and value), we can use the built-in
#   function "enumerate()"
# * The "enumerate()" function will return both data (index and value) as a
#   tuple
# * We can unpack the returned tuple in the for as separated variables, like
#   the example below
collection = ['A', 'B', 'C']
for index, value in enumerate(collection):
    print(f'{index}: {value}', end=', ')
print()
# 0: A, 1: B, 2: C,


###############################################################################
# For Loop with Else
###############################################################################


# Create a for loop with else
# * Python has a additional curious syntax. It is the "else" that can also be
#   used to "for" loops.
# * The else block in a for expression is always be executed after the loop
#   terminates normally (without a break)
# * It can be useful to ensure that some code will be performed only if the
#   loop is executed
for i in range(5):
    print(i, end=' ')
else:
    print('done')
# 0 1 2 3 4 done
