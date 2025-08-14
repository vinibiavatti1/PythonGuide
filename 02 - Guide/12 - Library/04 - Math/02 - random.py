"""
Random

* The random module provides functions for generating random numbers
* It uses the Mersenne Twister as the core generator
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import random


###############################################################################
# Bookkeeping functions
###############################################################################


# seed(a=None, version=2)
# * Initialize the random number generator with the specified seed
# * The seed is used to set the initial state of the generator
# * If a is omitted or None, the current system time is used
# * If randomness sources are provided by the operating system, they are used
#   instead of the system time
# * If a is an int, it is used directly
# * With version 2 (the default), a str, bytes, or bytearray object gets
#   converted to an int and all of its bits are used
# * With version 1, the hash() of a is used instead
random.seed(2)


# getstate()
# * Return a tuple representing the internal state of the generator
# * The tuple has three elements: the version, tuple integer values, and an
#   integer index
x = random.getstate()
print(x)
# (3, (2147483648, 507, 314, ...), None)


# setstate(state)
# * Restore the internal state of the generator
# * A state tuple returned by the `getstate()` method can be passed to this
#   method to restore the state
random.setstate(x)


###############################################################################
# Functions for bytes
###############################################################################


# randbytes(n)
# * Generate an amount (`n`) of random bytes
x = random.randbytes(5)
print(x)
# b'\x8b\x1e\x8b\x1e\x8b'


###############################################################################
# Functions for integers
###############################################################################


# randrange(stop)
# * Return a randomly selected value from a range that starts at 0 and stops at
#   the specified value
# * Alias for `randrange(0, stop)`
# * This is roughly equivalent to `choice(range(stop))`
x = random.randrange(10)
print(x)
# 5


# randrange(start, stop[, step])
# * Return a randomly selected value from a range that starts at the specified
#   value and stops at the specified value
# * The step parameter can be used to specify the increment value
# * This is roughly equivalent to `choice(range(start, stop, step))`
x = random.randrange(10, 20, 5)
print(x)
# 15


# randint(a, b)
# * Return a randomly selected integer from the specified range
# * Alias for `randrange(a, b+1)`
x = random.randint(10, 20)
print(x)
# 15


# getrandbits(k)
# * Return a non-negative randomly selected integer with `k` random bits
x = random.getrandbits(10)
print(x)
# 369


###############################################################################
# Functions for sequences
###############################################################################


# choice(seq)
# * Return a randomly selected element from the specified sequence
x = random.choice([1, 2, 3, 4])
print(x)
# 3


# choices(population, weights=None, *, cum_weights=None, k=1)
# * Return a `k` length list of elements chosen from the population with
#   replacement
# * The relative weights or cumulative weights can be specified
x = random.choices([1, 2, 3, 4], k=2)
print(x)
# [3, 4]


# shuffle(x)
# * Shuffle the sequence `x` in place
# * Note that this function only shuffles the sequence and does not return
#   anything
x = [1, 2, 3, 4]
random.shuffle(x)
print(x)
# [4, 2, 3, 1]


# sample(population, k)
# * Return a `k` length list of unique elements chosen from the population
#   sequence or set
# * Used for random sampling without replacement
x = random.sample([1, 2, 3, 4], 2)
print(x)
# [3, 1]


###############################################################################
# Discrete distributions
###############################################################################


# binomialvariate(n=1, p=0.5)
# * Return the number of successes for n independent trials with the
#   probability of success in each trial being `p`
x = random.binomialvariate(10, 0.5)
print(x)
# 5


###############################################################################
# Real-valued distributions
###############################################################################


# random()
# * Return the next random floating point number in the range [0.0, 1.0]
x = random.random()
print(x)
# 0.8710329683679704


# uniform(a, b)
# * Return a random floating point number N such that:
#   (a <= N <= b) for (a <= b) and (b <= N <= a) for (b < a)
x = random.uniform(3, 6)
print(x)
# 4.092043283542108


# triangular(low, high, mode)
# * Return a random floating point number N such that:
#   (low <= N <= high) and with the specified mode between the bounds
x = random.triangular(3, 6, 4.5)
print(x)
# 5.446203550809874


# betavariate(alpha, beta)
# * Return a random floating point number N such that:
#   (0 <= N <= 1) and follows a beta distribution
x = random.betavariate(0.1, 0.9)
print(x)
# 0.23616708374068


# expovariate(lambd=1.0)
# * Return a random floating point number N such that:
#   (0 <= N) and follows an exponential distribution
x = random.expovariate(0.5)
print(x)
# 0.39065903450367145


# gammavariate(alpha, beta)
# * Return a random floating point number N such that:
#  (0 <= N) and follows a gamma distribution
x = random.gammavariate(0.1, 0.9)
print(x)
# 5.492692558241367e-07


# gauss(mu, sigma)
# * Return a random floating point number N such that:
#   (N) follows a Gaussian distribution
x = random.gauss(0, 1)
print(x)
# 0.5518138791134164


# lognormvariate(mu, sigma)
# * Return a random floating point number N such that:
#   (0 <= N) and follows a log-normal distribution
x = random.lognormvariate(0.1, 0.9)
print(x)
# 0.7078619999717166


# normalvariate(mu, sigma)
# * Return a random floating point number N such that:
#   (N) follows a normal distribution
x = random.normalvariate(0, 1)
print(x)
# -0.1593295143821587


# vonmisesvariate(mu, kappa)
# * Return a random floating point number N such that:
#   (0 <= N <= 2π) and follows a von Mises distribution
x = random.vonmisesvariate(0, 1)
print(x)
# 5.314386572559804


# paretovariate(alpha)
# * Return a random floating point number N such that:
#   (0 <= N) and follows a Pareto distribution
x = random.paretovariate(0.5)
print(x)
# 6.051291084665149


# weibullvariate(alpha, beta)
# * Return a random floating point number N such that:
#   (0 <= N) and follows a Weibull distribution
x = random.weibullvariate(0.5, 1)
print(x)
# 0.22461946339613983


###############################################################################
# Random Classes
###############################################################################


# Creating a random object
# * The Random class can be used to create a random object
# * The random object can be used to generate random numbers, and each object
#   has its own internal state
# * The `x` parameter can be used to set the seed for the random object
x = random.Random(2)
y = x.randint(10, 20)
print(y)
# 10


# Creating a system random object
# * The SystemRandom class can be used to create a system random object which
#   uses the system's random number generator when available
# * The `x` parameter can be used to set the seed for the random object
x = random.SystemRandom(2)
y = x.randint(10, 20)
print(y)
# 10
