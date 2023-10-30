"""
Open

* Open file and return a corresponding file object.
* If the file cannot be opened, an OSError is raised
* NOTE: Files don't need to be closed due GC will care it
* Syntax
  * open(file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None)
* Parameters
  * file: Path to file
  * mode: Modes to open the file (Check the modes table)
  * buffering: Used for setting buffering policy
  * encoding: The encoding format
  * errors: String specifying how to handle encoding/decoding errors
  * newline​: How newlines mode works (None, ' ', '\n', 'r', or '\r\n')
  * closefd: Must be True (Default); Used only with file descriptors
  * opener: A custom opener, must return an open file descriptor
* NOTE: To work with directories, check _os.py file

Open Modes
###############################################################################
Key     Description
###############################################################################
Mode to open file
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists

Type to handle file (text or binary)
'b'     binary mode
't'     text mode (default)
'+'     open for updating (reading and writing)
###############################################################################
* The default mode is 'r' (open for reading text, synonym of 'rt'). Modes 'w+'
  and 'w+b' open and truncate the file. Modes 'r+' and 'r+b' open the file with
  no truncation
"""
import os
import sys


###############################################################################
# File paths
###############################################################################


CURRENT_PATH = sys.path[0]
FILE_CREATE = os.path.join(CURRENT_PATH, '../../resources/file_create.txt')
FILE_READ = os.path.join(CURRENT_PATH, '../../resources/file_read.txt')
FILE_WRITE = os.path.join(CURRENT_PATH, '../../resources/file_write.txt')
FILE_IMAGE = os.path.join(CURRENT_PATH, '../../resources/image.png')


###############################################################################
# Create and remove file
###############################################################################


# Create file
# * Creates the file with open w function
# * NOTE: For guarantee, the file is closed after creation using .close()
open(FILE_CREATE, 'w').close()
os.remove(FILE_CREATE)


###############################################################################
# Open
###############################################################################


# Open file
# * Without specify the mode, the file will be opened with 'r' mode as default
f = open(FILE_READ)


# Close file
# * NOTE: It is not necessary because GC already close opened files
f = open(FILE_READ)
f.close()


# Using with and open
# * This way, the with will close the file after use it automatically
with open(FILE_READ) as f:
    pass


###############################################################################
# Read
###############################################################################


# read()
# * Read all lines of the file
# * After read, the cursor will be set on the end of the file
f = open(FILE_READ)
print(f.read())
# Lorem ipsum dolor sit amet...


# readlines()
# * Read each line of the file
f = open(FILE_READ)
for line in f.readlines():
    print(line, end='')
print()
# Lorem ipsum dolor sit amet...


# read() in 'b' (binary) mode
# * Read file as binary adding the 'b' to the read mode
f = open(FILE_IMAGE, 'rb')
print(f.read())
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR...


###############################################################################
# Write
###############################################################################


# write() in 'w' (write) mode
# * Write in file (The content will be overwrited)
# * If the file is with mode 'w', the previous content will be cleared
f = open(FILE_WRITE, 'w')
f.write('Lorem ipsum')
# In file: Lorem ipsum


# write() in 'a' (append) mode
# * Append some content in file
# * If the file is with mode 'a', the previous content will be kept
f = open(FILE_WRITE, 'a')
f.write('Lorem')
f.write(' ')
f.write('ipsum')
# In file: Lorem ipsum


# truncate()
# * Resizes the file to the given number of bytes
# * It can be used to clear the file content
f = open(FILE_WRITE, 'r+')
f.truncate(0)  # content cleared


###############################################################################
# Cursor
###############################################################################


# seek(offset)
# * Move the cursor to position (0 - to define the cursor to the begin)
with open(FILE_READ) as f:
    f.seek(22)  # Cursor set to the 20 position
    print(f.read())
# amet, consectetur adipiscing elit...


###############################################################################
# Handling errors
###############################################################################


# Try, except
# * Use try, except to handler some open error
try:
    open('not_exists.txt', 'r')
except OSError as e:
    print(e)
    # No such file or directory: 'not_exists.txt'


# Try, except, with
# * Use try, except to handler some open error
try:
    with open('not_exists.txt', 'r') as f:
        pass
except OSError as e:
    print(e)
    # No such file or directory: 'not_exists.txt'
