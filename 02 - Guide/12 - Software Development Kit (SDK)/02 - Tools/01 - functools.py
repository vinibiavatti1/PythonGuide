"""
Functools

* The `functools` module provides tools for working with functions and other
  callable objects
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import functools


###############################################################################
# Reduce Function
###############################################################################


# Reduce
# * Reduce is used to reduce the iterable to a single value, manipulating the
#   current value and the accumulator value
# * Syntax: reduce(function, iterable[, initializer])
x = [5, 2, 7, 8, 3, 5]
y = functools.reduce(lambda acc, el: acc + el, x)
print(y)
# 30


###############################################################################
# Partials
###############################################################################


# Partial
# * Freezes the positional args and kwargs of a function and return a new
#   function with these parameters already set
# * Syntax: partial(func, /, *args, **keywords)
fn = functools.partial(lambda x, y: x + y, 4, 6)
x = fn()
print(x)
# 10


# Partial Method
# * Return a new partialmethod descriptor which behaves like partial except
#   that it is designed to be used as a method definition rather than being
#   directly callable
# * In the example below, we are fixing the argument `state` to `True` to
#   create a new version of the method
# * Syntax: partialmethod(func, /, *args, **keywords)
class Lamp:

    def __init__(self):
        self.state = False

    def set_state(self, state):
        self.state = state

    turn_on = functools.partialmethod(set_state, True)


# Using the partial method
# * In the example bellow, we will use the `turn_on` method to set the state to
#   `True` without needing to pass the `state` argument
x = Lamp()
x.turn_on()  # Same as `x.set_state(True)`
print(x.state)
# True


###############################################################################
# Cache
###############################################################################


# Cache
# * The `@cache` is a decorator that wraps a function with a memoizing callable
# * In other words, it caches the result of the function for the same input
#   without needing to recompute it when it was already computed at least once
# * Syntax: @cache(user_function)
@functools.cache
def factorial(value):
    result = 1
    while value > 1:
        result *= value
        value -= 1
    return result


# Using the cache
# * In the example below, we will compute the factorial of `5` and then we will
#   try to compute it again
x = factorial(5)  # Will compute the value
y = factorial(5)  # Will not recompute the value (it will use cache)
print(x, y, sep=', ')
# 120, 120


# Cached Property
# * Transform a method of a class into a property whose value is computed once
#   and then cached as a normal attribute for the life of the instance
# * Syntax: @cached_property(func)
class Calc:

    def __init__(self, value):
        self.value = value

    @functools.cached_property
    def cubic(self):
        return self.value ** 3


# Using the cached property
# * In the example below, we will compute the cubic of `5` and then we will try
#   to compute it again
x = Calc(5)
y = x.cubic  # Will compute the value
z = x.cubic  # Will not recompute the value (it will use cache)
print(y, z, sep=', ')
# 125, 125


###############################################################################
# Total Ordering
###############################################################################


# Total Ordering
# * Given a class defining one or more rich comparison ordering methods
# * To make the decorator work, the class must define one of the rich
#   comparison methods (`__lt__()`, `__le__()`, `__gt__()`, or `__ge__()`) and
#   supply the `__eq__()` method as mandatory
# * Syntax: @total_ordering
@functools.total_ordering
class CustomValue:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other

    def __lt__(self, other):
        return self.value < other


# Using the total ordering
# * In the example below, we will compare the `CustomValue` class instances
#   using the rich comparison methods
# * Note that the decorator will automatically implement the other rich
#   comparison methods based on the ones we defined
x = CustomValue(5)
print(x == 3, x != 3, x < 3, x <= 3, x > 3, x >= 3, sep=', ')
# False, True, False, False, True, True


###############################################################################
# Overloading
###############################################################################


# Single Dispatch
# * Transform a function into a single-dispatch generic function
# * In other words, it will transform a function into a generic function
#   dispatch where the implementation is chosen based on the type of a single
#   argument
# * Other functions must be registered using the `@<function>.register`
#   decorator to set the other implementations (overloading)
# * Syntax: @singledispatch(func)
@functools.singledispatch
def say(message):
    print('Default:', message)


# Registering (with int type)
# * After defining the generic function, we can register other implementations
#   using the `@<function>.register` decorator
# * These implementations will be chosen based on the type of the argument when
#   calling the function
@say.register
def _(message: int):
    print('Integer:', message)


# Registering (with float type)
# * We will register more one implementation for the `say` function, that will
#   accepts a `float` type argument
@say.register
def _(message: float):
    print('Float:', message)


# Calling the function
# * Note that we will make multiple calls to the `say` function with different
#   types of arguments, and the function will choose the implementation based
#   on the type of the argument
x1 = say('Test')  # Will call the default implementation
x2 = say(1)       # Will call the integer implementation
x3 = say(1.0)     # Will call the float implementation
print(x1, x2, x3, sep=', ')
# Default: Test, Integer: 1, Float: 1.0


# Single Dispatch Method
# * Transforms a method into a single-dispatch generic function
# * A form of generic function dispatch where the implementation is chosen
#   based on the type of a single argument
# * This is the same as above, but for methods
# * Syntax: @singledispatchmethod(func)
# * Syntax: @<function>.register
class CustomMessage:

    @functools.singledispatchmethod
    def say(self, message):
        print('Default:', message)

    @say.register
    def say(self, message: int):
        print('Integer:', message)

    @say.register
    def say(self, message: float):
        print('Float:', message)


# Calling the method
# * As the example above, the method will choose the implementation based on
#   the type of the argument
x = CustomMessage()
y1 = x.say('Test')  # Will call the default implementation
y2 = x.say(1)       # Will call the integer implementation
y3 = x.say(1.0)     # Will call the float implementation
print(y1, y2, y3, sep=', ')
# Default: Test, Integer: 1, Float: 1.0


###############################################################################
# Wraps
###############################################################################


# Wraps
# * The `@wraps` decorator is used to update the wrapper function to look like
#   the wrapped function
# * This is used when creating decorators to keep the original function
#   metadata
# * Syntax: @wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS,
#                  updated=WRAPPER_UPDATES)
def decorator(fn):
    @functools.wraps(fn)
    def wrapper():
        fn()
    return wrapper
