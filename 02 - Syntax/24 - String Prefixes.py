"""
String Prefixes

* In Python, strings can be prefixed with:
###############################################################################
Prefix      Description         Example
###############################################################################
r           Raw string          r'Hello, World\n'
b           Bytes string        b'Hello, World!'
f           Formatted string    f'Hello, {name}!'
###############################################################################
* Raw strings are used to ignore escape sequences
* Bytes strings are used to represent binary data
* Formatted strings are used to format strings with variables (interpolation)
"""


###############################################################################
# Raw String
###############################################################################


# Defining a raw string
# * To define a raw string, use the 'r' prefix before the string literal
# * Raw strings are used to ignore escape sequences, like '\n', '\t', etc...
# * It is useful when defining regular expressions, file paths, etc...
x = r'Hello\nWorld'
print(x)
# Hello\nWorld


# Defining a regular expression
# * Raw strings are commonly used to define regular expressions
# * In this case, the escape sequences are not processed
x = r'\$\s[0-9,]+'
print(x)
# \$\s[0-9,]+


###############################################################################
# Bytes String
###############################################################################


# Defining a bytes string
# * Bytes string are used to represent binary data
# * To define a bytes string, use the 'b' prefix before the string literal
# * NOTE: The object type is 'bytes' when using the 'b' prefix, not 'str'
x = b'Hello, World!'
print(x, type(x))
# b'Hello, World!' <class 'bytes'>


###############################################################################
# Formatted String (Interpolation)
###############################################################################


# Defining a formatted string
# * We can use the interpolation syntax to define formatted strings
# * To define a formatted string, use the 'f' prefix before the string literal
# * Formatted strings are used to format strings with variables, without
#   needing to concatenate them
x = 'John'
y = f'Hello, {x}'
print(x)
# Hello, John


# Defining a formatted string (using other data types)
# * When using variables with other data types, the data will be automatically
#   converted to string
x1 = 10
x2 = 5.25
x3 = [1, 2, 3]
y = f'x1: {x1}, x2: {x2}, x3: {x3}'
print(y)
# x1: 10, x2: 5.25, x3: [1, 2, 3]


# Functions
# * We can call functions in the interpolated strings
x = f'{str(1)}'
print(x)
# 1


# Expressions
# * We can use expressions inside the interpolated strings
# * The syntax is: {expression}
x = 10
y = f'{x + 5}'
print(y)
# 15


# Conversion functions
# * We can use the '!' character to apply string conversion functions
# * The available functions are:
#   * !s: str()
#   * !r: repr()
#   * !a: ascii()
x = '10'
y = f'{x!s}, {x!r}, {x!a}'
print(y)
# 10, '10', '10'


# Numeric notations
# * We can use the 'x', 'o', and 'e' format specifiers to convert numbers to
#   hexadecimal, octal, and scientific notations
# * NOTE: The variable must be a number to use these format specifiers
x = 255
y = f'{x:x}, {x:o}, {x:e}'
print(y)
# ff, 377, 2.550000e+02


# Interpolation width
# * We can use the ':' character with a number to specify the width of the
#   string
# * The string will be padded with spaces to match the width
# * We can use the '<', '>', and '^' characters to justify the string to the
#   left, right, and center
x = 'Hello'
y1 = f'{x:10}'
y2 = f'{x:<10}'  # Left (default)
y3 = f'{x:^10}'  # Center
y4 = f'{x:>10}'  # Right
print(y1, y2, y3, y4, sep='\n')
# Hello
# Hello
#   Hello
#      Hello


# Number precision
# * We can use the ':' character with a '.' and a number to specify the
#   precision of the value into the string
# * The precision is used to limit the number of characters in the string
#   (for numbers, it is the number of decimal places)
x = 5.123456789
y = f'{x:.2f}'
print(y)
# 5.12


# Comma separator
# * We can use the ',' character to add a comma separator to the number
x = 1234567890
y = f'{x:,}'
print(y)
# 1,234,567,890


# Date formatting
# * We can set the date format in interpolated strings after the ':' character
# * For this example, we must import the 'datetime' module to create a date
#   object
from datetime import datetime
x = datetime.now()
y = f'{x:%Y-%m-%d %H:%M:%S}'
print(y)
# 2024-03-26 15:01:09


# Ternary operator
# * We can use the ternary operator in the interpolated strings
# * The syntax is: {value if condition else value}
x = 10
y = f'{x if x > 5 else 0}'
print(y)
# 10


# Multiline f-strings
# * We can use the multiline syntax to define formatted strings
# * The multiline syntax is: f'''string'''
x = 'Hello'
y = f'''
    {x}
    World
'''
print(y)
# Hello
# World


# Debugging
# * There is a special format specifier '=' to set the variable name and value
#   into the string
# * It can be used to debug the code, without needing to concatenate the string
#   with the variable name and value
# * The syntax is: {variable=}
x = 10
y = f'{x=}'
print(y)
# x=10


