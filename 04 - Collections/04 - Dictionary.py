"""
Dictionary

* Dictionaries are used to store data values in key:value pairs
* A dictionary is a collection which is ordered, changeable and does not allow
  duplicates keys
* A dictionary is indexed by its keys, so it facilitates the access for a
  specific value, without needing to iterate over the entire collection
* The key can be any immutable type, like strings, numbers and tuples
* NOTE: keys are case-sensitive, i.e. 'name' and 'Name' are different keys
* Dictionaries are written with curly brackets "{}"
* By default, when a variable is set with a empty curly brackets "{}", it is
  considered as a dictionary, not a empty set

Properties:
(X) Ordered
(X) Mutable
( ) Allow Duplicate
(X) Indexed
"""


###############################################################################
# Dictionary Operations
###############################################################################


# Creating a Dictionary
# * A dictionary can be created using curly brackets "{}"
# * Different from tuples, the curly brackets are mandatory
# * Dictionary is organized in key:value pairs, where the key is the index and
#   the value is the value of the element
# * NOTE: When using empty brackets, a dictionary will be created, not a set
x = {'name': 'John'}             # One key:value pair
x = {'name': 'John', 'age': 50}  # Two key:value pairs
x = {True: 1, False: 2}          # Other keys type
x = {}                           # Empty
x = dict()                       # With `dict()` function
x = dict(name='John', age=50)    # With `dict()` function and kwargs


# Type hint for a Dictionary
# * To set a type hint for a dictionary, two types must be defined, one for the
#   key and one for the value
# * You can use the Any type to define that the key or value can be any type
x: dict[str, int] = {'sum': 100, 'avg': 50, 'acc': 200}


# Cloning a Dictionary
# * Dictionaries can be cloned using the `dict()` function, passing the
#   dictionary to be cloned as argument
x = {'name': 'John', 'age': 50}
y = dict(x)
print(y)
# {'name': 'John', 'age': 50}


# Assignation by reference
# * When assigning a dictionary to another variable, the dictionary will be
#   passed by reference, so that any change in the new variable will affect
#   the original
# * To avoid this, the dictionary must be cloned
# * In the example below, note that the "y" variable was changed, and it
#   affected the "x" variable as well
x = {'name': 'John', 'age': 50}
y = x
y['name'] = 'Mary'
print(x)
# {'name': 'Mary', 'age': 50}


###############################################################################
# Dictionary Elements
###############################################################################


# Getting a value by key
# * A value from a dictionary can be obtained by its key
# * NOTE: If the key does not exists, it will raise an error. Use the method
#   `get()` to avoid raising an error or to set a default value when the key
#   does not exists
x = {'name': 'John', 'age': 50}
y = x['name']
print(y)
# John


# Setting a value by key
# * Since dictionaries are mutable and indexed, the elements can be changed
#   after creation by setting a value by key
# * If the key does not exists, it will be created
x = {'name': 'John', 'age': 50}
x['name'] = 'Mary'
x['gender'] = 'Female'
print(x)
# {'name': 'Mary', 'age': 50, 'gender': 'Female'}


# Removing key with del
# * The `del` keyword can be used to remove a key from a dictionary
x = {'name': 'John', 'age': 50}
del x['name']
print(x)
# {'age': 50}


# Checking if a key exists in a Dictionary
# * The `in` operator can be used to check if a key exists in a dictionary
x = {'name': 'John', 'age': 50}
print('age' in x)
# True


###############################################################################
# Dictionary Properties
###############################################################################


# (X) Ordered
# * Dictionaries are ordered, so when iterating over a dictionary, the elements
#   will be returned in the same order as they were inserted
x = {'name': 'John', 'age': 50}
print(x.popitem())
# ('age', 50)


# (X) Mutable
# * Dictionaries are mutable, so the elements can be changed
x = {'name': 'John', 'age': 50}
x['name'] = 'Mary'
print(x)
# {'name': 'Mary', 'age': 50}


# ( ) Allows Duplicate
# * Dictionaries don't allow duplicate keys, so if a key is duplicated, the
#   last value will be the one that will be stored
# * Note that in the example, the key 'x' is duplicated, so the value 1 will be
#   replaced by 2
x = {'name': 'John', 'name': 'Mary'}
print(x)
# {'name': 'Mary'}


