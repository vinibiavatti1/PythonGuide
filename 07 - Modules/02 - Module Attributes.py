"""
Module Attributes

* Modules in Python contains (by default) some attributes that contains
  important information
* You can see the available attributes at current module by executing "dir()"
  function, without any argument
* These attributes are set by the Python interpreter when the code is executed
* The available module attributes are:

###############################################################################
Attribute           Description
###############################################################################
Main Attributes
__name__            Name of the module (__main__ when the module is main)
__package__         Package of the module
__file__            Path of the file
__cached__          Path to any compiled version of the code
__annotations__     Annotations defined in locals
__builtins__        Module with direct access to all builtin resources
__doc__             Docstring of the module

For Introspection (not documented)
__path__            Name of dir holding the package's __init__.py
__loader__          Loader object used by loader machinery (introspection)
__spec__            Information used by interpreter (introspection)
###############################################################################
"""


###############################################################################
# __name__
###############################################################################


# Get the name of the module
# * The __name__ attribute contains the name of the module
# * If the module is used to execute the application (used as entry point),
#   the __name__ will contain the value "__main__"
print(__name__)
# guide.modules._module_attributes


# Get the name of the module (when entry point)
# * If the module was used as the entry point (as the main module), the
#   __name__ will contain the value "__main__"
print(__name__)
# __main__


# Check if the module is main
# * To check if the module was executed as the entry point, we can use the
#   validation below. This will guarantee that the module was executed as
#   main or not.
# * It can be used to define specific logic or tests to a module that will only
#   be performed if the module is executed as the main module
if __name__ == '__main__':
    ...


###############################################################################
# __package__
###############################################################################


# Get the package of the module
# * The __package__ variable contains the package of the module
print(__package__)
# guide.modules


# Get the package of the module (when entry point)
# * If the module was executed as the main module, the __package__ variable
#   will contain the value None
print(__package__)
# None


###############################################################################
# __file__
###############################################################################


# Get the path of the module's file
# * The __file__ variable can be used to get the path of the file location of
#   the module
print(__file__)
# c:\guide\modules\_module_attributes.py


###############################################################################
# __cached__
###############################################################################


# Get the path of the compiled version of the module
# * Returns the path to the compiled version of the module (when it exists)
# * If the compiled version does not exist, the value will be None
print(__cached__)
# None


# Get the path of the compiled version of the module (when compiled)
# * When the module is compiled (.pyc extension), the variable will have the
#   value with the path to the compiled file
print(__cached__)
# C:\guide\modules\__pycache__\_module_attributes.pyc


###############################################################################
# __annotations__
###############################################################################


# Get the annotations of the module
# * Annotations are the type hints specified to the module resources
# * The __annotations__ variable contain all type hint definitions of the
#   module
# * It is used by type checkers to validate the types of the module, to create
#   a code documentation or for code analysis
# * It is a dict
value: int
print(__annotations__)
# {'value': <class 'int'>}


###############################################################################
# __builtins__
###############################################################################


# Get builtin functions and constants
# * The __builtin__ attribute contains a module with direct access to the
#   builtin resources (print, sum, all, any, ...)
print(__builtins__)
# <module 'builtins' (built-in)>


###############################################################################
# __doc__
###############################################################################


# Get the documentation (docstring) of the module
# * The documentation (aka docstring) of the module will be stored in the
#   __doc__ variable
print(__doc__)
"""
Module Attributes

* Modules in Python contains ...
"""
