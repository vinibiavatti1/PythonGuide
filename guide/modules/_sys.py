"""
Sys module

* The sys module provides functions and variables used to manipulate different
  parts of the Python runtime environment
"""
import sys


# argv
# * Returns a list of command line arguments passed to a Python script
print(sys.argv)
# ['c:/git/PythonGuide/guide/modules/_sys.py']


# maxsize
# * Returns the largest integer a variable can take
print(sys.maxsize)
# 9223372036854775807


# path
# * This is an environment variable that is a search path for all Python
#   modules
# * As initialized upon program startup, the first item of this list, path[0],
#   is the directory containing the script that was used to invoke the Python
#   interpreter
print(sys.path)
# ['c:\\git\\PythonGuide\\guide\\modules', ...]


# version
# * This attribute displays a string containing the version number of the
#   current Python interpreter
print(sys.version)
# 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55)
# [MSC v.1928 64 bit (AMD64)]


# exit(arg)
# * This causes the script to exit back to either the Python console or the
#   command prompt
# * This is generally used to safely exit from the program in case of
#   generation of an exception
sys.exit('Some error ocurred!')
