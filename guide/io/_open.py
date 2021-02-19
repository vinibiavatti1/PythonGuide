"""
Open

* Open file and return a corresponding file object.
* If the file cannot be opened, an OSError is raised
* NOTE: Files dont need to be closed due GC will care it
* Syntax
  * open(file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None)
* Parameters
  * file: Path to file
  * mode: Modes to open the file
    * 'r': Read content. Raise error if file not exists (Default)
    * 'a': Append content. Creates a file if file not exists
    * 'w': Write content. Creates a file if file not exists
    * 'x': Create file. Raise error if file not exists
    * In addition you can specify if the file should be handled as binary or
      text mode
      * 't': Text mode (Default)
      * 'b': Binary mode (Used to images for example)
      * '+': Open for updating (reading and writing)
  * buffering: Used for setting buffering policy
  * encoding: The encoding format
  * errors: String specifying how to handle encoding/decoding errors
  * newline​: How newlines mode works (None, ' ', '\n', 'r', or '\r\n')
  * closefd: Must be True (Default); Used only with file descriptors
  * opener: A custom opener, must return an open file descriptor
* The default mode is 'r' (open for reading text, synonym of 'rt'). Modes 'w+'
  and 'w+b' open and truncate the file. Modes 'r+' and 'r+b' open the file with
  no truncation
"""
import os
import sys
current_path = sys.path[0]


# Open file
file_path = os.path.join(current_path, '../../resources/file_read.txt')
f = open(file_path)


# Read file
file_path = os.path.join(current_path, '../../resources/file_read.txt')
f = open(file_path)
print(f.read())
# Lorem ipsum dolor sit amet...


# Read lines
file_path = os.path.join(current_path, '../../resources/file_read.txt')
f = open(file_path)
for line in f.readlines():
    print(line, end='')
print()
# Lorem ipsum dolor sit amet...


# Append in file
file_path = os.path.join(current_path, '../../resources/file_write.txt')
f = open(file_path, 'a')
f.write('Lorem')
f.write(' ')
f.write('ipsum')
# In file: Lorem ipsum


# Write in file (The content will be overwrited)
file_path = os.path.join(current_path, '../../resources/file_write.txt')
f = open(file_path, 'w')
f.write('Lorem ipsum')
# In file: Lorem ipsum


# Read binary file
file_path = os.path.join(current_path, '../../resources/image.png')
f = open(file_path, 'rb')
print(f.read())
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR...


# Try except
try:
    open('not_exists.txt', 'r')
except OSError as e:
    print(e)
    # No such file or directory: 'not_exists.txt'


# Clear file content
file_path = os.path.join(current_path, '../../resources/file_write.txt')
f = open(file_path, 'r+')
f.truncate(0)


# Close the file after open
# * NOTE: It is not necessary because GC already close opened files
file_path = os.path.join(current_path, '../../resources/file_read.txt')
f = open(file_path)
f.close()
