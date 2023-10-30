"""
BytesIO

* BytesIO is an object to create a stream based on a binary file in-memory
* With this object, we can manipulate a binary file in memory
"""
from io import BytesIO


###############################################################################
# Creating a BytesIO object
###############################################################################


# Create in-memory bytes file
# * NOTE: The content must be a binary content
initial_content = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
f = BytesIO(initial_content)


###############################################################################
# Manipulating a BytesIO object
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
# * NOTE: The content must be a binary content
f.write(b'Some content...')


# seek()
# * Change cursor inside file
f.seek(20)


# truncate()
# * Resizes the file to the given number of bytes
f.truncate(0)