# (X) Indexed
# * Dictionaries are indexed by its keys, so it facilitates the access for a
#   specific value, without needing to iterate over the entire collection
x = {'name': 'John', 'age': 50}
print(x['name'])
# John


###############################################################################
# Dictionary Built-in Functions
###############################################################################


# Dictionary Built-in Functions
# * The Python built-in functions for collections can be used with
#   dictionaries
# * Note that the functions `sum()`, `min()` and `max()` will return the
#   result based on the keys, not the values
x = {5: 'Five', 3: 'Three', 8: 'Eight'}
print(sum(x))  # 16    (The sum of keys)
print(min(x))  # 3     (The min key (if key can be ordered))
print(max(x))  # 8     (The max key (if key can be ordered))
print(len(x))  # 3     (The length (number of keys))
print(all(x))  # True  (All keys are True)
print(any(x))  # True  (Any key is True)


###############################################################################
# Dictionary Methods
###############################################################################


# items()
# * Returns a list containing a tuple with each key value pair
x = {'name': 'John', 'age': 50}
y = x.items()
print(y)
# dict_items([('name', 'John'), ('age', 50)])


# keys()
# * Returns a list containing all the keys in the dictionary
x = {'name': 'John', 'age': 50}
y = x.keys()
print(y)
# dict_keys(['name', 'age'])


# values()
# * Returns a list containing all the values in the dictionary
x = {'name': 'John', 'age': 50}
y = x.values()
print(y)
# dict_values(['John', 50])


# clear()
# * Removes all the elements (key value pairs) from the dictionary
x = {'name': 'John', 'age': 50}
x.clear()
print(x)
# {}


# copy()
# * Returns a copy of the dictionary
x = {'name': 'John', 'age': 50}
y = x.copy()
print(y)
# {'name': 'John', 'age': 50}


# fromkeys(__iterable, __value = None)
# * Creates a new dictionary with the specified keys
# * If value is specified, all the keys will have the informed value
x = {}
y1 = x.fromkeys(('name', 'age'))
y2 = x.fromkeys(('x', 'y'), 10)
print(x, y1, y2, sep='\n')
# {}
# {'name': None, 'age': None}
# {'x': 10, 'y': 10}


# get(__key, __default = None)
# * Returns the value of the specified key
# * Default is None when not set
# * This method will not raise an error if the key does not exists, different
#   from the index access
x = {'name': 'John', 'age': 50}
y1 = x.get('name')
y2 = x.get('gender')
y3 = x.get('gender', 'Male')
print(y1, y2, y3, sep='\n')
# John
# None
# Male


# pop(__key)
# * Removes the element with the specified key and returns the value
x = {'name': 'John', 'age': 50}
y = x.pop('name')
print(x, y)
# {'age': 50} John


# popitem()
# * Removes the last inserted key-value pair
x = {'name': 'John', 'age': 50}
y = x.popitem()
print(x, y)
# {'name': 'John'} ('age', 50)


# setdefault(__key, __default = None)
# * Returns the value of the specified key. If the key does not exist it will
#   be inserted with the specified value, and the new value will be returned
x = {'name': 'John', 'age': 50}
y1 = x.setdefault('name', 'Mary')
y2 = x.setdefault('gender', 'Male')
y3 = x.setdefault('age')
y4 = x.setdefault('surname')
print(x, y1, y2, y3, y4, sep='\n')
# {'name': 'John', 'age': 50, 'gender': 'Male', 'surname': None}
# John
# Male
# 50
# None


# update(__m)
# * Updates the dictionary with the specified key-value pairs
# * If the key already exists, the value will be updated
# * If the key does not exists, it will be created
x1 = {'name': 'John', 'age': 50}
x2 = {'name': 'Mary', 'gender': 'Female'}
x1.update(x2)
print(x1)
# {'name': 'Mary', 'age': 50, 'gender': 'Female'}


###############################################################################
# Dictionary Iteration
###############################################################################


# Iterating over the dictionary items (with for-each) (XXX recommended XXX)
# * The for-each loop can be used to iterate over the dictionary items
# * Dictionary items is a list of tuples, where each tuple contains a key-value
#   pair
# * To iterate over the dictionary items, the `items()` method must be used
x = {'name': 'John', 'age': 50}
for key, value in x.items():
    print(key, value, sep=': ')
