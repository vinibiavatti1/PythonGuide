"""
Garbage Collector (GC)

* Python has an automated garbage collection, i.e. it has an algorithm to
  deallocate objects which are no longer needed
* Python has two ways to delete unused objects from the memory:
  * Reference counting
  * Generational Garbage Collection
* The `gc` module is a Python module that provides some features to manipulate
  the Garbage Collector algorithm
"""


###############################################################################
# Memory Management
###############################################################################


# Importing the `sys` module
# * We will need some `sys` module functions to demonstrate the GC process
import sys


# Python memory management
# * Python uses the concept of reference counting for memory management, which
#   means that it uses counters to check how many pointers some object has
# * When some object lose all of the pointers, the GC (Garbage Collector) of
#   Python removes this object from the heap space, allowing space in RAM
# * To check how many pointers some object have, we can use the getrefcount()
#   function from `sys` module
a = []
b = a
print('Result:', sys.getrefcount(a))
# Result: 3
# 1. The a itself
# 2. The b var
# 3. the variable inside the getrefcount fn


# Reference counting algorithm
# * The garbage collector alrotithm runs automatically in Python execution,
#   cleaning the RAM sometimes
# * The algorithm checks the reference count of the object, and if it has zero
#   pointers, it is deleated from heap space
a = []
b = 1
a = 1  # The array will be collected by reference counting algorithm


# Generational garbage collection algorithm
# * Used to handle cyclic references (An object has a reference for itself). In
#   this situation, the reference count will not be zero, and the GC will not
#   collect this using the Referect counting algorithm
# * If Python executes a garbage collection process on a generation and an
#   object survives, it moves up into a second, older generation
# * There are three generation layers
# * For each generation, the garbage collector module has a threshold number of
#   objects
# * If the number of objects exceeds that threshold, the garbage collector will
#   trigger a collection process. For any objects that survive that process,
#   they're moved into an older generation
a = []
a.append(a)
del a  # The object will be collected by generational algorithm
