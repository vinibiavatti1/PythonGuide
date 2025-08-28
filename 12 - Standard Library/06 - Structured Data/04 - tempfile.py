"""
Tempfile

* The tempfile module provides functions to create temporary files and
  directories.
* These files and directories are created in the default temporary directory
  of the operating system.
* Temporary files can be used to store data temporarily during the execution
  of a program.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import tempfile


###############################################################################
# Temp Location
###############################################################################


# Getting the temporary directory location
# * We can get the temporary directory location using the `gettempdir` function
# * This function returns the path to the default temporary directory of the
#   operating system
x = tempfile.gettempdir()
print(x)
# C:\Temp


###############################################################################
# Temp File
###############################################################################


# Creating a temporary file
# * We can create a temporary file using the `TemporaryFile` function
# * This function creates a file in the default temporary directory of the
#   operating system
# * This temporary file will not have a visible name in the file system, so the
#   file cannot be opened by other programs
# * NOTE: The file will be removed automatically when it is closed
with tempfile.TemporaryFile() as x:
    print(x.name)
# C:\Temp\tmpnjwvzofm


# Creating a temporary file (visible)
# * We can create a named temporary file using the `NamedTemporaryFile`
#   function
# * This function creates a file in the default temporary directory of the
#   operating system
# * This temporary file will have a visible name in the file system, so the
#   file can be opened by other programs
# * NOTE: The file will be removed automatically when it is closed
with tempfile.NamedTemporaryFile() as x:
    print(x.name)
# C:\Temp\tmp3x4y5z6a


# Writing and Reading binary data
# * We can write binary data to the temporary file using the `write` method
# * We can read the data from the temporary file using the `read` method
with tempfile.TemporaryFile() as x:
    x.write(b'This is a temporary file')
    x.seek(0)  # Move the cursor to the beginning of the file
    content = x.read()
    print(content)
# b'This is a temporary file'


# Writing and Reading text data
# * We can write text data to the temporary file by opening it in text mode
# * We can read the data from the temporary file using the `read` method
with tempfile.TemporaryFile(mode='w+t') as x:
    x.write('This is a temporary file in text mode')
    x.seek(0)  # Move the cursor to the beginning of the file
    content = x.read()
    print(content)
# This is a temporary file in text mode


###############################################################################
# Temp Directory
###############################################################################


# Creating a temporary directory
# * We can create a temporary directory using the `TemporaryDirectory` function
# * This function creates a directory in the default temporary directory of the
#   operating system
# * NOTE: The directory will be removed automatically when it is closed
with tempfile.TemporaryDirectory() as x:
    print(x)
# C:\Temp\tmp12345678


# Creating a temporary directory with temporary files
# * We can create temporary files inside a temporary directory by passing the
#   `dir` parameter to the `TemporaryFile` function
# * This allows us to create temporary files that are stored in a specific
#   temporary directory
with tempfile.TemporaryDirectory() as x:
    with tempfile.TemporaryFile(dir=x) as y:
        print(y.name)
# C:\Temp\tmp12345678\tmpabcdefgh
