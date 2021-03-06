"""
Lambda

* Is a small anonymous function.
* Can take any number of arguments, but can only have ONE expression.

* Syntax:
  * lambda arguments : expression
"""


# Lambda Function
# NOTE: PEP8 recomend to use def for this case
calc = lambda x, y: x + y
print(calc(5, 5))
# 10


# Lambda Function with default args
# * You can use this way to freeze values to the parameters
calc = lambda x=1, y=2: x + y
print(calc())
# 3


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


# Function returning lambda
# * This is a usefull feature to make some function return a different action
#   by the parameters
def math_operation(operation):
    dct = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    return dct.get(operation)


operation1 = math_operation('*')
operation2 = math_operation('/')
print(operation1(5, 5))  # 25
print(operation2(8, 3))  # 2.6666666666666665
