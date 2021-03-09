"""
Set

* Sets are used to store multiple items in a single variable.
* Set is one of 4 built-in data types in Python used to store collections of
  data, the other 3 are List, Tuple, and Dictionary, all with different
  qualities and usage
* A set is a collection which is both unordered and unindexed.
* Sets are written with curly brackets.
* NOTE: The print results can be in other order then the commentaries

( ) Ordered
(V) Changeable
( ) Allow Duplicate
( ) Indexed
"""


###############################################################################
# Intro
###############################################################################


# Create set
st = {1, 2, 3}  # With values
st = set()      # With set()
st = set()      # Empty
# st = {}       # NOTE: Empty brackets create a dict, not a set!!!


# Create set from other collection
st = set((1, 2, 3))
st = set([1, 2, 3])


# Copy set
st1 = {1, 2, 3}
st2 = set(st1)
print(st2)
# {1, 2, 3}


# Join sets
st1 = {1, 2, 3}
st2 = {4, 5, 6}
# print(st1 + st2)  # It not works for sets
st1 = st1.union(st2)
print(st1)
# {1, 2, 3, 4, 5, 6}


# NOT Ordered
st = {'a', 'b', 'c', 'd', 'e'}
# print(st[0])
# ERROR


# Changeable
st = set()
st.add('a')
print(st)
# {'a'}


# NOT Allow Duplicate
st = {1, 1, 1}
print(st)
# {1}


# Length
st = {'a', 'b', 'c'}
length = len(st)
print(length)
# 3


###############################################################################
# Umpack
###############################################################################


# Umpack as arguments
def sum(x, y):
    return x + y


st = {3, 6}
print(sum(*st))
# 9


###############################################################################
# Data access
###############################################################################


# Check if item exists
st = {'a', 'b', 'c', 'd', 'e'}
if 'c' in st:
    print('"c" is present')
    # 'c' is present


# For each
st = {'a', 'b', 'c', 'd', 'e'}
for el in st:
    print(el, end=', ')
    # a, b, c, d, e,
print()


# Print with set comprehension
st = {'a', 'b', 'c', 'd', 'e'}
{print(el, end=', ') for el in st}
# a, b, c, d, e,
print()


###############################################################################
# Change data
###############################################################################


# The data on set cannot be changed because it is unordered. To make changes,
# the right way is to remove the element and add the other one
st = {'a', 'b', 'c'}
st.remove('a')
st.add('d')
print(st)
# {'d', 'b', 'c'}


###############################################################################
# Filter
###############################################################################


# With function
def adults(el):
    return el >= 18


st1 = {5, 19, 4, 26, 18}
st2 = set(filter(adults, st1))
print(st2)
# {19, 26, 18}


# With lambda
st1 = {5, 19, 4, 26, 18}
st2 = set(filter(lambda el: el >= 18, st1))
print(st2)
# {19, 26, 18}
