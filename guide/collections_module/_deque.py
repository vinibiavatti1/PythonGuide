"""
Deque

* List-like container with fast appends and pops on either end
* You have methods to manipulate both sides of the list

* Methods
  * appendleft(x)
  * popleft(x)
  * extendleft(x)
  * rotate(n)

* Syntax
  * deque(iterable [, maxlen])
"""
import collections


# Append Left
dq = collections.deque([1, 2, 3])
dq.appendleft(0)
print(dq)
# deque([0, 1, 2, 3])


# Pop Left
dq = collections.deque([1, 2, 3])
pop = dq.popleft()
print(dq, pop, sep=', ')
# deque([2, 3]), 1


# Extend Left
dq = collections.deque([1, 2, 3])
dq.extendleft([-2, -1, 0])
print(dq)
# deque([0, -1, -2, 1, 2, 3])


# Rotate
dq = collections.deque([1, 2, 3, 4, 5, 6])
dq.rotate(3)
print(dq)
# deque([4, 5, 6, 1, 2, 3])
dq.rotate(-2)
print(dq)
# deque([6, 1, 2, 3, 4, 5])
