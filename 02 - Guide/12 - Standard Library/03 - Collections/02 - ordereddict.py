"""
Ordered Dict

* The OrderedDict is a dict subclass that remembers the order in which the
  elements were inserted.
* Even if a dict is already ordered in Python, the OrderedDict provides some
  functions that consider the ordering.
* Syntax
  * OrderedDict(dict)
"""


###############################################################################
# Importing Resource
###############################################################################


# Importing the resource
# * We can import the resource using the import statement below
from collections import OrderedDict


###############################################################################
# Creating Ordered Dicts
###############################################################################


# Creating an empty Ordered Dict
# * We can create an ordered dict using the OrderedDict class
x = OrderedDict()
print(x)
# OrderedDict()


# Creating an Ordered Dict (with dict)
# * We can create an ordered dict using a dict as a parameter
# * The order of the elements is the same as the order in the dict
x = {'name': 'John', 'age': 50}
y = OrderedDict(x)
print(y)
# OrderedDict([('name', 'John'), ('age', 50)])


###############################################################################
# Comparing Ordered Dicts
###############################################################################


# Comparing a standard dict
# * The comparison between standard dicts don't consider the order of the
#   the elements
x = {'name': 'John', 'age': 50}
y = {'age': 50, 'name': 'John'}
print(x == y)
# True


# Comparing an Ordered Dict
# * However, the comparison between ordered dicts consider the order of the
#   the elements
x = OrderedDict({'name': 'John', 'age': 50})
y = OrderedDict({'age': 50, 'name': 'John'})
print(x == y)
# False


###############################################################################
# Ordered Dict Functions
###############################################################################


# Move to End
# * The `move_to_end` function moves an element to the end of the ordered dict
x = OrderedDict({'name': 'John', 'age': 50})
x.move_to_end('name')
print(x)
# OrderedDict([('age', 50), ('name', 'John')])


# Pop Item (Last)
# * The `popitem` function removes the last element of the ordered dict and
#   returns it as a tuple
x = OrderedDict({'name': 'John', 'age': 50})
y = x.popitem()
print(x, y)
# OrderedDict([('name', 'John')]) ('age', 50)


# Pop Item (first)
# * The `popitem` has a parameter `last` that can be set to False to remove the
#   first element of the ordered dict instead of the first
# * As default, the `last` parameter is set to True
x = OrderedDict({'name': 'John', 'age': 50})
y = x.popitem(last=False)
print(x, y)
# OrderedDict([('age', 50)]) ('name', 'John')
