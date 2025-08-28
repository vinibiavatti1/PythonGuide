"""
Isinstance

* The `isinstance()` function returns True if the specified object is of the
  specified type, otherwise False.
* This is used to check if an object is an instance of a class or subclass.
* If the `type` parameter is a tuple, this function will return True if the
  object matches with one of the types inside the tuple.
###############################################################################
Syntax                      Description
###############################################################################
isinstance(object, type)    Check if the object is an instance of the type
isinstance(object, tuple)   Check if the object is an instance of one of the
                            types inside the tuple
###############################################################################
"""


###############################################################################
# Checking Native Types
###############################################################################


# Checking the object type
# * In the example below, we will check if the variable is of type int
x = 1
y = isinstance(x, int)
print(y)
# True


# Checking the object type (with multiple types)
# * To check if the object is an instance of one of multiple types, we can set
#   the second parameter as a tuple with the types we want to check
x1 = 'text'
x2 = 1.2
y1 = isinstance(x1, (int, str))
y2 = isinstance(x2, (int, str))
print(y1, y2)
# True, False


###############################################################################
# Checking Custom Types
###############################################################################


# Creating a custom class
# * We can use the `isinstance()` function to check if an object is an instance
#   of custom classes as well
# * In the example below, we will create a custom class
class CustomObject():
    pass


# Checking if the object is an instance of a custom class
# * Now, we will create an object of the custom class and check if it is an
#   instance of the class
x = CustomObject()
y = isinstance(x, CustomObject)
print(y)
# True
