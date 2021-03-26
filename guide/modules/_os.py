"""
OS module

* The OS module in Python provides functions for creating and removing a
  directory (folder), fetching its contents, changing and identifying the
  current directory, execute OS commands, get OS information, etc
"""
import os


###############################################################################
# OS attributes
# * NOTE: You can use platform module (_platform.py file) to get more info from
#   operating system
###############################################################################


# name
# * Gives the name of the operating system dependent module imported
print(os.name)
# nt


# linesep
# * Gives the line separator of OS
print(os.linesep)
# \r\n


###############################################################################
# Path commands
###############################################################################


# getcwd()
# * Getting Current Working Directory
print(os.getcwd())
# C:\git\PythonGuide


# mkdir(path, mode=511, dir_fd=None)
# * Creating a directory
# * NOTE: It is not recusive (Check makedirs())
os.mkdir('C:\\pg_test')


# makedirs(name, mode=0o777, exist_ok=False)
# * Creating a directory recursively
os.makedirs('C:\\pg_test\\python\\directory\\example')


# chdir(path)
# * Changing the Current Working Directory
os.chdir('C:\\pg_test')
print(os.getcwd())


# remove(path)
# * remove or delete a file path
# * This method can not remove or delete a directory
open('C:\\pg_test\\pg_file.txt', 'w')
os.remove('C:\\pg_test\\pg_file.txt')


# rmdir(path, dir_fd=None)
# * Removing a Directory
os.chdir('C:\\')
os.rmdir('C:\\pg_test\\python\\directory\\example')
os.rmdir('C:\\pg_test\\python\\directory')
os.rmdir('C:\\pg_test\\python')


# listdir()
# * List Files and Sub-directories
os.chdir('C:\\')
print(os.listdir())
# ['Windows', 'Program Files (x86)', 'Users', ...]


# rename(src, dst, src_dir_fd=None, dst_dir_fd=None)
# * Rename a file name
# NOTE: If a new directory is specified, the file will be moved
open('C:\\pg_test\\pg_file.txt', 'w')
os.rename('C:\\pg_test\\pg_file.txt', 'C:\\pg_test\\pg_other.txt')


# path.isdir(path)
# * Check if the path is a directory
print(os.path.isdir('C:\\pg_test'))
# True


# path.isfile(path)
# * Check if the path is a file
print(os.path.isfile('C:\\pg_test'))
# False


# path.isabs(path)
# * Check if the path is absolute
print(os.path.isabs('C:\\pg_test'))
# True


# path.join(path)
# * Join one or more path components intelligently (using the correct path
#   separator from the OS)
print(os.path.join(os.getcwd(), 'folder', 'file.txt'))
# C:\folder\file.txt


###############################################################################
# Execute OS command
###############################################################################


# system(command)
# * Execute some command in OS
os.chdir('C:\\')
result = os.system('dir')
print(result)
# 16/03/2021  19:39    <DIR>          Program Files
# 17/03/2021  17:31    <DIR>          Program Files (x86)
# 14/03/2021  22:59    <DIR>          Windows
# ...


# popen(cmd, mode="r", buffering=-1)
# Execute a command in OS and open a stream
stream = os.popen('echo test')
print(stream.read())
# test


###############################################################################
# Remove examples
###############################################################################


# Remove the examples used above
os.remove('C:\\pg_test\\pg_other.txt')
os.rmdir('C:\\pg_test')
