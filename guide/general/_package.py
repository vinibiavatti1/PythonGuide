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
project                             #  Project root
|- project                          #  Folder
   |- __init__.py                   #  Project package initializer
"""


# Project structure with packages
# * This is an example of the Python project structure with defined packages
"""
project                             #  Project root
|- project
   |- __init__.py                   #  Project package initializer
   |- models
      |- __init__.py                #  Models package initializer
      |- client.py
      |- person.py
   |- services
      |- __init__.py                #  Services package initializer
      |- client_service.py
      |- person_service.py
   |- repositories
      |- __init__.py                #  Repositores package initializer
      |- client_repository.py
      |- person_repository.py
   |- routes
      |- __init__.py                #  Routes package initializer
      |- client_route.py
      |- person_route.py
|- main.py                          #  Entry point
"""


# Access the package
# * The package can be accessed from the root package
# * For example:
"""
import project.models.client.Client
# or
from project.models.client import Client
"""
