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
# Docstring simple conventions
# * Simple way to document the code
###############################################################################


# Documentation
# * Explanation of the code, with code examples, tests, etc
def add(x, y):
    """
    Sum two integer or float numbers and returns the result

    >>> add(1, 3)
    4
    >>> add(1.5, 3.5)
    5.0
    """
    pass


###############################################################################
# Docstring advance conventions
# * Advance way to document the code
###############################################################################


# Summary
# * Every docstring must contain a summary as first
def fn_summary():
    """
    Example of 'Summary'
    """
    pass


# Parameters
# * Description of the function arguments, keywords and their respective types
def fn_parameters():
    """
    Example of 'Parameters' documentation

    Parameters
    ----------
    value
        Example of no type parameter
    number: int
        Example of integer parameter
    text: str
        Example of string parameter
    active: bool
        Example of bool parameter
    words: list[str]
        Example of list of string parameter
    status: {'success', 'error'}
        Example of enum parameter
    debug: bool, default False
        Example of parameter with default value
    ...
    """
    pass


# Returns
# * Explanation of the returned values and their types
def fn_returns():
    """
    Example of 'Returns' documentation

    Returns
    -------
    result: float
        Example of return value
    ...
    """
    pass


# Yields
# * Explanation of the yielded values and their types
def fn_yields():
    """
    Example of 'Yields' documentation

    Yields
    ------
    current: int
        Example of yield value
    ...
    """
    pass


# Raises
# * Explanation of excpetions that the function can raises
def fn_raises():
    """
    Example of 'Raises' documentation

    Raises
    ------
    TypeError
        Example of TypeError documentation
    ValueError
        Example of ValueError documentation
    ...
    """
    pass


# See also
# * Suggest for the user to see other resources
def fn_see_also():
    """
    Example of 'See Also' documentation

    See Also
    --------
    print
        Example of global function documentation
    math.cos
        Example of module function documentation
    math.pi
        Example of module constant documentation
    ...
    """
    pass


# Notes
# * Provides additional information about the code
def fn_notes():
    """
    Example of 'Notes' documentation

    Notes
    -----
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas a
    lobortis diam, id suscipit neque. Pellentesque malesuada mi nec dolor
    suscipit euismod
    ...
    """
    pass


# References
# * Provides references of information or something about the code
def fn_references():
    """
    Example of 'References' documentation

    References
    ----------
    Python website
        https://www.python.org/
    ...
    """
    pass


# Examples
# * Provides examples of the code usage
def fn_examples():
    """
    Example of 'Examples' documentation

    Examples
    --------
    >>> add(5, 5)
    10
    >>> add(3.5, 2.5)
    6.0
    ...
    """
    pass


# Class summary
# * The class can be documentad also, with a summary only
class Documentation:
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas a
    lobortis diam, id suscipit neque. Pellentesque malesuada mi nec dolor
    suscipit euismod
    ...
    """
    pass
