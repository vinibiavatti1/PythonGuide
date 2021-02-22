"""
Modules

* Consider a module to be the same as a code library
* A file containing a set of functions you want to include in your application
* To create a module just save the code you want in a file with the file
  extension .py
* Use import keyword to import a module
* You can create an alias when you import a module, by using the as keyword
* You can choose to import only parts from a module, by using the from keyword
"""


# Import module
import sys
print(sys.path[0])
# c:\PythonGuide\guide\syntax


# Import module with alias
import platform as plt
print(plt.platform())
# Windows-10-10.0.19041-SP0


# Import only parts from module
from math import pi
print(pi)
# 3.141592653589793
