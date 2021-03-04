"""
Decorator (@)

* A decorator, is a callable that is used to extend the functionality of other
  callables. In simple words, It allows you to decorate a function with
  another function
* The @ symbol in this context is sometimes referred to as Pie Syntax to a
  decorator
* The pie syntax makes it more easy to access and extend
* Decorators wrap a function, modifying its behavior

* Syntax
  * @<decorator_name>
    any_callable
"""
import functools


# Decorator without pie syntax
def decorator(func):
    def wrapper(text):
        print(f'Function {func.__name__} called')
        return func(text)
    return wrapper


def my_print(text):
    print(text)


my_print = decorator(my_print)
my_print('Hi decorator!')
# Function my_print called
# Hi decorator!


# Decorator with pie syntax
def show_fn_name(func):
    def wrapper(text):
        print(f'Function {func.__name__} called')
        return func(text)
    return wrapper


@show_fn_name
def my_print2(text):
    print(text)


my_print2('Hi Pie Decorator!')
# Function my_print2 called
# Hi Pie Decorator!


# Decorator with parameters
def join_text(join_text):           # decorator
    def decorator_wrapper(func):    # decorator wrapper
        def wrapper(text):          # function wrapper
            return func(f'{text} {join_text}')
        return wrapper
    return decorator_wrapper


@join_text('Decorator text')
def my_print3(text):
    print(text)


my_print3('Func text')
# Func text Decorator text


# Nesting decorators
@show_fn_name
@join_text('joined text')
def my_print4(text):
    print(text)


my_print4('Nesting...')
# Function wrapper called  NOTE: The incorrect named was displayed
# Nesting... joined text


# Functools wrap
# * Used to make reference to corret function, not to the wrapper function
# * If used dir or help command in a function witout wraps, the incorrenct
#   information will be displayed. To fix it, the functools.wraps function
#   can be used
def show_fn_name_wrapped(func):
    @functools.wraps(func)
    def wrapper(text):
        print(f'Function {func.__name__} called')
        func(text)
    return wrapper


@show_fn_name_wrapped
def my_print5(text):
    print(text)


print(my_print5.__name__)  # my_print5
my_print5('Wraps!')
# Function my_print5 called
# Wraps!


# Decorator in class
def class_decorator(cls):
    @functools.wraps(cls)
    def wrapper():
        print(cls.__name__)
        return cls()
    return wrapper


@class_decorator
class MyClass():
    pass


my_class = MyClass()
# MyClass
