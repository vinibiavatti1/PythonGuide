"""
Math module

* This module provides access to the mathematical functions defined by the C
  standard
* Reference:
  * https://docs.python.org/3/library/math.html
* NOTE: Just most common functions are shown in this file
"""
import math


###############################################################################
# Number-theoretic and representation functions
###############################################################################


# ceil(x)
# * Return the ceiling of x, the smallest integer greater than or equal to x
print(math.ceil(5.7))
# 6


# floor(x)
# * Return the floor of x, the largest integer less than or equal to x
print(math.floor(5.7))
# 5


# fabs(x)
# * Return the absolute value of x
print(math.fabs(-7))
# 7.0


# factorial(x)
# * Return x factorial as an integer
print(math.factorial(5))
# 120


# gcd(a, b)
# * Return the greatest common divisor of the specified integer arguments
print(math.gcd(3, 6))
# 3


# isfinite(x)
# * Return True if x is neither an infinity nor a NaN, and False otherwise
print(math.isfinite(4.89))
# True


# isinf(x)
# * Return True if x is a positive or negative infinity, and False otherwise
print(math.isinf(float('inf')))
# True


# isnan(x)
# * Return True if x is a NaN (not a number), and False otherwise
print(math.isnan(float('nan')))
# True


# isqrt(n)
# * Return the integer square root of the nonnegative integer n
print(math.isqrt(25))
# 5


# lcm(*integers)
# * Return the least common multiple of the specified integer arguments
print(math.lcm(12, 30))
# 60


# modf(x)
# * Return the fractional and integer parts of x
print(math.modf(7.5))
# (0.5, 7.0)


# prod(iterable, *, start=1)
# * Calculate the product of all the elements in the input iterable
print(math.prod([1, 2, 3, 4, 5]))
# 120


# trunc(x)
# * Return the Real value x truncated to an Integral (usually an integer)
# * Delegates to x.__trunc__()
print(math.trunc(15.5))
# 15


###############################################################################
# Power and logarithmic functions
###############################################################################


# log(x[, base])
# * With one argument, return the natural logarithm of x (to base e)
# * With two arguments, return the logarithm of x to the given base
print(math.log(2))
# 0.6931471805599453


# pow(x, y)
# * Return x raised to the power y
print(math.pow(2, 8))
# 256.0


# sqrt(x)
# * Return the square root of x
print(math.sqrt(25))
# 5.0


###############################################################################
# Trigonometric functions
###############################################################################


# acos(x)
# * Return the arc cosine of x, in radians
print(math.acos(1))
# 0.0


# asin(x)
# * Return the arc sine of x, in radians
print(math.asin(1))
# 1.5707963267948966


# atan(x)
# * Return the arc tangent of x, in radians
print(math.atan(1))
# 0.7853981633974483


# atan2(y, x)
# * Return atan(y / x), in radians. The result is between
print(math.atan2(5, 3))
# 1.0303768265243125


# cos(x)
# * Return the cosine of x radians
print(math.cos(1))
# 0.5403023058681398


# sin(x)
# * Return the sine of x radians
print(math.cos(1))
# 0.5403023058681398


# tan(x)
# * Return the tangent of x radians
print(math.cos(1))
# 0.5403023058681398


# dist(p, q)
# * Return the Euclidean distance between two points p and q
print(math.dist([5, 3], [7, 8]))
# 5.385164807134505


# hypot(*coordinates)
# * Return the Euclidean norm
# * For a two dimensional point (x, y), this is equivalent to computing the
#   hypotenuse of a right triangle using the Pythagorean theorem,
#   sqrt(x*x + y*y)
print(math.hypot(3, 4))
# 5.0


###############################################################################
# Angular conversion
###############################################################################


# degrees(x)
# * Convert angle x from radians to degrees
print(math.degrees(3.141592653589793))
# 180.0


# radians(x)
# * Convert angle x from degrees to radians
print(math.radians(180))
# 3.141592653589793


###############################################################################
# Hyperbolic functions
###############################################################################


# cosh(x)
# * Return the hyperbolic cosine of x
print(math.cosh(0.5))
# 1.1276259652063807


# sinh(x)
# * Return the hyperbolic sine of x
print(math.sinh(0.5))
# 0.5210953054937474


# tanh(x)
# * Return the hyperbolic tangent of x
print(math.tanh(0.5))
# 0.46211715726000974


# acosh(x)
# * Return the inverse hyperbolic cosine of x
print(math.acosh(2))
# 1.3169578969248166


# asinh(x)
# * Return the inverse hyperbolic sine of x
print(math.asinh(2))
# 1.4436354751788103


# atanh(x)
# * Return the inverse hyperbolic tangent of x
print(math.atanh(0.1))
# 0.1003353477310756


###############################################################################
# Constants
###############################################################################


# pi
# * The mathematical constant π
print(math.pi)
# 3.141592653589793


# e
# * The mathematical constant euler
print(math.e)
# 2.718281828459045


# tau
# * The mathematical constant τ (Equivalent to 2π)
print(math.tau)
# 6.283185307179586


# inf
# * A floating-point positive infinity
# * For negative infinity, use -math.inf
print(math.inf)
# inf


# nan
# * A floating-point “not a number” (NaN) value
print(math.nan)
# nan
