"""
Parameters

* Function parameters are the names listed in the function's definition
* Function arguments are the real values passed to the function
* Parameters are initialized to the values of the arguments supplied
* There are different kind of parameters that accepts the arguments in a
  different way
* There are different definitions to specify a rule for arguments in a function

###############################################################################
Argument / Definition               Example
###############################################################################
Positional arguments                fn(3, 4)
Keyword arguments                   fn(age=26)
Default arguments                   def fn(name='Vini')
Arbitrary positional arguments      def fn(*args)
Arbitrary keyword arguments         def fn(**kwargs)
Bare *                              def fn(name, *, age)
Slash /                             def fn(x, y, /)
###############################################################################
"""
from math import pi


###############################################################################
# Positional Arguments | (fn(3, 4))
###############################################################################


# Define a function with positional arguments
# * Positional arguments are arguments that can be called by their position in
#   the function definition
def calc(x, y):
    return x + y


# Call function with positional arguments
# * To set the positional arguments, you must follow the positions of each
#   parameter in a function
result = calc(7, 3)
print(result)
# 10


###############################################################################
# Keyword Arguments | (fn(age=26))
###############################################################################


# Define a function with keyword arguments
# * Keyword arguments (or named arguments) are values that, when passed into a
#   function, are identifiable by specific parameter names
def message(name, surname):
    return name + ' ' + surname


# Call a function with keyword arguments
# * To set the keyword arguments, you can specify the name of the arguyment and
#   set the value for this
result = message(name='Vinicius', surname='Biavatti')
print(result)
# Vinicius Biavatti


# Umpack dictionary as keyword arguments
# * You can umpack a dictionary to pass its values as keyword arguments to a
#   function call
# * To umpack the values from a dictionary, you can use the "**" char in front
#   of the name of the dict inside the function arguments
# * NOTE: The dict must contains the exact mandatory arguments for the function
args = {"name": 'Vinicius', "surname": 'Biavatti'}
result = message(**args)
print(result)
# Vinicius Biavatti


###############################################################################
# Default arguments | def fn(name='Vini')
###############################################################################


# Define a function with default arguments
# * To define a default value for argument, you can specify the value using
#   the "=" operator.
# * NOTE: You cannot define a positional argument after a default argument,
#   cause the interpreter will no be able to recognise the kind of argument
def text(message, dot=False):
    if dot:
        message += '.'
    return message


# Call a function with default arguments
# * You dont need to define the argument when it has a default value.
# * You can change the value of the default argument if you want
r1 = text('Hello world')
r2 = text('Thank you', True)
print(r1, r2, sep=', ')
# Hello world, Thank you.


# Define a function with default arguments as constants or variables
# * You can define a default value for some argument as a constant or variable
#   value
def calc_degree(rad=pi):
    return rad


# Define a positional argument after a default argument
# * This is not allowed and a SyntaxError will be raised
"""
def error(x=1, y):
    pass

SyntaxError: non-default argument follows default argument
"""


###############################################################################
# Arbitrary positional arguments | def fn(*args)
###############################################################################


# Define a function with arbitrary positional arguments
# * To define some argument as an arbitrary you must use the "*" char in front
#   of the name of the argument
# * The values for this argument can be passed separated by comma "," and these
#   will be represented as a tuple
# * This can be used when you want to pass more then once value for one
#   parameter
# * The default name used for this argument is *args
def sum_elements(*args):
    result = 0
    for element in args:
        result += element
    return result


# Call a function with arbitrary arguments
# * To set the arbitraty arguments, you can specify each element separated with
#   comma
# * These elements will became a tuple inside the function
result = sum_elements(1, 5, 7, 2)
print(result)
# 15


# Define positional arguments before arbitraty arguments
# * The positional arguments before arbitraty arguments can be set normally
def sum_val_from_elements(val, *args):
    result = []
    for element in args:
        result.append(element + val)
    return result


# Call a function with arbitrary arguments and positional arguments
# * To call a function that contains positional arguments before an arbitraty,
#   you can pass the positional normally
result = sum_val_from_elements(3, 4, 6, 9, 5)  # Arguments: (3, (4, 6, 9, 5))
print(result)
# [7, 9, 12, 8]


# Define positional arguments after arbitraty arguments
# * The positional arguments after arbitraty arguments must be set as keyword
#   arguments as mandatory
def sub_val_from_elements(*args, val):
    result = []
    for element in args:
        result.append(element - val)
    return result


# Call a function with arbitrary arguments and positional arguments
# * To call a function that contains positional arguments after an arbitraty,
#   you must pass it as keyword argument
result = sub_val_from_elements(4, 6, 9, 5, val=3)
print(result)
# [1, 3, 6, 2]


# Define a default value for arbitraty argument is not valid
# * Arbitrary arguments don't accept default values
"""
def sum_elements(*args=(1, 2, 3)):
    pass

SyntaxError: invalid syntax
"""


