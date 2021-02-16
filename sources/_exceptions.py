"""
Exceptions
"""


# Create exception class
class MyException(Exception):
    pass


# try, except and raise
def raise_error():
    raise MyException('My Error')


try:
    raise_error()
except MyException as e:
    print(e)
    # My Error


# More excepts
x = 2


def raise_some_error(x):
    if x == 1:
        raise ArithmeticError('First error')
    else:
        raise StopIteration('Second error')


try:
    raise_some_error(x)
except ArithmeticError as e:
    print(e)
except StopIteration as e:
    print(e)
    # Second error


# with
# TODO
