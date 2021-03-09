"""
Frozenset

* Frozenset is jufst an immutable version of a Python frozenset object
* While elements of a frozenset can be modified at any time, elements of the
  frozenset remain the same after creation
* NOTE: The print results can be in other order then the commentaries

( ) Ordered
( ) Changeable
( ) Allow Duplicate
( ) Indexed
"""


###############################################################################
# Intro
###############################################################################


# Create frozenset
fst = {1, 2, 3}


# Create frozenset from other collection
fst = frozenset((1, 2, 3))
fst = frozenset([1, 2, 3])


# Copy frozenset
fst1 = {1, 2, 3}
fst2 = frozenset(fst1)
print(fst2)
# frozenset({1, 2, 3})


# Join frozensets
fst1 = frozenset({1, 2, 3})
fst2 = frozenset({4, 5, 6})
# print(fst1 + fst2)  # It not works for frozensets
fst1 = fst1.union(fst2)
print(fst1)
# frozenset({1, 2, 3, 4, 5, 6})


# NOT Ordered
fst = frozenset({'a', 'b', 'c', 'd', 'e'})
# print(fst[0])
# ERROR


# NOT Changeable
fst = frozenset()
# fst.add('a')
# ERROR


# NOT Allow Duplicate
fst = frozenset({1, 1, 1})
print(fst)
# frozenset({1})


# Length
fst = frozenset({'a', 'b', 'c'})
length = len(fst)
print(length)
# 3


###############################################################################
# Data access
###############################################################################


# Check if item exifsts
fst = frozenset({'a', 'b', 'c', 'd', 'e'})
if 'c' in fst:
    print('"c" is present')
    # 'c' is present


# For each
fst = frozenset({'a', 'b', 'c', 'd', 'e'})
for el in fst:
    print(el, end=', ')
    # a, b, c, d, e,
print()


# Print with frozenset comprehension
fst = frozenset({'a', 'b', 'c', 'd', 'e'})
{print(el, end=', ') for el in fst}
# a, b, c, d, e,
print()


###############################################################################
# Filter
###############################################################################


# With function
def adults(el):
    return el >= 18


fst1 = frozenset({5, 19, 4, 26, 18})
fst2 = frozenset(filter(adults, fst1))
print(fst2)
# frozenset({26, 18, 19})


# With lambda
fst1 = frozenset({5, 19, 4, 26, 18})
fst2 = frozenset(filter(lambda el: el >= 18, fst1))
print(fst2)
# frozenset({26, 18, 19})
