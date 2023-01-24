"""
Dunder (__)

* Dunder is an acronym to "Double Underscores"
* Dunder is defined by objects in Python that contains two underscores together
  in their identifier
* This nomenclature is used to avoid conflicts with simple names in python, to
  represent some special behavior to some object or to define that the object
  has the name reserved
* Example: __init__ (Constructor method name)
"""


###############################################################################
# In Code
###############################################################################


# Dunder magic method
# * Represents some special characteristics for the methods
# * The example below shows how to define a class constructor
class Person:
    def __init__(self):  # Double Underscores as prefix and suffix
        pass


# Dunder variable
# * Represents some special characteristics or reserved name for variables
# * NOTE: Check the _name.py file
print(__name__)
# __main__


# Private variable in module
# * The dunder used as prefix to variables can be used to define the access
#   modifier of this variable
__internal_variable = 106


###############################################################################
# Files/Directories
###############################################################################


# Dunder module
# * The example below is used to mark some folder as a package
""" __init__.py """


# Dunder package
# * The example below is used by Python to store cache for some package
""" src/__pycache__ """
