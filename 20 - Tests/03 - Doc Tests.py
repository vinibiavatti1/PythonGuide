"""
Doc Tests

* The doctest module provides a way to test that doctests in docstrings.
* The doctests in docstrings are written in a way that they can be
  executed as if they were in an interactive Python session.
* We can also use doctests in docstrings to demonstrate examples of how to use
  a function or a class.
* To run the doctests, we can use the command below in the command line:
  `python -m doctest module.py`
* The doctests below will be used to demonstrate the doctest module. Note that
  there are some tests that will fail.
>>> 1 + 1
2
>>> 2 + 2
5
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import doctest


###############################################################################
# Testing a Module
###############################################################################


# Testing a module
# * We can test a module using the `doctest.testmod()` function
# * If no module is specified, the `__main__` module will be used to test
# * The function will return a `TestResults` object with the number of tests
#   run, the number of failures, and the number of errors
# * We can also execute the module test using the command line with the
#   command `python -m doctest module.py`
x = doctest.testmod()
print(x)
# TestResults(failed=1, attempted=2)
# Failed example:
#     2 + 2
# Expected:
#     5
# Got:
#     4


###############################################################################
# Testing an Object
###############################################################################


# Defining an Object with Doctests
# * We will define an object with some doctests in its docstring to be used for
#   testing
def function():
    """
    >>> 1 + 1
    2
    >>> 2 + 2
    5
    """
    ...


# Running Doctests on an Object
# * We can test examples associated with an object using the
#   `doctest.run_docstring_examples()` function
# * The first argument is the object to test, and the second argument is the
#   global variables to use for the test
x = doctest.run_docstring_examples(function, globals())
print(x)
# TestResults(failed=1, attempted=2)
# Failed example:
#     2 + 2
# Expected:
#     5
# Got:
#     4