# name: John
# age: 50


# Iterating over the dictionary keys (with for-each)
# * To iterate only over the dictionary keys, the `keys()` method must be used
x = {'name': 'John', 'age': 50}
for key in x.keys():
    print(key)
# name
# age


# Iterating over the dictionary values (with for-each)
# * To iterate only over the dictionary values, the `values()` method must be
x = {'name': 'John', 'age': 50}
for value in x.values():
    print(value)
# John
# 50


# Iterating over the dictionary items (with comprehension)
# * The comprehension can be used to iterate over the dictionary items
# * In this case, the comprehension result will not be stored into a variable,
#   since we will not need the result
# * To iterate over the dictionary items, the `items()` method must be used
x = {'name': 'John', 'age': 50}
[print(key, value, sep=': ') for key, value in x.items()]
# name: John
# age: 50


# Iterating over the dictionary keys (with comprehension)
# * The comprehension can be used to iterate over the dictionary keys
# * To iterate over the dictionary keys, the `keys()` method must be used
x = {'name': 'John', 'age': 50}
[print(key) for key in x.keys()]
# name
# age


# Iterating over the dictionary values (with comprehension)
# * The comprehension can be used to iterate over the dictionary values
# * To iterate over the dictionary values, the `values()` method must be used
x = {'name': 'John', 'age': 50}
[print(value) for value in x.values()]
# John
# 50


# Iterating over the dictionary items (with while)
# * The while loop can be used to iterate over the dictionary items
# * To iterate over the dictionary items, the `items()` method must be used
# * Note that we must cast the items to a tuple, since the dict_items object
#   does not support indexing
# * NOTE: Its is not recommended to use the while loop to iterate over a
#   dictionary since it is more verbose than the for-each loop
x = {'name': 'John', 'age': 50}
items = tuple(x.items())
i = 0
while i < len(items):
    key, value = items[i]
    print(key, value, sep=': ')
    i += 1
# name: John
# age: 50


# Iterating over the dictionary keys (with while)
# * The while loop can be used to iterate over the dictionary keys
# * To iterate over the dictionary keys, the `keys()` method must be used
# * Note that we must cast the items to a tuple, since the dict_items object
#   does not support indexing
# * NOTE: Its is not recommended to use the while loop to iterate over a
#   dictionary since it is more verbose than the for-each loop
x = {'name': 'John', 'age': 50}
keys = tuple(x.keys())
i = 0
while i < len(keys):
    print(keys[i])
    i += 1
# name
# age


# Iterating over the dictionary values (with while)
# * The while loop can be used to iterate over the dictionary values
# * To iterate over the dictionary keys, the `values()` method must be used
# * Note that we must cast the items to a tuple, since the dict_items object
#   does not support indexing
# * NOTE: Its is not recommended to use the while loop to iterate over a
#   dictionary since it is more verbose than the for-each loop
x = {'name': 'John', 'age': 50}
values = tuple(x.values())
i = 0
while i < len(values):
    print(values[i])
    i += 1
# John
# 50


###############################################################################
# Dictionary Mapping
###############################################################################


# Mapping a Dictionary (with comprehension) (XXX recommended XXX)
# * A mapping process is a process that will transform each element of a
#   collection into another element
# * The comprehension can be used to map a dictionary
# * In this example, we will use the result of the comprehension, so the
#   result will be stored in memory
x = {'n1': 1, 'n2': 2, 'n3': 3}
y = {key: value * 2 for key, value in x.items()}
print(y)
# {'n1': 2, 'n2': 4, 'n3': 6}


# Mapping a Dictionary (with for-each)
# * The for-each loop can be used to map a dictionary
# * Note that we created a new dictionary that will be the result of the
#   mapping process
x = {'n1': 1, 'n2': 2, 'n3': 3}
y = {}
for key, value in x.items():
    y[key] = value * 2
print(y)
# {'n1': 2, 'n2': 4, 'n3': 6}


# Mapping a Dictionary (with map)
# * The `map` function can be used to iterate over a dictionary transforming
#   each element into another element in a new dictionary
# * The `map` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the result to a dictionary, since the
#   result of a map operation is a map object
x = {'n1': 1, 'n2': 2, 'n3': 3}
y = dict(map(lambda item: (item[0], item[1] * 2), x.items()))
print(y)
# {'n1': 2, 'n2': 4, 'n3': 6}


