"""
Bytes IO

* The `BytesIO` object represents a binary file in memory, which can be used to
  read or write binary data
* It implements an in-memory file-like object
"""


###############################################################################
# Creating a File
###############################################################################


# Importing BytesIO
# * To create a BytesIO file, you need to import the `BytesIO` class from the
#   `io` module
from io import BytesIO


# Creating a BytesIO file (in-memory string file)
# * We can pass a binary data to the `BytesIO` constructor to create a file
#   with that content
# * Note that we are passing a binary string (b'Hello World') instead of a
#   regular string ('Hello World')
x = BytesIO(b'Hello World')


###############################################################################
# Manipulating the Cursor
###############################################################################


# Seeking cursor in BytesIO file
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


# Reading content from BytesIO file (with getvalue)
# * The `getvalue` method is used to read all of content from the file,
#   ignoring the cursor position
y = x.getvalue()
print(y)
# b'Hello World'


# Reading content from BytesIO file (with read)
# * The `read` method is used to read content from the file, although it reads
#   based on the cursor position
y = x.read()
print(y)
# b'Hello World'


# Reading content from BytesIO file (with readlines)
# * The `readlines` method is used to read each line of the file
# * It returns a list of strings, where each string is a line of the file
# * The `hint` parameter can be used to specify the number of bytes to read
x.seek(0)
y = x.readlines()
print(y)
# [b'Hello World']


# Reading content from BytesIO file (with readline)
# * In this case, we have to iterate over the lines to get the content
x.seek(0)
while True:
    y = x.readline()
    if not y:
        break
    print(y)
# b'Hello World'


###############################################################################
# Writing Content
###############################################################################


# Writing content in BytesIO file
# * The `write` method is used to write content in the file
x.write(b'Other content...')


# Truncating content in BytesIO file
# * The `truncate` method is used to resize the file to the given number of
#   bytes
# * In the example below, we are truncating the file to 0 bytes (empty file)
x.truncate(0)
