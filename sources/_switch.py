"""
Switch

* NOTE: There is no switch in Python. But we can use dicts to make a similar
"""


# Simple switch
number = 'two'
switch = {
    'one': 1,
    'two': 2,
    'three': 3
}
print(switch.get(number))
# 2


# Switch with lambda
operator = '*'


def calc(x, y, operator):
    switch = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return switch.get(operator, lambda x, y: None)(x, y)


result = calc(5, 5, '*')
print(result)
# 25
