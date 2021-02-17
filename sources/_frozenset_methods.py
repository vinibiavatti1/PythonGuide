"""
Frozenset methods

* NOTE: The print results can be in other order then the commentaries
"""


# copy()
# Returns a copy of the set
fst1 = frozenset({'a', 'b', 'c'})
fst2 = fst1.copy()
print(fst2)
# frozenset({'a', 'b', 'c'})


# difference(s)
# Returns a set containing the difference between two or more sets
fst1 = frozenset({'a', 'b', 'c'})
fst2 = frozenset({'c', 'd'})
fst3 = fst1.difference(fst2)
print(fst3)
# frozenset({'a', 'b'})


# intersection()
# Returns a set, that is the intersection of two other sets
fst1 = frozenset({'a', 'b', 'c'})
fst2 = frozenset({'c', 'd'})
fst3 = fst1.intersection(fst2)
print(fst3)
# frozenset({'c'})


# symmetric_difference(s)
# Returns a set with the symmetric differences of two sets
fst1 = frozenset({'a', 'b', 'c'})
fst2 = frozenset({'c', 'd'})
fst3 = fst1.symmetric_difference(fst2)
print(fst3)
# frozenset({'a', 'b', 'd'})


# isdisjoint(s)
# Returns True if two sets have no intersection
fst1 = frozenset({'a', 'b', 'c'})
fst2 = frozenset({'c', 'd', 'e'})
fst3 = frozenset({'x', 'y', 'z'})
print(fst1.isdisjoint(fst2))  # False
print(fst1.isdisjoint(fst3))  # True


# issubset(s)
# Returns True if another set contains this set
fst1 = frozenset({'b', 'c'})
fst2 = frozenset({'a', 'b', 'c', 'd'})
fst3 = frozenset({'x', 'y', 'z'})
print(fst1.issubset(fst2))  # True
print(fst1.issubset(fst3))  # False


# issuperset(s)
# Returns True if this set contains the other set
fst1 = frozenset({'a', 'b', 'c', 'd'})
fst2 = frozenset({'b', 'c'})
fst3 = frozenset({'x', 'y', 'z'})
print(fst1.issuperset(fst2))  # True
print(fst1.issuperset(fst3))  # False


# union(s)
# Return a set containing the union of sets
fst1 = frozenset({'a', 'b'})
fst2 = frozenset({'c', 'd'})
fst3 = fst1.union(fst2)
print(fst3)
# frozenset({'a', 'b', 'c', 'd'})
