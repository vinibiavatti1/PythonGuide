"""
OS Module

* The "os" module in Python provides a way of using operating system-dependent
  functionality like reading or writing to the file system.
* It includes functions to interact with the file system, process management,
  and environment variables.
* The "os" module is part of the Python Standard Library, so it comes
  pre-installed with Python.
* It is a powerful module that allows you to perform a wide range of tasks
  related to the operating system.
* NOTE: To perform file system paths operations, such as creating or removing
  directories/file, it is recommended to use the "pathlib" module.
"""

###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import os


###############################################################################
# System Command Line
###############################################################################


# chdir
# * The `os.chdir()` function is used to change the current working directory.
os.chdir('C:\\')
print(os.getcwd())
# C:\


# system(command)
# * The `os.system()` function is used to execute a command in the operating
#   system.
os.chdir('C:\\')
x = os.system('dir')
print(x)
# 16/03/2021 19:39 <DIR> Program Files
# 17/03/2021 17:31 <DIR> Program Files (x86)
# 14/03/2021 22:59 <DIR> Windows
# ...


# popen(cmd, mode="r", buffering=-1)
# * The `os.popen()` function is used to open a pipe to or from a command.
x = os.popen('echo test')
print(x.read())
# test


###############################################################################
# Environment Variables
###############################################################################


# Setting an Environment Variable
# * To set an environment variable, we can use the `os.environ` dictionary.
os.environ['MY_VAR'] = 'some_value'


# Getting Environment Variables
# * We can retrieve all environment variables as a dictionary using the
#   `os.environ` dictionary.
print(os.environ)
# {'Path': 'C:\\Program Files\\...', ...}


# Getting Environment Variables (by key)
# * We can get a specific environment variable using the `os.getenv()`
#   function.
# * The `os.getenv()` function takes the name of the environment variable
#   as an argument and returns its value.
x = os.getenv('Path')
print(x)
# C:\Program Files\...
