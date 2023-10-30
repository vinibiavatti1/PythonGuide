"""
List

* Lists are used to store multiple items in a single variable. Differently from
  tuples, lists are mutable and can be changed after creation
* Usually, lists stores a unique data type. Different from tuples, the type
  of the elements in a list is defined for the entire list, instead for each
  index position
* To create a list, the brackets notation is used "[]"
* Lists are the most dynamic collection in Python, and the most used due to
  the flexibility

Properties:
(X) Ordered
(X) Mutable
(X) Allow Duplicate
(X) Indexed
"""


###############################################################################
# List Operations
###############################################################################


# Creating a List
# * A list can be created using brackets "[]"
# * Different from tuples, the brackets are mandatory
# * When a list will be defined with a single element, the comma is not
#   required as it is for tuples
x = [1, 2, 3]  # Brackets
x = [1]        # Brackets with one element
x = []         # Empty
x = list()     # With list() function


# Type hint for a List
# * To set a type hint for a list, only one type will be set to define the type
#   of all elements in the list
x: list[int] = [1, 2, 3, 4, 5]


# Casting to List
# * The `list()` function can be used to cast a collection into a list
x = list((1, 2, 3))
print(x)
# [1, 2, 3]


# Cloning a List
# * A list can be cloned by using the `list()` function with the list to be
#   cloned as argument
x = [1, 2, 3]
y = list(x)
print(y)
# [1, 2, 3]


# Joining Lists (concatenating)
# * The `+` operator can be used to join two lists into a new list
x1 = [1, 2, 3]
x2 = [4, 5, 6]
y = x1 + x2
print(y)
# [1, 2, 3, 4, 5, 6]


# Multiplying Lists
# * The `*` operator can be used to multiply a list
# * It will create a new list with the same elements repeated
x = [1, 2, 3]
y = x * 2
print(y)
# [1, 2, 3, 1, 2, 3]


# Comparing Lists
# * The comparison operators can be used to compare lists
# * The comparison will be made by comparing the elements in the same index
#   position
print([1, 5] == [1, 7])  # False
print([1, 5] != [1, 7])  # True
print([1, 5] > [1, 7])   # False
print([1, 5] >= [1, 7])  # False
print([1, 5] < [1, 7])   # True
print([1, 5] <= [1, 7])  # True


# Assignation by reference
# * When assigning a list to another variable, the list will be passed by
#   reference, so that any change in the new variable will affect the original
# * To avoid this, the list must be cloned
# * In the example below, note that the "y" variable was changed, and it
#   affected the "x" variable as well
x = [1, 2, 3]
y = x
y[1] = 5
print(x)
# [1, 5, 3]


###############################################################################
# List Elements
###############################################################################


# Getting elements by index
# * Lists are indexed, so the elements can be accessed by their index position
# * If the index is negative, it will be counted from the end of the list
# * If the index does not exist, an IndexError will be raised
x = [1, 2, 3]
y1 = x[1]
y2 = x[-1]
print(y, y2, sep=', ')
# 2, 3


# Getting elements by slice
# * We can obtain a range of values by using the slice notation
# * Below there is a table that represents the index positions of a list with
#   5 elements
# * When using a negative step, the elements will be returned in reverse order
# * Slice syntax: [start:stop:step]
"""
|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04|
|  1|  2|  3|  4|  5|
"""
x = [1, 2, 3, 4, 5]
print(x[:])      # [1, 2, 3, 4, 5]
print(x[1:])     # [2, 3, 4, 5]
print(x[:4])     # [1, 2, 3, 4]
print(x[2:4])    # [3, 4]
print(x[::2])    # [1, 3, 5]
print(x[2:5:2])  # [3, 5]
print(x[::-1])   # [5, 4, 3, 2, 1]
print(x[-5:-1])  # [1, 2, 3, 4]


