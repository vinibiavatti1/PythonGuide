"""
Fibonacci

* In Python, you dont need to use auxiliary varaibles sometimes, like in this
  algorithm, because Python has the umpack feature
"""


# Algorithm
amount = 1000
x, y = 1, 1
while y < amount:
    print(x, end=', ')
    x, y = y, x + y
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
