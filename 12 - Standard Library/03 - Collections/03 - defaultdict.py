"""
Default Dict

* The defaultdict class is a subclass of the built-in dict class. It can be
  used to create dictionaries with default values for keys that don't exist.
* The defaultdict class is available in the collections module.
* It has a default_factory parameter that defines the type of the default
  value. When a key is not found, the default_factory is called to provide the
  default value.
* Syntax
  * defaultdict(default_factory [, map])
"""


###############################################################################
# Importing Resource
###############################################################################


# Importing the resource
# * We can import the resource using the import statement below
from collections import defaultdict


###############################################################################
# Creating Default Dicts
###############################################################################


# Creating an empty Default Dict (with int as default type)
# * In this case, the default type is int. It means that if a key is not found,
#   the default value will be 0 (default int value)
x = defaultdict(int)
print(x, x['invalid_key'])
# defaultdict(<class 'int'>, {}) 0


# Creating an empty Default Dict (with str as default type)
# * For this example, we used str as the default type. When a key is not found,
#   the default value will be an empty string
x = defaultdict(str)
print(x, x['invalid_key'])
# defaultdict(<class 'str'>, {}) ''


# Creating a Default Dict from a dict (with int as default type)
# * We can create a default dict from a dict using the defaultdict class
x = {'name': 'John', 'age': 50}
y = defaultdict(int, x)
print(y, y['invalid_key'])
# defaultdict(<class 'int'>, {'name': 'John', 'age': 50}) 0


# Creating a Default Dict (with a function as default type)
# * We can create a default dict using a function as the default type
# * For this scenario, when a key is not found, the function will be called to
#   provide the default value
x = defaultdict(lambda: 'Not found')
print(x, x['invalid_key'])
# defaultdict(<function <lambda> at ...>, {}) Not found


# Creating an empty Default Dict (With no default type)
# * We can create a default dict using the defaultdict class
# * When the type is not defined, the default type is None and a KeyError will
#   be raised when a key is not found
"""
x = defaultdict()
print(x, x['invalid_key'])

KeyError: 'invalid_key'
"""


###############################################################################
# Default Dicts Behavior
###############################################################################


# Defining a key when it doesn't exist
# * Default dicts creates the key if it doesn't exist after the first access
# * Note that in the example below, the key 'name' was created after the first
#   access
x = defaultdict(str)
_ = x['name']
print(x)
# defaultdict(<class 'str'>, {'name': ''})
