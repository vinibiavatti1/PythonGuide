"""
Package

* Packages are a way of structuring Python's module namespace by using "dotted
  module names"
* For example, the module name A.B designates a submodule named B in a package
  named A
* The __init__.py files are required to make Python treat directories
  containing the file as packages
* In the simplest case, __init__.py can just be an empty file
"""


###############################################################################
# Packages
###############################################################################


# Init
# * Each python package has to have the __init__.py file to identify that the
#   folder is a Python package
"""
###############################################################################
Structure          Description
###############################################################################
project            Project root folder (Not a Python package)
|- package         Folder
   |- __init__.py  Package initializer (Turns folder into package)
"""


# Project structure with packages
# * This is an example of the Python project structure with defined packages
# * NOTE: The resources folder is not considered a package since it does not
#   have the __init__.py file to define it as a package
"""
###############################################################################
Structure              Description
###############################################################################
project                Project root folder (Not a Python package)
|- models ()           Models package
   |- __init__.py      Models package initializer
   |- ball.py          Ball module
   |- cube.py          Cube module
|- services            Services package
   |- __init__.py      Services package initializer
   |- ball_service.py  Ball service module
   |- cube_service.py  Cube service module
! - resources          Resources folder (Not a Python package)
   !- image.jpg        Image file
|- main.py             Main module (entry point)
"""


# Access the package
# * Since Python will recognize that the folders are packages, we can import
#   them as modules
# * Take a look at _import_export.py for more information about importing
#   modules
"""
from models import ball
from services import ball_service
import services.cube_service
"""
