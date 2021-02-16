"""
Function examples

* In Python a function is defined using the "def" keyword
* A "parameter" is the variable listed inside the parentheses in the function definition.
* An "argument" is the value that is sent to the function when it is called.
"""
##############################################
# Intro                                      #
##############################################

# Function
def prt():
    print('Function!') 
prt() # Function!

# Function with parameters
def prt2(txt):
    print(txt)
prt2('abc') # abc

# Function with return
def sum(x, y):
    return x + y
print(sum(5, 5)) # 10

##############################################
# Arbitrary Arguments                        #
##############################################

# *args
def prt3(*args):
    print(args)
prt3(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)

# args, *args
def prt4(txt, *args):
    print(txt, args)
prt4(1, 2, 3, 4, 5) # 1 (2, 3, 4, 5)

# *args, args
def prt5(*args, txt):
    print(args, txt)
prt5(1, 2, 3, 4, 5, txt='6') # (1, 2, 3, 4, 5) 6 NOTE: After *args, the arguments must be set as 'Keyword Arguments'

# *args, *args (You cant have more then once *args)
# def prt(*args, *txts): ERROR
#     print(vals, txts)

##############################################
# Keyword Arguments                          #
##############################################

# Normal parameter used as keyword argument
def prt6(txt):
    print(txt)
prt6(txt='abc') # abc

# *args, kargs
def prt7(*args, txt, sep):
    print(args, sep, txt)
prt7(1, 2, 3, txt='four', sep=',') # (1, 2, 3) , four

# Using dict **
args = {'x': 5, 'y': 5}
def sum2(x, y):
    return x + y
print(sum2(**args)) # 10

##############################################
# Arbitrary Keyword Arguments                #
##############################################

# **kargs
def sum3(**kwargs):
    return kwargs['x'] + kwargs['y']
print(sum3(x=5, y=5)) # 10

# args, **kargs
def sum4(x, **kwargs):
    return x + kwargs['y']
print(sum4(5, y=5, z=10))

# *args, **kargs
def show(*args, **kwargs):
    print(args, end=' ')
    print(kwargs)
show(1, 2, 3, a='one', b='two', c='three') # (1, 2, 3) {'a': 'one', 'b': 'two', 'c': 'three'}

# **kargs, args
# If put args after **kargs, it will raise a syntax error
# def sum(**args, y): SyntaxError: invalid syntax
#     return vals['x'] + y
# print(sum(x=2, 3))

##############################################
# Default parameter values                   #
##############################################

# args
def sum6(x=3, y=7):
    return x + y
print(sum6()) # 10

# variable / constant value as default
PI = 3.14
def sum7(x=PI, y=PI):
    return x + y
print(sum7()) # 6.28

# The arbitraty and arbitraty keyword arguments cannot have default values
# def sum(*args=(1,2,3))  Syntax Error
# def sum(**args={'a':1}) Syntax Error

##############################################
# Recursive Function                         #
##############################################

# Recursive operation
def arithmetic_progression(start, amount, result=0):
    if start == amount:
        return result
    else:
        return arithmetic_progression(start + 1, amount, result + start)
print(arithmetic_progression(1, 10)) # 45

##############################################
# Functions as variables                     #
##############################################

# Define variable as function
def prt8(txt):
    print(txt)
fn = prt8
fn('Hello World') # Hello World

# Passing function as parameters
ages = (10, 20, 15, 18)
def age_filter(age):
    return age >= 18
ages = filter(age_filter, ages)
print(tuple(ages)) # (20, 18)

# Function inside dictionary
def sum8(x, y):
    return x + y
dct = {'action': sum8}
print(dct['action'](5, 5)) # 10

##############################################
# Functions with more return values          #
##############################################
# NOTE: To return more values some collection has to be used like tuples

# Tuple (Implicit)
def sum_and_sub(x, y):
    return x - y, x + y # This is a implicit tuple creation
sum, sub = sum_and_sub(5, 5)
print(sum, sub, sep=', ') # 10, 0

# Tuple
def sum_and_sub2(x, y):
    return (x - y, x + y)
(sum, sub) = sum_and_sub2(5, 5)
print(sum, sub, sep=', ') # 10, 0

##############################################
# Functions with datatype                    #
##############################################

# Function parameters and return with type
def sum_with_type(x: int, y:int) -> int:
    return x + y
print(sum_with_type(5, 5)) # 10