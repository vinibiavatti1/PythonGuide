"""
Comprehension

* Comprehension is a concise way to create lists, sets and dictionaries
* We can use comprehension to iterate over a sequence and apply an operation
Syntax
###############################################################################
Collection      Syntax
###############################################################################
List            [<expression> for <item> in <iterable> if <condition>]
Set             {<expression> for <item> in <iterable> if <condition>}
Dictionary      {<key>: <value> for <item> in <iterable> if <condition>}
###############################################################################
* NOTE: The condition is optional
* NOTE: Using tuple syntax, will create a generator, not a tuple
"""


###############################################################################
# Comprehensions
###############################################################################


# List Comprehension
# * The example below creates a list with list comprehension
x = [el for el in range(5)]
print(x)
# [0, 1, 2, 3, 4]


# Set Comprehension
# * The example below creates a set with set comprehension
x = {el for el in range(5)}
print(x)
# {0, 1, 2, 3, 4}


# Dictionary Comprehension
# * The example below creates a dictionary with set dict comprehension
# * Note that in this way, we have to set a key and a value
x = {el: str(el) for el in range(5)}
print(x)
# {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}


###############################################################################
# Operations
###############################################################################


# Creating a list
# * We will create a list using list comprehension to be used by the next
#   examples
base = [el for el in range(5)]
print(base)
# [0, 1, 2, 3, 4]


# Filtering
# * We can filter the elements using the `if` statement in the comprehension
y = [el for el in base if el >= 2]
print(y)
# [2, 3, 4]


# Mapping
# * We can apply an operation to the elements using the expression in the
#   comprehension
y = [el * 2 for el in base]
print(y)
# [0, 2, 4, 6, 8]


# Mapping (with expression condition)
# * We can use the ternary if statement in the expression to apply a condition
#   to the operation
y = [None if el == 0 else el * 2 for el in base]
print(y)
# [None, 2, 4, 6, 8]
