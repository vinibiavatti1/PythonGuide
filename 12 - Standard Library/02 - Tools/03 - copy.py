"""
Copy Module

* We can use the `copy` module of Python for shallow and deep copy operations
* In python, there are two different kinds of copy:
  * Shallow Copy (`copy()`)
    * A shallow copy creates a new object which stores the reference of the
      original elements. So, a shallow copy doesn't create a copy of nested
      objects, instead it just copies the reference of nested objects
    * Ex: If we have a list of lists, a shallow copy will create a new list
      object, but it will copy the references of the inner lists
  * Deep copy (`deepcopy()`)
    * A deep copy creates a new object and recursively adds the copies of
      nested objects present in the original elements
    * Ex: If we have a list of lists, a deep copy will create a new list object
      and it will create a new list object for each inner list
* The module methods call the Copy Protocol methods `__copy__` and
  `__deepcopy__` to create a copy of this object
"""


###############################################################################
# Copy
###############################################################################


# Importing the `copy` method
# * We will import the `copy` method from the `copy` module
from copy import copy


# Shallow Copy
# * A shallow copy creates a new object which stores the reference of the
#   original elements. So, a shallow copy doesn't create a copy of nested
#   objects, instead it just copies the reference of nested objects
x = [1, 2, 3]
y = copy(x)
y[0] = 9
print(x, y, sep=' / ')
# [1, 2, 3] / [9, 2, 3]


# Shallow Copy (with nested objects)
# * In this example, we have a list of lists
# * Note that after copying the list, the inner lists are not copied, only the
#   references are copied, so, the change will reflect in both lists
x = [[1, 2], [3, 4]]
y = copy(x)
y[0][0] = 9
print(x, y, sep=' / ')
# [[9, 2], [3, 4]] / [[9, 2], [3, 4]]


###############################################################################
# Deep Copy
###############################################################################


# Importing the `deepcopy` method
# * We will import the `deepcopy` method from the `copy` module
from copy import deepcopy


# Deep Copy
# * A deep copy creates a new object and recursively adds the copies of nested
#   objects present in the original elements
# * On this example, the result will be the same as the shallow copy, since
#   there are no nested objects
x = [1, 2, 3]
y = deepcopy(x)
y[0] = 9
print(x, y, sep=' / ')
# [1, 2, 3] / [9, 2, 3]


# Deep Copy (with nested objects)
# * In this example, we have a list of lists
# * Using the `deepcopy` method, the inner lists are also copied, so, the
#   change will only reflect in the copied list
x = [[1, 2], [3, 4]]
y = deepcopy(x)
y[0][0] = 9
print(x, y, sep=' / ')
# [[1, 2], [3, 4]] / [[9, 2], [3, 4]]


###############################################################################
# Copy Protocol
###############################################################################


# Implementing the Copy Protocol
# * We can implement the Copy Protocol in our classes by defining the
#   `__copy__` and `__deepcopy__` methods
# * The `__copy__` method is called to create a shallow copy of the object
# * The `__deepcopy__` method is called to create a deep copy of the object
# * The `memo` parameter is used to track the objects that have been copied
#   already, to avoid infinite recursion
class CustomList:

    def __init__(self, *data):
        self.data = data

    def __copy__(self):
        return CustomList(*self.data)

    def __deepcopy__(self, memo={}):
        data = deepcopy(self.data, memo)
        return CustomList(*data)


# Using the `copy` method
# * The `copy` method will call the `__copy__` method to create a shallow copy
#   of the object
x = CustomList(1, 2, 3)
y = copy(x)
y.data[0] = 9
print(x.data, y.data, sep=' / ')
# (1, 2, 3) / (9, 2, 3)


# Using the `deepcopy` method
# * The `deepcopy` method will call the `__deepcopy__` method to create a deep
#   copy of the object
# * In the example below, we created a list of lists, and the `deepcopy` method
#   will create a new list object for each inner list
x = CustomList([1, 2], [3, 4])
y = deepcopy(x)
y.data[0][0] = 9
print(x.data, y.data, sep=' / ')
# ([1, 2], [3, 4]) / ([9, 2], [3, 4])
