"""
Timeit

* Module used to check the time for some Python operations
* This module evaluates the code to check the execution time
"""
import timeit


###############################################################################
# Timeit
###############################################################################


# Check time for statement
# * The timeit function will return the execution time (seconds) of the
#   statement by a number of times
# * NOTE: The default number of times is 1000000
stmt = '"-".join(str(n) for n in range(10))'
time = timeit.timeit(stmt)
print(time)
# 2.2554848


# Check time for statement by a number of times
# * The number of times was changed to 100
stmt = '"-".join(str(n) for n in range(100))'
time = timeit.timeit(stmt, number=100)
print(time)
# 0.002292100000000019
