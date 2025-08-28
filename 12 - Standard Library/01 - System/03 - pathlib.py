"""
Path Lib

* The `pathlib` module is a part of the standard library in Python.
* It provides an object-oriented interface for working with file system paths.
* The `Path` class is the main class in the `pathlib` module.
* It represents a filesystem path and provides methods for common path
  operations.
* The `pathlib` module is cross-platform and works on Windows, macOS, and
  Linux.
* It is recommended to use `pathlib` instead of `os.path` for new code.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows.
# * Note that we are importing the `Path` class from the `pathlib` module since
#   all operations are performed using this class.
from pathlib import Path


###############################################################################
# Defining and Joining Paths
###############################################################################


# Defining Paths
# * To define a path, we can use the constructor of the Path class.
x = Path('C:/', 'Windows', 'System32')
print(x)
# C:\Windows\System32


# Defining Paths (Current Dir)
# * When creating a Path object, it is relative to the current working
#   directory '.'.
x = Path()
print(x)
# .


# Joining Paths
# * The pathlib module supports the division operator (/) to join paths.
# * This makes it easy to construct paths in a platform-independent way.
x = Path('C:/')
y = x / 'Windows' / 'System32'
print(y)
# C:\Windows\System32


###############################################################################
# Expanding and Resolving Paths
###############################################################################


# cwd() (Absolute Current Dir)
# * To get the current directory, we can use the `Path.cwd()` method.
# * NOTE: The current directory is the directory from which the script is run.
x = Path.cwd()
print(x)
# C:\Git\PythonGuide


# home()
# * To get the home directory, we can use the `Path.home()` method.
x = Path.home()
print(x)
# C:\Users\Username


# absolute()
# * To get the absolute path, we can use the `Path.absolute()` method.
# * Note that the path was resolved with the real filesystem path.
x = Path('.')
y = x.absolute()
print(y)
# C:\Git\PythonGuide


###############################################################################
# Querying File Type and Status
###############################################################################


# stat()
# * The `Path.stat()` method is used to get the status of a file or directory.
# * It returns informations like file size, modification time, and more.
x = Path('pyproject.toml')
y = x.stat()
print(y)
# os.stat_result(st_mode=33206, st_ino=1125899907484026, ...


# exists()
# * The `Path.exists()` method checks if a file or directory exists.
x = Path('pyproject.toml')
y = x.exists()
print(x)
# True


# is_file()
# * The `Path.is_file()` method checks if the path is a file.
x = Path('pyproject.toml')
y = x.is_file()
print(y)
# True


# is_dir()
# * The `Path.is_dir()` method checks if the path is a directory.
x = Path('pyproject.toml')
y = x.is_dir()
print(y)
# False


# samefile()
# * The `Path.samefile()` method checks if two paths refer to the same file.
x = Path('pyproject.toml')
y = Path('pyproject.toml')
z = Path('README.md')
print(x.samefile(y))
print(x.samefile(z))
# True
# False


x.is_absolute()


###############################################################################
# Reading and Writing Files
###############################################################################


# open
# * The `Path.open()` method is used to open a file.
# * It returns a file object that can be used to read or write the file.
# * This is the same of built-in `open()` function.
x = Path('__resources', 'file_read.txt')
y = x.open('r')
print(y)
# <_io.TextIOWrapper name='pyproject.toml' mode='r' encoding='UTF-8'>


# read_text
# * The `Path.read_text()` method is used to read the contents of a text file.
# * It returns the contents of the file as a string.
x = Path('__resources', 'file_read.txt')
y = x.read_text()
print(y)
# Lorem ipsum dolor sit amet...

# read_bytes
# * The `Path.read_bytes()` method is used to read the contents of a binary
#   file.
# * It returns the contents of the file as bytes.
x = Path('__resources', 'python_data.dat')
y = x.read_bytes()
print(y)
# b'\x80\x04\x955\x00\x00\x00\x00\x00\x00\x00...


# write_text
# * The `Path.write_text()` method is used to write text to a file.
# * It creates the file if it does not exist.
x = Path('__resources', 'file_write.txt')
x.write_text('Hello, World!')
print(x.read_text())
# Hello, World!


# write_bytes
# * The `Path.write_bytes()` method is used to write bytes to a file.
# * It creates the file if it does not exist.
x = Path('__resources', 'file_write.txt')
x.write_bytes(b'\x80\x04\x95\x00\x00\x00\x00\x00\x00\x00')
y = x.read_bytes()
print(y)
# b'\x80\x04\x95\x00\x00\x00\x00\x00\x00\x00'


###############################################################################
# Reading Directories
###############################################################################


# walk
# * The `Path.walk()` method is used to iterate over all files and directories
#   in a directory tree.
# * It yields a tuple (root, dirs, files) for each directory in the tree.
# * Note that this method is recursive, i.e., it will traverse all
#   subdirectories.
x = Path('__resources')
for root, dirs, files in x.walk():
    print(root, dirs, files)
# __resources ['example_dir'] ['bricks.bmp', 'bricks.png', ...]
# __resources\example_dir [] ['file.txt']


###############################################################################
# Creating Files and Directories
###############################################################################


# touch
# * The `Path.touch()` method is used to create a new file or update the
#   timestamp of an existing file.
x = Path('__resources', 'file_touch.txt')
x.touch()
print(x.exists())
# True


# mkdir
# * The `Path.mkdir()` method is used to create a new directory.
x = Path('__resources', 'new_directory')
x.mkdir()
print(x.exists())
# True


###############################################################################
# Renaming and Deleting
###############################################################################


# rename
# * The `Path.rename()` method is used to rename a file or directory.
x = Path('__resources', 'file_touch.txt')
y = Path('__resources', 'file_renamed.txt')
z = x.rename(y)
print(z.exists())
# True


# replace
# * The `Path.replace()` method is used to replace a file or directory.
x = Path('__resources', 'file_renamed.txt')
y = Path('__resources', 'new_directory', 'file_renamed.txt')
z = x.replace(y)
print(z.exists())
# True


# unlink
# * The `Path.unlink()` method is used to delete a file.
x = Path('__resources', 'new_directory', 'file_renamed.txt')
x.unlink()
print(x.exists())
# False


# rmdir
# * The `Path.rmdir()` method is used to remove an empty directory.
x = Path('__resources', 'new_directory')
x.rmdir()
print(x.exists())
# False
