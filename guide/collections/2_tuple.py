"""
Tuple

* Tuples are used to store multiple items in a single variable. Differently
  from lists, tuples are immutable
* Usually, tuples contain multiple data types, since each tuple position can
  be assigned to a different data type. Lists in the other hand, are defined
  to store a single data type
* A tuple can be defined without parentheses

Properties:
(X) Ordered
( ) Mutable
(X) Allow Duplicate
(X) Indexed
"""


###############################################################################
# Tuple Operations
###############################################################################


# Creating a Tuple
# * A tuple can be created using parentheses "()" or omitting them
# * NOTE: When a tuple has only one element, a comma must be added after the
#   element to indicate that it is a tuple and not a single value or a
#   generator if parentheses were used
x = (1, 2, 3)  # Parentheses
x = (1,)       # Parentheses with one element (requires comma)
x = 1, 2, 3    # Without parentheses
x = 1,         # Without parentheses with one element (requires comma)
x = ()         # Empty
x = tuple()    # With tuple() function


# Type hint for a Tuple
# * To set a type hint for a tuple, each index must has the type defined
x: tuple[int, str, bool] = 1, 'a', True


# Casting to Tuple
# * The `tuple()` function can be used to cast a collection into a tuple
x = tuple([1, 2, 3])
print(x)
# (1, 2, 3)


# Cloning a Tuple
# * A tuple can be cloned by using the `tuple()` function with the tuple to be
#   cloned as argument
x = 1, 2, 3
y = tuple(x)
print(y)
# (1, 2, 3)


# Joining Tuples (concatenating)
# * The `+` operator can be used to join two tuples into a new tuple
x1 = 1, 2, 3
x2 = 4, 5, 6
y = x1 + x2
print(y)
# (1, 2, 3, 4, 5, 6)


# Multiplying Tuples
# * The `*` operator can be used to multiply a tuple
# * It will create a new tuple with the same elements repeated
x = 1, 2, 3
y = x * 2
print(y)
# (1, 2, 3, 1, 2, 3)


# Comparing Tuples
# * The comparison operators can be used to compare tuples
# * The comparison will be made by comparing the elements in the same index
#   position
print((1, 5) == (1, 7))  # False
print((1, 5) != (1, 7))  # True
print((1, 5) > (1, 7))   # False
print((1, 5) >= (1, 7))  # False
print((1, 5) < (1, 7))   # True
print((1, 5) <= (1, 7))  # True


# Assignation by reference
# * When assigning a tuple to another variable, the tuple will be passed by
#   reference, it means that the variable will point to the same tuple in
#   memory
# * In the example below, note that the "y" variable has the same memory
#   address as the "x" variable
x = [1, 2, 3]
y = x
print(id(x) == id(y))
# True


###############################################################################
# Tuple Elements
###############################################################################


# Getting elements by index
# * Tuples are indexed, so the elements can be accessed by their index position
# * If the index is negative, it will be counted from the end of the tuple
# * If the index does not exist, an IndexError will be raised
x = 1, 2, 3
y1 = x[1]
y2 = x[-1]
print(y, y2, sep=', ')
# 2, 3


# Getting elements by slice
# * We can obtain a range of values by using the slice notation
# * Below there is a table that represents the index positions of a tuple with
#   5 elements
# * When using a negative step, the elements will be returned in reverse order
# * Slice syntax: [start:stop:step]
"""
|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04|
|  1|  2|  3|  4|  5|
"""
x = 1, 2, 3, 4, 5
print(x[:])      # (1, 2, 3, 4, 5)
print(x[1:])     # (2, 3, 4, 5)
print(x[:4])     # (1, 2, 3, 4)
print(x[2:4])    # (3, 4)
print(x[::2])    # (1, 3, 5)
print(x[2:5:2])  # (3, 5)
print(x[::-1])   # (5, 4, 3, 2, 1)
print(x[-5:-1])  # (1, 2, 3, 4)


# Checking if an item exists in a Tuple
# * The `in` operator can be used to check if an item exists in a tuple
x = 1, 2, 3
y = 2 in x
print(y)
# True


