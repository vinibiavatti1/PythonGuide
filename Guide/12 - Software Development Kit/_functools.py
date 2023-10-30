"""
Functools

* The functools module is for higher-order functions: functions that act on or
  return other functions. In general, any callable object can be treated as a
  function for the purposes of this module
"""
import functools


###############################################################################
# Functions
###############################################################################


# reduce(function, iterable[, initializer])
# * Reduce is used to reduce the iterable to a single value, manipulating the
#   current value and the accumulator value
# * NOTE: Check the _reduce.py file for more details
def plus(accumulator, current):
    return accumulator + current


lst = [5, 2, 7, 8, 3, 5]
result = functools.reduce(plus, lst)
print(result)
# 30


# partial(func, /, *args, **keywords)
# * Freezes the positional args and kwargs of a function and return a new
#   function with these parameters already set
def add(x, y):
    return x + y


# partialmethod(func, /, *args, **keywords)
# * Return a new partialmethod descriptor which behaves like partial except
#   that it is designed to be used as a method definition rather than being
#   directly callable
class Lamp:
    def set_state(self, state):
        self.state = state

    turn_on = functools.partialmethod(set_state, True)
    turn_off = functools.partialmethod(set_state, True)


###############################################################################
# Decorators
###############################################################################


# @cache(user_function)
# * Simple lightweight unbounded function cache. Sometimes called "memoize"
@functools.cache
def factorial(collection):
    result = 1
    for value in collection:
        result *= value
    return value


fn = functools.partial(add, 4, 6)
print(fn())
# 10


# @cached_property(func)
# * Transform a method of a class into a property whose value is computed once
#   and then cached as a normal attribute for the life of the instance
class Calc:
    def __init__(self, value):
        self.value = value

    @functools.cached_property
    def cubic(self):
        return self.value ** 3


# @total_ordering
# * Given a class defining one or more rich comparison ordering methods
# * The class must define one of __lt__(), __le__(), __gt__(), or __ge__()
# * In addition, the class should supply an __eq__() method
@functools.total_ordering
class Student:
    def __gt__(self, other):
        return 1 > other


# @singledispatch and @register
# * Transform a function into a single-dispatch generic function
# * A form of generic function dispatch where the implementation is chosen
#   based on the type of a single argument
# * Use @<fun>.register to set the other implementation
@functools.singledispatch
def say(message):
    print('Str:', message)


@say.register
def _(message: int):
    print('Integer:', message)


@say.register
def _(message: tuple):
    print('Tuple:', message)


say('Test')
say(1)
say((1, 2, 3))
# Str: Test
# Integer: 1
# Tuple: (1, 2, 3)


# singledispatchmethod(func) and @register
# * Transform a method into a single-dispatch generic function
# * A form of generic function dispatch where the implementation is chosen
#   based on the type of a single argument
# * Use @<fun>.register to set the other implementation
class Person:
    @functools.singledispatchmethod
    def say(self, message):
        print(message)

    @say.register
    def say(self, message: int):
        print('Integer:', message)

    @say.register
    def say(self, message: tuple):
        print('Tuple:', message)


# wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# * This is a convenience function for invoking update_wrapper() as a function
#   decorator when defining a wrapper function
def decorator(fn):
    @functools.wraps(fn)
    def wrapper():
        fn()
    return wrapper
