"""
Random module

* You can generate random numbers in Python by using random module
* These are pseudo-random number as the sequence of number generated depends on
  the seed
"""
import random


# -----------------------------------------------------------------------------
# Common functions


# random()
# * Return the next random floating point number in the range [0.0, 1.0]
rnd = random.random()
print(rnd)
# 0.5


# randint(a, b)
# * Return a random integer N such that a <= N <= b.
# * Alias for randrange(a, b+1)
rnd = random.randint(10, 20)
print(rnd)
# 15


# randrange(start, stop [, step])
# * Returns a random integer from the range, and the step if this was informed
rnd1 = random.randrange(10)         # (stop)
rnd2 = random.randrange(10, 20)     # (start, stop)
rnd3 = random.randrange(10, 20, 2)  # (start, stop, step)
print(rnd1, rnd2, rnd3, sep=', ')
# 5, 15, 12


# seed(a=None, version=2)
# * Initialize the random number generator
random.seed(2)
print(random.random())  # 0.9560342718892494
print(random.random())  # 0.9478274870593494
print(random.random())  # 0.05655136772680869


# -----------------------------------------------------------------------------
# Functions for collections


# choice(seq)
# * Return a random element from the non-empty sequence seq. If seq is empty,
#   raises IndexError
# * NOTE: dicts are not allowed
lst = [1, 2, 3, 4]
choice = random.choice(lst)
print(choice)


# shuffle(x)
# * Used to shuffle collection of data (tuple or list)
lst = [1, 2, 3, 4]
random.shuffle(lst)
print(lst)
# [4, 2, 3, 1]


# sample(population, k, *, counts=None)
# * Return a k length list of unique elements chosen from the population
#   sequence or set. Used for random sampling without replacement
# * Repeated elements can be specified one at a time or with the optional
#   keyword-only counts parameter. For example, sample(['red', 'blue'],
#   counts=[4, 2], k=5) is equivalent to sample(['red', 'red', 'red', 'red',
#   'blue', 'blue'], k=5)
lst = [1, 2, 3]
sample = random.sample(lst, 2, counts=[2, 3, 4])
print(sample)
# [3, 1]


# -----------------------------------------------------------------------------
# Functions for bytes


# randbytes(n)
# * Generate an amount of bytes
rnd = random.randbytes(3)
print(rnd)
# b'\xa0[\xa7'