# Setting a value by index
# * Since lists are mutable and indexed, the elements can be changed after
#   creation by setting a value by index
x = [1, 2, 3]
x[1] = 5
x[-1] = 6
print(x)
# [1, 5, 6]


# Setting values by slice
# * The slice notation can be used to set values in a list
# * The slice will be replaced by the new values
# * Note in the example that the slice length is 2, but the values to update
#   have length 3. The slice will be replaced by the new values, and the
#   remaining values will be inserted after the slice
x = [1, 2, 3, 4, 5]
x[1:3] = [5, 6, 7]
print(x)
# [1, 5, 6, 7, 4, 5]


# Removing elements with del
# * The `del` keyword can be used to remove an element from a list by its index
#   position
x = [1, 2, 3]
del x[1]
print(x)
# [1, 3]


# Removing slice with del
# * The `del` keyword can be used to remove a slice from a list
x = [1, 2, 3, 4, 5]
del x[1:3]
print(x)
# [1, 4, 5]


# Checking if an item exists in a List
# * The `in` operator can be used to check if an item exists in a list
x = [1, 2, 3]
y = 2 in x
print(y)
# True


###############################################################################
# List Properties
###############################################################################


# (X) Ordered
# * Lists are ordered, so the elements will be in the same order as they were
#   inserted
x = [1, 2, 3]
print(x[1])
# 2


# (X) Mutable
# * Lists are mutable and can be changed after creation
x = [1, 2, 3]
x[1] = 5
print(x)
# [1, 5, 3]


# (X) Allows Duplicate
# * Lists allow duplicate elements
x = [1, 1, 1]
print(x[1])
# 1


# (X) Indexed
# * Lists are indexed, so the elements can be accessed by their index position
x = [1, 2, 3]
print(x[1])
# 2


###############################################################################
# List Built-in Functions
###############################################################################


# List Built-in Functions
# * The Python built-in functions for collections can be used with lists
x = [1, 2, 3, 4]
print(sum(x))  # 10    (The sum of elements)
print(min(x))  # 1     (The min value)
print(max(x))  # 4     (The max value)
print(len(x))  # 4     (The length)
print(all(x))  # True  (All values are True)
print(any(x))  # True  (Any value is True)


###############################################################################
# List Methods
###############################################################################


# append(__object)
# * Adds an element at the end of the list
x = [1, 2, 3]
x.append(4)
print(x)
# [1, 2, 3, 4]


# insert(__index, __object)
# * Adds an element at the specified index position
# * It will offset the elements after the insertion, without remove any element
x = [2, 3, 4]
x.insert(0, 1)
print(x)
# [1, 2, 3, 4]


# extend(__iterable)
# * Add the elements of a list (or any iterable), to the end of the current
#   list
x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y)
print(x)
# [1, 2, 3, 4, 5, 6]


# remove(__value)
# * Remove first occurrence of value
x = [1, 2, 3]
x.remove(2)
print(x)
# [1, 3]


# pop(__index = -1)
# * Removes the element at the specified position and returns it
# * If the index is not set, the last element will be removed
x = [1, 2, 3, 4, 5]
el1 = x.pop()
el2 = x.pop(0)
print(x, el1, el2, sep='\n')
# [2, 3, 4]
# 5
# 1


# clear()
# * Removes all the elements from the list
x = [1, 2, 3]
x.clear()
print(x)
# []


# copy()
# * Returns a copy of the list
x = [1, 2, 3]
y = x.copy()
print(y)
# [1, 2, 3]


# count(__value)
# * Return number of occurrences of value in the list
x = [1, 2, 3, 2, 1]
y = x.count(1)
print(y)
# 2


# index(__value, __start = 0, __stop = max)
# * Returns the index of the first element with the specified value
# * Raises ValueError if the value is not present
x = [1, 2, 3, 2, 1]
i1 = x.index(2)
i2 = x.index(2, 2)
print(i1, i2, sep=', ')
# 1, 3


