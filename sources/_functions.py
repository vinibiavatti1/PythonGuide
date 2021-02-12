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
def prt(txt):
    print(txt)
prt('abc') # abc

# Function with return
def sum(x, y):
    return x + y
print(sum(5, 5)) # 10

##############################################
# Arbitrary Arguments                        #
##############################################

# *args
def prt(*vals):
    print(vals)
prt(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)

# args, *args
def prt(txt, *vals):
    print(txt, vals)
prt(1, 2, 3, 4, 5) # 1 (2, 3, 4, 5)

# *args, args
def prt(*vals, txt):
    print(vals, txt)
prt(1, 2, 3, 4, 5, txt='6') # (1, 2, 3, 4, 5) 6 NOTE: After *args, the arguments must be set as 'Keyword Arguments'

# *args, *args (You cant have more then once *args)
# def prt(*vals, *txts): ERROR
#     print(vals, txts)

##############################################
# Keyword Arguments                          #
##############################################

# Normal parameter used as keyword argument
def prt(txt):
    print(txt)
prt(txt='abc') # abc

# *args, kargs
def prt(*vals, txt, sep):
    print(vals, sep, txt)
prt(1, 2, 3, txt='four', sep=',') # (1, 2, 3) , four

# Using dict **
args = {'x': 5, 'y': 5}
def sum(x, y):
    return x + y
print(sum(**args)) # 10

##############################################
# Arbitrary Keyword Arguments                #
##############################################

# **kargs
def sum(**vals):
    return vals['x'] + vals['y']
print(sum(x=5, y=5)) # 10

# args, **kargs
def sum(x, **vals):
    return x + vals['y']
print(sum(5, y=5, z=10))

# *args, **kargs
def show(*vals, **txts):
    print(vals, end=' ')
    print(txts)
show(1, 2, 3, a='one', b='two', c='three') # (1, 2, 3) {'a': 'one', 'b': 'two', 'c': 'three'}

# **kargs, args
# If put args after **kargs, it will raise a syntax error
# def sum(**vals, y): SyntaxError: invalid syntax
#     return vals['x'] + y
# print(sum(x=2, 3))

##############################################
# Default parameter values                   #
##############################################

# args
def sum(x=3, y=7):
    return x + y
print(sum()) # 10

# variable / constant value as default
PI = 3.14
def sum(x=PI, y=PI):
    return x + y
print(sum()) # 6.28

# The arbitraty and arbitraty keyword arguments cannot have default values
# def sum(*vals=(1,2,3))  Syntax Error
# def sum(**vals={'a':1}) Syntax Error

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
def prt(txt):
    print(txt)
fn = prt
fn('Hello World') # Hello World

# Passing function as parameters
ages = (10, 20, 15, 18)
def age_filter(age):
    return age >= 18
ages = filter(age_filter, ages)
print(tuple(ages)) # (20, 18)

# Function inside dictionary
def sum(x, y):
    return x + y
dct = {'action': sum}
print(dct['action'](5, 5)) # 10