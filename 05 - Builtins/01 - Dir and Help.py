"""
Dir and Help

* The functions `dir` and `help` are used to get information about some 
  resources or contexts
* The `dir` function is used to list all resources (attributes, methods, etc.) 
  of any object. If the function is called without any argument, it will list
  all resources of the current context
* The `help` function is used to get help about some resource, i.e. the 
  docstring of the resource will be printed
* Syntax:
  * dir(object = ...)
  * help(object = ...)
"""

###############################################################################
# Dir Function
###############################################################################


# Listing all resources of some object
# * The `dir` function will return a list of all resources of the object
# * It can be used to know what resources are available to be used
x = dir(int)
print(x)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', ...]


# Listing all resources of the current context
# * If no argument is given to the `dir` function, it will list all resources
#   of the current context
x = dir()
print(x)
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', ...]


###############################################################################
# Help Function
###############################################################################


# Printing information of some resource
# * The `help` function will print informations about some resource (the 
#   signature of the resource, the docstring, etc.)
# * It is used to auxiliate the developer to know how to use some resource
# * NOTE: The function will not return the documentation, instead, it will 
#   automatically print it
help(int)
"""
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  ...
"""


# Create a custom resource
# * Here we will create a custom resource to test the `help` function
# * The resource will be a simple class with a docstring
class Math:
    """
    This is a math class.
    """

    @staticmethod
    def sum(x, y):
        """
        Sum the values of x + y and return it
        """
        return x + y


# Printing the docstring of the custom resource
# * Now, we will use the `help` function to print informations about the Math 
#   class
# * Note that other implicit data is present in the documentation
help(Math)
"""
class Math(builtins.object)
 |  This is a math class.
 |
 |  Static methods defined here:
 |
 |  sum(x, y)
 |      Sum the values of x + y and return it
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
"""