# reverse()
# * Reverses the order of the list
x = [1, 2, 3]
x.reverse()
print(x)
# [3, 2, 1]


# sort(key = None, reverse = False)
# * Sorts the list
# * The key parameter can be used to process the element before sorting is
#   being evaluated
# * The reverse parameter can be used to sort the list in reverse order
# * For the "x3" and "x4" lists, we needed to specify the key to sort by the
#   correct value
# * NOTE: The difference between the `sort()` and `sorted()` functions is that
#   the `sort()` function will change the original list, while the `sorted()`
#   function will return a new list
x1 = [1, 3, 2, 4]
x2 = [1, 3, 2, 4]
x3 = ['ID-2', 'ID-1', 'ID-3']
x4 = [{'year': 2021}, {'year': 2012}, {'year': 2023}]
x1.sort()
x2.sort(reverse=True)
x3.sort(key=lambda el: int(el[3]))
x4.sort(key=lambda el: el['year'], reverse=True)
print(x1, x2, x3, x4, sep='\n')
# [1, 2, 3, 4]
# [4, 3, 2, 1]
# ['ID-1', 'ID-2', 'ID-3']
# [{'year': 2023}, {'year': 2021}, {'year': 2012}]


###############################################################################
# List Iteration
###############################################################################


# Iterating over a List (with for-each) (XXX recommended XXX)
# * The for-each notation can be used to iterate over a list without the need
#   of a preset index variable
# * This syntax is more clean then the `while` loop
x = [1, 2, 3]
for el in x:
    print(el, end=', ')
print()
# 1, 2, 3,


# Iterating over a List (with for-each and enumerate)
# * If the index is needed, the `enumerate()` function can be used to get the
#   index of each element in for-each loop
# * The enumerate function returns a tuple with the index and the element
#   value
x = ['a', 'b', 'c']
for i, el in enumerate(x):
    print(i, el, sep=': ', end=', ')
print()
# 0: a, 1: b, 2: c,


# Iterating over a List (with while)
# * The `while` loop can be used to iterate over a list
# * In this case, we must set a index variable
# * The `len()` method can be used to get the length of the list
x = [1, 2, 3]
i = 0
while i < len(x):
    print(x[i], end=', ')
    i += 1
print()
# 1, 2, 3,


# Iterating over a List (with comprehension)
# * The comprehension syntax can be used to iterate over a list
# * In this example, we will not use the result of the comprehension, so the
#   result will not be stored in memory
x = [1, 2, 3]
[print(el) for el in x]
# 1
# 2
# 3


# Iterating over a List (with iter)
# * The `iter` function can be used to iterate over a list
# * In this case, we must use the `next` function to get the next element
#   returned by the iterator
x = [1, 2, 3]
y = iter(x)
print(next(y))  # 1
print(next(y))  # 2
print(next(y))  # 3


# Iterating over multiple Lists (with zip)
# * The `zip` function can be used to iterate over multiple lists
# * The `zip` function returns a tuple with the elements of each collections in
#   the same index position
# * The `strict` argument can be used to indicate that an exception must be
#   raised if the collections have different lengths
x1 = [1, 2, 3]
x2 = ['a', 'b', 'c', 'd']
for el1, el2 in zip(x1, x2):
    print(el1, el2, sep=', ')
# 1, a
# 2, b
# 3, c


###############################################################################
# List Mapping
###############################################################################


# Mapping a List (with comprehension) (XXX recommended XXX)
# * A mapping process is a process that will transform each element of a
#   collection into another element
# * The comprehension syntax can be used to iterate over a list
# * In this example, we will use the result of the comprehension, so the
#   result will be stored in memory
x = [1, 2, 3]
y = [el * 2 for el in x]
print(y)
# 2, 4, 6


# Mapping a List (with for-each)
# * The for-each notation can be used to iterate over a list without the need
#   of a preset index variable
# * In this case, we will create a new list using the for-each notation
x = [1, 2, 3]
y = []
for el in x:
    y.append(el * 2)
