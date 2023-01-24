"""
Import/Export Modules

To use the import syntax, you have to know three concepts:
###############################################################################
Concept             Description
###############################################################################
Modules             A python file (file with ".py" extension)
Packages            A folder with python modules
Definitions         Resources inside a python module (variables, functions...)
###############################################################################

Import
* The import statement is the most common way of invoking the import machinery
  to import other modules to your code
* It is used to import names (definitions) from Python modules, like variables,
  classes and functions
* We can import specific names (definitions) from a module without importing
  the whole module using "from" keyword

###############################################################################
Syntax                                        Description
###############################################################################
import <module>                               Import whole module
import <package>.<module>                     Import whole module from package
from <package> import <module>                Import whole module from package
from <module> import <definition>             Import definitions from module
from <package>.<module> import <definition>   Import definitions from package
###############################################################################

Export
* Python does not contain a syntax to declare what will be exported from a
  Python module
* All definitions inside a Python module always can be imported
"""


###############################################################################
# import <module>
###############################################################################


# Import
# * Used to import the module as an object that contains all definitions inside
import typing


# Import with alias
# * The imported module can be referenced by an alias
import typing as tp


###############################################################################
# import <package>.<module>
###############################################################################


# Import module specifying package
# * You can define the location of the module that will be imported by
#   specifying the package that the module is located
import example.modules.example_module


# Import module specifying package with alias
# * The same alias rule can be used on this import method
import example.modules.example_module as example


###############################################################################
# from <package> import <module>
###############################################################################


# Import module from package
# * The same syntax can be used to import a whole module instead
from example.modules import example_module


# Import module from package with alias
# * The alias can be set to the imported module too
from example.modules import example_module as example


###############################################################################
# from <module> import <definition>
###############################################################################


# Import all definitions from a module
# * The "*" char can be used to represent all definitions of a module
# * If the module has defined the __all__ variable, only the names defined to
#   this variable will be imported
# * NOTE: Not recommended if you are going to use only few definitions of the
#   imported module, since it will take more memory space
from typing import *


# Import definition from module
# * To import a definition located inside a module, you can use the "from"
#   keyword to specify where the definition is located
from typing import Union


# Import definition from module with alias
# * You can specify the alias like the examples above
from typing import Union as un


###############################################################################
# from <package>.<module> import <definition>
###############################################################################


# Import all definition from module on package
# * To import all definitions from a module specifying the location of the
#   module, you can use the syntax below
# * NOTE: Not recommended if you are going to use only few definitions of the
#   imported module, since it will take more memory space
# * The example module has defined a __all__ variable, so, only the definitions
#   determined in this variable will be imported when using the "*" char.
#   For this example, only ("message" and "CustomType") will be imported. The
#   "OtherCustomType" will be ignored since it is not defined in __all__
#   variable.
from example.modules.example_module import *


# Import definition from module on package
# * To import a single definition from a module specifying the location of the
#   module, you can use the syntax below
from example.modules.example_module import message


# Import definition from module on package with alias
# * The alias can be set to the imported definition
from example.modules.example_module import message as msg


###############################################################################
# Importing Multiple Definitions
###############################################################################


# Import multiple definitions in a tuple
# * The definitions can be defined in a tuple to be imported in a single import
#   expression
from typing import (
    Any,
    Union,
    Final
)


# Import multiple definitions in a tuple with alias
# * Each imported definition can has an alias
from typing import (
    Any,
    Union as un,
    Final as fn
)


###############################################################################
# Type Checking
###############################################################################


# Import resources only for type checking
# * In some cases, we will have to import specific resources only used for the
#   static type checker. This can create a circular dependency if the import
#   is made using the common way. To control this, we can use the TYPE_CHECKING
#   variable from "typing" module to ensure that the module will only be
#   imported for the static type checker.
import typing
if typing.TYPE_CHECKING:
    from example.modules.example_module import CustomType
