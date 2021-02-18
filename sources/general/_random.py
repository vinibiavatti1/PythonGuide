"""
Random

* To use the random, its module needs to be imported with "import random"
"""
import random


# Random
# Generates a float value (0.0 ~ 1.0)
rnd = random.random()
print(rnd)
# 0.5


# Randrange
# Get random value from range by step
rnd1 = random.randrange(10)         # (stop)
rnd2 = random.randrange(10, 20)     # (start, stop)
rnd3 = random.randrange(10, 20, 2)  # (start, stop, step)
print(rnd1, rnd2, rnd3, sep='\n')
# 5, 15, 12


# Randint
# Return a random integer N such that a <= N <= b.
# Alias for randrange(a, b+1)
rnd = random.randint(10, 20)
print(rnd)
# 15


# Randbytes
# Generate an amount of bytes
rnd = random.randbytes(3)
print(rnd)
# b'\xa0[\xa7'


# Choice
# Select a random item from collection (tuple, list or set)
# NOTE: dicts are not allowed
lst = [1, 2, 3, 4]
choice = random.choice(lst)
print(choice)
# 1


# Shuffle
# Used to shuffle collection of data (tuple or list)
lst = [1, 2, 3, 4]
random.shuffle(lst)
print(lst)
# [4, 2, 3, 1]
