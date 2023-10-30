"""
Counter

* Dict subclass for counting hashable objects
* Used to count every element individually
* Syntax
  * Counter([iterable-or-mapping])
"""
import collections


# Counter
lst = list('mississippi')
lst_counter = collections.Counter(lst)
print(lst_counter)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


# Most common
print(lst_counter.most_common(3))
# [('i', 4), ('s', 4), ('p', 2)]
