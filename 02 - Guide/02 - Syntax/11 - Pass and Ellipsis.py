"""
Pass and Ellipsis (...)

* The pass keyword and the ellipsis are used to define an empty block in Python
* These instructions doesn't do anything, only are used to correct the syntax
  for the Python interpreter
* Empty instructions like if, class, functions, etc. without pass will raise
  an error

###############################################################################
Instruction         Description
###############################################################################
pass                Define an empty block (that contains nothing)
...                 Define an empty block (that contains something)
###############################################################################
"""


###############################################################################
# Pass
###############################################################################


# If
# * Define an empty block to condition
if 1 == 1:
    pass
else:
    pass


# While
# * Define an empty block to loop
while False:
    pass


# For
# * Define an empty block to loop (iteration)
for i in range(5):
    pass


# Function
# * Define an empty block to a function
def sum(x, y):
    pass


# Class
# * Define an empty block to a class
class Client():
    pass


# try, except, finally
# * Define an empty block to try, except, finally
try:
    pass
except BaseException as e:
    pass
finally:
    pass


# With
# * Define an empty block to with instruction
with True:
    pass


###############################################################################
# Ellipsis (...)
###############################################################################


# If
# * Define an empty block to condition
if 1 == 1:
    ...
else:
    ...


# While
# * Define an empty block to loop
while False:
    ...


# For
# * Define an empty block to loop (iteration)
for i in range(5):
    ...


# Function
# * Define an empty block to a function
def calc(x, y):
    ...


# Class
# * Define an empty block to a class
class Person():
    ...


# try, except, finally
# * Define an empty block to try, except, finally
try:
    ...
except BaseException as e:
    ...
finally:
    ...


# With
# * Define an empty block to with instruction
with True:
    ...
