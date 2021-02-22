"""
PEP (Python Enhancement Proposals)

* PEP8 is a documentation to describe the good practices for Python
* This is allowed in https://www.python.org/dev/peps/
* The idea is to describe the way to type code using 'Pythonic' way
"""

# -----------------------------------------------------------------------------
# Naming


# Variables
# * Use a good representation name
# * Use underscore to separete
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
client_name = 'Vini'


# Constants
# * Use a good representation name
# * Use undercore to separete
# * Use all letters capitalized
# * Do not use special symbols
PI = 3.14


# Functions
# * Use a good representation name
# * Use undercore to separete
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
def sum(x, y):
    return x + y


# Classes
# * Use a good representation name
# * Do not use undercore to separete
# * Use camel case
# * Do not use special symbols
# * Capitalize all letters of an abbreviation
# * Do not use letters to represent the type like "I" for interface
class HTTPServer:
    pass


# Methods
# * Use a good representation name
# * Use undercore to separete
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


# Private properties
# * Use a good representation name
# * Use undercore to separete
# * Do not use camel case
# * Do not use special symbols
# * Always start the property name with uderscore
# * Do not use capital letters
class Bus:
    def __init__(self, name):
        self._name = name


# Packages
# * Use a good representation name
# * Use undercore to separete
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
"""/src/classes/client.py"""


# Modules
# * Use a good representation name
# * Use undercore to separete
# * Do not use camel case
# * Do not use special symbols
# * Do not use capital letters
from abc import ABC


# Strings
# * Always use ' char to strings
text = 'Hello'


# -----------------------------------------------------------------------------
# Importation


# Import in multiple lines
# * Do not use different imports at same line like import sys, abc
# * Always put the imports at the top of the file of after the first comment
import sys
import abc


# Import a big amount of resources
# Use multi line to import the resources
from abc import (
    ABC,
    ABCMeta
)


# -----------------------------------------------------------------------------
# Comments


# Inline comments
# * Use two spaces after expression for inline comments
x = 10  # My variable


# Multiline comments
# * Use """ the single quotes always
"""
Lorem ipsum
"""


# -----------------------------------------------------------------------------
# Code recomendations


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
if 1 == 1:
    pass


# Dont use unecessary spaces
# * Do not put more spaces in lists, parameters, function names, etc
# * Do not try to inline vertically some text with spaces
lst = [1, 2, 3, 4, 5]
x = 1
long_variable = 5


# EOF new line
# * Always use a blank line as EOF (end of file) line
