"""
Frozenset comprehension

* Frozenset comprehension offers a shorter syntax when you want to create a set
  based on the values of an existing frozenset
* NOTE: To become a frozenset again, it needs to be cast
* NOTE: The print results can be in other order then the commentaries

Syntax: frozenset({expression for item in iterable if condition == True})
"""


# Clone set
st1 = frozenset({'a', 'b', 'c', 'd'})
st2 = frozenset({el for el in st1})
print(st2)
# frozenset({'a', 'b', 'c', 'd'})


# Static value
st1 = frozenset({'a', 'b', 'c', 'd'})
st2 = frozenset({1 for el in st1})
print(st2)
# frozenset({1, 1, 1, 1})


# Transform element
st1 = frozenset({'a', 'b', 'c', 'd'})
st2 = frozenset({el.upper() for el in st1})
print(st2)
# frozenset({'A', 'B', 'C', 'D'})


# Condition in element
st1 = frozenset({'a', 'b', 'c', 'd'})
st2 = frozenset({el if el == 'a' else 'z' for el in st1})
print(st2)
# frozenset({'a', 'z', 'z', 'z'})


# Condition in for
st1 = frozenset({1, 2, 3, 4, 5})
st2 = frozenset({el for el in st1 if el > 3})
print(st2)
# frozenset({4, 5})


# Condition (in) in for
st1 = frozenset({'apple', 'pineaple', 'nothing'})
st2 = frozenset({el for el in st1 if 'a' in el})
print(st2)
# frozenset({'apple', 'pineaple'})
