"""
Numbers

* Python has three number datatypes (int, float, complex)
* Python doesn't have a `long` datatype since the `int` datatype is
  flexible
###############################################################################
Datatype  Max Size
###############################################################################
int       unlimited (flexible)
float     64 bits
complex   64 bits (Real) + 64 bits (Imaginary)
###############################################################################
"""


###############################################################################
# Assigning Numbers
###############################################################################


# Assigning integers to variables
# * We can assign integers to variables in different ways:
#   * Positive
#   * Negative
#   * Hexadecimal (0x)
#   * Octal (0o)
# * The `int` datatype is flexible, so it can store unlimited numbers (it
#   depends on the memory)
x = 1     # int (positive)
x = -5    # int (negative)
x = 0xF   # int (hexadecimal)
x = 0o7   # int (octal)


# Assigning floats to variables
# * We can assign integers to variables in different ways:
#   * Positive
#   * Negative
#   * Simplified (.)
#   * Scientific (e or E) (the exponent has to be an integer)
# * The `float` datatype is limited to 64 bits, so it can store a limited
#   number of digits
x = 3.5   # float (positive)
x = -0.3  # float (negative)
x = 1.    # float (simplified: 1.0)
x = .1    # float (simplified: 0.1)
x = 2e3   # float (scientific: 2 * 10^3)


# Assigning complex to variables
# * Complex numbers are written with a "j" as the imaginary part `sqrt(-1)`
# * We can assign complex to variables in different ways:
#   * Positive
#   * Negative
#   * Simplified (.)
#   * Scientific (e or E) (the exponent has to be an integer)
x = 2j    # complex (positive)
x = -2j   # complex (negative)
x = 2.j   # complex (simplified: 2.0j)
x = .2j   # complex (simplified: 0.2j)
x = 2e3j  # complex (scientific: 2 * 10^3j)


###############################################################################
# Complex Numbers
###############################################################################


# Accessing the real and imaginary parts of a complex number
# * Python has a built-in complex datatype that can be used to represent a
#   number with a real and imaginary part
# * Since all in Python is an object, the complex datatype is an object that
#   contains two floats (real and imag)
x = 2 + 3j
print(x.real, x.imag)
# 2.0 3.0


# Working with complex numbers
# * The cmath module can be used to work with complex numbers, which contains
#   specific functions for complex numbers
from cmath import sqrt
y = sqrt(x)
print(y)
# (1.6741492280355401+0.8959774761298381j)


###############################################################################
# Truncating Numbers
###############################################################################


# Truncating numbers (int)
# * Since integers in Python are flexible, the value can be as big as the
#   memory allows, so that, the value will not be truncated
x = 213612783613682163621638268362176
print(x)
# 213612783613682163621638268362176


# Truncating numbers (float)
# * When a float value that is bigger than 64 bits is assigned to a variable,
#   the value will be truncated
x = 3.9826321638217637216371283686213
print(x)
# 3.982632163821764


# Truncating numbers (complex)
# * The same behavior as the float datatype will happen with the complex
#   datatype
# * Since the complex datatype is composed of two floats, the value will be
#   truncated when the float value is bigger than 64 bits
x = 3.9826321638217637216371283686213j
print(x)
# 3.982632163821764j


###############################################################################
# Casting
###############################################################################


# Casting numbers
# * A number can be cast by using the built-in functions
# * If the number could not be cast, a ValueError will be raised
x = int(1)          # 1
x = int(1.5)        # 1
x = int('1')        # 1
x = float(1)        # 1.0
x = float(1.5)      # 1.5
x = float('1.5')    # 1.5
x = float('1.')     # 1.0
x = float('.1')     # 0.1
x = float('1e3')    # 1000.0
x = complex(1)      # 1+0j
x = complex(1.5)    # 1.5+0j
x = complex('1')    # 1+0j
x = complex('1.5')  # 1.5+0j


# Coercion
# * Coercion is the implicit conversion of one datatype to another made by the
#   interpreter
# * Some cases, the coercion will be made without any problem, but in other
#   cases, a manual conversion is required to prevent runtime errors
# * In the case below, the "10" will be cast to float before the sum
x = 3.5 + 10  # Equivalent to x = 3.5 + float(10)


# Casting to int with a custom base
# * The int() function allows to specify numbers in other base, but setting the
#   base parameter
# * It can be useful to cast hexadecimal, octal, etc... numbers to int,
#   without using a wrong base
x = int('15')           # 15 is a decimal number
y = int('15', base=16)  # 15 is a hexadecimal number
print(x, y, sep=', ')
# 15, 21


###############################################################################
# Underscore
###############################################################################


# Using underscore in numbers
# * The underscore can be used in numbers to facilitate reading
# * It will not change the value of the number
x = 1_000_000
y = 2.123_456
z = 3.123_456j
w = 2e3_1
print(x, y, z, w)
# 1000000 2.123456 3.123456j 2e+31
