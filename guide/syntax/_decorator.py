"""
Decorator (@)

* A decorator, is a callable that is used to extend the functionality of other
  callables. In simple words, It allows us to decorate a function with
  another function. This behavior uses the concept of Higher Order Functions
* Decorators can be made using two syntax:
  * Without the at "@" char
  * With the at "@" char (Syntax sugar) (Preferred)
* The @ symbol in this context is sometimes referred as pie syntax
* The pie syntax makes it more easy to manage and to understand. It is
  preferred using the pie syntax for decorators
* Decorators wrap a function modifying its behavior. It works like a defined
  parent callable that will be handled before the decorated function
* A callable can be decorated with multiple decorators
* Usually, functions, methods and classes uses decorators
* Java annotations is a different concept of Python decorators
* Syntax
  * @<decorator_name>(<parameters>)
    <callable>
"""


###############################################################################
# Decorator Without Syntax Sugar
###############################################################################


# Define a decorator function for some function
# * A decorator is a function that will decorate a callable object
# * The decorator function will be processed before the execution of the
#   decorated function
# * This is known as a design pattern for programming languages that accepts
#   hight order functions
# * In this example, we will define a decorator function that will be used for
#   the next examples. This decorator will print the current date time when the
#   decorated function is called
# * Note that the decorator function requires the decorated function as
#   argument
# * The decorator function must return a wrapper function that will be
#   performed
from datetime import datetime
def print_current_date(fn):
    def wrapper():
        print(datetime.now())
        return fn()
    return wrapper


# Define a function to be decorated
# * Now, we have to create a function that will be decorated in the next
#   example
# * The function below does not accept any argument, it doesn't do anything. It
#   will be used only for example purposes
def operation():
    pass


# Decorates a function with the decorator
# * This example shows how to decorate a function without using the syntax
#   sugar "@"
decorated_operation = print_current_date(operation)


# Call a decorated function
# * In this example, the decorated function was called
# * Note that when the function was called, the datetime was printed to the
#   console
decorated_operation()
# 2023-02-06 14:14:57.465277


###############################################################################
# Decorator With Syntax Sugar "@"
###############################################################################


# Decorate using Syntax Sugar "@" (Preferred)
# * The same behavior of above can be reached by using the at char "@" to
#   decorate a function
# * This is considered syntax sugar, and is recommended to make the code
#   cleaner and more readable
@print_current_date
def operation():
    pass


# Call a syntax sugar decorated function
# * In this example, the second decorated function was called
# * The same behavior happened
# * For this case, we didn't need to set a variable with the function to wrap
#   it. When the function itself is called, the decorator will be triggered
operation()
# 2023-02-06 14:20:36.326822


###############################################################################
# Decorator With Parameters
###############################################################################


# Declare a decorator with parameters
# * A decorator function can accepts parameters like any function
# * The arguments will be set when the decorator is used to decorate some
#   callable object
# * A decorator function that accepts parameters must has two wrapper
#   functions:
#   * 1. Decorator wrapper
#   * 2. Function wrapper
# * In this example, a decorator function was defined that accepts a text that
#   will be printed before the original call of the decorated function
def print_text(text):
    def decorator_wrapper(fn):
        def wrapper():
            print(text)
            return fn()
        return wrapper
    return decorator_wrapper


# Decorate a function with a decorator with parameters
# * The argument of the decorator is set now
# * NOTE: The above decorator still not support the decorated function
#   arguments. In the next examples, we will check how to support them
@print_text('Calling operation...')
def operation():
    print('Operation completed')


# Call the decorated function
# * When calling the decorated function, the decorator is triggered and the
#   text offered by argument is printed
operation()
# Calling operation...
# Operation completed


###############################################################################
# Decorator With Parameters Support
###############################################################################


# Define a decoration with parameters functional support
# * The decorators above does not work in a function that requires arguments
# * In this example, we will see a decorator with parameters support, i.e. a
#   decorator that supports decorator parameters and function parameters
# * For this, we must use the concept of arbitrary arguments, and the concept
#   of unpack (*args, **kwargs)
# * The parameters will be passed to the wrapper function, and they will be
#   unpacked to the original function call
# * The decorator will be the same of the above examples, but with parameters
#   support
def print_text(text):
    def decorator_wrapper(fn):
        def wrapper(*args, **kwargs):
            print(text)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


# Decorate a function with a decorator with parameters support
# * The function that will be decorated will accepts arguments, and the
#   "print_text" decorator now will supports the function parameters
@print_text('Calling operation...')
def operation(name):
    print(f'Operation "{name}" completed')


# Call the decorated function
# * Now, we can call the function setting the arguments to it, and the
#   decorator function will works normally
operation('Python Development')
# Calling operation...
# Operation "Python Development" completed


###############################################################################
# Decorating a Class
###############################################################################


