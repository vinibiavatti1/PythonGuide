"""
Repr (Representation)

* The `repr()` function calls the `__repr__` method inside the object
* For objects, the `__repr__` returns a string containing the memory position
  by default
* The return value can be set by implementing the Representation Protocol
"""


###############################################################################
# Representation of Native Objects
###############################################################################


# Representation of an integer
# * The integer will return the value as a string
x = 1
print(repr(x))
# 1


# Representation of a string
# * The string will return its value
x = 'text'
print(repr(x))
# 'text'


# Representation of a collection
# * The collection will return the collection as a string
x = [1, 2, 3]
print(repr(x))
# [1, 2, 3]


###############################################################################
# Representation of Custom Objects
###############################################################################


# Creating a custom object (without Representation Protocol)
# * In this example, the custom object will not implement the Representation
#   Protocol, so the `repr` function will return the default representation
class CustomObject:
    pass


# Representation of a custom object
# * The default representation of an object is the memory position
x = CustomObject()
print(repr(x))
# <__main__.CustomObject object at 0x000001E1A889B920>


# Creating a custom object (without Representation Protocol)
# * We can implement the Representation Protocol to define the representation
#   of the object
class CustomObject:
    def __repr__(self):
        return 'Custom Object'


# Representation of a custom object
# * When the `repr` function is called, it will return the result of the
#   `__repr__` function
x = CustomObject()
print(repr(x))
# Custom Object
