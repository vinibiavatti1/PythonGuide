"""
Docstring

* PEP 257 is the convention for docstrings in Python
* Appears after the definition of a function, method, class, or module
* NOTE: Check _doctests.py too
* References: https://google.github.io/styleguide/pyguide.html
              https://www.python.org/dev/peps/pep-0257/
"""


###############################################################################
# Module Docstrings
###############################################################################


# Module docstring
# * All modules must contain a docstring at the top of the file
# * It can has some examples of code to show the purpose of it
"""
A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes ad functions and/or usage
examples.n

Examples:
    Typical usage example:
    foo = ClassFoo()
    bar = foo.FunctionBar()

See Also:
    math.pi: Example of module constant documentation.

Notes:
    Some notes here.

Authors:
    John Due: john.due@email.com

References:
    Python website: https://www.python.org/
"""


###############################################################################
# Class Docstrings
###############################################################################


# Class docstring
# * It can has a list of attributes/methods description
class SampleClass:
    """
    Summary of class here.

    More optional class information...

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.

    Examples:
        Sum two integer or float numbers and returns the result
        add(1, 3) -> 4

    See Also:
        math.pi: Example of module constant documentation.

    Notes:
        Some notes here.

    References:
        Python website: https://www.python.org/

    Tests:
        Sum two integer or float numbers and returns the result
        >>> obj = SampleClass()
    """


###############################################################################
# Function/Methods Docstrings
###############################################################################


# Functions/Methods
# * Use sections to separate documentation for arguments, keyword-arguments,
#   returns, yeilds, etc.
def functions_and_methods(value, *values, **kwargs):
    """
    Summary of function/methods here.

    Args:
        value: Positional argument description with some information and with
            break line for multi-line description.
        *values: Arbitraty argument description.
        **kwvalue: Keyword argument description.

    Returns:
        Return type description.

    Yields:
        Return type description used when the function is a generator.

    Raises:
        IOError: Error description and some information.

    Examples:
        Sum two integer or float numbers and returns the result
        add(1, 3) -> 4

    See Also:
        math.pi: Example of module constant documentation.

    Notes:
        Some notes here.

    References:
        Python website: https://www.python.org/

    Tests:
        Sum two integer or float numbers and returns the result
        >>> add(1, 3)
        4
    """


###############################################################################
# Print docstring
###############################################################################


# Access the docstring of object
print(sum.__doc__)
"""
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value. This function is intended
specifically for use with numeric values and may reject non-numeric types.
"""
