"""
Set comprehension

* Set comprehension offers a shorter syntax when you want to create a new set
  based on the values of an existing set.
* NOTE: The print results can be in other order then the commentaries

Syntax: {expression for item in iterable if condition == True}
"""


# Clone set
st1 = {'a', 'b', 'c', 'd'}
st2 = {el for el in st1}
print(st2)
# {'a', 'b', 'c', 'd'}


# Static value
st1 = {'a', 'b', 'c', 'd'}
st2 = {1 for el in st1}
print(st2)
# {1, 1, 1, 1}


# Transform element
st1 = {'a', 'b', 'c', 'd'}
st2 = {el.upper() for el in st1}
print(st2)
# {'A', 'B', 'C', 'D'}


# Condition in element
st1 = {'a', 'b', 'c', 'd'}
st2 = {el if el == 'a' else 'z' for el in st1}
print(st2)
# {'a', 'z', 'z', 'z'}


# Condition in for
st1 = {1, 2, 3, 4, 5}
st2 = {el for el in st1 if el > 3}
print(st2)
# {4, 5}


# Condition (in) in for
st1 = {'apple', 'pineaple', 'nothing'}
st2 = {el for el in st1 if 'a' in el}
print(st2)
# {'apple', 'pineaple'}
