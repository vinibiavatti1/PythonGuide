"""
Function

* In Python a function is defined using the "def" keyword
* A "parameter" is the variable listed inside the parentheses in the function
  definition.
* An "argument" is the value that is sent to the function when it is called
* Functions are used to decompose problems
* When pass arguments to a function that doesnt have parameters, it will raise
  a TypeError
"""


# -----------------------------------------------------------------------------
# Intro


# Function
def prt():
    print('Function!')


prt()
# Function!


# Function with parameters
def prt2(txt):
    print(txt)


prt2('abc')
# abc


# Function with return
def sum(x, y):
    return x + y


print(sum(5, 5))
# 10


# Function returns None if no return provided
def strange_function(n):
    if(n % 2 == 0):
        return True


print(strange_function(0))  # True
print(strange_function(1))  # None


# -----------------------------------------------------------------------------
# Arbitrary Arguments (*args)
# * Used to use more values as parameters (It will become a tuple)


# *args
def prt3(*args):
    print(args)


prt3(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)


# args, *args
def prt4(txt, *args):
    print(txt, args)


prt4(1, 2, 3, 4, 5)
# 1 (2, 3, 4, 5)


# *args, args
def prt5(*args, txt):
    print(args, txt)


prt5(1, 2, 3, 4, 5, txt='6')
# (1, 2, 3, 4, 5) 6
# NOTE: After *args, the arguments must be set as 'Keyword Arguments'


# *args, *args (You cannot have more then once *args)
# def prt(*args, *txts): ERROR
#     print(vals, txts)


# -----------------------------------------------------------------------------
# Keyword Arguments (kwargs)
# * Used to accept arguments defined with their name


# Normal parameter used as keyword argument
def prt6(txt):
    print(txt)


prt6(txt='abc')
# abc


# *args, kargs
def prt7(*args, txt, sep):
    print(args, sep, txt)


prt7(1, 2, 3, txt='four', sep=',')
# (1, 2, 3) , four


# Using dict **
args = {'x': 5, 'y': 5}


def sum2(x, y):
    return x + y


print(sum2(**args))
# 10


# -----------------------------------------------------------------------------
# Arbitrary Keyword Arguments (**kwargs)
# * Used to define dict that will get the kwargs


# **kargs
def sum3(**kwargs):
    return kwargs['x'] + kwargs['y']


print(sum3(x=5, y=5))
# 10


# args, **kargs
def sum4(x, **kwargs):
    return x + kwargs['y']


print(sum4(5, y=5, z=10))
# 10


# *args, **kargs
def show(*args, **kwargs):
    print(args, end=' ')
    print(kwargs)


show(1, 2, 3, a='one', b='two', c='three')
# (1, 2, 3) {'a': 'one', 'b': 'two', 'c': 'three'}


# **kargs, args
# If put args after **kargs, it will raise a syntax error
# def sum(**args, y): SyntaxError: invalid syntax
#     return vals['x'] + y
# print(sum(x=2, 3))


# -----------------------------------------------------------------------------
# Default parameter values (fn(value=1))
# * Set the default value when the argument is not inserted


# args
def sum6(x=3, y=7):
    return x + y


print(sum6())
# 10


# variable / constant value as default
PI = 3.14


def sum7(x=PI, y=PI):
    return x + y


print(sum7())
# 6.28


# The arbitraty and arbitraty keyword arguments cannot have default values
# def sum(*args=(1,2,3))  Syntax Error
# def sum(**args={'a':1}) Syntax Error


# After default parameter, a position parameter cannot be defined
# def sum(x, y=1, z): SyntaxError: non-default argument follows default
#     pass            argument


# -----------------------------------------------------------------------------
# Recursive Function (fn(): fn())
# * Function that call himselves inside


# Recursive operation
def arithmetic_progression(start, amount, result=0):
    if start == amount:
        return result
    else:
        return arithmetic_progression(start + 1, amount, result + start)


print(arithmetic_progression(1, 10))
# 45


# -----------------------------------------------------------------------------
# Functions as variables (var = fn)
# * Define a variable with function


# Define variable as function
def prt8(txt):
    print(txt)


fn = prt8
fn('Hello World')
# Hello World


# Passing function as parameters
ages = (10, 20, 15, 18)


def age_filter(age):
    return age >= 18


ages = filter(age_filter, ages)
print(tuple(ages))
# (20, 18)


# Function inside dictionary
def sum8(x, y):
    return x + y


dct = {'action': sum8}
print(dct['action'](5, 5))
# 10


# -----------------------------------------------------------------------------
# Functions with more return values (return x, y)
# NOTE: To return more values some collection has to be used like tuples


# Tuple (Implicit)
def sum_and_sub(x, y):
    # This is a implicit tuple creation
    return x - y, x + y


sum, sub = sum_and_sub(5, 5)
print(sum, sub, sep=', ')
# 10, 0


# Tuple
def sum_and_sub2(x, y):
    return (x - y, x + y)


(sum, sub) = sum_and_sub2(5, 5)
print(sum, sub, sep=', ')
# 10, 0


# -----------------------------------------------------------------------------
# Functions with datatype (fn(x: int) -> str)
# * Define the datatype to parameters and return


# Function parameters and return with type
def sum_with_type(x: int, y: int) -> int:
    return x + y


print(sum_with_type(5, 5))
# 10


# -----------------------------------------------------------------------------
# Bare * (fn(x, *, y))
# * Used to force the caller to use named arguments for arguments after bare


def sum_bare(x, y, *, z):
    return x + y + z


sum_bare(1, 2, z=3)
# sum_bare(1, 2, 3)  ERROR (Bare cannot let to put the kwargs as normal arg)


# -----------------------------------------------------------------------------
# Slash / (fn(x, y, /))
# * Used to force the parameters before / to be used as positional parameters


def sum_slash(x, y, /, z):
    return x + y + z


sum_slash(1, 2, z=3)
# sum_slash(1, y=2, z=3)  ERROR (sum_slash() got some positional-only arguments
#                         passed as keyword arguments: 'y')


# -----------------------------------------------------------------------------
# Parameters coorect sequence
# 1. Required args     (x, y)
# 2. Arbitrary args    (x, y, *args)
# 3. Default args      (x, y, *args, z=True)
# 4. Arbitrary kwargs  (x, y, *args, z=True, **kwargs)


# Parameters in order
def do(x, y, *args, z=True, **kwargs):
    pass


do(1, '2')
do(1, '2', 3, 4, 5)
do(1, '2', 3, 4, 5, z=False)
do(1, '2', 3, 4, 5, z=False, h=True)

# Scheme
# ----------------------------------
#  args     *args   default   **kw
# .--^--.  .--^--.  .--^--.  .--^--.
do(1, '2', 3, 4, 5, z=False, h=True)


# -----------------------------------------------------------------------------
# Arguments in no parameters function


# Type error
def nothing():
    pass


# nothing(1)  TypeError: nothing() takes 0 positional arguments but 1 was given
# nothing(x=1) TypeError: nothing() got an unexpected keyword argument 'x'


# -----------------------------------------------------------------------------
# Shadowing
# * Mechanism to differs the parameters from the varaibles


# Shadowing example
def prt_name(name):  # Name will be shadow, to dont change the actual name var
    print(name)


name = 'Vini'
prt_name('Ana')  # Ana
print(name)      # Vini
