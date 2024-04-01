"""
GC Module (Garbage Collector)

* The `gc` module is a Python module that provides some features to manipulate
  the Garbage Collector algorithm
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import gc


###############################################################################
# Module Resources
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
