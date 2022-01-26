"""
Doctest module

* The doctest module searches for pieces of text that look like interactive
  Python sessions, and then executes those sessions to verify that they work
  exactly as shown. There are several common ways to use doctest:
  * To check that a module's docstrings are up-to-date by verifying that all
    interactive examples still work as documente
  * To perform regression testing by verifying that interactive examples from a
    test file or a test object work as expected
  * To write tutorial documentation for a package, liberally illustrated with
    input-output examples. Depending on whether the examples or the expository
    text are emphasized, this has the flavor of "literate testing" or
    "executable documentation"
* NOTE: Run the file with the -v switch, to check details of tests
* NOTE: Check the _doctest.py file in general

This is an example of a doctest with error:
>>> 5 + 5
0
"""
import doctest
import os
import sys
current_path = sys.path[0]


###############################################################################
# Testing doctests
###############################################################################


# testfile(filename)
# * Execute a file containing a doctest
file_path = os.path.join(current_path, '../../resources/doctest.txt')
doctest.testfile(file_path)
# Failed example:
#     3 + 3
# Expected:
#     5
# Got:
#     6


# testmod(m=None)
# * Test a python module
# * If m is None, the __main__ module will be used to test
doctest.testmod()
# Failed example:
#     5 + 5
# Expected:
#     0
# Got:
#     10


# run_docstring_examples(f, globs)
# * Test examples associated with object f; for example, f may be a string, a
#   module, a function, or a class object
def func():
    """
    >>> 1 + 1
    10
    """
    pass


doctest.run_docstring_examples(func, globals())
# Failed example:
#     1 + 1
# Expected:
#     10
# Got:
#     2