###############################################################################
# Tuple Properties
###############################################################################


# (X) Ordered
# * Tuples are ordered, so the elements will be in the same order as they were
#   inserted
x = 1, 2, 3
print(x[1])
# 2


# ( ) Mutable
# * Tuples are immutable, so they cannot be changed after creation
# * To change a tuple, it must be cast to a list first
"""
x = 1, 2, 3
x[1] = 5

TypeError: 'tuple' object does not support item assignment
"""


# (X) Allows Duplicate
# * Tuples allow duplicate elements
x = 1, 1, 1
print(x[1])
# 1


# (X) Indexed
# * Tuples are indexed, so the elements can be accessed by their index position
x = 1, 2, 3
print(x[1])
# 2


###############################################################################
# Tuple Built-in Functions
###############################################################################


# Tuple Built-in Functions
# * The Python built-in functions for collections can be used with tuples
x = (1, 2, 3, 4)
print(sum(x))  # 10    (The sum of elements)
print(min(x))  # 1     (The min value)
print(max(x))  # 4     (The max value)
print(len(x))  # 4     (The length)
print(all(x))  # True  (All values are True)
print(any(x))  # True  (Any value is True)


###############################################################################
# Tuple Methods
###############################################################################


# count(__value)
# * Return number of occurrences of value
x = 1, 2, 3, 2, 1
y = x.count(1)
print(y)
# 2


# index(__value, __start = 0, __stop = max)
# * Returns the index of the first element with the specified value
# * Raises ValueError if the value is not present
x = 1, 2, 3, 2, 1
i1 = x.index(2)
i2 = x.index(2, 2)
print(i1, i2, sep=', ')
# 1, 3


###############################################################################
# Tuple Iteration
###############################################################################


# Iterating over a Tuple (with for-each) (XXX recommended XXX)
# * The for-each notation can be used to iterate over a tuple without the need
#   of a preset index variable
# * This syntax is more clean then the `while` loop
x = 1, 2, 3
for el in x:
    print(el, end=', ')
print()
# 1, 2, 3,


# Iterating over a Tuple (with for-each and enumerate)
# * If the index is still needed, the `enumerate()` function can be used to
#   get the index of each element in for-each loop
x = 'a', 'b', 'c'
for i, el in enumerate(x):
    print(i, el, sep=': ', end=', ')
print()
# 0: a, 1: b, 2: c,


# Iterating over a Tuple (with while)
# * The `while` loop can be used to iterate over a tuple
# * In this case, we must set a index variable
# * The `len()` method can be used to get the length of the tuple
x = 1, 2, 3
i = 0
while i < len(x):
    print(x[i], end=', ')
    i += 1
print()
# 1, 2, 3,


# Iterating over a Tuple (with comprehension)
# * The comprehension syntax can be used to iterate over a tuple
# * In this example, we will not use the result of the comprehension, so the
#   result will not be stored in memory
# * Note that we needed to convert the comprehension to a tuple, since the
#   result of a "tuple comprehension" is a generator
x = 1, 2, 3
tuple(print(el, end=', ') for el in x)
print()
# 1, 2, 3,


# Iterating over a Tuple (with iter)
# * The `iter` function can be used to iterate over a tuple
# * In this case, we must use the `next` function to get the next element
#   returned by the iterator
x = 1, 2, 3
y = iter(x)
print(next(y))  # 1
print(next(y))  # 2
print(next(y))  # 3


###############################################################################
# Tuple Mapping
###############################################################################


# Mapping a Tuple (with comprehension) (XXX recommended XXX)
# * A mapping process is a process that will transform each element of a
#   collection into another element
# * The comprehension syntax can be used to iterate over a tuple
# * In this example, we will use the result of the comprehension, so the
#   result will be stored in memory
# * Note that we needed to convert the comprehension to a tuple, since the
#   result of a "tuple comprehension" is a generator
x = 1, 2, 3
y = tuple(el * 2 for el in x)
print(y)
# 2, 4, 6


