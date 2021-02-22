"""
List

* List items are ordered, changeable, and allow duplicate values.
* List items are indexed, the first item has index [0], the second item has
  index [1] etc.

(V) Ordered
(V) Changeable
(V) Allow Duplicate
(V) Indexed
"""


# -----------------------------------------------------------------------------
# Intro


# Create list
lst = [1, 2, 3]


# Create list from other collection
lst = list((1, 2, 3))
lst = list({1, 2, 3})


# Copy list
lst1 = [1, 2, 3]
lst2 = list(lst1)
print(lst2)
# [1, 2, 3]


# Join lists
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1 + lst2)
# [1, 2, 3, 4, 5, 6]


# Ordered
lst = ['a', 'b', 'c']
print(lst[0])
# a


# Changeable
lst = []
lst.append('a')
print(lst[0])
# a


# Allow Duplicate
lst = [1, 1, 1]
print(lst[2])
# 1


# Length
lst = ['a', 'b', 'c']
length = len(lst)
print(length)
# 3


# Umpack
lst = ['a', 'b', 'c']
el1, el2, el3 = lst
print(el1, el2, el3)
# a b c


# Umpack *
lst = ['a', 'b', 'c', 'd', 'e']
left, *middle, right = lst
print(left, middle, right)
# a ['b', 'c', 'd'] e


# Multiply list
lst = ['a', 'b']
lst *= 2
print(lst)
# ['a', 'b', 'a', 'b']


# -----------------------------------------------------------------------------
# Data access


# Index [start, stop, step]
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[0])    # a
print(lst[1:3])  # ['b', 'c']
print(lst[3:])   # ['d', 'e']
print(lst[:3])   # ['a', 'b', 'c']
print(lst[-1])   # e (inverse access)


# Check if item exists
lst = ['a', 'b', 'c', 'd', 'e']
if 'c' in lst:
    print('"c" is present')
    # "c" is present


# For range
lst = ['a', 'b', 'c', 'd', 'e']
for i in range(len(lst)):
    print(lst[i], end=', ')
    # a, b, c, d, e,
print()


# For each
lst = ['a', 'b', 'c', 'd', 'e']
for el in lst:
    print(el, end=', ')
    # a, b, c, d, e,
print()


# For each with index
lst = ['a', 'b', 'c', 'd', 'e']
for idx, el in enumerate(lst):
    print(f'{idx}: {el}', end=', ')
    # 0: a, 1: b, 2: c, 3: d, 4: e,
print()


# While
lst = ['a', 'b', 'c', 'd', 'e']
i = 0
while i < len(lst):
    print(lst[i], end=', ')
    # a, b, c, d, e,
    i += 1
print()


# Print with list comprehension
lst = ['a', 'b', 'c', 'd', 'e']
[print(el, end=', ') for el in lst]
# a, b, c, d, e,
print()


# -----------------------------------------------------------------------------
# Change data


# Change by index
lst = ['a', 'b', 'c']
lst[1] = 'd'
print(lst)
# ['a', 'd', 'c']


# Change by range
lst = ['a', 'b', 'c']
lst[1:3] = ['d', 'e']
print(lst)
# ['a', 'd', 'e']


# Change by range (With less elements)
# The range of elements will be replaced with the elements
lst = ['a', 'b', 'c', 'd', 'e']
lst[1:4] = 'f'
print(lst)
# ['a', 'f', 'e']


# Change by range (With more elements)
# If the amount of elements to change is more then the range, these will be
# inserted in the list
lst = ['a', 'b', 'c']
lst[1:2] = ['d', 'e']
print(lst)
# ['a', 'd', 'e', 'c']


# Change by range (More than the size)
# Just change until the limit of the list
lst = ['a', 'b', 'c']
lst[1:10] = ['d', 'd']
print(lst)
# ['a', 'd', 'd']


# Remove index with del
lst = ['a', 'b', 'c']
del lst[1]
print(lst)
# ['a', 'c']


# Remove range with del
lst = ['a', 'b', 'c']
del lst[1:3]
print(lst)
# ['a']


# -----------------------------------------------------------------------------
# Filter


# With function
def adults(el):
    return el >= 18


lst1 = [5, 19, 4, 26, 18]
lst2 = list(filter(adults, lst1))
print(lst2)
# [19, 26, 18]


# With lambda
lst1 = [5, 19, 4, 26, 18]
lst2 = list(filter(lambda el: el >= 18, lst1))
print(lst2)
# [19, 26, 18]