# Decorates a class with the decorator
# * The same syntax can be used for any decorator type
# * In this case, we will use the "print_text" decorator for a class
# * Class decorators can be useful to define special behaviors to some class,
#   like the singleton design pattern.
@print_text('Calling operation...')
class Operation:

    def __init__(self, name):
        print(f'Operation "{name}" completed')


# Call a decorated class
# * When the class is called to make a new instance of the class, the decorator
#   will be triggered
# * The example below, shows a code that creates a new instance of "Operation"
instance = Operation('Python Development')
# Calling operation...
# Operation "Python Development" completed


###############################################################################
# Multiple Decorators
###############################################################################


# Decorate a function with multiple decorators
# * Python objects accepts multiple decorators to be performed before the
#   original execution
# * The decorators should be stacked on the top of the Python object
# * In this example, we will use the decorators that we created before in a
#   single resource
@print_current_date
@print_text('Calling Operation...')
def operation():
    print('Operation Complete')


# Call a multiple decorated function
# * Now, we will call the function that has multiple decorators
# * NOTE: The order of the decorators is important since it will change which
#   decorator will be performed first
operation()
# 2023-02-06 16:17:39.641775
# Calling Operation...
# Operation Complete


###############################################################################
# Decorator Wraps
###############################################################################


# Call the decorated function without wraps
# * If we try to access information of a decorated object, we will see that the
#   returned information will be from the wrapped function defined inside the
#   decorator
# * To solve this problem, Python has the built-in "wraps()" decorator that
#   will be used to wraps the inner object with the original object reference
# * In the example below, we tried to access the name of the decorated
#   function, but the returned name was from the wrapper function instead
name = operation.__name__
print(name)
# wrapper


# Declare a decorator with wraps
# * To avoid the problem above, we can use the "functools" module to access the
#   "wraps()" built-in decorator
# * This decorator changes the reference of the function to the original
#   function without changing the logical behavior
# * The "wraps()" function will decorate the wrapper inner function
import functools
def print_text(text):
    def decorator_wrapper(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(text)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


# Decorate a function
# * The function below will be decorated with the decorator above
# * Since the decorator has the "wraps()" decorator for the wrapper function,
#   the reference of the function that will be accessed will be the original
#   one, not the wrapper function
@print_text('Calling Operation...')
def operation():
    pass


# Check information of decorated function
# * Now, if we access the name of the function, the original name will be
#   present
name = operation.__name__
print(name)
# operation


###############################################################################
# Decorator With Full Support (Template)
###############################################################################


# Declare a decorator with full support (Template)
# * A decorator with full support is considered a decorator that:
#   * 1. Supports function parameters
#   * 2. Can be assigned to classes
#   * 3. Has the "wraps()" decorator
# * Make sure when you create your own decorators to check these items above,
#   to ensure your decorator has full support. It is always recommended to
#   define only decorators with full support for consistency
# * The decorator below can be used as template for the development of new
#   decorators
def decorator(arg1, arg2):
    def decorator_wrapper(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # Decorator Actions
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


###############################################################################
# Examples
###############################################################################


# Declare constants for the examples below
# * In here, we will declare some values to be used by the decorators below
# * We will use a global class to store the values
# * Be free to change the value to check the result of the decorated function
#   below
class UserData:
    authenticated = True
    role = 'Administrator'
    token = '869c98b0191d1a226cbc51f35c560120'


# Declare a decorator that checks authentication
# * Some APIs uses decorators in the route functions to check if the user is
#   authenticated. This is a good example for the usage of it
# * The decorator below is an example for how a validation guard can be created
#   to check if the used is authenticated of not
def check_authentication():
    def decorator_wrapper(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if not UserData.authenticated:
                return '401 - Unauthorized'
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


# Declare a decorator that checks authority
# * This example is similar to the above one, but it checks the user roles
# * It is other good example for how the authority is validated for some APIs
def check_authority(roles=[]):
    def decorator_wrapper(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if UserData.role not in roles:
                return '401 - Forbidden'
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


# Declare a decorator that store logs
# * This decorator will be used only to print a log
# * It is other good example for how some HTTP frameworks store logs using
#   decorators
def logger(message):
    def decorator_wrapper(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(datetime.now(), message)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


# Decorate a function
# * The three above decorators will be used to decorate a function
# * The function below will have multiple decorators. Remember that the order
#   of the decorators changes the code order that will be performed
@check_authentication()
@check_authority(roles=['Administrator'])
@logger('Call to get_user_token')
def get_user_token():
    return UserData.token


# Call decorated function
# * Lets simulate a request that calls a function that returns the user token
# * This function is decorated with some behaviors before the original
#   operation, so, the decorators will be performed first as guards to check if
#   the user is authorized to get this information
token = get_user_token()
print(token)
# 2023-02-06 19:29:43.940884 Call to get_user_token
# 869c98b0191d1a226cbc51f35c560120
