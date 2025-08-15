"""
Json

* The json module is a built-in Python library that provides functions to
  work with JSON (JavaScript Object Notation) data
* It allows you to parse JSON strings, convert Python objects to JSON format,
  and read/write JSON data to/from files
* NOTE that different from the pickle module, the json module don't store the
  type of the object, so it is not possible to restore the object to its
  original type after loading it from JSON. The loaded object will be always a
  dictionary or a list, depending on the JSON structure.
* The json module provides the main functions below:
  * "dump" and "load": Write and read Python objects to/from files.
  * "dumps" and "loads": Write and read Python objects to/from in-memory.
* The table below maps the common Python data types to their JSON equivalents:
###############################################################################
Python	          JSON Equivalent
###############################################################################
dict	          object
list, tuple	      array
str	              string
int, float, int	  number
True	          true
False	          false
None	          null
###############################################################################
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import json


###############################################################################
# Dump Objects
###############################################################################


# Persisting an Object
# * We can persist a python object (dict, list, etc...) using the "dump" or
#   "dumps" functions
# * The "dump" function writes the object to a file, while the "dumps" function
#   writes the object to a string
# * For this example, we will use the "dumps" function to write the object
#   to a string
x = {
    "name": "example",
    "value": [1, 2, 3]
}
y = json.dumps(x)
print(y)
# {"name": "example", "value": [1, 2, 3]}


###############################################################################
# Load Objects
###############################################################################


# Loading a Object
# * We can load the object using the "load" or "loads" functions
# * The "load" function reads the object from a file, while the "loads"
#   function reads the object from a string.
# * The "loads" function will be used to read the object from the string above
x = json.loads(y)
print(x, type(x))
# {'name': 'example', 'value': [1, 2, 3]}
# <class 'dict'>
