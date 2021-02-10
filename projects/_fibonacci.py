"""
Fibonacci
"""
x, y, z = 1, 0, 0
while y < 500:
    z = x + y
    print(z, end=', ')
    x = y
    y = z