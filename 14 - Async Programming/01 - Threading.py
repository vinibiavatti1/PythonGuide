"""
Threading

* Threads are lightweight, independent units of execution within a process.
* They share the same memory space and can communicate with each other more
  easily than separate processes.
* Threads are managed by the operating system, which can schedule them to run
  on different CPU cores.
* Python provides the `threading` module to work with threads in a more
  convenient way.
* Since the Global Interpreter Lock (GIL) allows only one thread to execute at
  a time in CPython, the `threading` module is best suited for I/O-bound tasks
  rather than CPU-bound tasks.
* The multiprocessing module can be used to create separate processes, each
  with its own Python interpreter and memory space, allowing for true
  parallelism.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import threading


###############################################################################
# Function Thread
###############################################################################


# Defining a function
# * We can start threads based on functions.
# * Below, we will define a function that will be run in a separate thread.
def fn():
    print("Thread is running")


# Using the function in a thread
# * We can create a thread by instantiating the Thread class and passing the
#   function as the target.
# * When the thread is created, it can be started using the `start()` method.
thread = threading.Thread(target=fn)
thread.start()
# Thread is running


# Defining a function (with parameters)
# * We can also start threads using function with parameters.
# * Below, we will define a function that takes parameters.
def fn(param1, param2):
    print(f"Thread is running with parameters: {param1}, {param2}")


# Using the function in a thread (with parameters)
# * When setting the thread's target to a function with parameters, we can use
#   the `args` argument to pass the parameters as a tuple.
thread = threading.Thread(target=fn, args=("value1", "value2"))
thread.start()
# Thread is running with parameters: value1, value2


###############################################################################
# Thread Subclass
###############################################################################


# Defining a thread subclass
# * We can define a subclass of the Thread class and override the run() method.
# * This is useful when we want to encapsulate thread behavior within a class.
class MyThread(threading.Thread):
    def run(self):
        print("Thread is running")


# Running the thread class
# * To start the thread, we need to create an instance of the MyThread class
#   and call the start() method.
thread = MyThread()
thread.start()
# Thread is running


###############################################################################
# Daemon Threads
###############################################################################


# Defining a function
# * We will define a function that will be run in the thread below.
def fn():
    print("Daemon thread is running")


# Defining a Daemon Thread
# * A daemon thread is a thread that runs in the background and is
#   terminated when the main program exits.
# * Daemon threads are useful for tasks that should not block the
#   program from exiting, such as background tasks or services.
# * To define a daemon thread, we can set the `daemon` attribute to `True`
thread = threading.Thread(target=fn)
thread.daemon = True
thread.start()
# Daemon thread is running


###############################################################################
# Joining Threads
###############################################################################


# Defining a function
# * We will define a function that will be run in the thread below.
def fn():
    print("Thread is running")


# Joining Threads
# * We can use the `join()` method to wait for a thread to finish.
# * This is useful when we want to ensure that a thread has completed its work
#   before proceeding.
thread = threading.Thread(target=fn)
thread.start()
thread.join()  # Wait for the thread to finish
print('Finished')
# Thread is running
# Finished


###############################################################################
# Lock
###############################################################################


# Defining a Lock
# * A Lock is a synchronization primitive that is used to protect shared
#   resources from being accessed by multiple threads simultaneously.
# * It allows only one thread to access the resource at a time, preventing race
#   conditions and ensuring thread safety.
# * If another thread tries to enter a with locker: block (with the same
#   locker object), it's delayed until the first thread exits the block.
# * To create a Lock, we can use the threading.Lock() constructor.
# * NOTE: Different from `multiprocessing.Lock()`, this Lock uses only boolean
#   flags to control access. This is simpler and more lightweight.
lock = threading.Lock()


# Acquiring and releasing a Lock
# * To use a Lock, we need to acquire it before accessing the shared resource
#   and release it when we're done.
# * This guarantees that only one thread can access the resource at a time.
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


# Check if the lock is acquired
# * We can use the `locked()` method to check if the lock is currently held by
#   any thread (acquired)
x = lock.locked()
print(x)
# False
