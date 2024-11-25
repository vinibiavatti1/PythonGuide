"""
Str and Repr

* The `__str__` and `__repr__` methods are used to define the string
  representation of the object
* To use the `__str__` method, we need to implement the String Protocol
* To use the `__repr__` method, we need to implement the Representation
  Protocol
* These methods are used by the `str` and `repr` functions, respectively
* NOTE: The `str()` function will call the `__str__` method. If this method is
  not available, it will call the `__repr__` method instead
* The table below shows the behavior of the `str` and `repr` functions when the
  `__str__` and `__repr__` methods are available/not available:
###############################################################################
__str__     __repr__    str()       repr()
###############################################################################
No          No          Default     Default
No          Yes         __repr__    __repr__
Yes         No          __str__     Default
Yes         Yes         __str__     __repr__
###############################################################################
"""


###############################################################################
# String Protocol
###############################################################################


# Implementing the String Protocol
# * In the example below, we created a class that implements the String
#   protocol
class CustomClass:
    def __str__(self):
        return 'str'


# Using the str function
# * When using the `str()` function, it will call the `__str__` method
x = CustomClass()
y = str(x)
print(y)
# str


###############################################################################
# Representation Protocol
###############################################################################


# Implementing the Representation Protocol
# * In the example below, we created a class that implements the Representation
#   protocol
class CustomClass:
    def __repr__(self):
        return 'repr'


# Using the repr function
# * When using the `repr()` function, it will call the `__repr__` method
x = CustomClass()
y = repr(x)
print(y)
# repr


###############################################################################
# Precedence
###############################################################################


# String Protocol Impl: No / Representation Protocol Impl: No
# * If neither the `__str__` nor the `__repr__` methods are implemented, the
#   default behavior will be used
class CustomClass:
    pass
x = CustomClass()
y1 = str(x)
y2 = repr(x)
print(y1, y2)
# <__main__.CustomClass object at ...> <__main__.CustomClass object at ...>


# String Protocol Impl: No / Representation Protocol Impl: Yes
# * If the `__repr__` method is implemented, the `repr()` and `str()` functions
#   will call it
class CustomClass:
    def __repr__(self):
        return 'repr'
x = CustomClass()
y1 = str(x)
y2 = repr(x)
print(y1, y2)
# repr repr


# String Protocol Impl: Yes / Representation Protocol Impl: No
# * If the `__str__` method is implemented, the `str()` function will call it
#   and the `repr()` function will call the default behavior
class CustomClass:
    def __str__(self):
        return 'str'
x = CustomClass()
y1 = str(x)
y2 = repr(x)
print(y1, y2)
# str <__main__.CustomClass object at ...>


# String Protocol Impl: Yes / Representation Protocol Impl: Yes
# * If both the `__str__` and `__repr__` methods are implemented, the `str()`
#   function will call the `__str__` method and the `repr()` function will call
#   the `__repr__` method
class CustomClass:
    def __str__(self):
        return 'str'
    def __repr__(self):
        return 'repr'
x = CustomClass()
y1 = str(x)
y2 = repr(x)
print(y1, y2)
# str repr
