"""
Type

* The `type()` can be used for two purposes:
  * to get the type of an object
  * to create a new class (at runtime)
* When only the first argument is set, type() returns the type of the object
* When three arguments are passed, type() returns a new class
* The `type` is the default metaclass for created classes
###############################################################################
Syntax                      Description
###############################################################################
type(object)                Returns the type of the object
type(name, bases, dict)     Returns a new class object (at runtime)
###############################################################################
"""


###############################################################################
# Using Type to Check Types
###############################################################################


# Getting the type of objects
# * The `type()` function can be used to get the type of any object
x1 = type(1)
x2 = type(3.5)
x3 = type('Hello world')
x4 = type([1, 2, 3])
print(x1, x2, x3, x4, sep=', ')
# <class 'int'>, <class 'float'>, <class 'str'>, <class 'list'>


###############################################################################
# Using Type to Create Classes
###############################################################################


# Creating a new class
# * The `type()` function can be used to create a new class object at runtime
# * This approach can be useful for meta-programming
CustomObject = type('CustomObject', (), {})
x = CustomObject()
print(x)
# <__main__.CustomObject object at 0x00000216A4F76390>


# Creating a new class (with a base class)
# * The second parameter accepts a tuple with the base classes for the class
#   that will be created
CustomObject = type('CustomObject', (int,), {})
x = CustomObject(5)
print(x)


# Creating a new class (with attributes)
# * The third parameter accepts a dictionary with the attributes and default
#   values for this class.
CustomObject = type('CustomObject', (), {'value': 10})
x = CustomObject()
print(x.value)
# 10


###############################################################################
# Using Type to Create Classes With a Custom Base Class
###############################################################################


# Creating a custom base class
# * We will create a custom base class that will be used as the base class in
#   the type function
# * Note: The default value will be 10
class CustomValue:
    def __init__(self):
        self.x = 1


# Creating a new class (with a custom base class)
# * Now, we will create a new class at runtime using the custom class as the
#   base class
# * Note that the attribute `y` was added to the new class and the 'x' value
#   was not replaced
# * NOTE: The attributes set for the type function will not replace the base
#   attribute values
CustomObject = type('CustomObject', (CustomValue,), {'x': 2, 'y': 2})
x = CustomObject()
print(x.x, x.y)
# 1 2
