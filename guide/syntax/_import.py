"""
Import keyword

* The import statement is the most common way of invoking the import machinery
* It is used to import names (definitions) from Python modules like variables,
  classes and functions
* We can import specific names (definitions) from a module without importing
  the module as a whole using "from" keyword
* Syntax:
  * import <module> [as <alias>]
  * from <package|module> import <module|definition> [as <alias>]
"""


# Import
# * NOTE: Not recommended if a few definitions will be used
import random


# Module alias
# * Change the module name with alias
import random as rng


# Import specific definitions (from)
# * NOTE: Recommended to control execution memory
from random import uniform


# Import specific definitions (from) with alias
# * NOTE: The alias can be used in module or in definition
from random import randint as rdi


# Import more then once definitions
# * NOTE: PEP8: Use parenthesis to organize
from random import (
    uniform,
    randint as rdi
)


# Import all defitions (*)
# * NOTE: Not recommended if a few definitions will be used
from random import *


# Import own module from other directory
# * NOTE: You have to call the module from root (The directory where the app
#   was executed from)
import example._example_module as example
print(example.MESSAGE)
# Hello World


# Import for type checking only
# * To import data just to usage on type hints, the typing.TYPE_CHECKING can
#   be used.
# * NOTE: Check _typing.py file for more details
import typing
if typing.TYPE_CHECKING:
    from abc import ABC
