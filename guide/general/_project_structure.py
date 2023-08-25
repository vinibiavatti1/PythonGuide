"""
Project Structure

* The Python project structure can be defined following the single
  responsibility concept.
* The proposal has some optional contents, like configuration files for common
  plugins, etc.
* The __init__.py file was omitted in the representation of a project
  structure for packages.
"""


###############################################################################
# Project Structure
###############################################################################


# Basic project structure example
# * Below there is a representation of a basic project structure in Python
"""
###############################################################################
Structure          Description
###############################################################################
.git               Git folder
.venv              Python environment folder
.vscode            VSCode workspace configuration folder
scripts            Scripts folder (common scripts)
|- run_tests.ps1   Script to run tests (example)
resources          Resources folder
|- image.jpg       Image file (example)
src                Sources folder
|- main.py         Main file (entry point)
|- package         Package
   |- __init__.py  Package initializer
.editorconfig      Editor config file
.gitignore         Git ignore file
README.md          Repository documentation
requirements.txt   Project PIP dependencies
pyproject.toml     Project configuration file
"""
