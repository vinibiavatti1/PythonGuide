"""
Iterator design pattern

* Book: GOF
* Iterator is a behavioral design pattern that lets you traverse elements of a
  collection without exposing its underlying representation (list, stack, tree,
  etc.)
* The main idea of the Iterator pattern is to extract the traversal behavior of
  a collection into a separate object called an iterator
* NOTE: Check the _iter.py file for iterator details
"""
from collections.abc import Iterable


# Alphabet class
class Alphabet(Iterable):
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.size = len(self.alphabet)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.size:
            raise StopIteration()
        return self.alphabet[self.index]


# Algorithm
alphabet = Alphabet()
alphabet_iter = iter(alphabet)
print(next(alphabet_iter))  # A
print(next(alphabet_iter))  # B
print(next(alphabet_iter))  # C
print(next(alphabet_iter))  # D
