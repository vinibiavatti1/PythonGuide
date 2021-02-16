"""
Iterators

* An iterator is an object that contains a countable number of values
* Technically, in Python, an iterator is an object which implements the
  iterator protocol, which consist of the methods __iter__() and __next__()
* Lists, tuples, dictionaries, strings and sets are all iterable objects
* All these objects accepts the iter() method which is used to get an iterator

Syntax: iter(iterable)
        next(iterator)
"""


# Tuple / list / set
tpl = (1, 2, 3, 4)
tpl_iter = iter(tpl)
print(next(tpl_iter))   # 1
print(next(tpl_iter))   # 2
print(next(tpl_iter))   # 3
print(next(tpl_iter))   # 4
# print(next(tpl_iter)) # StopIteration


# Dict
dct = {'name': 'Vini', 'age': 26}
dct_iter = iter(dct)
print(next(dct_iter))   # name
print(next(dct_iter))   # age
# print(next(dct_iter)) # StopIteration


# String
txt = 'Vini'
txt_iter = iter(txt)
print(next(txt_iter))   # V
print(next(txt_iter))   # i
print(next(txt_iter))   # n
print(next(txt_iter))   # i
# print(next(txt_iter)) # StopIteration


# Create iterator
# Implement __iter__ and __next__ methods to make it as iterable
class MyList:
    def __init__(self, *args):
        self.list = args

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        current = self.list[self.index]
        self.index += 1
        return current


my_list = MyList(1, 2, 3, 4)
my_list_iter = iter(my_list)
print(next(my_list_iter))   # 1
print(next(my_list_iter))   # 2
print(next(my_list_iter))   # 3
print(next(my_list_iter))   # 4
# print(next(my_list_iter)) # StopIteration
