"""
Iterator

* The Iterator pattern is a behavioral design pattern that provides a way to
  access the elements of an aggregate object sequentially without exposing its
  underlying representation.
* It consists of two main components: the Iterator and the Iterable (or
  Aggregate).
* The Iterator is responsible for iterating over the elements, while the
  Iterable provides a way to create an Iterator.
"""


###############################################################################
# Iterator
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from collections.abc import Iterable
from typing import Iterator


# List
# * We will create a custom list, with the Iterator protocol implemented.
# * The methods `__iter__` and `__next__` make the class iterable.
class List(Iterable):
    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __iter__(self) -> Iterator:
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration()


# Testing (with iter)
# * Now, we can test the list. It can be used with the iter function to return
#   an iterator.
my_list = List(['A', 'B', 'C'])
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# A B C


# Testing (with for)
# * It also supports for-each loops.
my_list = List(['A', 'B', 'C'])
for item in my_list:
    print(item)
# A B C
