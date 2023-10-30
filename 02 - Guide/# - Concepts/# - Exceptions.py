"""
Exceptions

* In Python, all exceptions must be instances of a class that derives from
  BaseException. In a try statement with an except clause that mentions a
  particular class, that clause also handles any exception classes derived from
  that class (but not exception classes from which it is derived)
* Here there are the most common exceptions and examples to raise these
* Reference: https://docs.python.org/3/library/exceptions.html
* Below there is the exceptions hierarchy:

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""


###############################################################################
# Base Exceptions
###############################################################################


# BaseException
# * The base class for all built-in exceptions.
# * NOTE: It is not meant to be directly inherited by user-defined classes
#   (for that, use Exception)
"""
raise BaseException('Base exception')  # NOTE: Use Exception instead

BaseException: Base exception
"""


# Exception
# * All built-in, non-system-exiting exceptions are derived from this class.
# * All user-defined exceptions should also be derived from this class
"""
raise Exception('Exception')

Exception: Exception
"""


###############################################################################
# Common Exceptions
###############################################################################


# SyntaxError
# * Raised when the parser encounters a syntax error. This may occur in an
#   import statement, in a call to the built-in functions exec() or eval(), or
#   when reading the initial script or standard input (also interactively)
"""
def func:  # Without parenthesis
    pass

SyntaxError: invalid syntax
"""


# NameError
# * Raised when a local or global name is not found. This applies only to
#   unqualified names.
# * The associated value is an error message that includes the name that could
#   not be found
"""
x = 1
if x == 2:
    txt = 'test'
print(txt)  # There is no txt defined if x is not 2

NameError: name 'txt' is not defined
"""


# TypeError
# * Raised when an operation or function is applied to an object of
#   inappropriate type.
# * The associated value is a string giving details about the type mismatch
"""
x = 1
length = len(x)  # Int is not interable

TypeError: object of type 'int' has no len()
"""


# IndexError
# * Raised when a sequence subscript is out of range
"""
lst = [1, 2, 3]
print(lst[5])  # There is no index 5 in the list

IndexError: list index out of range
"""


# ValueError
# * Raised when an operation or function receives an argument that has the
#   right type but an inappropriate value
"""
x = '123'
y = 'abc'
cast1 = int(x)  # It works!
cast2 = int(y)  # Error

ValueError: invalid literal for int() with base 10: 'abc'
"""


# KeyError
# * Raised when a mapping (dictionary) key is not found in the set of existing
#   keys
"""
dct = dict(name='Vini')
dct['age']  # Try to access an undefined key

KeyError: 'age'
"""


# AttributeError
# * Raised when an attribute reference or assignment fails
"""
class Person:
    pass


person = Person()
name = person.name  # Person has no attribute name

AttributeError: 'Person' object has no attribute 'name'
"""


# IndentationError
# * Base class for syntax errors related to incorrect indentation
"""
if x == 1:
print(True)

IndentationError: expected an indented block
"""


# StopIteration
# * Raised by built-in function next() and an iterator's __next__() method to
#   signal that there are no further items produced by the iterator
"""
iterator = iter([1, 2])
next(iterator)
next(iterator)
next(iterator)  # Raise StopIteration

StopIteration
"""


# AssertionError
# * Raised when an assert statement fails
"""
x = 1
assert x == 2  # Incorrect value for x

AssertionError
"""


# ModuleNotFoundError
# * A subclass of ImportError which is raised by import when a module could not
#   be located
"""
import invalid_module

ModuleNotFoundError: No module named 'invalid_module'
"""


# ImportError
# * Raised when the import statement has troubles trying to load a module.
# * Also raised when the "from list" in from ... import has a name that cannot
#   be found
"""
from math import invalid_function

ImportError: cannot import name 'invalid_function' from 'math'
(unknown location)
"""


# RuntimeError
# * Raised when an error is detected that doesn't fall in any of the other
#   categoriesS
# * The associated value is a string indicating what precisely went wrong
"""
raise RuntimeError('Generic error')

RuntimeError: Generic error
"""


# NotImplementedError
# * This exception is derived from RuntimeError. In user defined base classes,
#   abstract methods should raise this exception when they require derived
#   classes to override the method, or while the class is being developed to
#   indicate that the real implementation still needs to be added
"""
from abc import ABC


class Person(ABC):
    def get_name(self):
        raise NotImplementedError()


class Customer(Person):
    pass


customer = Customer()
name = customer.get_name()  # Method not implemented

NotImplementedError
"""


# RecursionError
# * This exception is derived from RuntimeError. It is raised when the
#   interpreter detects that the maximum recursion depth
"""
def recursive():
    recursive()


recursive()  # Call infinity loop function

RecursionError: maximum recursion depth exceeded
"""


###############################################################################
# User-defined Exceptions
###############################################################################


# Create a user exception
# * NOTE: To create an exception, use "Exception" class as base class
# * NOTE: PEP8 - The name o the exception must have suffix with "Error" word
"""
class MyValidationError(Exception):
    pass


raise MyValidationError('Some error ocurred')

__main__.MyValidationError: Some error ocurred
"""


# Create and override exception data
# * The Exception class has a constructor with message attribute
"""
class MyValidationError(Exception):
    def __init__(self, message, submessage):
        super().__init__(message + ': ' + submessage)


raise MyValidationError('Error', 'Invalid Value')

__main__.MyValidationError: Error: Invalid Value
"""
