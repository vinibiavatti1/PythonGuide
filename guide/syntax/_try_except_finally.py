"""
Try Except Finally

* The "try, except and finally" instructions are used to handle exceptions
* The "raise" instruction is used to raise an exception manually
* Each keyword has a specific purpose:
  * try: Used to define the begin of a block that can generate an exception
  * except: Used to identify and handle an exception generated in the "try"
    block
  * else: Used to perform an operation if no exception was raised
  * finally: Used to execute a code block independent if some
    exception was raised or not


* Raise syntax (used to raise an exception):

raise <exception>(<message>)
raise <exception>(<message>) from <exception>

* "Try Except Finally" syntax (used to handle an exception):

try:
    ...
except <exception>:
    ...
except <exception> as err:
    ...
except (<exception>, <exception>, ...) as err:
    ...
else:
    ...
finally:
    ...
"""


###############################################################################
# Raise
###############################################################################


# Define a function that implicitly raises an exception
# * Python has built-in exceptions that can raised in some cases. For example:
#   when the code tries to divide some number by zero. When it happens, the
#   ArithmeticError will be raised
# * The function below raises an exception implicitly when the second parameter
#   receives as argument the number zero
# * The raise keyword was not used, so, the exception will be raised implicitly
def divide(x, y):
    return x / y


# Define a function that explicitly raises an exception
# * An exception that is raised explicitly is when the keyword "raise" is used
# * In this way, the "raise" instruction will raises the specified exception
def divide_with_validation(x, y):
    if y == 0:
        raise ValueError('Y cannot be zero')
    return x / y


# Define a function that explicitly raises multiple exception
# * Multiple "raises" can be defined to a function, so, the function can throw
#   multiple exceptions
# * The exceptions can be different, like the example below:
def divide_with_validations(x, y):
    if x is None or y is None:
        raise ValueError('Input cannot be None')
    if y == 0:
        raise ArithmeticError('Y cannot be zero')
    return x / y


# Call a function that implicitly raises an exception
# * If we call the functions above using the zero as argument, some exception
#   will be raised
# * The code below was commented to avoid stopping the code execution
"""
divide(5, 0)

ZeroDivisionError: division by zero
"""


# Call a function that explicitly raises an exception
# * The same behavior of the above code will happens, but the exception that
#   will be raised will be different due to the data validation
"""
divide_with_validation(5, 0)

ValueError: Y cannot be zero
"""


# Call a function that explicitly raises multiple exceptions
# * The function will raise the failed validation correspondent exception, when
#   multiple exceptions are raised
"""
divide_with_validations(5, None)

ValueError: Input cannot be None

divide_with_validations(5, 0)

ArithmeticError: Y cannot be zero
"""


###############################################################################
# Try Except Else Finally
###############################################################################


# Handle an exception without identification
# * Handling exceptions is useful to perform some operation when an exception
#   is raise. Example: When a file should be open, but it does't exist
# * In Python, it is not mandatory to identify the raised exception
# * It is always recommended to identify the raised exception. It permits
#   working with the exception data (message, stacktrace, etc.)
# * In example below, the implicitly ArithmeticError is raised, and the except
#   block is performed
try:
    divide(5, 0)
except ArithmeticError:
    print('an error ocurred')
# an error ocurred


# Handle an exception with identification
# * It is always a good practice to identify the exception to work with it.
# * The identified exceptions are objects that contain information about the
#   error
# * To identify an exception, we can use the alias keyword "as", and introduce
#   a name for the exception
# * As a standard, the name "err" is used
try:
    divide_with_validation(5, 0)
except ValueError as err:
    print(err)
# Y cannot be zero


# Handle multiple exceptions
# * Multiple "except" blocks can be defined to handle the exception that was
#   raised
# * For example, if the ArithmeticError was raised, the except block for the
#   ArithmeticError will be performed. If the ValueError was raised, the except
#   block for the ValueError will be performed
# * If you change the second argument in the called function to zero (0), the
#   ArithmeticError except will be performed instead of the ValueError
try:
    divide_with_validations(5, None)
except ValueError as err:
    print(err)
except ArithmeticError as err:
    print(err)
# Input cannot be None


# Handle multiple exceptions at the same block
# * If the handle code is the same for the multiple exceptions, the same block
#   can be used to handle multiple exceptions. This is good to avoid code
#   repetition
# * In this syntax, the parenthesis "()" are required to specify that the block
#   will raise work for multiple exceptions
try:
    divide_with_validations(5, 0)
except (ValueError, ArithmeticError) as err:
    print(err)
# Y cannot be zero


# Handle an exception with a "finally" block
# * The "finally" block is used to ensure that a code is performed
#   independent if an exception is raised or not
# * This can be useful, for example, to close a file independent if the file
#   could be written or not, or to close a database connection independent if
#   the statement could be processed correctly or not
try:
    divide_with_validation(5, 0)
except ValueError as err:
    print(err)
finally:
    print('close')
# Y cannot be zero
# close


# Handle an exception with a "finally" and an "else" block
# * The else block is allowed into the "try except" statement too. It will be
#   performed when no exception was raised
try:
    divide_with_validation(5, 2.5)
except ValueError as err:
    print(err)
else:
    print('end')
finally:
    print('close')
# end
# close


###############################################################################
# Raise From
###############################################################################


# Raise a exception using "raise from" syntax
# * The "raise from" syntax is used to preserve the traceback of the original
#   exception, making it easier to identify the root cause of the error
# * It can only be used when there is a parent exception, and the parent
#   exception cause will be preserved into the exception that will be raised
# * The information of the original exception can be get from __cause__
#   attribute in the current exception
try:
    try:
        divide_with_validations(5, 0)
    except ArithmeticError as err:
        raise ValueError('cannot divide by zero') from err
except ValueError as err:
    print(err, err.__cause__, sep=', ')
# cannot divide by zero, Y cannot be zero


###############################################################################
# Exception Notes
###############################################################################


# Add a note to an exception
# * Python permits to add notes (additional information) to the exception
# * To add notes to an exception, we can use the "add_note()" method
# * The example below does not throw an exception to make the code easier to
#   read and understand
# * The empty raise statement is a short way to raise the current exception. It
#   is equivalent to "raise err"
try:
    divide_with_validation(5, 3)
except ValueError as err:
    err.add_note('The input is wrong')
    raise


# Raise an exception and add notes to it
# * In this example, the exception is raised and the notes are read
# * The __notes__ attribute contains a list of added notes
try:
    try:
        divide_with_validation(5, 0)
    except ValueError as err:
        err.add_note('The input is wrong')
        raise
except ValueError as err:
    print(err.__notes__[0])
# The input is wrong


###############################################################################
# Custom Exceptions
###############################################################################


# Create a custom exception
# * A custom exception is an exception that is not considered native in Python
#   i.e. it is not a builtin exception provided by Python's SDK
# * To create a custom exception, we have to create a class that inherits from
#   the "Exception" class
# * It can be useful to have a better control and a better identification of
#   the errors in a application
# * The convention assumes that all custom exceptions should has the "Error"
#   word as suffix
class CustomError(Exception):
    pass


# Raise a custom exception
# * The CustomError exception can be handled in the same way for any built-in
#   exception
try:
    raise CustomError('An error ocurred')
except CustomError as err:
    print(err)
# An error ocurred
