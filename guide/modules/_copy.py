"""
Copy module

* We use the copy module of Python for shallow and deep copy operations
* In python, there are two different kinds of copy
  * Shallow Copy
    * A shallow copy creates a new object which stores the reference of the
      original elements. So, a shallow copy doesn't create a copy of nested
      objects, instead it just copies the reference of nested objects
  * Deep copy
    * A deep copy creates a new object and recursively adds the copies of
      nested objects present in the original elements
* The module has two methods (copy and deepcopy)
* The module methods call the magic methods __copy__ and __deepcopy__ to create
  a copy of this object
* The deepcopy memo parameter is used by the deepcopy method, to pass params
  while processing the deepcopy recursivity
"""
import copy


# Shallow copy
lst = [1, 2, 3]
clone = copy.copy(lst)
clone[0] = 9
print(lst, clone, sep=', ')
# [1, 2, 3], [9, 2, 3]


# Deep copy
matrix = [[x for x in range(3)] for y in range(3)]
clone = copy.deepcopy(matrix)
clone[0][0] = 9
print(matrix, clone, sep=', ')
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[9, 1, 2], [0, 1, 2], [0, 1, 2]]


# Custom shallow copy
class List:
    def __init__(self, *args):
        self.list = args

    def __copy__(self):
        return List(*self.list)

    def __deepcopy__(self, memo={}):
        clone = copy.deepcopy(self.list)
        return List(*clone)


lst = List(1, 2, 3)
clone = copy.copy(lst)
print(lst.list, clone.list, sep=', ')
# (1, 2, 3), (1, 2, 3)
