"""
GIL (Global Interpreter Lock)

* The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a
  lock) that allows only one thread to hold the control of the Python
  interpreter
* This means that only one thread can be in a state of execution at any point
  in time
* Python uses reference counting for memory management by GC (Gabage Collector)
  To prevent concurrency problems with the reference counting,
  Python allows just one thread to be ran
* Adding locks to prevent concurrency problems can solve the problem, but it
  will be able to geenrate some deadlocks, and it will impact in performance
* The most popular way to prevent GIL is to use a multi-processing approach
  where you use multiple processes instead of threads. Each Python process gets
  its own Python interpreter and memory space so the GIL won't be a problem.
  Python has a multiprocessing module which lets us create processes easily
* NOTE: Check the _gc.py file for more details of GC
* NOTE: Check the _gc.py for Garbage Collector details
* Reference: https://realpython.com/python-gil/
"""
import sys
import threading
import multiprocessing
import time


###############################################################################
# Operation
###############################################################################


# Operation
# * This is an operation that takes a little time to be finished and it will be
#   used in the tests with single-thread, multi-thread and multi-processing
def operation(n):
    return [x for x in range(n)]


###############################################################################
# Single-thread
###############################################################################


# Single-thread
# * The execution time will be calculated in single thread program
if __name__ == '__main__':
    start = time.time()
    operation(100_000_000)
    end = time.time()
    print('Seconds:', end - start)
# Seconds: 4.4968931674957275


###############################################################################
# Multi-thread
###############################################################################


# Multi-thread
# * The execution time will be calculated using threads
# * NOTE: This tooks almost the same time of single thread because the GIL
if __name__ == '__main__':
    thread1 = threading.Thread(target=operation, args=(50_000_000,))
    thread2 = threading.Thread(target=operation, args=(50_000_000,))
    start = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end = time.time()
    print('Seconds:', end - start)
# Seconds: 4.522751092910767


###############################################################################
# Multi-processing
###############################################################################


# Multi-processing
# * Using multi processing, other Python interpreter will execute the operation
# * The GIL will not be considered in this situation, since it is executing as
#   a process, not thread
# * NOTE: Check _multiprocessing.py file for more details
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=operation, args=(50_000_000,))
    process2 = multiprocessing.Process(target=operation, args=(50_000_000,))
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    print('Seconds:', end - start)
# Seconds: 2.945467948913574
