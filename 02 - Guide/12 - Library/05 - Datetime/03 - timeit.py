"""
Timeit

* This module provides a simple way to measure the execution time of small code
  snippets.
* It can be used to measure the execution time of a statement or a function.
* The timeit module avoids a number of common traps for measuring execution
  times.
* The command "python -m timeit module.py" can be used to run the timeit
  module on a specific Python file.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import timeit


###############################################################################
# Timeit
###############################################################################


# Measuring execution time
# * The timeit function will return the execution time (seconds) of the
#   statement passed as an argument
# * NOTE: The default number of times is 1000000
x = '"-".join(str(n) for n in range(10))'
y = timeit.timeit(x)
print(y)
# 2.2554848


# Measuring execution time (custom number of times)
# * We can specify the number of times to execute the statement using the
#   `number` argument
# * The default number of times is 1000000
x = '"-".join(str(n) for n in range(100))'
y = timeit.timeit(x, number=100)
print(y)
# 0.002292100000000019
