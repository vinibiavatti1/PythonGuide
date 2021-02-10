"""
Tuple methods examples
"""
# count(object)
# Returns the number of elements with the specified value
tpl = ('a', 'a', 'b')
count = tpl.count('a')
print(count) # 2

# index(object, [start], [stop])
# Returns the index of the first element with the specified value
tpl = ('a', 'b', 'c')
idx = tpl.index('b')
print(idx) # 1

tpl = ('a', 'b', 'c', 'a', 'b', 'c', 'a')
idx = tpl.index('a', 1, 5)
print(idx) # 3