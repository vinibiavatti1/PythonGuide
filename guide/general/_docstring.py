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
    ...


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


###############################################################################
# Docstring parameters
###############################################################################


# Docstring parameters documentation
# * Docstring are free-form. This is not a real convention.
# * This way to create docstrings is from Numpy lib
# * Reference:
#   * https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
def fn(number, name, skills, genre, active=True, **kwargs):
    """
    Example of function parameters documentation

    Parameters
    ----------
    number: int
        Identifier number
    name: str
        Name of the member
    skills: list[str]
        Skills of the person
    genre: {'M', 'F'}
        The genre of the person
    active: bool, default: True
        Set True if this record is active, otherwise set False to make this
        record inactive
    persist: bool, default: False
        Set True to persist the record
    """
    ...
