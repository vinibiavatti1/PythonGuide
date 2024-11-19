"""
Deque

* A deque is a double-ended queue (i.e. a list-like container with functions to
  work on both ends).
* The deque class is available in the collections module.
* Deques are thread-safe and support fast appends and pops on either end.
* Syntax: deque(iterable [, maxlen])
"""


###############################################################################
# Importing Resource
###############################################################################


# Importing the resource
# * We can import the resource using the import statement below
from collections import deque


###############################################################################
# Creating Deques
###############################################################################


# Creating an empty Deque
# * We can create an empty deque using the deque class
x = deque()
print(x)
# deque([])


# Creating a Deque (with any iterable)
# * We can create a deque using any iterable as a parameter
x = deque([1, 2, 3])
print(x)
# deque([1, 2, 3])


# Creating a Deque (with maxlen)
# * The maxlen parameter is used to limit the deque size (i.e. the number of
#   elements)
# * When the deque reaches the limit, the oldest element is removed
x = deque([1, 2, 3], maxlen=2)
print(x)
# deque([2, 3], maxlen=2)


###############################################################################
# Deque Methods
###############################################################################


# Append Right
# * The `append()` method is used to add an element to the right side of the
#   deque, like a common list
x = deque([1, 2, 3])
x.append(4)
print(x)
# deque([1, 2, 3, 4])


# Append Left
# * The `appendleft()` method is used to add an element to the left side of the
#   deque
x = deque([1, 2, 3])
x.appendleft(0)
print(x)
# deque([0, 1, 2, 3])


# Pop Right
# * The `pop()` method is used to remove and return the rightmost element of
#   the deque
x = deque([1, 2, 3])
y = x.pop()
print(x, y)
# deque([1, 2]), 3


# Pop Left
# * The `popleft()` method is used to remove and return the leftmost element of
#   the deque
x = deque([1, 2, 3])
y = x.popleft()
print(x, y)
# deque([2, 3]), 1


# Extend Right
# * The `extend()` method is used to add multiple elements to the right side of
#   the deque
# * The elements should be passed as an iterable
x = deque([1, 2, 3])
x.extend([4, 5])
print(x)
# deque([1, 2, 3, 4, 5])


# Extend Left
# * The `extendleft()` method is used to add multiple elements to the left side
#   of the deque
# * NOTE: The elements will be added in reverse order
x = deque([1, 2, 3])
x.extendleft([0, -1])
print(x)
# deque([-1, 0, 1, 2, 3])


# Rotate
# * The `rotate()` method is used to rotate the deque n steps to the right
# * If n is negative, the deque will rotate to the left
x = deque([1, 2, 3, 4, 5, 6])
x.rotate(2)
print(x)
# deque([5, 6, 1, 2, 3, 4])


# Rotate (Negative)
# * When `n` is negative, the deque will rotate to the left
x = deque([1, 2, 3, 4, 5, 6])
x.rotate(-2)
print(x)
# deque([3, 4, 5, 6, 1, 2])
