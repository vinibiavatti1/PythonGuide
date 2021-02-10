"""
List comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Syntax: [expression for item in iterable if condition == True]
"""
# Clone list
lst1 = ['a', 'b', 'c', 'd']
lst2 = [el for el in lst1]
print(lst2) # ['a', 'b', 'c', 'd']

# Static value
lst1 = ['a', 'b', 'c', 'd']
lst2 = [1 for el in lst1]
print(lst2) # [1, 1, 1, 1]

# Transform element
lst1 = ['a', 'b', 'c', 'd']
lst2 = [el.upper() for el in lst1]
print(lst2) # ['A', 'B', 'C', 'D']

# Condition in element
lst1 = ['a', 'b', 'c', 'd']
lst2 = [el if el == 'a' else 'z' for el in lst1]
print(lst2) # ['a', 'z', 'z', 'z']

# Condition in for
lst1 = [1, 2, 3, 4, 5]
lst2 = [el for el in lst1 if el > 3]
print(lst2) # [4, 5]

# Condition (in) in for
lst1 = ['apple', 'pineaple', 'nothing']
lst2 = [el for el in lst1 if 'a' in el]
print(lst2) # ['apple', 'pineaple']