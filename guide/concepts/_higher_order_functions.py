"""
Higher-order Functions (HOF)

* In mathematics and computer science, a higher-order function is a function
  that does at least one of the following:
  * takes one or more functions as arguments or
  * returns a function as its result
* Examples of HOF functions are (map(), filter(), sorted(), etc.), and the
  decorators "@" in Python
* This concept for functions is called First-class function, in which the
  Python programming language has support for it
* References
  * https://en.wikipedia.org/wiki/Higher-order_function
  * https://en.wikipedia.org/wiki/First-class_function
"""


###############################################################################
# Function as Argument
###############################################################################


# Define a function that accepts another function as argument
# * Python supports the concept of First-class function, which means that a
#   function can be passed as argument to another function
def compute(fn, iterable):
    for i in range(len(iterable)):
        iterable[i] = fn(iterable[i])


# Call a function that accepts another function as argument
# * The function above will be called passing a function as argument
# * The iterable will be modified by the function
def action(num):
    return num * 2


lst = [1, 2, 3, 4, 5]
compute(action, lst)
print(lst)
# [2, 4, 6, 8, 10]


# Call a function that accepts another function as argument (lambda)
# * In this example, a lambda function is passed as argument that will result
#   in the same of the previous example
# * Take a look at _lambda.py file for more details about
lst = [1, 2, 3, 4, 5]
compute(lambda e: e * 2, lst)  # Multiply each element by two
print(lst)
# [2, 4, 6, 8, 10]


###############################################################################
# Function as Return
###############################################################################


# Define a function that returns another function
# * A function in Python can return another function
# * The example below defines a function that returns another function based
#   on the argument
def get_operation(name):
    if name == 'add':
        def add(x, y):
            return x + y
        return add
    elif name == 'sub':
        def sub(x, y):
            return x - y
        return sub
    return None


# Call a function that returns another function (lambda)
# * The function above can be simplified by using lambdas, since the returned
#   functions has only one expression
def get_operation_lambda(name):
    if name == 'add':
        return lambda x, y: x + y
    elif name == 'sub':
        return lambda x, y: x - y
    return None


# Call a function that returns another function
# * The function above will be called to get a function as return
# * The returned function will be used to perform the operation
operation = get_operation('sub')
print(operation(10, 5))
# 5


###############################################################################
# Function as Argument and Return
###############################################################################


# Define a function with a function as argument and that returns a function
# * In this example, the function will do both, accept a function as argument
#   and return a function
# * Note that we defined a wrapper function that will be returned and will
#   receive the arguments for the function
# * In Python, this concept is called Decorator, since we are decorating a
#   function with some additional behavior
def twice(fn):
    def wrapper(arg):
        fn(arg)
        fn(arg)
    return wrapper


# Call the function above
# * The function above will be called passing a function as argument
# * We will get the returned function and call it, to get the result
print_twice = twice(print)
print_twice('Hello World')
# Hello World
# Hello World


###############################################################################
# Decorator
###############################################################################


# Define a decorator function
# * The same concept of the previous example can be simplified by using the "@"
# * The "@" is a syntactic sugar to define a decorator function in Python
# * Take a look at _decorator.py file for more details about it
@twice
def my_print(txt):
    print(txt)


# Call a decorated function
# * The function above will be called to show the result
my_print('Hello World')
# Hello World
# Hello World
