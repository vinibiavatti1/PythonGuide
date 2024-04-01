"""
Tempfile module

* The tempfile module provides functions to create and handle temporary files
"""
import tempfile as tmp


###############################################################################
# Temporary file and directories
###############################################################################


# TemporaryFile()
# * Parameters: mode='w+b', buffering=-1, encoding=None, newline=None,
#   suffix=None, prefix=None, dir=None, delete=True, *, errors=None
# * Create one temporary file to the default tempfile location. This location
#   may be different between operating systems
# * The temporary file created by TemporaryFile() will be removed automatically
#   whenever it the file is closed
# * Create a file with no visible name in the file system
# * No other program will be able to open the file
with tmp.TemporaryFile() as tmp_file:
    print(tmp_file.name)
# C:\Users\USER\AppData\Local\Temp\tmpuv24kq_2


# NamedTemporaryFile()
# * Parameters: mode='w+b', buffering=-1, encoding=None, newline=None,
#   suffix=None, prefix=None, dir=None, delete=True, *, errors=None
# * Create a file with a visible name in the file system
# * Other program will be able to open the file
# * NamedTemporaryFile() works the same as TemporaryFile()
with tmp.NamedTemporaryFile() as tmp_file:
    print(tmp_file.name)
# C:\Users\USER\AppData\Local\Temp\tmpmklc7dwr


# TemporaryDirectory()
# * Parameters: suffix=None, prefix=None, dir=None
# * Create a temporary directory
with tmp.TemporaryDirectory() as tmp_dir:
    print(tmp_dir)
# C:\Users\USER\AppData\Local\Temp\tmpyrp8soix


# TemporaryDirectory() with TemporaryFile(dir)
# Create temp file in directory
with tmp.TemporaryDirectory() as tmp_dir:
    with tmp.TemporaryFile(dir=tmp_dir) as tmp_file:
        print(tmp_file.name)
# C:\Users\USER\AppData\Local\Temp\tmpygbkpww6\tmpqiqgq027


###############################################################################
# Writing and reading
###############################################################################


# write() binary
# * Write data to temporary file
# * NOTE: The default mode for temporary file set the content to binary only
with tmp.TemporaryFile() as tmp_file:
    tmp_file.write(b'Hello World')


# write() text
# * Write data to temporary file
# * NOTE: The mode was changed to accept text data
with tmp.TemporaryFile(mode='w+t') as tmp_file:
    tmp_file.write('Hello World')


# read()
# * Read data from temporary file
with tmp.TemporaryFile() as tmp_file:
    tmp_file.write(b'Hello World')
    tmp_file.seek(0)
    content = tmp_file.read()
    print(content)
# b'Hello World'


###############################################################################
# Functions
###############################################################################


# gettempdir()
# * Get the OS temp directory that will be used to create the files
print(tmp.gettempdir())
# C:\Users\USER\AppData\Local\Temp
