"""
Dir and Help

* Functions to help the user
* This is usually used for Python REPL

Dir
* Dir returns list of the attributes and methods of any object (functions,
  modules, strings, lists, dictionaries etc.)
* If no argument is passed, dir will return the attributes and methods of the
  current scope, not for the specified object
* Syntax: dir([object])

Help
* Help is used to get help related to the object passed during the call.
* It takes an optional parameter and returns help information. If no argument
  is given, it shows the Python help console
* Syntax: help(*args, **kwargs)
"""
import math


# Dir
# * With no parameters
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'math']


# Dir
# * With some object
print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
# 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb',
# 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp',
# 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
# 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
# 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan',
# 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin',
# 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


# Help
# * With some object
txt = 'Hello World'
help(txt.lower)
# lower() method of builtins.str instance
#    Return a copy of the string converted to lowercase.


# Help
# * Define the help for custom function
def sum(x, y):
    """
    Sum the values of x + y and return it
    """
    return x + y


help(sum)
# sum(x, y)
#    Sum the values of x + y and return it


# Help
# * With no parameters
# NOTE: Do not need to print
help()
# Welcome to Python 3.9's help utility!
#
# If this is your first time using Python, you should definitely check out
# the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.
#
# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To quit this help utility and
# return to the interpreter, just type "quit".
#
# To get a list of available modules, keywords, symbols, or topics, type
# "modules", "keywords", "symbols", or "topics".  Each module also comes
# with a one-line summary of what it does; to list the modules whose name
# or summary contain a given string such as "spam", type "modules spam".
exit()
