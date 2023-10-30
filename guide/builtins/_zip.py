"""
Zip

* Make an iterator that aggregates elements from each of the iterables
* Syntax
  * zip(*iterables)
"""


# Iterables
tpl1 = (5, 6, 7)
tpl2 = ('house', 'person', 'dog')
for v1, v2 in zip(tpl1, tpl2):
    print(f'{v1}: {v2}', end=', ')
    # 5: house, 6: person, 7: dog,
print()


# Cast
lst1 = ['name', 'age']
lst2 = ['Vini', 26]
zp = zip(lst1, lst2)
print(set(zp))    # {('name', 'Vini'), ('age', 26)}
print(tuple(zp))  # (('name', 'Vini'), ('age', 26))
print(dict(zp))   # {'name': 'Vini', 'age': 26}


# Enumerated iterables
tpl1 = (5, 6, 7)
tpl2 = ('house', 'person', 'dog')
for index, (v1, v2) in enumerate(zip(tpl1, tpl2)):
    print(f'{index}: {v1} {v2}', end=', ')
    # 0: 5 house, 1: 6 person, 2: 7 dog,
print()