# Define function with more arbitraty arguments
# * This is not possible, and the function can has just one arbitraty argument
"""
def more_arbitrary(*args1, *args2):
    pass

SyntaxError: invalid syntax
"""


###############################################################################
# Arbitrary keyword arguments | def fn(**kwargs)
###############################################################################


# Define a function with arbitrary keyword arguments
# * To define some argument as an arbitrary keyword you must use the "**" char
#   in front of the name of the argument
# * The values for this argument can be passed as keyword arguments
# * This can be used when you want to pass any number of arguments to the
#   function as keyword arguments
# * The arguments will become a dictionary inside the function
# * The default name used for this argument is **kwargs
def mount_text(**kwargs):
    txt = ''
    for word in kwargs.values():
        txt += word + ' '
    return txt


# Call a function with arbitrary keyword arguments
# * To set the arbitraty keyword arguments, you can specify each element as
#   a keyword argument
# * These elements will became a dictionary inside the function
result = mount_text(header='Hello', footer='World!')
print(result)
# Hello World!


# Umpack dictionary as arbitrary keyword arguments
# * You can umpack a dictionary to pass its values as kwargs to a function call
# * To umpack the values from a dictionary, you can use the "**" char in front
#   of the name of the dict inside the function arguments
args = {"name": 'Vinicius', "surname": 'Biavatti'}
result = mount_text(**args)
print(result)
# Vinicius Biavatti


# Define a function with *args and **kwargs
# * You can use both (*args and **kwargs) as arguments for some function
# * This is the most comprehensive way in which it makes the function as
#   flexible as possible
def join(*args, **kwargs):
    txt = ' '.join(args)
    if kwargs.get('rev', False):
        return ''.join(reversed(txt))
    return txt


# Call a function with *args and **kwargs
# * To call the function that accepts *args and **kwargs you can follow the
#   same way to define both of these arguments
r1 = join('Hello', 'World')            # ('Hello', 'World') {}
r2 = join('Hello', 'World', rev=True)  # ('Hello', 'World') {'rev': True}
print(r1, r2, sep=', ')
# Hello World, dlroW olleH


# Define a function with positional arguments after kwargs
# * This is not possible. Its is recommended to keep the kwargs as the last
#   argument in the function
"""
def mount_text(**kwargs, arg):
    pass

SyntaxError: invalid syntax
"""


###############################################################################
# Bare definition "*" | def fn(name, *, age)
###############################################################################


# Define function with a bare definition
# * Bare is used to force the parameters after bare "*" to be used as
#   keyword-only parameters
# * To define a bare, you must use the "*" symbol as a parameter
def sum_values(x, y, *, z):
    return x + y + z


# Call function with a bare definition
# * Bare definitions change the consistency of the function, limiting the
#   parameters after the bare be set as keyword arguments only
# * If you try to set these arguments as positional, a TypeError will be
#   ocurred
result = sum_values(3, 4, z=5)
print(result)
# 12


# Call function with a bare passing arg as positional
# * This will raise a TypeError
"""
result = sum_values(3, 4, 5)

TypeError: sum_values() takes 2 positional arguments but 3 were given
"""


###############################################################################
# Slash definition "/" | fn(x, y, /)
###############################################################################


# Define function with a slash definition
# * This is the oposite for the bare, that is used to force the parameters
#   before slash "/" to be used as positional-only parameters
# * To define a slash, you must use the "/" symbol as a parameter
def sub_values(x, y, z, /):
    return x + y + z


# Call function with a slash definition
# * Slash definitions change the consistency of the function, limiting the
#   parameters before the slash to be set as positional arguments only
# * If you try to set these arguments as keyword arguments, a TypeError will be
#   ocurred
result = sub_values(3, 4, 5)
print(result)
# 12


# Call function with a slahs passing arg as keyword
# * This will raise a TypeError
"""
result = sub_values(3, 4, z=5)

TypeError: sub_values() got some positional-only arguments passed as keyword
arguments: 'z'
"""


###############################################################################
# Order
###############################################################################


# Define a function using the correct order for arguments
# * NOTE: You have to follow this order to avoid consistency problems
# * The order is:
#   * 1. Positional arguments         (x, y)
#   * 2. Arbitrary arguments          (x, y, *args)
#   * 3. Default arguments            (x, y, *args, z=True)
#   * 4. Arbitrary Keyword arguments  (x, y, *args, z=True, **kwargs)
def order(x, y, *args, other=True, **kwargs):
    pass


# Call a function using the correct order for arguments
# * This is an example to call a function following the correct order
order(4, 6)
order(4, 6, 'a', 'b', 'c')
order(4, 6, 'a', 'b', 'c', other=False)
order(4, 6, 'a', 'b', 'c', other=False, process=True)


# Scheme
# * The scheme used for the order arguments to the previous function is:
order(4, 6, 'a', 'b', 'c', other=False, process=True)
#    [pos-] [*args-------] [default---] [**kwargs---]
