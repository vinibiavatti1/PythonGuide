"""
Sorted

* The `sorted()` builtin function is used to sort iterables
* Different then the `sort()` method from the list class, the `sorted()`
  function will return a new list with the sorted values, instead of sorting
  the list itself
* Consider using the `list.sort()` method when a big list is being sorted, to
  avoid using unnecessary memory
* The `sorted()` has three parameters:
  * iterable: The iterable to be sorted
  * key: A function to identify the key to be used to sort the iterable
  * reverse: If the iterable should be sorted in reverse order
* Syntax: sorted(iterable, key = None, reverse = False)
"""


###############################################################################
# Sorted Operations
###############################################################################


# Sorting a collection
# * The `sorted()` function will return a new list with the sorted values
x = [3, 1, 3, 2]
y = sorted(x)
print(y)
# [1, 2, 3, 3]


# Sorting a collection (in reverse order)
# * The `reverse` parameter can be used to sort the collection in reverse order
x = [3, 1, 3, 2]
y = sorted(x, reverse=True)
print(y)
# [3, 3, 2, 1]


# Sorting a collection (using a common key selector)
# * The `key` parameter can be used to set a function that will select the
#   correct key that will be used to sort the collection
# * In the example below, we are sorting a list of strings by the length of
#   each string
x = ['xxxx', 'xxxxxxx', 'xx']
y = sorted(x, key=len)
print(y)
# ['xx', 'xxxx', 'xxxxxxx']


# Sorting a collection (using a custom key selector)
# * Different from the previous example, we can use a custom function to select
#   the key that will be used to sort the collection
# * In this example, we will use a lambda function to select the second value
#   in the tuples to sort the list
x = [(2, 5), (3, 4), (1, 6)]
y = sorted(x, key=lambda v: v[1])
print(y)
# [(3, 4), (2, 5), (1, 6)]


###############################################################################
# Sorted vs list.sort
###############################################################################


# Sorting a list (with sorted())
# * When using the `sorted()` function, a new list will be created with the
#   sorted values
# * This is different from the `list.sort()` method, that will sort the list
#   itself
x = [3, 1, 3, 2]
y = sorted(x)
print(x, y)
# [3, 1, 3, 2] [1, 2, 3, 3]


# Sorting a list (with list.sort())
# * When using the `list.sort()` method, the list itself will be sorted
#   instead of creating a new list
# * This is better when sorting a big list, because it will not use unnecessary
#   memory to store both lists
# * NOTE: Check the "List.py" file for more details about the `list.sort()`
x = [3, 1, 3, 2]
x.sort()
print(x)
# [1, 2, 3, 3]


###############################################################################
# Custom Comparisons (functools.cmp_to_key)
###############################################################################


# Creating a custom comparison function
# * The `sorted()` function can be used with a custom comparison function
# * The comparison function must receive two values and return:
#   * -1: If the first value is less than the second
#   * 0: If the first value is equal to the second
#   * 1: If the first value is greater than the second
# * In the example below, we are defining a custom comparison function to sort
#   a list of strings by the length of each string
def compare(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    return 0


# Sorting a list (with custom comparison)
# * To use a custom comparison, we must use the `functools.cmp_to_key()`
#   function to convert the comparison function to a key function
# * The `cmp_to_key()` function will receive the comparison function and return
#   a key function that can be used to sort the list
from functools import cmp_to_key
x = ['xxxx', 'xxxxxxx', 'xx']
y = sorted(x, key=cmp_to_key(compare))
print(y)
# ['xx', 'xxxx', 'xxxxxxx']
