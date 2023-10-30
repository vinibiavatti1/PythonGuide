"""
Unpack

* The unpack syntax is used to separate the values of a collection to specific
  variables
* It can be also used to unpack collection data as argument to functions
"""


###############################################################################
# Unpack Collections into Variables
###############################################################################


# Unpack collection data to variables (all collection data)
# * The syntax below can be used to store collection values to variables
# * The tuple is used as a collection for this example
collection = (1, 2, 3)
x, y, z = collection
print(x, y, z)
# 1 2 3


# Unpack collection data to variables (* in the beginning)
# * We can define a variable with "*" as prefix to be the group of the leftover
#   data. The "*" variable will take the "rest" of the data as a collection.
# * The list is used as a collection for this example
collection = [1, 2, 3, 4, 5]
*x, y, z = collection
print(x, y, z)
# [1, 2, 3] 4 5


# Unpack collection data to variables (* in the middle)
# * In this case, the middle variable will store the "rest" of the data
x, *y, z = collection
print(x, y, z)
# 1 [2, 3, 4] 5


# Unpack collection data to variables (* in the end)
# * In this case, the last variable will store the "rest" of the data
x, y, *z = collection
print(x, y, z)
# 1 2 [3, 4, 5]


###############################################################################
# Unpack Collections as Arguments
###############################################################################


# Define a function
# * We will define a dummy function that will be used for the next examples
def show_values(x, y, z=None):
    print(x, y, z)


# Unpack collection as arguments (tuple)
# * The wildcard "*" is used in front of the collection to define that it will
#   be unpacked as arguments to a function
# * For this case, the arguments will have these values: (x=1 y=2 z=3)
# * This is the same of:
#   * show_values(collection[0], collection[1], collection[2])
collection = (1, 2, 3)
show_values(*collection)
# 1 2 3


# Unpack collection as arguments (list)
# * In this example, we will only pass the required amount of variables to the
#   function. The "z" variable will have the default value "None"
collection = ['A', 'B']
show_values(*collection)
# A B None


# Unpack collection as arguments (dict)
# * The dictionary must has the keys as the same of the arguments name. This
#   will guarantee that each variable will be related for the specific
#   function argument
# * NOTE: We must specify two wildcards (**) to define that the values of the
#   dictionary has to be used, otherwise, the keys of the dictionary will be
#   passed as the positional function arguments
# * This will be the same of:
#   * show_values(y=2, x=1, z=3)
dictionary = {'y': 2, 'x': 1, 'z': 3}
show_values(*dictionary)
show_values(**dictionary)
# y x z (wrong)
# 1 2 3 (correct)


# Unpack generator data to a single variable
# * We can use a single variable to unpack data from a collection or a
#   generator
# * It will be the same of: (x = list(generator))
# * NOTE: The comma is mandatory for the unpack syntax, even for single
#   variables
generator = (x for x in range(5))
*x, = generator
print(x)
# [0, 1, 2, 3, 4]
