"""
Named Tuple

* A Named Tuple is a tuple subclass available in the collections module, and
  can be used to create tuple-like objects with named fields.
* The `namedtuple()` function from the `collections` module is used to create
  named tuples. It returns a new tuple subclass with named fields.
* After creating a tuple subclass, this subclass can be used to create tuple
  objects with named fields, like a class with attributes.
* The `namedtuple()` function has some parameters. Take a look below to see
  them.
* Syntax: namedtuple(typename, field_names, *, rename=False, defaults=None,
  module=None)

###############################################################################
Parameter      Description
###############################################################################
typename       The name of the new tuple subclass
field_names    A sequence of field names (can be a string or a list)
rename         If True, invalid field names are replaced with positional names
defaults       A sequence of default values for the fields
module         The module name to use in the __module__ attribute of the named
###############################################################################
"""


###############################################################################
# Importing Resource
###############################################################################


# Importing the resource
# * We can import the resource using the import statement below
from collections import namedtuple


###############################################################################
# Creating Named Tuples
###############################################################################


# Creating a Named Tuple (with list)
# * We can create a named tuple using a list of field names
Point = namedtuple('Point', ['x', 'y'])
x = Point(10, 20)
print(x)
# Point(x=10, y=20)


# Creating a Named Tuple (with string)
# * We can create a named tuple using a string of field names. The string
#   should be separated by commas
# * This will result in the same named tuple as the previous example
Point = namedtuple('Point', 'x, y')
x = Point(10, 20)
print(x)
# Point(x=10, y=20)


# Creating a Named Tuple (with rename)
# * The rename parameter is used to replace invalid field names with positional
#   names
# * Note that we used keywords that are reserved in Python, so the field names
#   were replaced with positional names. If the rename parameter is set to
#   False, an error will be raised
Point = namedtuple('Point', ['class', 'def'], rename=True)
x = Point(10, 20)
print(x)
# Point(_0=10, _1=20)


# Creating a Named Tuple (with defaults)
# * The defaults parameter is used to set default values for the fields
Point = namedtuple('Point', ['x', 'y'], defaults=[10, 20])
x = Point()
print(x)
# Point(x=10, y=20)


# Creating a Named Tuple (with module)
# * The module parameter is used to set the module name in the __module__ field
# * This is useful when we want to know where the named tuple was created
# * When not defined, the __module__ field will be set to the current module
#   name. In this case, it will be set to '__main__'
Point = namedtuple('Point', ['x', 'y'], module='my_module')
x = Point(10, 20)
print(x.__module__)
# my_module


###############################################################################
# Named Tuple Attributes Access
###############################################################################


# Accessing Named Tuple Attributes (by index)
# * We can access the named tuple attributes by index
Point = namedtuple('Point', ['x', 'y'])
x = Point(10, 20)
print(x[0], x[1], sep=', ')
# 10, 20


# Accessing Named Tuple Attributes (by name)
# * We can access the named tuple attributes by name
Point = namedtuple('Point', ['x', 'y'])
x = Point(10, 20)
print(x.x, x.y, sep=', ')
# 10, 20


###############################################################################
# Named Tuple Methods
###############################################################################


# Make
# * The `_make()` method is used to create a new instance of the named tuple
#   from an iterable
# * The iterable should have the same number of elements as the named tuple
#   fields, otherwise an error will be raised
Point = namedtuple('Point', ['x', 'y'])
attributes = [10, 20]
x = Point._make(attributes)
print(x)
# Point(x=10, y=20)


# As Dict
# * The `_asdict()` method is used to return the named tuple as a dictionary
Point = namedtuple('Point', ['x', 'y'])
x = Point(10, 20)
print(x._asdict())
# {'x': 10, 'y': 20}
