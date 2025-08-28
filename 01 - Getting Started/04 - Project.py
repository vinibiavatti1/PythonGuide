"""
Project

* To create a Python project, we can simply create a new directory and add our
  Python files there.
* The project structure can be organized into packages and modules for better
  maintainability and scalability. This allows for a clear separation of
  concerns and makes it easier to manage dependencies and functionality.
* This document demonstrates the proposed project structure and best practices
  for organizing Python projects.
"""


###############################################################################
# Project Structure
###############################################################################


# Standard Project Structure
# * The structure below represents a standard project structure in Python.
# * It is designed to be simple and easy to understand, while also being
#   flexible enough to accommodate the needs of most projects.
# * Usually, a python project will contain more files and folders (i.e. .git,
#   .vscode, .editorconfig, etc.). We are only including the essential files
#   and folders in this representation.
"""
###############################################################################
Structure             Description
###############################################################################
project               Project root folder
|- .venv              Virtual environment folder
|- app                Sources folder
   |- main.py         Main module (entry point)
   |- package         Package
      |- __init__.py  Package initializer
|- requirements.txt   Project PIP dependencies
|- pyproject.toml     Project configuration file
###############################################################################
"""


# Packages
# * Packages are a way to organize related modules into a single namespace.
# * A package is simply a directory that contains a special file named
#   __init__.py
# * The __init__.py file can be empty, or it can contain valid Python code
#   that initializes the package.
# * Python will only recognize a directory as a package if it contains an
#   __init__.py file.
"""
###############################################################################
Structure          Description
###############################################################################
project            Project root folder (Not a Python package)
|- package1        Folder (Package)
   |- __init__.py  Package initializer (Turns folder into package)
   |- module.py    Module
|- package2        Folder (Not a package)
   |- module.py    Module (Cannot be imported)
###############################################################################
"""


# Packages Example
# * This is an example of the Python project structure with defined packages
# * NOTE: The resources folder is not considered a package since it does not
#   have the __init__.py file to define it as a package
"""
###############################################################################
Structure                  Description
###############################################################################
project                    Project root folder (Not a Python package)
|- models                  Models package
   |- __init__.py          Models package initializer
   |- user.py              User module
   |- customer.py          Customer module
|- services                Services package
   |- __init__.py          Services package initializer
   |- user_service.py      User service module
   |- customer_service.py  Customer service module
|- resources              Resources folder (Not a Python package)
   |- image.jpg            Image file
|- main.py                 Main module (entry point)
###############################################################################
"""


###############################################################################
# Editor Config
###############################################################################


# Enabling Editor Config
# * Editor config is a plugin that auto-configure your IDE based on
#   .editorconfig file.
# * It is recommended to keep consistence between the projects and to help
# * new developers to configure their IDE.
# * To configure the EditorConfig in your project:
#   1. Install the "editorconfig" extension
#   2. In your project, create a file named .editorconfig
#   3. Put the content bellow in the file: (This is the standard configuration)
"""
root = true

[*]
indent_style = space
indent_size = 4
insert_final_newline = true
trim_trailing_whitespace = true
end_of_line = lf
charset = utf-8

[*.py]
max_line_length = 79

[*.md]
trim_trailing_whitespace = false
"""
