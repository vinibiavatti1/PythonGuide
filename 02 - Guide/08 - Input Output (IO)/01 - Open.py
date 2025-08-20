"""
Open

* The `open` function is used to open a file and return a corresponding file
  object
* If the file cannot be opened, an OSError is raised
* NOTE: When a file is opened, it must be closed after use to free the
  resources. If it is not closed, it will be closed by the garbage collector,
  which is not recommended. To close a file, we can use the `close` method or
  use the `with` statement (recommended)
* Syntax
  * open(file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None)
  * Parameters
    * file: Path to file
    * mode: Modes to open the file (Check the modes table)
    * buffering: Used for setting buffering policy
    * encoding: The encoding format
    * errors: String specifying how to handle encoding/decoding errors
    * newline: How newlines mode works (None, ' ', '\n', 'r', or '\r\n')
    * closefd: Must be True (Default); Used only with file descriptors
    * opener: A custom opener, must return an open file descriptor
  * Mode Pattern: '{mode}{+}{type}'

###############################################################################
Key     Description             Truncate       Cursor         Default
###############################################################################
Modes
'r'     Reading                 No             Beginning      Default
'r+'    Reading and Writing     No             Beginning      ---
'w'     Writing                 Yes            Beginning      ---
'w+'    Reading and Writing     Yes            Beginning      ---
'a'     Appending               No             End            ---
'a+'    Reading and Appending   No             End            ---
'x'     Creation Only           ---            ---            ---
###############################################################################
Types
't'     Text mode               ---            ---            Default
'b'     Binary mode             ---            ---            ---
###############################################################################
* The default mode is 'r' (open for reading text, synonym of 'rt'). Modes 'w+'
  and 'w+b' open and truncate the file. Modes 'r+' and 'r+b' open the file with
  no truncation
* The `Path.open()` method from "pathlib" is a wrapper around the built-in
  `open()` function and provides the same functionality.
"""


###############################################################################
# Declaring Resources
###############################################################################


# Importing os and sys modules
# * We will use the pathlib to determine the file paths that will be used on
#   the examples below.
from pathlib import Path


# Defining file paths for the examples below
# * The files paths below will be used in the examples below to show how to
#   handle file operations
FILE_CREATE = Path('__resources', 'file_create.txt')
FILE_READ = Path('__resources', 'file_read.txt')
FILE_WRITE = Path('__resources', 'file_write.txt')
FILE_IMAGE = Path('__resources', 'file_image.png')


###############################################################################
# Openning and Closing a file
###############################################################################


# Open a file
# * To open a file, we can use the `open` function passing the file path as the
#   first argument.
# * Since the mode is not specified, the file will be opened in read mode ('r')
#   as default.
# * Since the 'with' statement is used, the file will be closed automatically
#   at the end of the block.
with open(FILE_READ) as file:
    pass


# Open a file (using Path)
# * The `Path.open()` method can also be used to open a file.
# * There is no difference in functionality between `open()` and `Path.open()`.
with FILE_READ.open() as file:
    pass


###############################################################################
# Creating a file
###############################################################################


# Creating a file
# * To create a file, we can use the `open` function with the 'x' mode
# * This mode is used only to create a file, and it will raise an error if the
#   file already exists
with open(FILE_CREATE, 'x') as file:
    pass


# Creating a file (with 'w' mode)
# * To create a file, we can use the `open` function with the 'w' mode
# * The 'w' mode will open the file for writing, truncating the file first
# * If the file does not exist, it will be created
# * If the file exists, the content will be cleared (truncated)
with open(FILE_CREATE, 'w') as file:
    pass


###############################################################################
# Manipulating the Cursor
###############################################################################


# Seeking cursor in a file
# * To control the cursor position in a file, we can use the `seek` method
# * The `seek` method receives the position as the first argument
# * In the example below, we are setting the cursor to the beginning of the
#   file
with open(FILE_READ) as file:
    file.seek(0)


# Telling the current cursor position
# * The `tell` method is used to get the current cursor position in the file
with open(FILE_READ) as file:
    print(file.tell())
# 0


###############################################################################
# Reading a file ('r')
###############################################################################


# Reading a file (with read)
# * To read a file, we can use the `read` method
# * This method will read the entire file content and return it as a string
with open(FILE_READ) as file:
    content = file.read()
    print(content)
# Hello World


# Reading a file (with readlines)
# * The `readlines` method reads the entire file content line by line and
#   returns it as a list of strings
with open(FILE_READ) as file:
    content = file.readlines()
    print(content)
# ['Hello World\n']


# Reading a file (with readline)
# * The `readline` method reads the file content line by line and returns it as
#   a string
with open(FILE_READ) as file:
    while True:
        content = file.readline()
        if not content:
            break
        print(content)
# Hello World


# Reading a file (in binary mode)
# * To read a file in binary mode, we can add the 'b' as suffix of 'r' mode to
#   open the file in read as binary mode
# * Note that the content will be returned as bytes
with open(FILE_IMAGE, 'rb') as file:
    content = file.read()
    print(content)
# b'Hello World\n'


###############################################################################
# Writing a file ('w' and 'a')
###############################################################################


# Writing a file
# * To write in a file, we can use the `write` method
# * The `write` method receives the content as the first argument, and writes
#   this content in the current cursor position
# * NOTE: The 'w' mode will truncate the file first
with open(FILE_WRITE, 'w') as file:
    file.write('Hello World')


# Appending in a file
# * To append content in a file, we can use the 'a' mode to open the file for
#   writing
# * On this way, we ensure that the previous content will be kept
with open(FILE_WRITE, 'a') as file:
    file.write('Hello World')


###############################################################################
# Reading and Writing a file ('+')
###############################################################################


# Reading and Writing a file ('r+' mode)
# * The '+' mode is used to open the file for reading and writing
# * The 'r+' mode will not truncate the file
with open(FILE_WRITE, 'r+') as file:
    pass


# Reading and Writing a file ('w+' mode)
# * The 'w+' mode will truncate the file first
with open(FILE_WRITE, 'w+') as file:
    pass


# Reading and Writing a file ('a+' mode)
# * The 'a+' mode will not truncate the file, and the cursor will be set to the
#   end of the file
with open(FILE_WRITE, 'a+') as file:
    pass


###############################################################################
# Handling File Errors
###############################################################################


# Reading a file that does not exist
# * When trying to open a file that does not exist, an OSError will be raised
# * To handle file errors, we can use the `try`, `except` block
try:
    with open('not_exists.txt') as file:
        pass
except OSError as err:
    print(err)
# No such file or directory: 'not_exists.txt'


# Creating a file that already exists
# * When trying to create a file that already exists, an OSError will be raised
try:
    with open(FILE_READ, 'x') as file:
        pass
except OSError as err:
    print(err)
# File exists: 'file_read.txt'


# Reading a file that is opened in write mode
# * When trying to read a file that is opened in write mode, an OSError will be
#   raised
try:
    with open(FILE_WRITE, 'w') as file:
        file.read()
except OSError as err:
    print(err)
# not readable


# Writing a file that is opened in read mode
# * When trying to write in a file that is opened in read mode, an OSError will
#   be raised
try:
    with open(FILE_READ, 'r') as file:
        file.write('Hello World')
except OSError as err:
    print(err)
# not writable
