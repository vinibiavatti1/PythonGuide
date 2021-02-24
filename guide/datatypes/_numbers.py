"""
Numbers

* Python has three number types:
  * int
  * float
  * complex
* Integers are unlimited (Since to fill the computer memory)
* Floats are limited (64 bits)
"""


# There are 3 number datatypes in Python
x = 1     # int
x = -5    # int (neg)
x = 0xF   # int (hex)
x = 0o7   # int (oct)
x = 3.5   # float
x = -0.3  # float (neg)
x = 1.    # float (1.0)
x = .1    # float (0.1)
x = 1j    # complex


# Int (unlimited)
x = 213612783613682163621638268362176
print(x)
# 213612783613682163621638268362176


# Float (limited 64 bits)
x = 3.9826321638217637216371283686213
print(x)
# 3.982632163821764


# Float as scientific numbers
# "e" or "E" to indicate "exponent" (power of 10)
# NOTE: the exponent (the value after the E) has to be an integer
x = 3.5e12  # (3.5 * 10^12) (not too big)
print(x)
# 3500000000000.0
x = 5E20    # (5 * 10^20) (too big)
print(x)
# 5e+20


# Complex
# 'j' or 'J' indicates the complex (imaginary sqrt(-1)) number
x = 1+4j
print(x)
# (1+4j)
print(4j * 4j)
# (-16+0j) (Complex multiplication)


# Number with underscore
# * Used to facilitate reading
x = 1_000_000
print(x)
# 1000000
