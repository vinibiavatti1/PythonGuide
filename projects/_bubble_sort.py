"""
Bubble sort

* It is a simple sorting algorithm that repeatedly steps through the list,
  compares adjacent elements and swaps them if they are in the wrong order
"""
from collections.abc import Iterable


# Bubble sort
def bubble_sort(collection):
    """
    List sorting algorithm
    """
    if not isinstance(collection, Iterable):
        raise ValueError('The collection must be iterable')
    sort = False
    while not sort:
        sort = True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                collection[i + 1], collection[i] = \
                    collection[i], collection[i + 1]
                sort = False
    return collection


# Algorithm
lst = [1, 5, 7, 2, 3, 7, 4, 8, 3]
print(bubble_sort(lst))
