# Mapping (with map())
# * A tuple can be mapped using the `map()` when a more complex expression is
#   needed
# * In this case we used a lambda function to define the condition
# * The `map()` function will return a map object, so that we must cast the
#   object to a tuple back
x = (1, 2, 3, 4)
y = tuple(map(lambda el: el * 2, x))
print(y)
# (2, 4, 6, 8)