print(y)
# 2, 4, 6


# Mapping a List (with map)
# * The `map` function can be used to iterate over a list transforming each
#   element into another element in a new list
# * The `map` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the result to a list, since the result of a
#   map operation is a map object
x = [1, 2, 3]
y = list(map(lambda el: el * 2, x))
print(y)
# 2, 4, 6


# Mapping a List (with while)
# * In this case, we will create a new list based on the original list
#   using the `while` loop
# * Since lists are immutable, we will need to create a new list and add
#   each element to it. Note that a new list is created on each iteration
#   and is concatenated with the previous list
x = [1, 2, 3]
y = []
i = 0
while i < len(x):
    y.append(x[i] * 2)
    i += 1
print(y)
# 2, 4, 6


###############################################################################
# List Filtering
###############################################################################


# Filtering a List (with comprehension) (XXX recommended XXX)
# * The filtering process is a process that will filter the elements of a
#   collection based on a condition
# * A condition can be applied to the comprehension to filter the elements
#   that will be returned
x = [1, 2, 3, 4]
y = [el for el in x if el > 2]
print(y)
# 3, 4


# Filtering a List (with for-each)
# * The for-each notation can be used to iterate over a list without the need
#   of a preset index variable
x = [1, 2, 3, 4]
y = []
for el in x:
    if el > 2:
        y.append(el)
print(y)
# 3, 4


# Filtering a List (with filter)
# * The `filter` function can be used to iterate over a list filtering each
#   element based on a condition
# * The `filter` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the comprehension to a list, since the
#   result of a filter operation is a filter object
x = [1, 2, 3, 4]
y = list(filter(lambda el: el > 2, x))
print(y)
# 3, 4


# Filtering a List (with while)
# * A new list with the elements filtered will be created
# * In this case, we will use the `while` loop to iterate over the list
x = [1, 2, 3, 4]
y = []
i = 0
while i < len(x):
    if x[i] > 2:
        y.append(x[i])
    i += 1
print(y)
# 3, 4


###############################################################################
# List Reducing
###############################################################################


# Reducing a List (with for-each) (XXX recommended XXX)
# * The reducing process is a process that will reduce the elements of a
#   collection into a single value
# * The reducing process can be done by using the for-each notation
# * Note that we can use the built-in functions `sum()`, `min()` and `max()`
#   for the most common reducing operations
x = [1, 2, 3, 4]
acc = 0
for el in x:
    acc += el
print(acc)
# 10


# Reducing a List (with reduce)
# * The `functools.reduce` function can be used to reduce a list
# * For this case, we must import the `reduce` function from the `functools`
#   module
# * The `reduce` function accepts a function as first argument that will be
#   applied for each element. The function has two arguments, the first is
#   the accumulator and the second is the current element
from functools import reduce
x = [1, 2, 3, 4]
result = reduce(lambda acc, el: acc + el, x)
print(result)
# 10


# Reducing a List (with while)
# * The while loop can be used to reduce a list
# * In this case, the index variable will be used to iterate over the list
x = [1, 2, 3, 4]
acc = 0
i = 0
while i < len(x):
    acc += x[i]
    i += 1
print(acc)
# 10


###############################################################################
# List Sorting
###############################################################################


# Sorting a List (with sorted)
# * The `sorted` function can be used to sort a list
x = [3, 1, 4, 2]
y1 = sorted(x)
y2 = sorted(x, reverse=True)
print(y1, y2, sep='\n')
# [1, 2, 3, 4]
# [4, 3, 2, 1]


# Sorting a List (with sort)
# * The `sort` method can be used to sort a tuple
# * The difference between the `sort` and `sorted` functions is that the
#   `sort` method will change the original tuple, while the `sorted` function
#   will return a new tuple
"""
Take a look at sort() method for more details...
"""
