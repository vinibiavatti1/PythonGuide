"""
Map

* Used to process all itens in collection
* Return an iterator that applies function to every item of iterable,
  yielding the results
* Syntax
  * map(function, iterable ...)
"""


# Map collection with def
def plus_five(number):
    return number + 5


lst = [1, 2, 3, 4, 5, 6, 7, 8]
mapped = list(map(plus_five, lst))
print(mapped)
# [6, 7, 8, 9, 10, 11, 12, 13]


# Map collection with lambda
lst = [1, 2, 3, 4, 5, 6, 7, 8]
mapped = list(map(lambda n: n + 5, lst))
print(mapped)
# [6, 7, 8, 9, 10, 11, 12, 13]


# Map more collections with lambda
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 1, 2, 1]
mapped = list(map(lambda n1, n2: n1 * n2, lst1, lst2))
print(mapped)
# [1, 4, 3, 8, 5]
