# Sorting (with sorted())
# * To sort a tuple, we can use the `sorted()` function
# * The sorted function will return a list, so that we must cast the result
#   back to a tuple
# * A lambda function can be used to define a custom sorting
# * The reverse parameter can be used to sort the tuple in reverse order
x = (1, 3, 2, 4)
y = tuple(sorted(x))
z = tuple(sorted(x, reverse=True))
print(y)
print(z)
# (1, 2, 3, 4)
# (4, 3, 2, 1)
