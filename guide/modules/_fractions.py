"""
Fractions module

* The fractions module provides support for rational number arithmetic
* Fraction instance can be constructed from a pair of integers, from another
  rational number, or from a string
"""
import fractions
import math


# -----------------------------------------------------------------------------
# Fraction


# Fraction()
# * Creates fraction
# * Syntax:
#   * Fraction(numerator=0, denominator=1)
#   * Fraction(other_fraction)
#   * Fraction(float)
#   * Fraction(decimal)
#   * Fraction(string)
f1 = fractions.Fraction(4, 3)
f2 = fractions.Fraction(f1)
f3 = fractions.Fraction(0.75)
f4 = fractions.Fraction(12)
f5 = fractions.Fraction('15/7')
print(f1, f2, f3, f4, f5, sep=', ')
# 4/3, 4/3, 3/4, 12, 15/7


# Get numerator and denominator
f = fractions.Fraction('15/7')
print(f.numerator, f.denominator, sep=', ')
# 15, 7


# limit_denominator(max_denominator=1000000)
# * Finds and returns the closest Fraction to self that has denominator at most
#   max_denominator. This method is useful for finding rational approximations
#   to a given floating-point number
f = fractions.Fraction(math.pi)
print(f)                         # 884279719003555/281474976710656
print(f.limit_denominator(100))  # 311/99


# -----------------------------------------------------------------------------
# Operations


# Sum
f1 = fractions.Fraction('4/2')
f2 = fractions.Fraction('7/2')
print(f1 + f2)
# 11/2


# Subtract
f1 = fractions.Fraction('4/2')
f2 = fractions.Fraction('7/2')
print(f1 - f2)
# -3/2


# Multiply
f1 = fractions.Fraction('24/3')
f2 = fractions.Fraction('8/2')
print(f1 * f2)
# 32


# Divide
f1 = fractions.Fraction('24/3')
f2 = fractions.Fraction('8/2')
print(f1 / f2)
# 2
