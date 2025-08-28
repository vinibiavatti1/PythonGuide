"""
Threading module

* The threading module builds on the low-level features of thread to make
  working with threads even easier and more pythonic
* Using threads allows a program to run multiple operations concurrently in the
  same process space
* Threads in python are locked by the GIL (Global Interpreter Lock) that allow
  just one thread do be executed. Check the _gil.py for more details. So, in
  Python, even if you create a Thread, the program will be executed as single
  thread. The multiprocessing can be used to run async operations in Python
"""


###############################################################################
# Defining thread
###############################################################################


# Imports
# * We will import the libraries below to be used on this document.
import threading
import time



# Define the worker as a function
# * This function will be executed in other thread
def worker(arg):
    print('Worker')


# Create thread with function
# * To create a Thread, the Thread class can be used setting a function as a
#   target
thread = threading.Thread(target=worker, args=('Some value',))
thread.start()
# Worker


# Define the worker as a class
# * The Thread class can be used as base class to create a thread too
class Worker(threading.Thread):
    def run(self):
        print('Worker')


# Create thread using class
# * The created class can be instantiated and executed as a thread
thread = Worker()
thread.start()
# Worker


###############################################################################
# Threading module methods
###############################################################################


# active_count()
# * Returns the number of thread objects that are active
count = threading.active_count()
print(count)
# 1


# current_thread()
# * Return the current Thread object, corresponding to the caller's thread of
#   control
# * If the caller's thread of control was not created through the threading
#   module, a dummy thread object with limited functionality is returned
current_thread = threading.current_thread()
print(current_thread)
# <_MainThread(MainThread, started 8020)>


# excepthook(args, /)
# * Handle uncaught exception raised by Thread.run()
# * Parameters received from callback:
#   exc_type: Exception type
#   exc_value: Exception value, can be None
#   exc_traceback: Exception traceback, can be None
#   thread: Thread which raised the exception, can be None
def erroneous_worker():
    raise Exception('Error')


def excepthook(args):
    print(args)


threading.excepthook = excepthook
thread = threading.Thread(target=erroneous_worker)
thread.start()
# _thread.ExceptHookArgs(exc_type=<class 'Exception'>,
# exc_value=Exception('Error'), exc_traceback=<traceback object at
# 0x00000297C84C12C0>, thread=<Thread(Thread-3, started 19920)>)


# get_ident()
# * Return the 'thread identifier' of the current thread. This is a nonzero
#   integer. Its value has no direct meaning; it is intended as a magic cookie
#   to be used
ident = threading.get_ident()
print(ident)
# 19248


# get_native_id()
# * Return the native integral Thread ID of the current thread assigned by the
#   kernel. This is a non-negative integer. Its value may be used to uniquely
#   identify this particular thread
native_id = threading.get_native_id()
print(native_id)
# 8144


# enumerate()
# * Return a list of all Thread objects currently alive. The list includes
#   daemonic threads, dummy thread objects created by current_thread(),
#   and the main thread
for t in threading.enumerate():
    print(t.getName())
# MainThread
# Thread-3


# main_thread()
# * Return the main Thread object. In normal conditions, the main thread is the
#   thread from which the Python interpreter was started
main_thread = threading.main_thread()
print(main_thread)
# <_MainThread(MainThread, started 11872)>


###############################################################################
# Thread methods
###############################################################################


# run()
# * The run() method is the entry point for a thread
# NOTE: Use the start() method to run the thread
class Job(threading.Thread):
    def run(self):  # Entry point
        print('Job')


# start()
# * The start() method starts a thread by calling the run method.
thread = Job()
thread.start()
# Job


# join(timeout)
# * The join() waits for threads to terminate
# * When the timeout argument is present and not None, it should be a floating
#   point number specifying a timeout for the operation in seconds
def work():
    time.sleep(1)
    print('Terminate')


thread = threading.Thread(target=work)
thread.start()
thread.join()  # Waits the thread to terminate before execute main thread
print('Main thread')
# Terminate
# Main thread


# is_alive()
# * The isAlive() method checks whether a thread is still executing
print(thread.is_alive())
# False


# setName()
# * The setName() method sets the name of a thread.
thread.setName('My Thread')


# getName()
# * The getName() method returns the name of a thread
print(thread.getName())
# My Thread


# setDaemon()
# * Daemon threads runs without blocking the main program from exiting
# * Using daemon threads is useful for services where there may not be an easy
#   way to interrupt the thread or where letting the thread die in the middle
#   of its work does not lose or corrupt data
def daemon_work():
    time.sleep(1)
    print('Terminate')


thread = threading.Thread(target=daemon_work)
thread.setDaemon(True)


# isDaemon()
# * Check if the thread is a daemon thread
print(thread.isDaemon())
# True


###############################################################################
# Lock
# * A primitive lock is a synchronization primitive that is not owned by a
#   particular thread when locked. In Python, it is currently the lowest level
#   synchronization primitive available, implemented directly by the _thread
#   extension module.
# * A primitive lock is in one of two states, 'locked' or 'unlocked'. It is
#   created in the unlocked state. It has two basic methods, acquire() and
#   release()
# * The with statement can be used with Lock object
# * NOTE: If another thread tries to enter a with locker: block (with the same
#   locker object), it's delayed until the first thread exits the block
###############################################################################


# Lock()
# * Creates a lock
lock = threading.Lock()


# acquire(blocking=True, timeout=-1)
# * When the state is unlocked, acquire() changes the state to locked and
#   returns immediately
# * When the state is locked, acquire() blocks until a call to release()
lock.acquire()


# release()
# * The release() method should only be called in the locked state
# * Tt changes the state to unlocked and returns immediately
lock.release()


# locked()
# * Return true if the lock is acquired
print(lock.locked())
# False


# Synchronization example (Using methods)
class DbUpdate(threading.Thread):
    def __init__(self, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = lock

    def run(self):
        self._lock.acquire()
        print(f'{self.getName()}: Updading...')
        time.sleep(1)  # updating delay simulation...
        print(f'{self.getName()}: Done!')
        self._lock.release()


lock = threading.Lock()  # NOTE: Need to use the same object for locks
update1 = DbUpdate(lock)
update2 = DbUpdate(lock)
update1.start()
update2.start()
# Thread-7: Updading...
# Thread-7: Done!
# Thread-8: Updading...
# Thread-8: Done!


# Synchronization example (Using with)
class DbInsert(threading.Thread):
    def __init__(self, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = lock

    def run(self):
        with self._lock:
            print(f'{self.getName()}: Inserting...')
            time.sleep(1)  # inserting delay simulation...
            print(f'{self.getName()}: Done!')


insert1 = DbInsert(lock)
insert2 = DbInsert(lock)
insert1.start()
insert2.start()
# Thread-9: Inserting...
# Thread-9: Done!
# Thread-10: Inserting...
# Thread-10: Done!
