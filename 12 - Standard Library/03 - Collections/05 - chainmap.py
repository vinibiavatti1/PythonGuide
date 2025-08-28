"""
Chain Map

* The ChainMap class is used to group multiple dictionaries into a single,
  unified view. This allows us to search through multiple dictionaries as if
  they were one.
* The ChainMap is available in the collections module
* Syntax
  * ChainMap(*maps)
"""


###############################################################################
# Importing Resource
###############################################################################


# Importing the resource
# * We can import the resource using the import statement below
from collections import ChainMap


###############################################################################
# Creating Chain Maps
###############################################################################


# Creating an empty Chain Map
# * We can create an empty Chain Map using the ChainMap class
x = ChainMap()
print(x)
# ChainMap({})


# Creating a Chain Map (with dictionaries)
# * The ChainMap accepts multiple dictionaries as parameters. Each dictionary
#   will be added to the Chain Map and all keys will be accessible
x1 = {'name': 'John'}
x2 = {'age': 50}
y = ChainMap(x1, x2)
print(y, y['name'], y['age'])
# ChainMap({'name': 'John'}, {'age': 50}) John 50


###############################################################################
# Chain Map Attributes
###############################################################################


# Maps
# * The `maps` attribute returns a list of all dictionaries in the Chain Map
x1 = {'name': 'John'}
x2 = {'age': 50}
y = ChainMap(x1, x2)
print(y.maps)
# [{'name': 'John'}, {'age': 50}]


# Parents
# * The `parents` property returns a new Chain Map containing all of the maps
#   in the current instance except the first one
x1 = {'name': 'John'}
x2 = {'age': 50}
y = ChainMap(x1, x2)
print(y.parents)
# ChainMap({'age': 50})


###############################################################################
# Chain Map Methods
###############################################################################


# New Child
# * The `new_child()` method returns a new Chain Map containing a new map
#   followed by all of the maps in the current instance
x1 = {'name': 'John'}
x2 = {'age': 50}
y = ChainMap(x1, x2)
z = y.new_child({'profession': 'Developer'})
print(z)
# ChainMap({'profession': 'Developer'}, {'name': 'John'}, {'age': 50})
