"""
Isinstance

* The isinstance() function returns True if the specified object is of the
  specified type, otherwise False.
* If the type parameter is a tuple, this function will return True
* If the object is one of the types in the tuple.

Formats: isinstance(object, type)
         isinstance(object, tuple)
"""


# Int
x = 1
print(isinstance(x, int))    # True
print(isinstance(x, float))  # False


# Str
x = 'text'
print(isinstance(x, (int, str, float)))  # True
print(isinstance(x, (int, float)))       # False


# Class
class Client():
    pass


client = Client()
print(isinstance(client, Client))  # True
print(isinstance(client, str))     # False
