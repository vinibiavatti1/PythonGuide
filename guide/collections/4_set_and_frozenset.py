"""
Set and Frozenset

* Sets are used to store multiple items in a single variable.
* A set will never contain the same element twice
* Differently from lists, sets are unordered and un-indexed. It means that the
  items will not be in the same order as they were inserted, and the items
  cannot be accessed by their index position
* Think in a set as a bucket of items. The items can be added and removed, but
  the order will not be kept
* Sets in Python follow the same math concept of sets. Some math operations
  like union, intersection, difference and symmetric difference can be applied
  to sets
* To define a set, the curly brackets notation "{}" is used
* Frozensets are immutable sets. They are created using the `frozenset()`
* NOTE: Since dictionaries also use curly brackets, it is important to
  differentiate them. Dictionaries must have a key and a value, while sets only
  have values. The interpreter will know if it is a set or a dictionary by the
  presence of the colon ":".

Properties (Set):
( ) Ordered
(X) Mutable
( ) Allow Duplicate
( ) Indexed

Properties (Frozenset):
( ) Ordered
( ) Mutable
( ) Allow Duplicate
( ) Indexed
"""


###############################################################################
# Set/Frozenset Operations
###############################################################################


# Creating a Set
# * A set can be created using curly brackets "{}"
# * Different from tuples, the curly brackets are mandatory
# * When a set will be defined with a single element, the comma is not
#   required as it is for tuples
# * NOTE: Empty brackets create a dict, not a set. To create an empty set, the
#   `set()` function must be used
x = {1, 2, 3}  # Curly brackets
x = {1}        # Curly brackets with one element
x = set()      # (Empty) with set() function


# Creating a Frozenset
# * The frozenset is only a normal set that cannot be changed after creation
# * The unique way to create a frozenset is by using the `frozenset()` function
#   with a existent set as argument
x = frozenset({1, 2, 3})  # From existent set
x = frozenset()           # Empty frozenset


# Type hint for a Set/Frozenset
# * To set a type hint for a set/frozenset, only one type will be used to
#   define the type of all elements in the set/frozenset
x: frozenset[int] = {1, 2, 3, 4, 5}
x: set[int] = {1, 2, 3, 4, 5}


# Casting to Set/Frozenset
# * The `set()` and `frozenset()` functions can be used to cast a collection
#   into a set/frozenset
x = set((1, 2, 3))
y = frozenset((1, 2, 3))
print(x, y, sep='\n')
# {1, 2, 3}
# frozenset({1, 2, 3})


# Cloning a Set/Frozenset
# * Sets and frozensets can be cloned by using the `set()` or `frozenset()`
#   functions with the set/frozenset to be cloned as argument
x = {1, 2, 3}
y1 = set(x)
y2 = frozenset(x)
print(y1, y2, sep='\n')
# {1, 2, 3}
# frozenset({1, 2, 3})


###############################################################################
# Set/Frozenset Elements
###############################################################################


# Getting elements from a Set/Frozenset
# * Since a set/frozenset is not indexed, the elements cannot be accessed by
#   their index position
# * To work with a set, the methods must be used
# * In the example below, we used the `pop()` method to get some element
#   of the set (note that sets and frozensets are not ordered, so the element
#   returned by `pop()` is random)
x = {1, 2, 3}
y = x.pop()
print(y)
# 2


# Setting elements in a Set/Frozenset
# * Since a set/frozenset is not indexed, elements cannot be added using index
#   position
# * To work with a set, the methods must be used
# * In the example below, we used the `add()` method to add an element to the
#   set
# * Since sets are not ordered, the element will be added in a random position
# * When the element already exists in the set, it will be ignored
x = {1, 2, 3}
x.add(4)
x.add(2)  # ignored
print(x)
# {3, 4, 1, 2}


# Checking if an item exists in a Set
# * The `in` operator can be used to check if an item exists in a set
x = {1, 2, 3}
y = 2 in x
print(y)
# True


###############################################################################
# Set/Frozenset Properties
###############################################################################


# ( ) Ordered
# * Sets aren't ordered, so the elements will not keep the same order as they
#   were inserted
# * Since they are not ordered, the elements cannot be accessed by their index
"""
x = {1, 2, 3}
print(x[1])

TypeError: 'set' object is not subscriptable
"""


# (X) Mutable (Set)
# * Sets are mutable, so the elements can be changed
# * Frozensets are a immutable version of sets
x = {1, 2, 3}
x.add(4)
print(x)
# {3, 1, 4, 2} (order not preserved)


