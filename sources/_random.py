"""
Random examples

* To use the random, its module needs to be imported with "import random"
"""
import random

# Random
# Generates a float value (0.0 ~ 1.0)
rnd = random.random()
print(rnd)

# Randrange
# Get random value from range by step
rnd1 = random.randrange(10) # randrange(stop)
rnd2 = random.randrange(10, 20) # randrange(start, stop)
rnd3 = random.randrange(10, 20, 2) # randrange(start, stop, step)
print(rnd1, rnd2, rnd3, sep='\n')

# Randint
# Return a random integer N such that a <= N <= b. 
# Alias for randrange(a, b+1)
rnd = random.randint(10, 20)
print(rnd)

# Randbytes
# Generate an amount of bytes
rnd = random.randbytes(3)
print(rnd)

# Choice
# Select a random item from collection
lst = [1, 2, 3, 4] # can be a tuble/set instead
choice = random.choice(lst)
print(choice)

# Shuffle
# Used to shuffle collection of data
lst = [1, 2, 3, 4]
random.shuffle(lst)
print(lst)