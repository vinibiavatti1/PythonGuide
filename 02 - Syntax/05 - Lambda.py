"""
Lambda

* The "lambda" instruction in Python is used to declare an anonymous function
* Anonymous functions are represented as function that has no name. These
  functions are usually used to define some action in a particular case
* It is called as "arrow function" in some programming languages, for the
  reason that they are declared using a arrow sign "=>".
  In Python, the "lambda" word is used to declare a lambda function
* The lambda function in Python can have only one expression. If you need a
  function with more expressions, you will have to create a conventional
  function
* The expression always returns a result. It has an implicitly "return"
  statement before the lambda expression
* The concept of lambda functions is a subject of functional programming. The
  lambdas usually are used to perform an operation together with the array
  processor functions (map, filter, reduce, etc.)
* Syntax:
  * lambda: <expression>
  * lambda <arguments>: <expression>
"""


###############################################################################
# Lambda Functions
###############################################################################


# Declare a lambda function
# * A lambda function can be declared using the "lambda" keyword
# * Lambda functions don't have a name, thats why it is considered an anonymous
#   function
# * The function bellow cannot be called since there is no way to reference the
#   function
lambda: print('Hello World')


# Declare a lambda function to a variable
# * Adding a lambda function to a variable permits that we call the function
# * The example below is the same of creating a normal function with the name
#   of the variable
# * NOTE: When a lambda function needs to be named, it is a good reason to
#   refactor the lambda function to a normal function
show_message = lambda: print('Hello World')


# Call a lambda function
# * Now that we have the lambda function associated to a variable, we can call
#   it and perform the function operation
show_message()
# Hello World


# Declare and call a lambda function
# * We can declare and call a lambda function at the same line
# * To do this, we can surround the function with parenthesis "()", and call it
#   as a common function
(lambda: print('Hello World'))()
# Hello World


###############################################################################
# Lambda Functions Parameters
###############################################################################


# Declare a lambda function with parameters
# * Like the common functions, lambda function can also have parameters
# * The parameters are defined after the "lambda" keyword
# * Note that there is an implicitly return statement before the function body:
#   (lambda x, y: return x + y)
lambda x, y: x + y


# Declare a lambda function with parameters to a variable
# * Like the other example above, we can store the lambda function to a
#   variable
sum_values = lambda x, y: x + y


# Call a lambda function with parameters
# * To call a lambda function with arguments, we can use the same way of a
#   normal function call
result = sum_values(7, 3)
print(result)
# 10


# Declare a lambda function with optional parameters
# * We can set a default value for the parameters in a lambda function like
#   the normal function
show_text = lambda text='Hello World': print(text)
show_text()
show_text('Hi!')
# Hello World
# Hi!


###############################################################################
# Lambda Functions in Functional Programming
###############################################################################


# Use a lambda function with map()
# * The "map()" function in Python is used to process an collection, performing
#   an lambda operation for each element of the collection
# * In this case, the lambda function can be used as a argument to the
#   function, to make the code easy to read, and to avoid having to define a
#   named function that will only be used in a particular context
# * Note that we must convert the return object of the "map()" function to a
#   list, since it returns a map object
collection = [1, 2, 3]
collection_mapped = map(lambda val: val * 2, collection)
result = list(collection_mapped)
print(result)
# [2, 4, 6]


# Use a lambda function with filter()
# * A lambda function can also be used as argument to the "filter()" function
# * The "filter()" function perform an operation for each element in a
#   collection, and discards the element if the lambda expression returns False
# * Don't forget to cast the returned object of the "filter()" function to a
#   list, as it was explained in the previous example
collection = [1, 2, 3, 4, 5, 6]
collection_filtered = filter(lambda val: val > 3, collection)
result = list(collection_filtered)
print(result)
# [4, 5, 6]


# Use a lambda function with sorted()
# * The "sorted()" function is used to order a collection by a criteria that
#   will be performed for each element
# * The reverse parameter permits to sort the collection in descending order
collection = [3, 1, 4, 2]
collection_sorted = sorted(collection, key=lambda val: val, reverse=True)
result = list(collection_sorted)
print(result)
# [4, 3, 2, 1]


# Use a lambda function with list.sort()
# * The "sort()" method located in a list object can also be used to sort the
#   collection. This will not create a new reference for the collection like
#   the other built-in functions presented above. For this reason, the "sort()"
#   function can be more performed when working with a big amount of data.
collection = [3, 1, 4, 2]
collection.sort(key=lambda val: val, reverse=True)
print(collection)
# [4, 3, 2, 1]


# Use a lambda function with functools.reduce()
# * The "reduce()" from the functools module accepts a function as argument
#   that can be used to define the action that will be performed for each
#   element
# * Array reduction is used to fold the array into a single value, for example,
#   to result the sum of all elements, or to result the subtraction of all
#   elements
# * This function is available at "functools" module, and needs to be imported
#   to become available for usage
# * The first argument of the "reduce" function is referred as the
#   "accumulator", and the second argument is the current element
from functools import reduce
collection = [1, 2, 3, 4]
result = reduce(lambda acc, val: acc + val, collection)
print(result)
# 10


# Define a function that accepts a lambda function as argument
# * We can define our own function that accepts a lambda function as argument
# * The function bellow is a variant of the "map()" function
# * The "key" argument requires a function, and the "collection" argument
#   requires a collection to work with
def compute(key, collection):
    return [key(val) for val in collection]


# Call a function that accepts a lambda function as argument
# * Below you can find an example of calling our own function that accepts a
#   lambda function as argument
collection = [1, 2, 3]
result = compute(lambda val: val * 2, collection)
print(result)
# [2, 4, 6]
