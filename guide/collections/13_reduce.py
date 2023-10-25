# Reducing (with functools.reduce())
# * To reduce a tuple, we can use the `functools.reduce()` function
# * The reduce function is not available as a built-in function, so that we
#   must import it from the `functools` module
# * A reduce function will process the tuple elements and return a single
#   value
# * The acc (accumulator) parameter will store the result of the previous
#   iteration, and the el (element) parameter will store the current element
from functools import reduce
x = (1, 2, 3, 4)
y = reduce(lambda acc, el: acc + el, x)
print(y)
# 10
