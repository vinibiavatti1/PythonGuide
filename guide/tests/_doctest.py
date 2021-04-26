"""
Doctest
* Use ">>>" sequence to define a doctext inside a docstring
* The definition is equivalet of the execution in Python console
* The expected result must be equal the result returned in the Python console
* The doctest module searches for pieces of text that look like interactive
  Python sessions, and then executes those sessions to verify that they work
  exactly as shown. There are several common ways to use doctest
* Use the command $ python -m doctest -v <module_name> to execute the doctest
  of this module from command line
* NOTE: Run the file with the -v switch, to check details of tests
* NOTE: Check the _doctest.py file in modules
"""
import doctest


###############################################################################
# Create Doctest
###############################################################################


# Create docstring with doctest
# * The doctest is created inside the docstring of the function, method, class,
#   etc.
def factorial(n):
    """
    Return the factorial of n, an exact integer >= 0

    >>> factorial(0)
    0
    >>> factorial(1)
    1
    >>> factorial(10)
    3628800
    >>> factorial(5.5)
    120
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n is less than zero
    """
    if n < 0:
        raise ValueError('n is less than zero')
    if n == 0:
        return n
    x = 1
    result = 1
    while x <= n:
        result *= x
        x += 1
    return result


###############################################################################
# Execute Doctest
###############################################################################


# Testing this module
# * To execute the doctest, the docttest.testmod() function can be used, from
#   doctest module
# * You can execute the doctests from some module by line command too, using:
#   $ python -m doctest -v <module_name>
doctest.testmod()
print('Test complete!')
