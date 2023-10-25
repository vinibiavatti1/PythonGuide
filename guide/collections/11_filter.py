# Filtering (with filter())
# * A tuple can be filtered using the `filter()` when a more complex condition
#   must be used
# * In this case we used a lambda function to define the condition
# * The `filter()` function will return a filter object, so that we must cast
#   the object to a tuple back
x = (1, 2, 3, 4)
y = tuple(filter(lambda el: el > 2, x))
print(y)
# (3, 4)
