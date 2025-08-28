"""
Docstring

* A docstring (documentation string) is a comment that describes Python
  resources like (modules, classes, functions, methods and packages)
* This comment is an example of a docstring
* Is is surrounded by triple double quotes
* The docstring comment appears at a specific location depending on the
  resource:
  * Modules: At the top of the file
  * Classes: Immediately after the class definition
  * Functions/methods: Immediately after the definition
  * Packages: In the __init__.py file
* The PEP-257 contains the definitions and the convention for docstrings in
  Python
* NOTE: The Python documentation is flexible and allows to use other formats.
  We don't need to use all the sections shown in the examples below. The
  purpose of this guide is to show the most common sections used in docstrings
  and to provider a template to use in our projects
* NOTE: Take a look at _doctests.py file to see how to use doctests in
  docstrings
* References:
  * https://google.github.io/styleguide/pyguide.html
  * https://www.python.org/dev/peps/pep-0257/
"""


###############################################################################
# Module Docstrings
###############################################################################


# Documenting a Module
# * All modules can contain a docstring at the top of the file that describes
#   the module
# * NOTE: We don't need to use all the sections shown in the example below. It
#   is not a requirement.
"""
Description of the module here

Examples:
    Typical usage example:
        foo = ClassFoo()
        bar = foo.FunctionBar()

See Also:
    math.pi: Example of module constant documentation

Notes:
    Some notes here

Authors:
    John Due: john.due@email.com

References:
    Python website: https://www.python.org/
"""


###############################################################################
# Class Docstrings
###############################################################################


# Class docstring
# * All classes can contain a docstring after the class declaration
class SampleClass:
    """
    Description of the class here

    Attributes:
        name: The name of the resource

    Examples:
        Sum two integer or float numbers and returns the result
            add(1, 3) -> 4

    See Also:
        math.pi: Example of module constant documentation

    Notes:
        Some notes here

    Authors:
        John Due: john.due@email.com

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
# * All functions/methods can contain a docstring after the declaration
# * NOTE: For functions, the self argument is not considered since it
#   represents the reference to the class instance
def add(self, arg, *args, arg2=3, **kwargs):
    """
    Function/Method description here

    Args:
        self: The class instance reference
        arg: Description about the argument 1
        *args: Description about arbitrary arguments
        arg2: Description about the argument 2 (Default 'w')
        **kwargs: Description about arbitrary keyword arguments

    Returns:
        Return type description

    Yields:
        Return type description used when the function is a generator

    Raises:
        IOError: Error description and some information

    Examples:
        Some example description here
            add(1, 2, arg2=4, debug=True) -> ...

    See Also:
        math.pi: Example of module constant documentation

    Notes:
        Some notes here

    Authors:
        John Due: john.due@email.com

    References:
        Python website: https://www.python.org/

    Tests:
        Sum two integer or float numbers and returns the result
        >>> add(1, 3)
        4
    """


###############################################################################
# Show the docstring
###############################################################################


# Showing the docstring of a Python resource
# * The docstring of a Python resource is stored into the __doc__ attribute
# * We can print the content of this attribute to show the docstring
# * The example below prints the docstring of the sum function
print(sum.__doc__)
"""
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value. This function is intended
specifically for use with numeric values and may reject non-numeric types.
"""
