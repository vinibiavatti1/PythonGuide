"""
Lambda

* Is a small anonymous function.
* Can take any number of arguments, but can only have ONE expression.

Syntax: lambda arguments : expression
"""


# Lambda Function
# NOTE: PEP8 recomend to use def for this case
sum = lambda x, y: x + y
print(sum(5, 5))
# 10


# Return lambda from function
def multiply_fn(x):
    return lambda y: y * x


multiply = multiply_fn(5)
print(multiply(5))
# 25


# Lambda as parameters
tpl = (10, 20, 15, 18)
tpl = tuple(filter(lambda el: el >= 18, tpl))
print(tpl)
# (20, 18)


# Lambda in dictionaries
dct = {'action': lambda x: x * 5}
print(dct['action'](5))
# 25


# Lambda with if ternary
# NOTE: PEP8 recomend to use def for this case
fn = lambda x: 'one' if x == 1 else 'other'
print(fn(1))  # one
print(fn(5))  # other
