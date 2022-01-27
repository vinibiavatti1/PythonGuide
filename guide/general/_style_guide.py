"""
Python Style Guide

* This file represents some concepts of:
  * PEP8: Style Guide for Python Code
  * PEP257: Docstring Conventions
  * PEP484: Type Hints
* This is allowed in https://www.python.org/dev/peps/
* The idea is to describe the way to type code using 'Pythonic' way
* Use the editorconfig plugin in your IDE and put the .editorconfig file on the
  root of this projecto to your projecto to configure the code format
* Reference: https://www.python.org/dev/peps/
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
    pass


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
        pass

    @classmethod
    def create(cls):
        pass

    @staticmethod
    def version():
        pass


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
from abc import ABC


# Main module
# * NOTE: Not real PEP recomendation
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
        self.name = name               # public
        self._size = size              # protected
        self.__country = country       # private

    def public_method(self): pass      # public
    def _protected_method(self): pass  # protected
    def __private_method(self): pass   # private


###############################################################################
# Importation
###############################################################################


# Import in multiple lines
# * Do not use different imports at same line like import sys, abc
# * Always put the imports at the top of the file of after the first comment
import sys
import abc as myabc


# Import a big amount of resources
# * Use multi line to import the resources
from abc import (
    ABC,
    ABCMeta as MyABCMeta
)


###############################################################################
# Comments
###############################################################################


# Inline comments
# * Use two spaces after expression for inline comments
x = 10  # My variable


# Multiline comments
# * Use """ the single quotes always
"""
Lorem ipsum
"""


# Section comments
# * NOTE: Not real PEP recomendation
# * To separate code sections, use the section comment with "#" char
# * NOTE: The example below is inside a multi-line comment just to differs from
#   the other section comments in this file
"""
###############################################################################
# Title
###############################################################################
"""


# Idented section comments
# * NOTE: Not real PEP recomendation
# * To use section inside code blocks, ident the section comments
"""
    ###########################################################################
    # Title
    ###########################################################################
"""


# Docstrings
# * NOTE: Not real PEP recomendation
# * Use a multiline comment with dual quotes
# * Do not use a multiline in just one line (inline) comment
def function():
    """
    This function returns True
    """
    return True


###############################################################################
# Function and Type hints
###############################################################################


# Function arguments
# * When some function exceeds the line length, use berak-line
def function(argument1, argument2, argument3, argument4, argument5, argument6,
             argument7):
    pass


# Type hints in functions
# * Always try to use type hints in functions
# * When no return type, specify None
# * Use typing module for more types
def typed_function(number: int, name: str, lst: list[str]) -> None:
    pass


# Type hints in functions (multi line)
# * When some function exceeds the line length, use berak-line
def typed_function(number: int, name: str, lst: list[str],
                   other: tuple[int], another: bool) -> None:
    pass


# Type hints in classes
# * The self and cls parameters does not need a type hint
class TypedClass:

    def method(self, name: str) -> str:
        pass

    @classmethod
    def class_method(cls, name: str) -> None:
        pass


###############################################################################
# Code recomendations
###############################################################################


# Spacement and line breaks
# * Use two line breaks before and after functions, classes and multi line
#   comments
def action():
    pass


class Person():
    pass


x = 1


"""
Comment
"""


# Line length
# * Respect the line length limit (79 chars)
x = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus nulla \
nisl'


# Identation
# * Always use 4 spaces to indent your code
# * NOTE: DO NOT use tabs
if 1 == 1:
    pass


# Do not use unecessary spaces
# * Do not put more spaces in lists, parameters, function names, etc
# * Do not try to inline vertically some text with spaces
lst = [1, 2, 3, 4, 5]
x = 1
long_variable = 5


# Backslash
# * For long python lines, it is recommended to use backlash (\) to wrap
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et ul " \
    "lamcorper ipsum. Nullam et elit nec ante porttitor finibus finibus di " \
    "gnissim nulla. In pharetra vulputate magna sodales consequat"


# Long if
# * To make a if with more lines, use parenthesis
# * From second condition onwards, the conditions must be indented
# * Always put the logical operator as the end of the line, to the first
if (1 == 1 and      # Dont use indentation
        2 == 2 and  # Use indentation
        3 == 3 or   # Use indentation
        4 == 4):    # Use indentation
    pass


# Unused resource
# * To mark some resource as unused intentionally, use the "_" char as the name
#   of the resource
for _ in range(10):
    pass


# EOF new line
# * Always use a blank line as EOF (end of file) line
