"""
Benchmark Tests

* Benchmark tests are used to measure the performance of a piece of code.
* They help identify bottlenecks and ensure that code changes do not negatively
  impact performance.
* The "timeit" module is commonly used for creating benchmark tests in Python.
* Benchmark tests can be written as unit tests by using the unittest framework.
* It is important to run benchmark tests in a controlled environment to obtain
  reliable results.
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
