# Filtering (with comprehension)
# * A tuple can be filtered using the comprehension syntax, defining a
#   condition to filter the elements
# * Note that the tuple comprehension syntax will return a generator, not a
#   tuple. Because of it, we need to cast the result to a tuple using `tuple()`
#   function
x = (1, 2, 3, 4)
y = tuple(el for el in x if el > 2)
print(y)
# (3, 4)

# Mapping (with comprehension)
# * A tuple can be mapped using the comprehension syntax, defining a
#   expression in the target element
# * Like before, the comprehension syntax will return a generator, so that
#   we must cast the result
x = (1, 2, 3, 4)
y = tuple(el * 2 for el in x)
print(y)
# (2, 4, 6, 8)
