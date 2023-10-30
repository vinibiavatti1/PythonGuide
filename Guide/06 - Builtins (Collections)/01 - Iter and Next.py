"""
Iterators

* An iterator is an object that contains a countable number of values
* Technically, in Python, an iterator is an object which implements the
  iterator protocol, which consist of the methods __iter__() and __next__()
* Lists, tuples, dictionaries, strings and sets are all iterable objects

iter(collection [, sentinel])
* Run the iter __iter__ method from object and return a iterator
* sentinel is used when the first parameter is a callable, and the value cant
  be known. The sentinel is the indicated value to stop the interation

next(iterator [, default])
* Retrieve the next item from the iterator by calling its __next__() method. If
  default is given, it is returned if the iterator is exhausted, otherwise
  StopIteration is raised
* If default is given and the iterator is exhausted, it is returned instead of
  raising StopIteration

Syntax: iter(iterable [, sentinel])
        next(iterator [, default])
"""


# Iter and next
# * Tuple / list / set
tpl = (1, 2, 3, 4)
tpl_iter = iter(tpl)
print(next(tpl_iter))   # 1
print(next(tpl_iter))   # 2
print(next(tpl_iter))   # 3
print(next(tpl_iter))   # 4
# print(next(tpl_iter)) # StopIteration


# Iter and next with default value
# * Tuple / list / set
lst = (1, 2, 3, 4)
lst_iter = iter(lst)
print(next(lst_iter))     # 1
print(next(lst_iter))     # 2
print(next(lst_iter))     # 3
print(next(lst_iter))     # 4
print(next(tpl_iter, 5))  # 5 (default value)


# Iter and next
# * Dict
dct = {'name': 'Vini', 'age': 26}
dct_iter = iter(dct)
print(next(dct_iter))   # name
print(next(dct_iter))   # age
# print(next(dct_iter)) # StopIteration


# Iter and next
# * String
txt = 'Vini'
txt_iter = iter(txt)
print(next(txt_iter))   # V
print(next(txt_iter))   # i
print(next(txt_iter))   # n
print(next(txt_iter))   # i
# print(next(txt_iter)) # StopIteration


# Create iterator
# * Implement __iter__ and __next__ methods to make it as iterable
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


# Using enumerate with custom iterator
my_list = MyList(1, 2, 3, 4)
for index, value in enumerate(my_list):
    print(f'{index}: {value}', end=', ')
    # 0: 1, 1: 2, 2: 3, 3: 4,
print()


# Iter with sentinel and next
# * To use sentinel, the first parameter needs to be a callable (Function)
i = 0


def fn():
    global i
    i += 1
    return i


lst_iter = iter(fn, 3)
print(next(lst_iter))     # 1
print(next(lst_iter))     # 2
# print(next(lst_iter))   # StopIteration
