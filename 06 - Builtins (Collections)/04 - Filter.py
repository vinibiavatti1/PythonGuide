"""
Filter

* The filter operation is used to filter elements from some collection
* We can use comprehensions to do a filter operation (recommended way), or use
  the `filter()` builtin function
* The result of the `filter()` function is a filter object, that is a iterable
* Syntax: filter(__function, __iterable)
"""


###############################################################################
# Filter Object
###############################################################################


# The filter object
# * The `filter()` function will be applied to every item of the iterable,
#   and if the function returns True, the item will be added to the new
#   iterable. If the function returns False, the item will be ignored
# * The function accepts two parameters:
#   * __function: The function that will be applied to every item of the
#     iterable
#   * __iterable: The iterable that will be used to apply the function
# * Note that the `filter()` function returns a filter object. Because of it
#   we need to convert the result of the filter into a list
# * In the example below, we are filtering the collection by the values that
#   are greater than 3
x = [1, 2, 3, 4, 5, 6]
x_filter = filter(lambda n: n > 3, x)
y = list(x_filter)
print(y)
# [4, 5, 6]


# The filter object (with None function)
# * When the function is None, the filter will return the elements that are
#   True applying the "truth testing procedure"
x = [0, 1, 0, 2, 0, 3]
x_filter = filter(None, x)
y = list(x_filter)
print(y)
# [1, 2, 3]


###############################################################################
# Filter Operations
###############################################################################


# Filtering a collection (with comprehension) (XXX recommended XXX)
# * The comprehension is the recommended way to do a filter operation since
#   comprehensions are more readable
# * To use the comprehension to do a filter operation, we can specify a
#   condition
# * In the example below, we are filtering the collection by the values that
#   are greater than 3
x = [1, 2, 3, 4, 5, 6]
y = [n for n in x if n > 3]
print(y)
# [4, 5, 6]


# Filtering a collection (with filter)
# * The `filter()` builtin function can be used to do a filter operation
# * It is commonly used when a more complex operation is needed
# * Note that the `filter()` function returns a filter object. Because of it
#   we need to convert the result of the filter into a list
x = [1, 2, 3, 4, 5, 6]
x_filter = filter(lambda n: n > 3, x)
y = list(x_filter)
print(y)
# [4, 5, 6]


# Filtering a collection (with for-each)
# * A normal for-each can also be used to do a filter operation as well
# * Since comprehensions are more readable it is recommended to use them
x = [1, 2, 3, 4, 5, 6]
y = []
for n in x:
    if n > 3:
        y.append(n)
print(y)
# [4, 5, 6]