# Mapping a Tuple (with while)
# * In this case, we will create a new tuple based on the original tuple
#   using the `while` loop
# * Since tuples are immutable, we will need to create a new tuple and add
#   each element to it. Note that a new tuple is created on each iteration
#   and is concatenated with the previous tuple
x = 1, 2, 3
y = ()
i = 0
while i < len(x):
    y += (x[i] * 2,)
    i += 1
print(y)
# 2, 4, 6


# Mapping a Tuple (with for-each)
# * The for-each notation can be used to iterate over a tuple without the need
#   of a preset index variable
# * In this case, we will create a new tuple using the for-each notation
x = 1, 2, 3
y = ()
for el in x:
    y += (el * 2,)
print(y)
# 2, 4, 6


# Mapping a Tuple (with map)
# * The `map` function can be used to iterate over a tuple transforming each
#   element into another element in a new tuple
# * The `map` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the comprehension to a tuple, since the
#   result of a map operation is a map object
x = 1, 2, 3
y = tuple(map(lambda el: el * 2, x))
print(y)
# 2, 4, 6


###############################################################################
# Tuple Filtering
###############################################################################


# Filtering a Tuple (with comprehension) (XXX recommended XXX)
# * The filtering process is a process that will filter the elements of a
#   collection based on a condition
# * A condition can be applied to the comprehension to filter the elements
#   that will be returned
# * Note that we needed to convert the comprehension to a tuple, since the
#   result of a "tuple comprehension" is a generator
x = 1, 2, 3, 4
y = tuple(el for el in x if el > 2)
print(y)
# 3, 4


# Filtering a Tuple (with while)
# * A new tuple with the elements filtered will be created
# * In this case, we will use the `while` loop to iterate over the tuple
x = 1, 2, 3, 4
y = ()
i = 0
while i < len(x):
    if x[i] > 2:
        y += (x[i],)
    i += 1
print(y)
# 3, 4


# Filtering a Tuple (with for-each)
# * The for-each notation can be used to iterate over a tuple without the need
#   of a preset index variable
x = 1, 2, 3, 4
y = ()
for el in x:
    if el > 2:
        y += (el,)
print(y)
# 3, 4


# Filtering a Tuple (with filter)
# * The `filter` function can be used to iterate over a tuple filtering each
#   element based on a condition
# * The `filter` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the comprehension to a tuple, since the
#   result of a filter operation is a filter object
x = 1, 2, 3, 4
y = tuple(filter(lambda el: el > 2, x))
print(y)
# 3, 4


###############################################################################
# Tuple Reducing
###############################################################################


# Reducing a Tuple (with for-each) (XXX recommended XXX)
# * The reducing process is a process that will reduce the elements of a
#   collection into a single value
# * The reducing process can be done by using the for-each notation
# * Note that we can use the built-in functions `sum()`, `min()` and `max()`
#   for the most common reducing operations
x = 1, 2, 3, 4
acc = 0
for el in x:
    acc += el
print(acc)
# 10


# Reducing a Tuple (with while)
# * The while loop can be used to reduce a tuple
# * In this case, the index variable will be used to iterate over the tuple
x = 1, 2, 3, 4
acc = 0
i = 0
while i < len(x):
    acc += x[i]
    i += 1
print(acc)
# 10


# Reducing a Tuple (with reduce)
# * The `functools.reduce` function can be used to reduce a tuple
# * For this case, we must import the `reduce` function from the `functools`
#   module
# * The `reduce` function accepts a function as first argument that will be
#   applied for each element. The function has two arguments, the first is
#   the accumulator and the second is the current element
from functools import reduce
x = 1, 2, 3, 4
result = reduce(lambda acc, el: acc + el, x)
print(result)
# 10


###############################################################################
# Tuple Sorting
###############################################################################


# Sorting a Tuple (with sorted)
# * The `sorted` function can be used to sort a tuple
# * Since tuples are immutable, the unique way to sort a tuple is to create a
#   new tuple with the sorted elements
x = 3, 1, 4, 2
y1 = tuple(sorted(x))
y2 = tuple(sorted(x, reverse=True))
print(y1, y2, sep='\n')
# (1, 2, 3, 4)
# (4, 3, 2, 1)
