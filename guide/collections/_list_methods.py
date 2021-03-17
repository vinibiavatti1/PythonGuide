"""
List methods
"""


# append(object)
# * Adds an element at the end of the list
lst = ['a', 'b', 'c']
lst.append('d')
print(lst)
# ['a', 'b', 'c', 'd']


# insert(index, object)
# * Adds an element at the specified position
lst = ['a', 'b', 'c']
lst.insert(0, 'c')
print(lst)
# ['c', 'a', 'b', 'c']


# extend(iterable)
# * Add the elements of a list (or any iterable), to the end of the current
#   list
lst = ['a', 'b', 'c']
lst.extend(('d', 'e'))
print(lst)
# ['a', 'b', 'c', 'd', 'e']


# remove(object)
# * Removes the item with the specified value
lst = ['a', 'b', 'c']
lst.remove('c')
print(lst)
# ['a', 'b']


# pop(index)
# * Removes the element at the specified position and returns it
lst = ['a', 'b', 'c']
item = lst.pop(1)
print(lst)
# ['a', 'c']

lst = ['a', 'b', 'c']
item = lst.pop()  # When index not set, the last item will be removed
print(lst)
# ['a', 'b']


# clear()
# * Removes all the elements from the list
lst = ['a', 'b', 'c']
lst.clear()
print(lst)
# []


# copy()
# * Returns a copy of the list
lst1 = ['a', 'b', 'c']
lst2 = lst1.copy()
print(lst2)
# ['a', 'b', 'c']


lst1 = ['a', 'b', 'c']
lst2 = list(lst1)  # Using list()
print(lst2)
# ['a', 'b', 'c']


# count(object)
# * Returns the number of elements with the specified value
lst = ['a', 'a', 'b']
count = lst.count('a')
print(count)
# 2


# index(object, [start], [stop])
# * Returns the index of the first element with the specified value
lst = ['a', 'b', 'c']
idx = lst.index('b')
print(idx)
# 1


lst = ['a', 'b', 'c', 'a', 'b', 'c', 'a']
idx = lst.index('a', 1, 5)
print(idx)
# 3


# reverse()
# * Reverses the order of the list
lst = ['a', 'b', 'c']
lst.reverse()
print(lst)
# ['c', 'b', 'a']


# sort([key=], [reverse=])
# * Sorts the list
# * NOTE: It will change the current list, so,
lst = ['c', 'b', 'a']
lst.sort()
print(lst)
# ['a', 'b', 'c']

lst = ['a', 'b', 'c']
lst.sort(reverse=True)
print(lst)
# ['c', 'b', 'a'] reverse


lst = ['A', 'b', 'C']
lst.sort()
print(lst)
# ['A', 'C', 'b'] Note that sort is case sensitive


lst = ['A', 'b', 'C']
lst.sort(key=str.lower)
print(lst)
# ['A', 'b', 'C'] Change the key to a lower function


# sort([key=], [reverse=])
# * using different key function
def sort(el):
    return el['year']


lst = [{'year': 2021}, {'year': 2015}, {'year': 2017}]
lst.sort(key=sort)
print(lst)
# [{'year': 2015}, {'year': 2017}, {'year': 2021}]


# sort([key=], [reverse=])
# * using different key lambda
lst = [{'year': 2021}, {'year': 2015}, {'year': 2017}]
lst.sort(key=lambda el: el['year'])  # Lambda
print(lst)
# [{'year': 2015}, {'year': 2017}, {'year': 2021}]
