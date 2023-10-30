"""
StringIO

* StringIO is an object to create a stream based on a file in-memory
* With this object, we can manipulate a file in memory
"""
from io import StringIO


###############################################################################
# Creating a StringIO file
###############################################################################


# Creating a in-memory string file
initial_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
f = StringIO(initial_content)


###############################################################################
# Manipulating a StringIO file
###############################################################################


# read()
# * Read content from file
print(f.read())
# Lorem ipsum dolor...


# readlines()
# * Read each line of the file
lines = f.readlines()
for line in lines:
    print(line)
# Lorem ipsum dolor...


# write()
# * Writing content in file
f.write('Some content...')


# seek()
# * Change cursor inside file
f.seek(20)


# truncate()
# * Resizes the file to the given number of bytes
f.truncate(0)
