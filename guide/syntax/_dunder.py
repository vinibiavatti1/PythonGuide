"""
Dunder

* Dunder means "Double Under (Underscores)"
* Dunder in Python are objects having two prefix and suffix underscores in the
  object name, like: __example__
* This nomenclature is used to avoid conflicts with simple names in python, or
  to represent some special behavior to some object
"""


# Dunder magic method
# * Represents some special characteristics for the methods
class Person:
    def __init__(self):  # Double Under (Underscores) as prefix and suffix
        pass


# Dunder variable
# * Represents some special characteristics for variables or avoid conflicts
# * NOTE: Check the _name.py file
print(__name__)
# __main__


# Dunder module
# * The example below is used to mark some folder as a package
""" __init__.py """


# Dunder package
# * The example below is used by Python to store cache for some package
""" src/__pycache__ """
