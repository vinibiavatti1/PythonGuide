"""
Tuple

* Tuples are used to store multiple items in a single variable.
* Tuple is one of 4 built-in data types in Python used to store collections of
  data, the
  other 3 are List, Set, and Dictionary, all with different qualities and usage
* A tuple is a collection which is ordered and unchangeable.
* Tuples are written with round brackets.

(V) Ordered
( ) Changeable
(V) Allow Duplicate
(V) Indexed
"""


# -----------------------------------------------------------------------------
# Intro


# Create tuple
tpl = (1, 2, 3)


# NOTE: To create tuples with just one value, the comma is necessary!
tpl = ('apple',)
not_tuple = ('apple')
print(type(not_tuple))
# <class 'str'>


# Create tuple from other collection
tpl = tuple([1, 2, 3])
tpl = tuple({1, 2, 3})


# Copy tuple
tpl1 = (1, 2, 3)
tpl2 = tuple(tpl1)
print(tpl2)
# (1, 2, 3)


# Join tuples
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
print(tpl1 + tpl2)
# (1, 2, 3, 4, 5, 6)


# Ordered
tpl = ('a', 'b', 'c')
print(tpl[0])
# a


# Allow Duplicate
tpl = (1, 1, 1)
print(tpl[2])
# 1


# Length
tpl = ('a', 'b', 'c')
length = len(tpl)
print(length)
# 3


# Umpack
tpl = ('a', 'b', 'c')
el1, el2, el3 = tpl
print(el1, el2, el3)
# a b c


# Umpack *
# NOTE: The umpack generated a list, not a tuple
tpl = ('a', 'b', 'c', 'd', 'e')
left, *middle, right = tpl
print(left, middle, right)
# a ['b', 'c', 'd'] e


# Multiply tuple
tpl = ('a', 'b')
tpl *= 2
print(tpl)
# ('a', 'b', 'a', 'b')


# -----------------------------------------------------------------------------
# Data access


# Index
tpl = ('a', 'b', 'c', 'd', 'e')
print(tpl[0])    # a
print(tpl[1:3])  # ('b', 'c')
print(tpl[3:])   # ('d', 'e')
print(tpl[:3])   # ('a', 'b', 'c')
print(tpl[-1])   # e (inverse access)


# Check if item exists
tpl = ('a', 'b', 'c', 'd', 'e')
if 'c' in tpl:
    print('"c" is present')
    # "c" is present


# For range
tpl = ('a', 'b', 'c', 'd', 'e')
for i in range(len(tpl)):
    print(tpl[i], end=', ')
    # a, b, c, d, e,
print()


# For each
tpl = ('a', 'b', 'c', 'd', 'e')
for el in tpl:
    print(el, end=', ')
    # a, b, c, d, e,
print()


# For each with index
tpl = ('a', 'b', 'c', 'd', 'e')
for idx, el in enumerate(tpl):
    print(f'{idx}: {el}', end=', ')
    # 0: a, 1: b, 2: c, 3: d, 4: e,
print()


# While
tpl = ('a', 'b', 'c', 'd', 'e')
i = 0
while i < len(tpl):
    print(tpl[i], end=', ')
    # a, b, c, d, e,
    i += 1
print()


# -----------------------------------------------------------------------------
# Change data


# Cast to list
# * Tuples are not changeable, so, to change data the tuple must be cast to
# list first
tpl = (1, 2, 3)
lst = list(tpl)
lst[0:] = ['a', 'b', 'c']
tpl = tuple(lst)
print(tpl)
# ('a', 'b', 'c')


# -----------------------------------------------------------------------------
# Filter


# With function
def adults(el):
    return el >= 18


tpl1 = (5, 19, 4, 26, 18)
tpl2 = tuple(filter(adults, tpl1))
print(tpl2)
# (19, 26, 18)


# With lambda
tpl1 = (5, 19, 4, 26, 18)
tpl2 = tuple(filter(lambda el: el >= 18, tpl1))
print(tpl2)
# (19, 26, 18)