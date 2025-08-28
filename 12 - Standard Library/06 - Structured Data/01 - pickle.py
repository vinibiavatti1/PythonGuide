"""
Pickle

* The pickle module is used to serialize and deserialize Python objects.
* It can be used to store Python objects in files or to send them over a
  network.
* The pickle module provides the main functions below:
  * "dump" and "load": Write and read Python objects to/from files.
  * "dumps" and "loads": Write and read Python objects to/from in-memory.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import pickle


###############################################################################
# Dump Objects
###############################################################################


# Defining an Object to Persist
# * We will define an object to be persisted using the pickle module
class ObjectToPersist:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'ObjectToPersist(name={self.name}, value={self.value})'


# Persisting the Object
# * We can persist the object using the "dump" or "dumps" functions
# * The "dump" function writes the object to a file, while the "dumps" function
#   writes the object to a bytes object
# * For this example, we will use the "dumps" function to write the object
#   to a bytes object
x = ObjectToPersist('example', 42)
y = pickle.dumps(x)
print(y)
# b'\x80\x04\x95\x1c\x00\x00\x00\x...


###############################################################################
# Load Objects
###############################################################################


# Loading the Object
# * We can load the object using the "load" or "loads" functions
# * The "load" function reads the object from a file, while the "loads"
#   function reads the object from a bytes object.
# * The "loads" function will be used to read the object from the bytes object
x = pickle.loads(y)
print(x)
# ObjectToPersist(name=example, value=42)
