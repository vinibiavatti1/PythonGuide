"""
Docstring

* PEP 257 is the convention for docstrings in Python
* Appears after the definition of a function, method, class, or module
"""


# Class
class Math:
    """
    Class with math operations
    """
    pass


help(Math)
# class Math(builtins.object)
# |  Class with math operations
# ...


# Function
def sum(x, y):
    """
    Add y to x and return the sum
    """
    return x + y


help(sum)
# sum(x, y)
#     Add y to x and return the sum


# Method
class Math2:
    @staticmethod
    def sum(x, y):
        """
        Add y to x and return the sum
        """
        return x + y


help(Math2.sum)
# sum(x, y)
#     Add y to x and return the sum


# Module
# * This is the first comment in the module (Python file)
import _datatypes
help(_datatypes)
# NAME
#     _datatypes - Datatypes
#
# DESCRIPTION
#     Text Type:          str
#     Numeric Types:  int, float, complex
#     Sequence Types: list, tuple, range
#     Mapping Type:   dict
#     Set Types:          set, frozenset
#     Boolean Type:   bool
#     Binary Types:   bytes, bytearray, memoryview
# ...
