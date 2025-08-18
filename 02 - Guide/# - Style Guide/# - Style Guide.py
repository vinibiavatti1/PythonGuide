"""
Python Style Guide

* This file represents some concepts of:
  * PEP008: Style Guide for Python Code
  * PEP257: Docstring Conventions
  * PEP484: Type Hints
* These PEPs can be found at https://www.python.org/dev/peps/
* The idea of this documentation is to be a quick reference for the most used
  concepts of how to write a good Python code (aka Pythonic code)
"""
import unittest


###############################################################################
# Naming
###############################################################################


# Variables
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
client_name = 'Vini'


# Constants
# * Use a good representation name
# * Use underscore to separate
# * Use all letters capitalized
# * Do not use special symbols
PI = 3.14


# Functions
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
def sum(x, y):
    ...


# Classes
# * Use a good representation name
# * Do not use underscore to separate
# * Use camel case
# * Do not use special symbols
# * Capitalize all letters of an abbreviation
# * Do not use letters to represent the type like "I" for interface
class HTTPServer:
    ...


# Class Functions
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Instance methods should have their first parameter named 'self'.
# * Class methods should have their first parameter named 'cls'
# * Static methods doesn't need to have a default first parameter
# * Do not use capital letters
class Car:
    def method(self):
        ...

    @classmethod
    def class_function(cls):
        ...

    @staticmethod
    def static_function():
        ...


# Test methods (TestCase)
# * Use "test_" as prefix
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Must have their first parameter named 'self'.
# * Do not use capital letters
class ListTest(unittest.TestCase):
    def test_append(self):
        ...


# Project (Root folder)
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
"""my_project"""


# Packages (Folders with __init__.py)
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
"""my_package"""


# Modules
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
"""my_module.py"""


# Main module
# * NOTE: Not real PEP recommendation
# * The main module is the entry module for the application
# * Use the 'main.py' name for this module
"""main.py"""


# Exceptions
# * Use a good representation name
# * Do not use underscore to separate
# * Use camel case
# * Do not use special symbols
# * Do not use letters to represent the type like "E" for Error
# * Use the 'Error' suffix in the exception class name
# * Extends an Exception subclass
class ValidationError(Exception):
    ...


# Exception alias
# * Use the 'err' identifier to reference the exception
try:
    ...
except ValueError as err:
    ...


# Strings
# * Use single quotes (') for strings
text = 'Hello'


# Class access modifiers
# * Use underline "_" to protected resources
# * Use dunder "__" to private resources
class Forest:

    def __init__(self, name, size, country):
        self.name = name          # public
        self._size = size         # protected
        self.__country = country  # private

    def public_method(self):      # public
        ...

    def _protected_method(self):  # protected
        ...

    def __private_method(self):   # private
        ...


# Reserved words/Builtin words
# * Never use a python reserved word or builtin word as name for any identifier
# * Use underscore "_" as suffix when you need to use a reserved word
from_ = 'Hello'
input_ = 'World'


###############################################################################
# Importation
###############################################################################


# Importing modules
# * Always use the import statement on the top of the file
import sys


# Import Alias
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
import statistics as st


###############################################################################
# Comments
###############################################################################


# Inline comments
# * Use two spaces after the expression for inline comments
x = 10  # My variable


# Multiline comments
# * Use double quotes ("") for multiline comments
"""
Lorem ipsum
"""


# Section comments
# * To separate code sections, use the section comment with "#" char
# * NOTE: The example below is inside a multi-line comment just to differs from
#   the other section comments in this file
"""
###############################################################################
# The Title
###############################################################################
"""


# Sub section comments
# * For sub sections, use the indentation in the section comment
"""
    ###########################################################################
    # The Title
    ###########################################################################
"""


# Documentation strings
# * Use a multiline comment with double quotes
def function():
    """This function returns something..."""
    ...


# Documentation strings (multi-line)
# * When the docstring is too long, use a break-line
def function():
    """
    This function returns something very long that exceeds the line length
    limit, so we will break-line it to fit the limit.
    """
    ...


###############################################################################
# Function and Type Hints
###############################################################################


# Function arguments
# * When some function exceeds the max line length, break-line the parameters
#   and fit the next line with the first parameters
def function(argument1, argument2, argument3, argument4, argument5, argument6,
             argument7):
    ...


# Function calls
# * When some function call exceeds the line length, break-line the arguments
#   and fit the next line with the first argument
function('argument1', 'argument2', 'argument3', 'argument4', 'argument5',
         'argument6', 'argument7')


# Function calls with big indentation
# * When some function indentation is too big, and the arguments exceeds the
#   line length, use break-line
function.function.function.function.function.function.function.function(
    'argument1', 'argument2', 'argument3', 'argument4', 'argument5'
)


# Type hints in functions
# * Use type hints in functions
# * When there is no return type, specify it using None
# * Use typing module for more types
def typed_function(number: int, name: str, lst: list[str]) -> None:
    ...


# Type hints in functions (multi line)
# * Use the same approach of function arguments with a break-line
def typed_function(number: int, name: str, lst: list[str],
                   other: tuple[int], another: bool) -> None:
    ...


# Type hints in functions (multi line for return only)
# * When only the return exceeds the line length, use break-line for return
def typed_function(number: int, name: str, lst: list[str], other: tuple[int]
                   ) -> None:
    ...


# Type hints in classes
# * The self and cls parameters does not need a type hint
class TypedClass:
    def method(self, name: str) -> str:
        ...

    @classmethod
    def class_method(cls, name: str) -> None:
        ...


###############################################################################
# Code Recommendations
###############################################################################


# Module line breaks
# * Use two line breaks to separete definitions
def function_1():
    ...


def function_2():
    ...


# Class line breaks
# * Use one line break before and after definitions inside classes
class Class:
    def method_1(self):
        ...

    def method_2(self):
        ...


# Line length
# * Try always to respect the line length limit (79 chars)
x = 'This is a big text that respects the line length limit (79 chars) and ' \
    'breaks the line to fit the limit'


# Indentation
# * Always use 4 spaces to indent your code
# * NOTE: DO NOT use tabs, use only spaces
if 1 == 1:
    pass


# Do not use un-necessary spaces
# * Do not put more spaces in lists, parameters, function names, etc
# * Do not try to inline vertically contents (only comments are allowed)
lst = [1, 2, 3, 4, 5]  # Comment 1
x = 1                  # Comment 2
long_variable = 5      # Comment 3


# Long if
# * To make a if with more lines, use parenthesis
# * From second condition onwards, the conditions must be indented
# * Always put the logical operator as the front of the condition
if ('This is a big text to the if' == 'This is a big text to the if'
    and 'This is a big text to the if' == 'This is a big text to the if'
    or 'This is a big text to the if' == 'This is a big text to the if'):
    ...


# Unused resource
# * To mark some resource as unused intentionally, use the "_" wildcard as the
#   identifier
_ = 'This is an unused variable'


# Multiple unused resources
# * Whe can re-use the "_" wildcard to multiple unused resources in the same
#   context
for _ in range(10):
    for _ in range(10):
        ...


# EOF new line
# * Always use a blank line as EOF (end of file) line
