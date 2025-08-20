"""
Math

* The math module provides mathematical functions
* These functions cannot be used with complex numbers; use the functions of
  the cmath module if you require support for complex numbers
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import math


###############################################################################
# Number-theoretic functions
###############################################################################


# comb(n, k)
# * Return the number of ways to choose k items from n items without repetition
#   and without order
# * This is often referred to as "n choose k"
x = math.comb(5, 2)
print(x)
# 10


# factorial(n)
# * Return n factorial
x = math.factorial(5)
print(x)
# 120


# gcd(a, b)
# * Return the greatest common divisor of the specified integer arguments
x = math.gcd(3, 6)
print(x)
# 3


# isqrt(n)
# * Return the integer square root of the nonnegative integer n
x = math.isqrt(25)
print(x)
# 5


# lcm(a, b)
# * Return the least common multiple of the specified integer arguments
x = math.lcm(12, 30)
print(x)
# 60


# perm(n, k=None)
# * Return the number of ways to choose k items from n items with order and
#   without repetition
# * This is often referred to as "n permute k"
x = math.perm(5, 2)
print(x)
# 20


###############################################################################
# Floating point arithmetic
###############################################################################


# ceil(x)
# * Return the ceiling of x, the smallest integer greater than or equal to x
x = math.ceil(5.7)
print(x)
# 6


# fabs(x)
# * Return the absolute value of x
x = math.fabs(-7)
print(x)
# 7.0


# floor(x)
# * Return the floor of x, the largest integer less than or equal to x
x = math.floor(5.7)
print(x)
# 5


# fma(x, y, z)
# * Return x * y + z with full IEEE 754 double precision accuracy
x = math.fma(2, 3, 4)
print(x)
# 10.0


# fmod(x, y)
# * Return fmod(x, y), as defined by the platform C library
# * Note that the Python expression x % y may not return the same result
x = math.fmod(5, 2)
print(x)
# 1.0


# modf(x)
# * Return the fractional and integer parts of x as a tuple of two numbers
x = math.modf(7.5)
print(x)
# (0.5, 7.0)


# remainder(x, y)
# * Return the IEEE 754-style remainder of x with respect to y
x = math.remainder(5, 2)
print(x)
# 1.0


# trunc(x)
# * Return the Real value x truncated to an Integral (usually an integer)
# * Delegates to x.__trunc__()
x = math.trunc(15.5)
print(x)
# 15


###############################################################################
# Floating point manipulation functions
###############################################################################


# copysign(x, y)
# * Return a float with the magnitude (absolute value) of x but the sign of y
x = math.copysign(3.0, -0.0)
print(x)
# -3.0


# frexp(x)
# * Return the mantissa and exponent of x as the pair (m, e)
# * "m" is a float and "e" is an integer such that x == m * 2**e exactly
x = math.frexp(10)
print(x)
# (0.625, 4)


# isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
# * Determine whether two floating point numbers are close in value
# * rel_tol is the relative tolerance – it is the maximum allowed difference
#   between a and b, relative to the larger absolute value of a or b
# * abs_tol is the minimum absolute tolerance – useful for comparisons near
#   zero
x = math.isclose(10, 10.00000000000001)
print(x)
# True


# isfinite(x)
# * Return True if x is neither an infinity nor a NaN, and False otherwise
x = math.isfinite(4.89)
print(x)
# True


# isinf(x)
# * Return True if x is a positive or negative infinity, and False otherwise
x = math.isinf(math.inf)
print(x)
# True


# isnan(x)
# * Return True if x is a NaN (not a number), and False otherwise
x = math.isnan(math.nan)
print(x)
# True


# ldexp(m, e)
# * Return x * (2**i). This is essentially the inverse of function frexp()
x = math.ldexp(0.625, 4)
print(x)
# 10.0


# nextafter(x, y)
# * Return the next floating-point value after x towards y
x = math.nextafter(10, 11)
print(x)
# 10.000000000000002


# ulp(x)
# * Return the value of the least significant bit of the float x
x = math.ulp(10)
print(x)
# 2.842170943040401e-14


###############################################################################
# Power, exponential and logarithmic functions
###############################################################################


# cbrt(x)
# * Return the cube root of x
x = math.cbrt(27)
print(x)
# 3.0


# exp(x)
# * Return e raised to the power x
x = math.exp(2)
print(x)
# 7.3890560989306495


# exp2(x)
# * Return 2 raised to the power x
x = math.exp2(3)
print(x)
# 8.0


# expm1(x)
# * Return e raised to the power x, minus 1
x = math.expm1(2)
print(x)
# 6.38905609893065


# log(x[, base])
# * With one argument, return the natural logarithm of x (to base e)
# * With two arguments, return the logarithm of x to the given base
x = math.log(2)
print(x)
# 0.6931471805599453


# log1p(x)
# * Return the natural logarithm of 1+x (base e)
x = math.log1p(2)
print(x)
# 1.0986122886681098


# log2(x)
# * Return the base-2 logarithm of x
x = math.log2(8)
print(x)
# 3.0


# log10(x)
# * Return the base-10 logarithm of x
x = math.log10(100)
print(x)
# 2.0


# pow(x, y)
# * Return x raised to the power y
x = math.pow(2, 8)
print(x)
# 256.0


# sqrt(x)
# * Return the square root of x
x = math.sqrt(25)
print(x)
# 5.0


###############################################################################
# Summation and product functions
###############################################################################


# dist(p, q)
# * Return the Euclidean distance between two points p and q
x = math.dist([5, 3], [7, 8])
print(x)
# 5.385164807134505


# fsum(iterable)
# * Return an accurate floating point sum of values in the iterable
x = math.fsum([0.1, 0.2])
print(x)
# 0.30000000000000004


# hypot(*coordinates)
# * Return the Euclidean norm
# * For a two dimensional point (x, y), this is equivalent to computing the
#   hypotenuse of a right triangle using the Pythagorean theorem,
#   sqrt(x*x + y*y)
x = math.hypot(3, 4)
print(x)
# 5.0


# prod(iterable, *, start=1)
# * Calculate the product of all the elements in the input iterable
x = math.prod([1, 2, 3, 4, 5])
print(x)
# 120


# sumprod(p, q)
# * Return the sum of products of values from two iterables p and q.
x = math.sumprod([2, 2], [3, 3])
print(x)
# 12


###############################################################################
# Angular conversion
###############################################################################


# degrees(x)
# * Convert angle x from radians to degrees
x = math.degrees(math.pi)
print(x)
# 180.0


# radians(x)
# * Convert angle x from degrees to radians
x = math.radians(180)
print(x)
# 3.141592653589793


###############################################################################
# Trigonometric functions
###############################################################################


# acos(x)
# * Return the arc cosine of x, in radians
x = math.acos(1)
print(x)
# 0.0


# asin(x)
# * Return the arc sine of x, in radians
x = math.asin(1)
print(x)
# 1.5707963267948966


# atan(x)
# * Return the arc tangent of x, in radians
x = math.atan(1)
print(x)
# 0.7853981633974483


# atan2(y, x)
# * Return atan(y / x), in radians. The result is between -π and π
x = math.atan2(5, 3)
print(x)
# 1.0303768265243125


# cos(x)
# * Return the cosine of x radians
x = math.cos(1)
print(x)
# 0.5403023058681398


# sin(x)
# * Return the sine of x radians
x = math.sin(1)
print(x)
# 0.8414709848078965


# tan(x)
# * Return the tangent of x radians
x = math.tan(1)
print(x)
# 1.5574077246549023


###############################################################################
# Hyperbolic functions
###############################################################################


# acosh(x)
# * Return the inverse hyperbolic cosine of x
x = math.acosh(2)
print(x)
# 1.3169578969248166


# asinh(x)
# * Return the inverse hyperbolic sine of x
x = math.asinh(2)
print(x)
# 1.4436354751788103


# atanh(x)
# * Return the inverse hyperbolic tangent of x
x = math.atanh(0.1)
print(x)
# 0.1003353477310756


# cosh(x)
# * Return the hyperbolic cosine of x
x = math.cosh(0.5)
print(x)
# 1.1276259652063807


# sinh(x)
# * Return the hyperbolic sine of x
x = math.sinh(0.5)
print(x)
# 0.5210953054937474


# tanh(x)
# * Return the hyperbolic tangent of x
x = math.tanh(0.5)
print(x)
# 0.46211715726000974


###############################################################################
# Special functions
###############################################################################


# erf(x)
# * Return the error function at x
x = math.erf(0.5)
print(x)
# 0.5204998778130465


# erfc(x)
# * Return the complementary error function at x
x = math.erfc(0.5)
print(x)
# 0.4795001221869535


# gamma(x)
# * Return the Gamma function at x
x = math.gamma(5)
print(x)
# 24.0


# lgamma(x)
# * Return the natural logarithm of the absolute value of the Gamma function at
#   x
x = math.lgamma(5)
print(x)
# 3.178053830347945


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
# * Equivalent to float('inf')
print(math.inf, -math.inf)
# inf -inf


# nan
# * A floating-point “not a number” (NaN) value
print(math.nan)
# nan