# ( ) Mutable (Frozenset)
# * Frozenset cannot be changed
"""
x = frozenset({1, 2, 3})
x.add(4)

AttributeError: 'frozenset' object has no attribute 'add'
"""


# ( ) Allows Duplicate
# * Sets do not allow duplicate elements
# * When a duplicate element is added, it will be ignored if the set already
#   has the element
x = {1, 1, 1}
print(x)
# {1}


# ( ) Indexed
# * Sets are not indexed, so the elements cannot be accessed by their index
#   position
"""
x = {1, 2, 3}
print(x[1])

TypeError: 'set' object is not subscriptable
"""


###############################################################################
# Set/Frozenset Built-in Functions
###############################################################################


# Set/Frozenset Built-in Functions
# * The Python built-in functions for collections can be used with
#   sets/frozensets
x = {1, 2, 3, 4}
print(sum(x))  # 10    (The sum of elements)
print(min(x))  # 1     (The min value)
print(max(x))  # 4     (The max value)
print(len(x))  # 4     (The length)
print(all(x))  # True  (All values are True)
print(any(x))  # True  (Any value is True)


###############################################################################
# Set/Frozenset Comparison
###############################################################################


# Equal (==)
# * The comparison operators can be used to compare sets
# * Set works different from lists and tuples. The comparing operators will
#   be evaluated in a mathematical way
"""
x1 ######          ###### x2
  #      #        #      #
 #        #      #        #
#          # == #          #
 #        #      #        #
  #      #        #      #
   ######          ######
"""
x1 = {1, 2}
x2 = {2, 1}
y = x1 == x2
print(y)
# True


# Not Equal (!=)
# * Same as equal, but inverted
"""
x1 ######          ###### x2
  #      #        #      #
 #        #      #        #
#          # != #          #
 #        #      #        #
  #      #        #      #
   ######          ######
"""
x1 = {1, 2}
x2 = {2, 1}
y = x1 != x2
print(y)
# False


# Superset (>=)
# * To check if a set is a super set of another set, the `>=` operator can be
#   used
# * The operator can be used as `x1 >= x2` or `x1.issuperset(x2)`
"""
x1 ######
  #      #
 # x2 ##  #
#    #  #  #
 #    ##  #
  #      #
   ######
"""
x1 = {1, 2, 3}
x2 = {2, 3}
y = x1 >= x2
print(y)
# True


# Subset (<=)
# * To check if a set is a sub set of another set, the `<=` operator can be
#   used
# * The operator can be used as `x1 <= x2` or `x1.issubset(x2)`
"""
x2 ######
  #      #
 # x1 ##  #
#    #  #  #
 #    ##  #
  #      #
   ######
"""
x1 = {2, 3}
x2 = {1, 2, 3}
y = x1 <= x2
print(y)
# True


# Union (|)
# * The union operator can be used to join two sets into a new set
# * The operator can be used as `x1 | x2` or `x1.union(x2)`
"""
x1 ###### ###### x2
  #      #      #
 #      # #      #
#   y  # y #  y   #
 #      # #      #
  #      #      #
   ###### ######
"""
x1 = {1, 2, 3}
x2 = {4, 5, 6}
y = x1 | x2
print(y)
# {1, 2, 3, 4, 5, 6}


# Intersection (&)
# * The intersection operator can be used to get the common elements between
#   two sets
# * The operator can be used as `x1 & x2` or `x1.intersection(x2)`
"""
x1 ###### ###### x2
  #      #      #
 #      # #      #
#      # y #      #
 #      # #      #
  #      #      #
   ###### ######
"""
x1 = {1, 2, 3}
x2 = {2, 3, 4}
y = x1 & x2
print(y)
# {2, 3}


# Difference (-)
# * The difference operator can be used to get the elements that are in one
#   set, but not in the other
# * The operator can be used as `x1 - x2` or `x1.difference(x2)`
# * Note that only items present in the first set "x1" will be returned. If
#   both sets must be returned, the symmetric difference must be used
"""
x1 ###### ###### x2
  #      #      #
 #      # #      #
#   y  #   #      #
 #      # #      #
  #      #      #
   ###### ######
"""
x1 = {1, 2, 3}
x2 = {3, 4, 5}
y = x1 - x2
print(y)
# {1, 2}


