"""
Bubble sort
"""


def bubble_sort(collection):
    sort = False
    while not sort:
        sort = True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                collection[i + 1], collection[i] = \
                    collection[i], collection[i + 1]
                sort = False
    return collection


lst = [1, 5, 7, 2, 3, 7, 4, 8, 3]
print(bubble_sort(lst))