# Mapping a Dictionary (with while)
# * The while loop can be used to map a dictionary too
# * The other ways above are better than this one, since this one is more
#   verbose
x = {'n1': 1, 'n2': 2, 'n3': 3}
y = {}
items = tuple(x.items())
i = 0
while i < len(items):
    key, value = items[i]
    y[key] = value * 2
    i += 1
print(y)
# {'n1': 2, 'n2': 4, 'n3': 6}


###############################################################################
# Dictionary Filtering
###############################################################################


# Filtering a Dictionary (with comprehension) (XXX recommended XXX)
# * The comprehension can be used to filter a dictionary using a condition
#   that will be applied for each element
# * In this example, we will use the result of the comprehension, so the
#   result will be stored in memory
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
y = {key: value for key, value in x.items() if value > 2}
print(y)
# {'n3': 3, 'n4': 4}


# Filtering a Dictionary (with for-each)
# * The for-each loop can be used to filter a dictionary using a condition
#   that will be applied for each element
# * Note that we created a new dictionary that will be the result of the
#   filtering process
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
y = {}
for key, value in x.items():
    if value > 2:
        y[key] = value
print(y)
# {'n3': 3, 'n4': 4}


# Filtering a Dictionary (with filter)
# * The `filter` function can be used to iterate over a dictionary filtering
#   each element based on a condition
# * The `filter` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the result to a dictionary, since the
#   result of a filter operation is a filter object
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
y = dict(filter(lambda item: item[1] > 2, x.items()))
print(y)
# {'n3': 3, 'n4': 4}


# Filtering a Dictionary (with while)
# * While can be used to filter a dictionary too
# * The other ways above are better than this one, since this one is more
#   verbose
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
y = {}
items = tuple(x.items())
i = 0
while i < len(items):
    key, value = items[i]
    if value > 2:
        y[key] = value
    i += 1
print(y)
# {'n3': 3, 'n4': 4}


###############################################################################
# Dictionary Reducing
###############################################################################


# Reducing a Dictionary (with for-each)
# * The reducing process is a process that will reduce the elements of a
#   collection into a single value
# * The reducing process can be done by using the for-each notation
# * Note that we can use the built-in functions `sum()`, `min()` and `max()`
#   for the most common reducing operations
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
acc = 0
for key, value in x.items():
    acc += value
print(acc)
# 10


# Reducing a Dictionary (with reduce)
# * The `functools.reduce` function can be used to reduce a dictionary
# * For this case, we must import the `reduce` function from the `functools`
#   module
# * The `reduce` function accepts a function as first argument that will be
#   applied for each element. The function has two arguments, the first is
#   the accumulator and the second is the current element
from functools import reduce
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
acc = reduce(lambda acc, item: acc + item[1], x.items(), 0)
print(acc)
# 10


# Reducing a Dictionary (with while)
# * The while loop can be used to reduce a dictionary
# * In this case, the index variable will be used to iterate over the
#   dictionary
# * The other ways above are better than this one, since this one is more
#   verbose
x = {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
acc = 0
items = tuple(x.items())
i = 0
while i < len(items):
    key, value = items[i]
    acc += value
    i += 1
print(acc)
# 10


###############################################################################
# Dictionary Sorting
###############################################################################


# Sorting a Dictionary (with sorted)
# * The `sorted` function can be used to sort a dictionary
# * For this case, we must pass the `items()` method as argument to the
#   `sorted` function
# * We needed to pass a lambda function as argument to the `key` parameter
#   to define that the sorting will be done by the second element of the
#   tuple, i.e. the value, not the key
# * Note that the result of the `sorted` function is a list of tuples, where
#   we needed to convert to a dictionary again
x = {'n3': 3, 'n1': 1, 'n4': 4, 'n2': 2}
y1 = dict(sorted(x.items(), key=lambda el: el[1]))
y2 = dict(sorted(x.items(), key=lambda el: el[1], reverse=True))
print(y1, y2, sep='\n')
# {'n1': 1, 'n2': 2, 'n3': 3, 'n4': 4}
# {'n4': 4, 'n3': 3, 'n2': 2, 'n1': 1}
