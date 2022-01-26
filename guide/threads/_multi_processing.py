"""
Multi-processing

* Multiprocessing refers to the ability of a system to support more than one
  processor at the same time. Applications in a multiprocessing system are
  broken to smaller routines that run independently. The operating system
  allocates these threads to the processors improving performance of the system
* A multiprocessing system can have:
  * multiprocessor: a computer with more than one central processor.
  * multi-core processor: a single computing component with two or more
    independent actual processing units (called "cores")
* In Python, the multiprocessing module includes a very simple and intuitive
  API for dividing work between multiple processes
"""
import multiprocessing


###############################################################################
# Worker
###############################################################################


# Worker
# * This is an operation that will be used in the examples to be executed by
#   the process
def worker(n):
    print('Cubic is:', n ** 3)


###############################################################################
# Process
###############################################################################


# Create a process to execute the operation
# * The Process class from multiprocessing can be used to create a new process
#   to execute some function
# * The function will be executed by other Python Interpreter
# * NOTE: Windows doesn't have fork, so there's no way to make a new process
#   just like the existing one. So the child process has to run your code
#   again, but now you need a way to distinguish between the parent process and
#   the child process, and __main__ is it
if __name__ == '__main__':
    process = multiprocessing.Process(target=worker, args=(5,))
    process.start()
    process.join()
    # Cubic is: 125


###############################################################################
# Pool
###############################################################################


# Create a pool of process to execute the operation
# * The Pool class represents a pool of worker processes. It has methods which
#   allows tasks to be offloaded to the worker processes in a few different
#   ways
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    pool.apply_async(func=worker, args=(6,))
    pool.apply_async(func=worker, args=(3,))
    pool.close()
    pool.join()
    # Cubic is: 216
    # Cubic is: 27


###############################################################################
# Process as base class
###############################################################################


# Define a process as a class
# * The Process class can be used as base class to define a Process
# * The run() method can be overrided to define the execution
class Worker(multiprocessing.Process):
    def run(self):
        print('Hello World!')


# Execute the process
# * An object must be created from the class and the start() method will be
#   execute to start the new process
if __name__ == '__main__':
    process = Worker()
    process.start()
    process.join()
    # Hello World!


###############################################################################
# Process methods
###############################################################################


# start()
# * Start the process's activity
if __name__ == '__main__':
    process = multiprocessing.Process(target=worker, args=(8,))
    process.start()
    # Cubic is: 512


# is_alive()
# * Return whether the process is alive
if __name__ == '__main__':
    print(process.is_alive())
    # True


# join([timeout])
# * If the optional argument timeout is None (the default), the method blocks
#   until the process whose join() method is called terminates
# * A process can be joined many times
# * A process cannot join itself because this would cause a deadlock
if __name__ == '__main__':
    process.join()


# terminate()
# * Terminate the process
if __name__ == '__main__':
    process.terminate()


# close()
# * Close the Process object, releasing all resources associated with it
if __name__ == '__main__':
    process.close()


###############################################################################
# Pool methods
###############################################################################


# apply(func[, args[, kwds]])
# * Call func with arguments args and keyword arguments kwds. It blocks until
#   the result is ready. Given this blocks, apply_async() is better suited for
#   performing work in parallel
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    pool.apply(func=worker, args=(9,))


# apply_async(func[, args[, kwds[, callback[, error_callback]]]])
# * A variant of the apply() method which returns a AsyncResult object
if __name__ == '__main__':
    pool.apply_async(func=worker, args=(9,))


# map(func, iterable[, chunksize])
# * A parallel equivalent of the map() built-in function
# * This method chops the iterable into a number of chunks which it submits to
#   the process pool as separate tasks
# * for multiple iterables see starmap()
if __name__ == '__main__':
    args = [1, 2, 3]
    pool.map(worker, args)  # It will create 3 workers with range as param


# map_async(func, iterable[, chunksize[, callback[, error_callback]]])
# * A variant of the map() method which returns a AsyncResult object
if __name__ == '__main__':
    args = [1, 2, 3]
    pool.map_async(worker, args)


# starmap(func, iterable[, chunksize])
# * Like map() except that the elements of the iterable are expected to be
#   iterables that are unpacked as arguments
if __name__ == '__main__':
    args = [(1,), (2,), (3,)]
    pool.starmap(worker, args)


# starmap_async(func, iterable[, chunksize[, callback[, error_callback]]])
# * A combination of starmap() and map_async() that iterates over iterable of
#   iterables and calls func with the iterables unpacked. Returns a result
#   object
if __name__ == '__main__':
    args = [(1, 2), (2, 3), (3, 4)]
    pool.starmap_async(worker, args)


# terminate()
# * Stops the worker processes immediately without completing outstanding work
if __name__ == '__main__':
    pool.terminate()


# close()
# * Prevents any more tasks from being submitted to the pool
if __name__ == '__main__':
    pool.close()


# join()
# * Wait for the worker processes to exit. One must call close() or terminate()
#   before using join()
if __name__ == '__main__':
    pool.join()
