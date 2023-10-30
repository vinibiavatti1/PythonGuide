"""
TODO

Range

* Range is used to create a sequence to iterate between
* Range can be used to create a collection with some sequence
* Range type represents an immutable sequence of numbers and is commonly used
  for looping a specific number of times in for loops
* NOTE: Python's range() can only do integers, not floating point
* Syntax
  * range(stop)
  * range(start, stop[, step])
"""


# range(stop)
for index in range(5):
    print(index, end=', ')
    # 0, 1, 2, 3, 4,
print()


# range(start, stop)
for index in range(5, 10):
    print(index, end=', ')
    # 5, 6, 7, 8, 9,
print()


# range(start, stop, step)
for index in range(0, 10, 2):
    print(index, end=', ')
    # 0, 2, 4, 6, 8,
print()


# Inverse range
for index in range(5, 0, -1):
    print(index, end=', ')
    # 5, 4, 3, 2, 1,
print()


# Floating points
# * NOTE: Range does not accept floating points. Use while loop instead
i = 0.0
while i <= 1.0:
    print(round(i, 2), end=', ')
    i += 0.1
print()
# 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,


# Create collection with range
numbers = tuple(range(5, 10))
print(numbers)
# (5, 6, 7, 8, 9)


# Create a custom range function
def custom_range(start, stop, step=1):
    while start < stop:
        yield start
        start += 1


for index in custom_range(2, 10):
    print(index, end=', ')
    # 2, 3, 4, 5, 6, 7, 8, 9,
print()
