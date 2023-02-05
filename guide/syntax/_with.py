"""
With

* The "with" instruction in Python is used to wrap a block of code that
  interacts with a resource, and ensure that this resource is cleaned up
* Basically, the "with" creates a context to the resource, and executes one
  operation when the resource is used in "with", and one operation is performed
  when the code block is finished
* Even if an exception raises, the clean up operation will be performed
* The objects that will be used as the resource for "with" needs to have the
  Context Manager protocol implements, i.e. the methods "__enter__" and
  "__exit__" implemented
* When the object is set to the "with", the "__enter__" method will be
  triggered, and when the cursor gets the end of the code block, the "__exit__"
  method will be triggered
* The "with" instruction can be useful to close a file after usage, to close a
  database connection after the execution of some statement, etc...
* Syntax
  * with <resource>:
  * with <resource> as <name>:
"""


###############################################################################
# With
###############################################################################


# Crete a path to a file
# * To demonstrate the behavior of the "with" instruction, we can use some
#   native object that implements the "__enter__" and "__exit__" methods
# * Python has some native objects that already has the implementation of the
#   methods, such as (IO objects, Thread locks, etc...)
# * In this example, we will define a path to a file that will be used for the
#   next examples
import os
import sys
file_path = os.path.join(
    sys.path[0], '..', '..', 'resources', 'file_with.txt'
)


# Create a context to a file using "with"
# * To create a context to the "file" resource, we can use the "with" syntax
# * When the "with" is performed, the method "__enter__" in the "file" object
#   is triggered
# * When the code block is finished, the method "__exit__" in the "file" object
#   is triggered
# * I used the "open()" function here to receive the file object to work with
with open(file_path, 'r'):
    pass


# Create a context to a named file using "with"
# * In the previous case, we didn't set a name to the file, so, we could't use
#   the file inside the code block
# * In this example, we used the "as" keyword to define an alias to the file
#   that we opened
with open(file_path, 'r') as file:
    pass


# Create a context to a named file using "with" and perform an operation
# * We can use the name to access the file and work with it
# * In this example, we will read the file data and print it
with open(file_path, 'r') as file:
    file_content = file.read()
    print(file_content)
# Python is an amazing language!


# Create a context to a Thread lock using "with"
# * Instead of the file, we can use other resource example: the Thread.Lock()
# * This object is used to perform an synchronous operation when working with
#   multiple threads
from threading import Lock
with Lock():
    pass


###############################################################################
# With Implementation
###############################################################################


# Declare a class that implements the context manager protocol
# * The context manager protocol is the name of a set of methods that allows
#   the usage of the "with" instruction
# * The methods of the context manager protocol are "__enter__" and "__exit__"
# * In this example, we will define a class that implement these methods, that
#   will be used to the next examples
# * NOTE: The "__enter__" method has to return the object that will be used as
#   the resource in the "with"
class Connection:
    def __enter__(self):
        print('Connection Open')
        return self

    def __exit__(self, exc, val, trace):
        print('Connection Close')

    def operation(self):
        print('Operation...')

    def bad_operation(self):
        raise Exception('An error ocurred!')


# Use the created class on "with" instruction
# * Since the class we declared implements the context manager protocol, we can
#   use the instances of this class into the "with" statement
# * When the "with" is performed and an object is created, the "__enter__"
#   method will be invoked
# * When the code block is finished, the method "__exit__" of the object will
#   be triggered
with Connection() as connection:
    connection.operation()
# Connection Open
# Operation...
# Connection Close


###############################################################################
# With and Exception
###############################################################################


# Use the with to handle an exception
# * When a exception is raised inside the code block, the "with" will be
#   performed normally, i.e. the method "__exit__" will be triggered
# * Note that the correct operation "operation()" method will not be executed
#   since an exception will be raised, but the "__exit__" method will be
#   performed anyway
try:
    with Connection() as connection:
        connection.bad_operation()
        connection.operation()
except Exception as err:
    print(err)
# Connection Open
# Connection Close
# An error ocurred!
