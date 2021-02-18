"""
Filter

* Used to filter elements from some collection
* Construct an iterator from those elements of iterable for which function
  returns true
* Syntax
  * filter(function, iterable)
"""


# Filter collection with def
def even(number):
    return number % 2 == 0


lst = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = list(filter(even, lst))
print(filtered)
# [2, 4, 6, 8]


# Filter collection with lambda
lst = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = list(filter(lambda n: n % 2 == 0, lst))
print(filtered)
# [2, 4, 6, 8]
