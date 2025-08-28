"""
Multi Processing

* The "multiprocessing" module allows you to create multiple processes, each
  with its own Python interpreter and memory space.
* This can be useful for CPU-bound tasks that need to take advantage of
  multiple cores.
* Different from threading, each process has its own memory space and runs
  truly in parallel.
* Since it creates a new process, it can be more resource-intensive than
  threading.

Important Note
* Note that all running examples below this point will use the
  `if __name__ == '__main__':` guard to ensure proper behavior on Windows. This
  is necessary because, on Windows, the fork system call is not supported,
  and the multiprocessing module needs to import the main module in a new
  process, and the `if __name__ == '__main__':` guard prevents the code from
  being run again and creating an infinite loop.
* In other platforms that support the fork system call (like Linux and macOS),
  this guard is not strictly necessary, but it's still a good practice to
  include it to avoid potential issues.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import multiprocessing


###############################################################################
# Function Process
###############################################################################


# Defining a function
# * We can start processes based on functions.
# * Below, we will define a function that will be run in a separate process.
def fn():
    print("Process is running")


# Using the function in a process
# * We can create a process by instantiating the Process class and passing the
#   function as the target.
# * When the process is created, it can be started using the `start()` method.
if __name__ == '__main__':
    process = multiprocessing.Process(target=fn)
    process.start()
# Process is running


# Defining a function (with parameters)
# * We can also start processes using function with parameters.
# * Below, we will define a function that takes parameters.
def fn(param1, param2):
    print(f"Process is running with parameters: {param1}, {param2}")


# Using the function in a process (with parameters)
# * When setting the process' target to a function with parameters, we can use
#   the `args` argument to pass the parameters as a tuple.
if __name__ == '__main__':
    process = multiprocessing.Process(target=fn, args=("value1", "value2"))
    process.start()
# Process is running with parameters: value1, value2


###############################################################################
# Process Subclass
###############################################################################


# Defining a process subclass
# * We can define a subclass of the Process class and override the run()
#   method.
# * This is useful when we want to encapsulate process behavior within a class.
class MyProcess(multiprocessing.Process):
    def run(self):
        print("Process is running")


# Running the process class
# * To start the process, we need to create an instance of the MyProcess class
#   and call the start() method.
if __name__ == '__main__':
    process = MyProcess()
    process.start()
# Process is running


###############################################################################
# Daemon Processes
###############################################################################


# Defining a function
# * We will define a function that will be run in the process below.
def fn():
    print("Daemon process is running")


# Defining a Daemon Process
# * A daemon process is a process that runs in the background and is
#   terminated when the main program exits.
# * Daemon processes are useful for tasks that should not block the
#   program from exiting, such as background tasks or services.
# * To define a daemon process, we can set the `daemon` attribute to `True`
if __name__ == '__main__':
    process = multiprocessing.Process(target=fn)
    process.daemon = True
    process.start()
# Daemon process is running


###############################################################################
# Joining Processes
###############################################################################


# Defining a function
# * We will define a function that will be run in the process below.
def fn():
    print("Process is running")


# Joining Processes
# * We can use the `join()` method to wait for a process to finish.
# * This is useful when we want to ensure that a process has completed its work
#   before proceeding.
if __name__ == '__main__':
    process = multiprocessing.Process(target=fn)
    process.start()
    process.join()  # Wait for the process to finish
    print('Finished')
# Process is running
# Finished


###############################################################################
# Pool
###############################################################################


# Defining a function
# * We will define a function that will be run in the process below.
def cubic(n):
    print("Cubic is:", n ** 3)


# Defining a Pool
# * The Pool is a class that allows you to create a pool of worker processes.
# * It provides a convenient way to parallelize the execution of a function
#   across multiple input values.
# * The Pool class can be used to manage a pool of worker processes and
#   distribute tasks to them.
# * The "processes" argument specifies the number of worker processes to
#   create.
# * NOTE: When the pool is created, the processes are started and ready to
#   accept tasks.
# * We can use the `apply_async()` method to submit tasks to the pool.
# * This will allow the tasks to be executed asynchronously.
# * If more functions are submitted than there are worker processes, the
#   tasks will be queued until a worker process is available.
# * The `close()` method is used to prevent any more tasks from being submitted
#   to the pool.
# * This ensures that no new tasks can be added, but already submitted tasks
#   will continue to run.
# * The `join()` method is used to wait for the worker processes to finish.
# * This will synchronize the main process with the worker processes.
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    pool.apply_async(func=cubic, args=(128,))
    pool.apply_async(func=cubic, args=(256,))
    pool.close()
    pool.join()
# Cubic is: 2097152
# Cubic is: 16777216


###############################################################################
# Lock
###############################################################################


# Defining a Lock
# * A Lock is a synchronization primitive that is used to protect shared
#   resources from being accessed by multiple processes simultaneously.
# * It allows only one process to access the resource at a time, preventing race
#   conditions and ensuring process safety.
# * If another process tries to enter a with locker: block (with the same
#   locker object), it's delayed until the first process exits the block.
# * To create a Lock, we can use the multiprocessing.Lock() constructor.
# * NOTE: Different from `threading.Lock()`, this Lock uses Operating System
#   primitives to ensure mutual exclusion.
lock = multiprocessing.Lock()


# Acquiring and releasing a Lock
# * To use a Lock, we need to acquire it before accessing the shared resource
#   and release it when we're done.
# * This guarantees that only one process can access the resource at a time.
lock.acquire()
print('Critical section (synchronized)')
lock.release()
# Critical section (synchronized)


# Acquiring and releasing a Lock (with statement)
# * We can also use the "with" statement to automatically acquire and release
#   the lock.
with lock:
    print('Critical section (synchronized)')
# Critical section (synchronized)
