"""
Decorator (@)

* A decorator, is a callable that is used to extend the functionality of other
  callables. In simple words, It allows you to decorate a function with
  another function. This concept is called Higher-order functions (Check
  _higher_order_functions.py file)
* The @ symbol in this context is sometimes referred to as Pie Syntax to a
  decorator
* The pie syntax makes it more easy to access and extend
* Decorators wrap a function, modifying its behavior

* Syntax
  * @<decorator_name>(<parameters>)
    any_callable
"""
import functools
from datetime import datetime


###############################################################################
# Decorator
###############################################################################


# Define a decorator function
# * To create a decorator, you must create a function that will be the
#   decorator, and a function inside that will be the wrapper
# * The decorator function must receive a function as argument
def show_date(func):
    def wrapper(text):
        print(datetime.today())
        return func(text)
    return wrapper


# Create a normal function
# * This function will be decorated with the decorator created before
def text(text):
    print(text)


# Decorating a function and call it (without pie syntax @)
# * To decorate some function, you must call the decorator function passing the
#   target function as argument, and the return will be the function decorated
# * NOTE: This way is not recommended since the Python has the Pie Syntax to
#   use for decorate function or classes (Check the next example)
text = show_date(text)
text('Hi decorator!')
# 2021-03-30 22:50:07.713562
# Hi decorator!


# Creating and decorating a function (with pie syntax @)
# * NOTE: This way is recommended and is beeter to undertanding
@show_date
def message(text):
    print(text)


# Call decorated function
# * In this way you can call the function and it will be decorated already
message('Hi Pie Decorator!')
# 2021-03-30 22:50:07.713562
# Hi Pie Decorator!


# Accepting any parameter in function
# * To accept any parameter in wrapper function you can use *args and **kwargs
def show_today(func):
    def wrapper(*args, **kwargs):
        print(datetime.today())
        return func(*args, **kwargs)
    return wrapper


# Creating and decorating functions with different parameters
# * This function will have different parameters
# * The decorator can handle different parameters, not only one
@show_today
def dialog(text):
    print(text)


@show_today
def conversation(name, text):
    print(name + ': ' + text)


# Call the function with different parameters
# * Both functions will work correctly
dialog('Hi')                   # 2021-03-31 13:41:22.014080 Hi
conversation('Vini', 'hello')  # 2021-03-31 13:41:22.014080 Vini: hello


###############################################################################
# Decorator parameters
###############################################################################


# Define a decorator with parameters
# * To define parameters to the decorator, it need three functions:
#   * 1. The decorator function (containing the decorator paramenters)
#   * 2. The decorator wrapper (containing the function as paramenter)
#   * 3. The function wrapper
def join_text(text):                # decorator
    def decorator_wrapper(func):    # decorator wrapper
        def wrapper(message):       # function wrapper
            return func(f'{text} {message}')
        return wrapper
    return decorator_wrapper


# Decorating a function (with parameters)
# * To decorate a function with a decorator that contains parameters, you can
#   just set the parameters to the decorator inside the parenthesis ()
@join_text('Guy says: ')
def say(message):
    print(message)


# Call decorated function (with parameters)
# * You can call the function using the same way
say('Hello my friend!')
# Guy says: Hello my friend!


###############################################################################
# Nested decorators
###############################################################################


# Set a nested decorators to function
# * You can add more then once decorator for a function or a class
@show_date
@join_text('Guy says: ')
def speak(text):
    print(text)


# Call a function that contains nested decorators
# * Use the same way to call a function, and the decorators will be executed
speak('This function is so decorated!')
# 2021-03-30 22:50:07.713562
# Guy says: This function is so decorated!


###############################################################################
# Wraps
###############################################################################


# Functools Wraps
# * The wraps decorator is used to make reference to corret function, not to
#   the wrapper function
# * If dir or help command is used in a function witout wraps, the incorrenct
#   information will be displayed. To fix it, the functools.wraps function
#   can be used
def show_time(func):
    @functools.wraps(func)
    def wrapper(text):
        print(datetime.today())
        func(text)
    return wrapper


# Decorate a function with a decorator using wraps
# * To decorate is the same way of others
@show_time
def ask(text):
    """
    Ask something
    """
    print(text)


# Check the information os a decorated function with wraps
# * To check the information you can check the attributes of the function or
#   use dir or help functions
print(ask.__name__)    # ask (With wraps)
print(speak.__name__)  # wrapper (Without wraps) (incorrect)
help(ask)              # ask(text)
help(speak)            # wrapper(text) (incorrect)


###############################################################################
# Class decorator
###############################################################################


# Define a decorator to some class
# * You can decorate classes too, to manipulate the way to instantiate objects
#   of it
# * The parameter for a class decorator will be the class, not a function
def class_name(cls):
    @functools.wraps(cls)
    def wrapper():
        print(f'Class name: {cls.__name__}')
        return cls()
    return wrapper


# Decorate a class
# * To decorate a class, you can use the same way to decorate a function
@class_name
class Person():
    pass


# Create a object from class
# * It will execute the wrapper fisrt
person = Person()
# Class name: Person
