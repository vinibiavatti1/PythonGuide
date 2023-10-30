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
    return x + y


# Classes
# * Use a good representation name
# * Do not use underscore to separate
# * Use camel case
# * Do not use special symbols
# * Capitalize all letters of an abbreviation
# * Do not use letters to represent the type like "I" for interface
class HTTPServer:
    ...


# Methods
# * Use a good representation name
# * Use underscore to separate
# * Do not use camel case
# * Do not use special symbols
# * Instance methods should have their first parameter named 'self'.
# * Class methods should have their first parameter named 'cls'
# * Static methods doesn't need to have a default first parameter
# * Do not use capital letters
class Car:

    def start_acceleration(self):
        ...

    @classmethod
    def create(cls):
        ...

    @staticmethod
    def version():
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
        pass


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
import collections.abc


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
    pass


# Exception alias
# * Use the 'err' name
try:
    pass
except ValueError as err:  # "err" word to reference the error
    pass


# Strings
# * Always use ' char to strings
text = 'Hello'


# Class access modifiers
# * Use nothing as prefix to public resources
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
# * Never use a python reserved word or builtin word as name for any artifact
# * Use underline "_" as suffix
from_ = 'Hello'
input_ = 'World'


###############################################################################
# Importation
###############################################################################


# Multiple module imports
# * Do not use different imports at same line like import sys, abc
# * Always put the imports at the top of the file after the module docstring
import sys
import abc as my_abc


# Multiple module resources imports
# * Use multi line to import the resources from a specific module
from abc import (
    ABC,
    ABCMeta as MyABCMeta
)


###############################################################################
# Comments
###############################################################################


# Inline comments
# * Use two spaces after the expression for inline comments
x = 10  # My variable


# Multiline comments
# * Use double quotes (""") for multiline comments
"""
Lorem ipsum
"""


# Section comments
# * NOTE: Not real PEP recommendation
# * To separate code sections, use the section comment with "#" char
# * NOTE: The example below is inside a multi-line comment just to differs from
#   the other section comments in this file
"""
###############################################################################
# The Title
###############################################################################
"""


# Sub section comments
# * NOTE: Not real PEP recommendation
# * For sub sections, use the indentation in the section comment
"""
    ###########################################################################
    # The Title
    ###########################################################################
"""


# Documentation strings
# * NOTE: Not real PEP recommendation
# * Use a multiline comment with double quotes
# * Don't use the quotes and the documentation in a single line
def function():
    """
    This function returns True
    """
    ...


###############################################################################
# Function and Type hints
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
# Code recommendations
###############################################################################


# Spacing and line breaks
# * Use two line breaks before and after functions, classes and multi-line
#   comments
def action():
    ...


class Person():
    ...


x = 1


"""
Comment
"""


# Line length
# * Respect the line length limit (79 chars)
x = 'This is a big text that respects the line length limit (79 chars) and ' \
    'breaks the line to fit the limit'


# Indentation
# * Always use 4 spaces to indent your code
# * NOTE: DO NOT use tabs, use only spaces
if 1 == 1:
    pass


# Do not use un-necessary spaces
# * Do not put more spaces in lists, parameters, function names, etc
# * Do not try to inline vertically some text with spaces
lst = [1, 2, 3, 4, 5]
x = 1
long_variable = 5


# Backslash
# * For long python lines, it is recommended to use backlash (\) to wrap
txt = 'This is a big text that respects the line length limit (79 chars) ' \
      'breaks the line to fit the limit'


# Long if
# * To make a if with more lines, use parenthesis
# * From second condition onwards, the conditions must be indented
# * Always put the logical operator as the front of the condition
if (
    1 == 1
    and 2 == 2
    or 3 == 3
):
    ...


# Unused resource
# * To mark some resource as unused intentionally, use the "_" char as the name
#   of the resource
for _ in range(10):
    ...


# Multiple unused resources in the same context
# * Concat more "_" to unused resources at same context
for _ in range(10):
    for __ in range(10):
        ...


# EOF new line
# * Always use a blank line as EOF (end of file) line