# Symmetric difference (^)
# * The symmetric difference operator can be used to get the elements that are
#   in one set, but not in the other
# * The operator can be used as `x1 ^ x2` or `x1.symmetric_difference(x2)`
# * The difference between the difference and the symmetric difference is that
#   the symmetric difference will return the items that are in the first set
#   "x1" and in the second set "x2"
"""
x1 ###### ###### x2
  #      #      #
 #      # #      #
#   y  #   #  y   #
 #      # #      #
  #      #      #
   ###### ######
"""
x1 = {1, 2, 3}
x2 = {3, 4, 5}
y = x1 ^ x2
print(y)
# {1, 2, 4, 5}


###############################################################################
# Set/Frozenset Methods
###############################################################################


# add(__element)
# * Adds an element to the set
x = {1, 2, 3}
x.add(4)
print(x)
# {1, 2, 3, 4}


# clear()
# * Removes all the elements from the set
x = {1, 2, 3}
x.clear()
print(x)
# set()


# copy()
# * Returns a copy of the set
x1 = {1, 2, 3}
x2 = x1.copy()
print(x2)
# {1, 2, 3}


# discard(__element)
# * Remove the specified item from the set
# * NOTE: It will not raise error if the element doesn't exist
x1 = {1, 2, 3}
x1.discard(1)
x1.discard(4)  # NOTE: Not raise error
print(x1)
# {2, 3}


# remove(__element)
# * Remove the specified item from the set
# * NOTE: It will raise error if the element doesn't exist
"""
x1 = {1, 2, 3}
x1.remove(4)

KeyError: 4
"""


# union(*s)
# * Same as the union operator "|"
# * The parameter "s" is arbitrary, so that it can receive any number of sets
x1 = {1, 2}
x2 = {3, 4}
x3 = {5, 6}
y = x1.union(x2, x3)
print(y)
# {1, 2, 3, 4, 5, 6}


# update(*s)
# * Same as union, but it will update the set instead of returning a new one
# * The parameter "s" is arbitrary, so that it can receive any number of sets
x1 = {1, 2}
x2 = {3, 4}
x3 = {5, 6}
x1.update(x2, x3)
print(x1)
# {1, 2, 3, 4, 5, 6}


# intersection(*s)
# * Same as the intersection operator "&"
# * The parameter "s" is arbitrary, so that it can receive any number of sets
x1 = {1, 2, 3}
x2 = {2, 3, 4}
x3 = {3, 4, 5}
y = x1.intersection(x2, x3)
print(y)
# {3}


# intersection_update(*s)
# * Same as intersection, but it will update the set instead of returning a new
#   one
# * The parameter "s" is arbitrary, so that it can receive any number of sets
x1 = {1, 2, 3}
x2 = {2, 3, 4}
x3 = {3, 4, 5}
x1.intersection_update(x2, x3)
print(x1)
# {3}


# difference(*s)
# * Same as the difference operator "-"
# * The parameter "s" is arbitrary, so that it can receive any number of sets
# * NOTE: This will only return the values of the first set. To get a
#   difference items of all sets, use symmetric difference
x1 = {1, 2, 3}
x2 = {2, 3, 4}
x3 = {3, 4, 5}
y = x1.difference(x2, x3)
print(y)
# {1}


# difference_update(*s)
# * Same as difference, but it will update the set instead of returning a new
#   one
# * The parameter "s" is arbitrary, so that it can receive any number of sets
x1 = {1, 2, 3}
x2 = {2, 3, 4}
x3 = {3, 4, 5}
x1.difference_update(x2, x3)
print(x1)
# {1}


# symmetric_difference(__s)
# * Same as the symmetric difference operator "^"
# * In this case, all different items of all sets will be returned
# * NOTE: This method doesn't accept multiple sets as parameter
x1 = {1, 2, 3}
x2 = {2, 3, 4}
y = x1.symmetric_difference(x2)
print(y)
# {1, 4}


# symmetric_difference_update(__s)
# * Same as symmetric difference, but it will update the set instead of
#   returning a new one
# * NOTE: This method doesn't accept multiple sets as parameter
x1 = {1, 2, 3}
x2 = {2, 3, 4}
x1.symmetric_difference_update(x2)
print(x1)
# {1, 4}


# isdisjoint(__s)
# * Return True if two sets have a null intersection
x1 = {1, 2, 3}
x2 = {4, 5, 6}
y = x1.isdisjoint(x2)
print(y)
# True


# issubset(__s)
# * Same as the subset operator "<="
# * Return True if this set is a subset of the other set
x1 = {2, 3}
x2 = {1, 2, 3}
y = x1.issubset(x2)
print(y)
# True


# issuperset(__s)
# * Same as the superset operator ">="
# * Return True if this set is a superset of the other set
x1 = {1, 2, 3}
x2 = {2, 3}
y = x1.issuperset(x2)
print(y)
# True


