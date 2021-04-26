"""
String interpolation

* String interpolation is a process substituting values of variables into
  placeholders in a string
* It is also known by f-strings
* Syntax:
  * f'{<expression> <optional !s, !r, or !a> <optional : format specifier>}'
* Reference:
  * https://zetcode.com/python/fstring/
"""
import decimal
import datetime
import math


###############################################################################
# Interpolation
###############################################################################


# Define an interpolation
# * Use 'f' in front of string to define this string as f-string
name = 'Vini'
age = 26
text = f'{name} is {age} years old'
print(text)
# Vini is 26 years old


# Define an interpolation with percent % (old style)
name = 'Vini'
age = 26
print('%s is %s years old' % (name, age))
# Vini is 26 years old


###############################################################################
# Shortcuts
###############################################################################


# !s
# * Shortcut to str() function
name = 'Vini'
txt = f'The name is: {name!s}'
print(txt)
# The name is: Vini


# !r
# * Shortcut to repr() function
name = 'Vini'
txt = f'The name is: {name!r}'
print(txt)
# The name is: 'Vini'


# !a
# * Shortcut to ascii() function
name = 'Vini'
txt = f'The name is: {name!a}'
print(txt)
# The name is: 'Vini'


###############################################################################
# Multi-line
###############################################################################


# Define multi-line fstring
# * The tuple is used to make multi-line
# * NOTE: No comma is used to make multi-line inside tuple!
sentence = 'Hello World'
msg = (
    f'The most used '
    f'sentence in programming '
    f'is {sentence}'
)
print(msg)
# The most used sentence in programming is Hello World


###############################################################################
# Formats
###############################################################################


# Datetime
# * The format following the Strftime can be used to format dates
dt = datetime.datetime.now()
print(f'The date is: {dt:%d-%m-%Y %H:%M:%S}')
# The date is: 26-04-2021 18:43:37


# Float
# * Floating point values have the f suffix
# * The precision can be set
val = 28.9372
print(f'Value: {val:.2f}')
# Value: 28.94


# Width
# * The width specifier sets the width of the value. The value may be filled
#   with spaces or other characters if the value is shorter than the specified
#   width
for x in range(11):
    print(f'{x:02}', f'{x * 10:3}')
# 00   0
# 01  10
# 02  20
# 03  30
# 04  40
# 05  50
# 06  60
# 07  70
# 08  80
# 09  90
# 10 100


# Justify
# * By default, the strings are justified to the left. We can use the >
#   character to justify the strings to the right
a, b, c = 'a', 'bb', 'ccc'
print(f'{a:>5}')
print(f'{b:>5}')
print(f'{c:>5}')
#     a
#    bb
#   ccc


###############################################################################
# Numeric notations
###############################################################################


# Hexadecimal
val = 255
print(f"{val:x}")
# ff


# Octal
val = 789
print(f"{val:o}")
# 1425


# Scientific
val = 4000
print(f"{val:e}")
# 4.000000e+03


###############################################################################
# Function
###############################################################################


# Call function in fstring
# * We can also call functions in f-strings
print(f'Cos: {math.cos(math.pi)}')
# Cos: -1.0


###############################################################################
# Objects
###############################################################################


# Define a class to represent as string
# * Python f-string accepts objects as well
# * The objects must have either __str__() or __repr__() magic functions
#   defined
class Person:
    def __repr__(self):
        return 'Person name: Vini'


# Format the object
# * The __repr__ or __str__ methods will be called (The str method is priority)
person = Person()
print(f'{person}')
# Person name: Vini


###############################################################################
# Debug
###############################################################################


# Debug with f-string
# * A short way to print values with the originary expression is available
# * With '=' char after the expression, the Python will print the expression
#   and the result
name = 'Vini'
print(f'{name.upper() = }')
# name.upper() = 'VINI''
