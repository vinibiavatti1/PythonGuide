"""
String IO

* The `StringIO` object represents a file in memory, which can be used to read
  or write strings
* It implements an in-memory file-like object
"""


###############################################################################
# Creating a File
###############################################################################


# Importing StringIO
# * To create a StringIO file, you need to import the `StringIO` class from the
#   `io` module
from io import StringIO


# Creating a StringIO file (in-memory string file)
# * We can pass a string to the `StringIO` constructor to create a file with
#   that content
x = StringIO('Hello World')


###############################################################################
# Manipulating the Cursor
###############################################################################


# Seeking cursor in StringIO file
# * The `seek` method is used to change the cursor position in the file
# * In the example below, we are setting the cursor to the beginning of the
#   file
x.seek(0)


# Telling the current cursor position in StringIO file
# * The `tell` method is used to get the current cursor position in the file
y = x.tell()
print(y)
# 0


###############################################################################
# Reading Content
###############################################################################


# Reading content from StringIO file (with getvalue)
# * The `getvalue` method is used to read all of content from the file,
#   ignoring the cursor position
y = x.getvalue()
print(y)
# Hello World


# Reading content from StringIO file (with read)
# * The `read` method is used to read content from the file, although it reads
#   based on the cursor position
y = x.read()
print(y)
# Hello World


# Reading content from StringIO file (with readlines)
# * The `readlines` method is used to read each line of the file
# * It returns a list of strings, where each string is a line of the file
# * The `hint` parameter can be used to specify the number of bytes to read
x.seek(0)
y = x.readlines()
print(y)
# ['Hello World']


# Reading content from StringIO file (with readline)
# * In this case, we have to iterate over the lines to get the content
x.seek(0)
while True:
    y = x.readline()
    if not y:
        break
    print(y)
# Hello World


###############################################################################
# Writing Content
###############################################################################


# Writing content in StringIO file
# * The `write` method is used to write content in the file
x.write('Other content...')


# Truncating content in StringIO file
# * The `truncate` method is used to resize the file to the given number of
#   bytes
# * In the example below, we are truncating the file to 0 bytes (empty file)
x.truncate(0)
