"""
Fractions

* The fractions module provides support for rational number arithmetic
* A fraction is a rational number with both a numerator and a denominator
* The table below shows the available ways to create a fraction
###############################################################################
Initialization                          Example
###############################################################################
Fraction(numerator=0, denominator=1)    Fraction(4, 3)
Fraction(other_fraction)                Fraction(Fraction(4, 3))
Fraction(float)                         Fraction(0.75)
Fraction(decimal)                       Fraction(Decimal('0.75'))
Fraction(string)                        Fraction('15/7')
###############################################################################
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module Fraction class
# * To start using fractions, we have to import the Fraction class from the
#   fractions module
# * This class provides support for rational number arithmetic
from fractions import Fraction


###############################################################################
# Creating a Fraction
###############################################################################


# Creating a default fraction
# * To create a fraction, we can use the Fraction class passing the numerator
#   and denominator as arguments
# * These arguments are optional and default to 0 and 1, respectively
# * There are other ways to create a fraction, as shown in the table above
x = Fraction()
print(x)
# 0


# Creating a fraction (with numerator and denominator)
# * The numerator and denominator can be passed as arguments to create a new
#   fraction
x = Fraction(3, 4)
print(x)
# 3/4


# Creating a fraction (based on another fraction)
# * Another fraction can be given as an argument to create a new fraction
x = Fraction(3, 4)
y = Fraction(x)
print(y)
# 3/4


# Creating a fraction (with a float)
# * A float number can be passed as an argument to create a new fraction
# * The float number will be converted to a fraction
x = Fraction(0.75)
print(x)
# 3/4


# Creating a fraction (with a decimal)
# * A decimal number can be passed as an argument to create a new fraction
# * The decimal number will be converted to a fraction
# * For this example, we had to import the Decimal class from the decimal
#   module
from decimal import Decimal
x = Fraction(Decimal('0.75'))
print(x)
# 3/4


# Creating a fraction (with a string)
# * A string can be passed as an argument to create a new fraction
# * The string will be converted to a fraction
# * The string must have the format 'numerator/denominator'
x = Fraction('3/4')
print(x)
# 3/4


###############################################################################
# Fraction Properties
###############################################################################


# Numerator
# * The numerator property returns the numerator of the fraction
x = Fraction('3/4')
print(x.numerator)
# 3


# Denominator
# * The denominator property returns the denominator of the fraction
x = Fraction('3/4')
print(x.denominator)
# 4


###############################################################################
# Fraction Operations
###############################################################################


# Sum
# * The Fraction class implements the Arithmetic Operations Protocol which
#   allows us to use the arithmetic operators with fractions
# * The sum of two fractions can be calculated using the '+' operator
# * Note that the result is automatically simplified, and on this case, the
#   result is an integer
x = Fraction('3/4')
y = Fraction('1/4')
z = x + y
print(z)
# 1


# Subtraction
# * The subtraction of two fractions can be calculated using the '-' operator
x = Fraction('3/4')
y = Fraction('1/4')
z = x - y
print(z)
# 1/2


# Multiplication
# * The multiplication of two fractions can be calculated using the '*'
#   operator
x = Fraction('3/4')
y = Fraction('1/4')
z = x * y
print(z)
# 3/16


# Division
# * The division of two fractions can be calculated using the '/' operator
x = Fraction('3/4')
y = Fraction('1/4')
z = x / y
print(z)
# 3


# Module
# * The module of two fractions can be calculated using the '%' operator
x = Fraction('3/4')
y = Fraction('1/4')
z = x % y
print(z)
# 0


# Power
# * The power of a fraction can be calculated using the '**' operator
x = Fraction('3/4')
y = Fraction('2/1')
z = x ** y
print(z)
# 9/16


###############################################################################
# Fraction Methods
###############################################################################


# as_integer_ratio()
# * The `as_integer_ratio()` method returns a tuple with the numerator and
#   denominator of the fraction
x = Fraction('3/4')
y = x.as_integer_ratio()
print(y)
# (3, 4)


# is_integer()
# * The `is_integer()` method returns True if the fraction is an integer
x = Fraction('4/4')
y = x.is_integer()
print(y)
# True


# limit_denominator(max_denominator=1000000)
# * The `limit_denominator()` method finds and returns the closest fraction to
#   self that has a denominator at most `max_denominator`
# * This method is useful for finding rational approximations to a given
#   floating-point number
x = Fraction(1.1)
y = x.limit_denominator(10)
print(y)
# 11/10
