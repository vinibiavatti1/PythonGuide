"""
Docstring

* PEP 257 is the convention for docstrings in Python
* Appears after the definition of a function, method, class, or module
* NOTE: Check _doctests.py too
"""


###############################################################################
# Docstrings
###############################################################################


# Class
class Math:
    """
    Class with math operations
    """
    pass


# Function
def sum(x, y):
    """
    Add y to x and return the sum
    """
    return x + y


# Method
class Math2:
    @staticmethod
    def sum(x, y):
        """
        Add y to x and return the sum
        """
        return x + y


###############################################################################
# Print docstring
###############################################################################


# Access the docstring of object
print(sum.__doc__)
# Add y to x and return the sum
