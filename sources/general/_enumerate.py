"""
Enumerate

* When you use enumerate(), the function gives you back two loop variables
  * The index of the current iteration
  * The value of the item at the current iteration

Syntax: enumerate(iterable [, start])
"""


# Enumerate in for
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(f'{index}: {value}', end=', ')
    # 0: a, 1: b, 2: c
print()


# Enumerate with start
lst = ['a', 'b', 'c']
for index, value in enumerate(lst, start=3):
    print(f'{index}: {value}', end=', ')
    # 3: a, 4: b, 5: c,
print()


# Enumerate as iter
lst = ['a', 'b', 'c']
lst_enumerate = enumerate(lst)
print(next(lst_enumerate))  # (0, 'a')
print(next(lst_enumerate))  # (1, 'b')
print(next(lst_enumerate))  # (2, 'c')


# Enumerate with list comprehension
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_even = [value for index, value in enumerate(lst) if index % 2 == 0]
print(lst_even)
# [1, 3, 5, 7, 9]


# Create enumerate function
def my_enumerate(iterable, start=0):
    for value in iterable:
        yield start, value
        start += 1


lst = ['a', 'b', 'c']
for index, value in my_enumerate(lst):
    print(f'{index}: {value}', end=', ')
    # 0: a, 1: b, 2: c
print()
