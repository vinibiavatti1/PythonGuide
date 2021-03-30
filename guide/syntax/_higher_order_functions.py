"""
Higher-order Functions (HOF)

* In mathematics and computer science, a higher-order function is a function
  that does at least one of the following:
  * takes one or more functions as arguments or
  * returns a function as its result
* Examples of HOF functions are (map(), filter(), sorted(), etc.), and the
  decorators @ in Python
* This concept for functions is called First-class function, in which the
  Python programming language has support for it
* References: https://en.wikipedia.org/wiki/Higher-order_function
              https://en.wikipedia.org/wiki/First-class_function
"""


# Function as argument
# * An example of HOF function is a function that accepts other function as
#   argument
# * The builtin functions (map(), sorted(), filter(), etc.) are examples of
#   HOF functions
def compute(fn, iterable):
    for i in range(len(iterable)):
        iterable[i] = fn(iterable[i])


lst = [1, 2, 3, 4, 5]
compute(lambda e: e * 2, lst)  # Multiply each element by two
print(lst)
# [2, 4, 6, 8, 10]


# Returing a function
# * This is an example of a decorator concept. In python, there is other way to
#   define a decorator, using @. Check the other example for more details
def twice(fn):
    def wrapper(arg):
        return fn(fn(arg))
    return wrapper


def double(num):
    return num * 2


double_twice = twice(double)
print(double(2), double_twice(2), sep=', ')
# 4, 8


# Decorator @
# * This is an example of a decorator pie syntax @ available in python to
#   create decorated functions
# * NOTE: Check the _decorator.py file inside syntax folder for more details
def twice_pie(fn):
    def wrapper(arg):
        return fn(fn(arg))
    return wrapper


@twice_pie
def triple(num):
    return num * 3


print(triple(2))
# 18
