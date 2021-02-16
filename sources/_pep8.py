"""
PEP (Python Enhancement Proposals)

* PEP8 is a documentation to describe the good practices for Python
* This is allowed in https://www.python.org/dev/peps/
* The idea is to describe the way to type code using 'Pythonic' way
"""

# -----------------------------------------------------------------------------
# Naming Convension


# Variables
# * Use a good representation name
# * Use undercore to separete
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
