"""
Pass and Ellipsis (...)

* The pass keyword is used to make some empty block in Python. This operator
  does nothing.
* Empty instructions like if, class, functions, etc. without pass will raise
  an error
* The ellipsis (...) operator can also be used for the same purpose
"""
from threading import Lock


###############################################################################
# Pass
###############################################################################


# If
if 1 == 1:
    pass
else:
    pass


# While
while False:
    pass


# For
for i in range(5):
    pass


# Function
def sum(x, y):
    pass


# Class
class Client():
    pass


# try, except, finally
try:
    pass
except BaseException as e:
    pass
finally:
    pass


# With
with Lock():
    pass


###############################################################################
# Ellipsis (...)
###############################################################################


# If
if 1 == 1:
    ...
else:
    ...


# While
while False:
    ...


# For
for i in range(5):
    ...


# Function
def calc(x, y):
    ...


# Class
class Person():
    ...


# try, except, finally
try:
    ...
except BaseException as e:
    ...
finally:
    ...


# With
with Lock():
    ...
