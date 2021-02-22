"""
Set Operations

* You can make operations like intersections, unions in sets using bitwise
  operators
* These operations are the same of the methods (union, intersection, ...)
* NOTE: Only sets accepts these operators
* Operators
  * Union (|)
  * Intersection (&)
  * Difference (-)
  * Symmetric Difference (^)
"""


# Union (|)
#  .---.---.
# / x /x\ x \
# \   \ /   /
#  `---'---´
st1 = {1, 2, 3, 4, 5, 6}
st2 = {4, 5, 6, 7, 8, 9}
st3 = st1 | st2
print(st3)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}


# Intersection (&)
#  .---.---.
# /   /x\   \
# \   \ /   /
#  `---'---´
st1 = {1, 2, 3, 4, 5, 6}
st2 = {4, 5, 6, 7, 8, 9}
st3 = st1 & st2
print(st3)
# {4, 5, 6}


# Difference (-)
#  .---.---.
# / x / \   \
# \   \ /   /
#  `---'---´
st1 = {1, 2, 3, 4, 5, 6}
st2 = {4, 5, 6, 7, 8, 9}
st3 = st1 - st2
print(st3)
# {1, 2, 3}


# Symmetric difference (^)
#  .---.---.
# / x / \ x \
# \   \ /   /
#  `---'---´
st1 = {1, 2, 3, 4, 5, 6}
st2 = {4, 5, 6, 7, 8, 9}
st3 = st1 ^ st2
print(st3)
# {1, 2, 3, 7, 8, 9}
