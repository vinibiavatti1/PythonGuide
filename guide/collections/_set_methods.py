"""
Set methods

* NOTE: The print results can be in other order then the commentaries
"""


# add(element)
# Adds an element to the set
st = {'a', 'b', 'c'}
st.add('d')
print(st)
# {'a', 'b', 'c', 'd'}


# clear()
# Removes all the elements from the set
st = {'a', 'b', 'c'}
st.clear()
print(st)
# set()


# copy()
# Returns a copy of the set
st1 = {'a', 'b', 'c'}
st2 = st1.copy()
print(st2)
# {'a', 'b', 'c'}


# discard(element)
# Remove the specified item
st1 = {'a', 'b', 'c'}
st1.discard('a')
st1.discard('d')  # NOTE: Not raise error
print(st1)
# {'b', 'c'}


# remove(element)
# Remove the specified item (Raise an error if the element doesn't exist)
st1 = {'a', 'b', 'c'}
st1.remove('a')
# st1.remove('d') NOTE: Raise error!
print(st1)
# {'b', 'c'}


# union(s)
# NOTE: Check _set_operations.py for other way to make this operation
# Return a set containing the union of sets
st1 = {'a', 'b'}
st2 = {'c', 'd'}
st3 = st1.union(st2)
print(st3)
# {'a', 'b', 'c', 'd'}


# update()
# Update the set with the union of this set and others
st1 = {'a', 'b'}
st2 = {'c', 'd'}
st1.update(st2)
print(st1)
# {'a', 'b', 'c', 'd'}


# intersection()
# NOTE: Check _set_operations.py for other way to make this operation
# Returns a set, that is the intersection of two other sets
st1 = {'a', 'b', 'c'}
st2 = {'c', 'd'}
st3 = st1.intersection(st2)
print(st3)
# {'c'}


# intersection_update()
# Removes the items in this set that are not present in other, specified set(s)
st1 = {'a', 'b', 'c'}
st2 = {'c', 'd'}
st1.intersection_update(st2)
print(st1)
# {'c'}


# difference(s)
# NOTE: Check _set_operations.py for other way to make this operation
# Returns a set containing the difference between two or more sets
st1 = {'a', 'b', 'c'}
st2 = {'c', 'd'}
st3 = st1.difference(st2)
print(st3)
# {'a', 'b'}


# difference_update(s)
# Removes the items in this set that are also included in another, specified
# set
st1 = {'a', 'b', 'c'}
st2 = {'a', 'b'}
st1.difference_update(st2)
print(st1)
# {'c'}


# symmetric_difference(s)
# NOTE: Check _set_operations.py for other way to make this operation
# Returns a set with the symmetric differences of two sets
st1 = {'a', 'b', 'c'}
st2 = {'c', 'd'}
st3 = st1.symmetric_difference(st2)
print(st3)
# {'a', 'b', 'd'}


# symmetric_difference_update(s)
# Inserts the symmetric differences from this set and another
st1 = {'a', 'b', 'c'}
st2 = {'c', 'd'}
st1.symmetric_difference_update(st2)
print(st1)
# {'a', 'b', 'd'}


# isdisjoint(s)
# Returns True if two sets have no intersection
st1 = {'a', 'b', 'c'}
st2 = {'c', 'd', 'e'}
st3 = {'x', 'y', 'z'}
print(st1.isdisjoint(st2))  # False
print(st1.isdisjoint(st3))  # True


# issubset(s)
# Returns True if another set contains this set
st1 = {'b', 'c'}
st2 = {'a', 'b', 'c', 'd'}
st3 = {'x', 'y', 'z'}
print(st1.issubset(st2))  # True
print(st1.issubset(st3))  # False


# issuperset(s)
# Returns True if this set contains the other set
st1 = {'a', 'b', 'c', 'd'}
st2 = {'b', 'c'}
st3 = {'x', 'y', 'z'}
print(st1.issuperset(st2))  # True
print(st1.issuperset(st3))  # False


# pop()
# Removes an element from the set
# NOTE: It will be a random element
st = {'a', 'b', 'c', 'd'}
print(st.pop())
# 'a'