# pop()
# * Removes a random element from the set
x = {1, 2, 3, 4}
y = x.pop()
print(x, y)
# {1, 3, 4} 2


###############################################################################
# Set/Frozenset Iteration
###############################################################################


# Iterating over a Set/Frozenset (with for-each) (XXX recommended XXX)
# * The for-each notation can be used to iterate over a set or frozenset
# * Since sets are not ordered and indexed, the elements will be returned in
#   a random order
# * NOTE: The while loop is not recommended for iterating over a set/frozenset
#   since it is not a ordered and indexed collection
x = {1, 2, 3}
for el in x:
    print(el, end=', ')
print()
# 3, 1, 2,


# Iterating over a List (with comprehension)
# * The comprehension syntax can be used to iterate over a Set/Frozenset
# * In this example, we will not use the result of the comprehension, so the
#   result will not be stored in memory
x = {1, 2, 3}
{print(el) for el in x}
# 1
# 3
# 2


# Iterating over a Set/Frozenset (with iter)
# * The `iter` function can be used to iterate over a Set/Frozenset
# * In this case, we must use the `next` function to get the next element
#   returned by the iterator
x = {1, 2, 3}
y = iter(x)
print(next(y))  # 2
print(next(y))  # 3
print(next(y))  # 1


###############################################################################
# Set/Frozenset Mapping
###############################################################################


# Mapping a Set/Frozenset (with comprehension) (XXX recommended XXX)
# * A mapping process is a process that will transform each element of a
#   collection into another element
# * The comprehension syntax can be used to iterate over a Set/Frozenset
# * In this example, we will use the result of the comprehension, so the
#   result will be stored in memory
x = {1, 2, 3}
y = {el * 2 for el in x}
print(y)
# 6, 2, 4


# Mapping a Set/Frozenset (with for-each)
# * The for-each notation can be used to iterate over a set or frozenset
# * Since sets are not ordered and indexed, the elements will be returned in
#   a random order
# * In this case, we will create a new list using the for-each notation
x = {1, 2, 3}
y = set()
for el in x:
    y.add(el * 2)
print(y)
# 6, 2, 4


# Mapping a List (with map)
# * The `map` function can be used to iterate over a Set/Frozenset transforming
#   each element into another element in a new set
# * The `map` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the comprehension to a set/frozenset, since
#   the result of a map operation is a map object
x = {1, 2, 3}
y = set(map(lambda el: el * 2, x))
print(y)
# 4, 2, 6


###############################################################################
# Set/Frozenset Filtering
###############################################################################


# Filtering a Set/Frozenset (with comprehension) (XXX recommended XXX)
# * The filtering process is a process that will filter the elements of a
#   collection based on a condition
# * A condition can be applied to the comprehension to filter the elements
#   that will be returned
x = {1, 2, 3, 4}
y = {el for el in x if el > 2}
print(y)
# 4, 3


# Filtering a Set/Frozenset (with for-each)
# * The for-each notation can be used to iterate over a list without the need
#   of a preset index variable
x = {1, 2, 3, 4}
y = set()
for el in x:
    if el > 2:
        y.add(el)
print(y)
# 4, 3


# Filtering a Set/Frozenset (with filter)
# * The `filter` function can be used to iterate over a list filtering each
#   element based on a condition
# * The `filter` function accepts a function as first argument that will be
#   applied for each element
# * Note that we needed to convert the comprehension to a Set/Frozenset, since
#   the result of a filter operation is a filter object
x = {1, 2, 3, 4}
y = set(filter(lambda el: el > 2, x))
print(y)
# 4, 3


###############################################################################
# Set/Frozenset Reducing
###############################################################################


# Reducing a Set/Frozenset (with for-each) (XXX recommended XXX)
# * The reducing process is a process that will reduce the elements of a
#   collection into a single value
# * The reducing process can be done by using the for-each notation
# * Note that we can use the built-in functions `sum()`, `min()` and `max()`
#   for the most common reducing operations
x = {1, 2, 3, 4}
acc = 0
for el in x:
    acc += el
print(acc)
# 10


# Reducing a Set/Frozenset (with reduce)
# * The `functools.reduce` function can be used to reduce a Set/Frozenset
# * For this case, we must import the `reduce` function from the `functools`
#   module
# * The `reduce` function accepts a function as first argument that will be
#   applied for each element. The function has two arguments, the first is
#   the accumulator and the second is the current element
from functools import reduce
x = {1, 2, 3, 4}
result = reduce(lambda acc, el: acc + el, x)
print(result)
# 10
