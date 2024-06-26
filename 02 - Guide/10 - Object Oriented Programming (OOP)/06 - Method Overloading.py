"""
Method Overloading

* Method overloading is a feature that allows a class to have more than one
  method having the same name, if their argument lists are different
* It is used to create dynamic forms of methods that will be performed
  depending on the type or number of parameters that will be given for the
  method
* In Python, we can use the `functools.singledispatch` decorator to create
  overloaded methods
"""


###############################################################################
# Overloaded Methods
###############################################################################


# Importing singledispatch from functools module
# * To create overloaded methods, we can use the
#   `functools.singledispatchmethod` decorator
from functools import singledispatchmethod


# Defining a class with overloaded methods
# * Now, we are going to define a class with overloaded methods
# * The generic version of the method should be defined using the
#   `@singledispath` decorator
# * The overloaded versions of the method should be defined using the
#   `@<method_name>.register` decorator and it needs to have a different name
#   from the generic method version
class CustomClass:

    @singledispatchmethod
    def process(self, message):
        print('Default:', message)

    @process.register
    def _(self, message: int):
        print('Integer:', message)

    @process.register
    def _(self, message: float):
        print('Float:', message)


# Calling the overloaded methods
# * In the example below, the method will choose the implementation based on
#   the type of the argument
x = CustomClass()
x.process('Test')  # Will call the default implementation
x.process(1)       # Will call the integer implementation
x.process(1.0)     # Will call the float implementation
# Default: Test
# Integer: 1
# Float: 1.0
