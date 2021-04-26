"""
GC (Garbage Collector)

* The gc module is a Python module that provides some features to manipulate
  the Garbage Collector algorithm
* Python has an automated garbage collection. It has an algorithm to deallocate
  objects which are no longer needed
* Python has two ways to delete the unused objects from the memory:
  * Reference counting
  * Generational Garbage Collection
* NOTE: Only the common methods will be shown in the methods section
"""
import sys
import gc


###############################################################################
# Memory Management
###############################################################################


# Python memory management
# * Python used the concept of reference counting for memory management, that
#   mean Python use counters to check how many pointers some object has
# * When some object lose all of the pointers, the GC (Garbage Collector) of
#   Python removes this object from the heap space, allowing space in RAM
# * To check how many pointers some object have, we can use the getrefcount()
#   function from sys module
a = []
b = a
print('Result:', sys.getrefcount(a))
# Result: 3
# 1. The a itself
# 2. The b var
# 3. the variable inside the getrefcount fn


###############################################################################
# GC Algorithms
###############################################################################


# Reference counting algorithm
# * The garbage collector alrotithm runs automatically in Python execution,
#   cleaning the RAM some times
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


###############################################################################
# GC Methods
###############################################################################


# disable()
# * Disable automatic garbage collection
gc.disable()


# enable()
# * Enable automatic garbage collection
gc.enable()


# isenabled()
# * Return True if automatic collection is enabled
print(gc.isenabled())
# True


# collect(generation=2)
# * With no arguments, run a full collection
# * The optional argument generation may be an integer specifying which
#   generation to collect (from 0 to 2)
# * The number of unreachable objects found is returned
gc.collect()


# set_debug(flags)
# * Set the garbage collection debugging flags
# * Debugging information will be written to sys.stderr
gc.set_debug(gc.DEBUG_STATS)


# get_debug()
# * Return the debugging flags currently set
print(gc.get_debug())
# 1 (DEBUG_STATS)


# get_stats()
# * Return a list of three per-generation dictionaries containing collection
#   statistics since interpreter start
print(gc.get_stats())
# [{'collections': 15, 'collected': 102, 'uncollectable': 0}, {'collections':
# 1, 'collected': 0, 'uncollectable': 0}, {'collections': 1, 'collected': 1,
# 'uncollectable': 0}]


# set_threshold(threshold0[, threshold1[, threshold2]])
# * Set the garbage collection thresholds (the collection frequency)
# * Setting threshold0 to zero disables collection
# * NOTE: It is not recommended to change the default values
gc.set_threshold(700, 10, 10)


# get_count()
# * Return the current collection counts as a tuple of (count0, count1, count2)
print(gc.get_count())
# (8, 0, 0)


# get_threshold()
# * Return the current collection thresholds as a tuple of (threshold0,
#   threshold1, threshold2)
print(gc.get_threshold())
# (700, 10, 10)
