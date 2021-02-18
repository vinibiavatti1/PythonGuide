"""
For
"""


# For range(stop)
for i in range(5):
    print(i, end=', ')
    # 0, 1, 2, 3, 4,
print()


# For range(start, stop)
for i in range(5, 10):
    print(i, end=', ')
    # 5, 6, 7, 8, 9,
print()


# For range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=', ')
    # 0, 2, 4, 6, 8,
print()


# For each string
txt = 'Hello world'
for char in txt:
    print(char, end='')
    # Hello world
print()


# For each tuple / list / set
tpl = (1, 2, 3)
for n in tpl:
    print(n, end=', ')
    # 1, 2, 3,
print()


# For each tuple / list / set with index
lst = ['a', 'b', 'c']
for i in range(len(lst)):
    print(f'{i}: {lst[i]}', end=', ')
    # 0: a, 1: b, 2: c,
print()


# For each dict
dct = {'name': 'Vini', 'age': 26}
for key in dct:
    print(key, end=', ')
    # name, age, (keys)
print()


for key in dct:
    print(dct[key], end=', ')
    # Vini, 26, (values)
print()


# For each dict items()
for key, val in dct.items():
    print(f'{key}: {val}', end=', ')
    # name: Vini, age: 26
print()


# Break
for i in range(50):
    print(i, end=', ')
    # 0, 1, 2, 3, 4, 5,
    if i == 5:
        break
print()


# Continue
for i in range(10):
    if i % 2 != 0:
        continue
    print(i, end=', ')
    # 0, 2, 4, 6, 8,
print()


# For else
for i in range(5):
    print(i, end=', ')
    # 0, 1, 2, 3, 4, end
else:
    print('end')
