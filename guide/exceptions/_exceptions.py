"""
Exceptions

* Used to control the exceptions and create validations
* The keyword used to manipulate exceptions are:
  * try
  * except
  * finally
"""


# Try except
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(e)
    # division by zero


# Create exception class
class MyException(Exception):
    pass


# try except raise with exception created
def raise_error():
    raise MyException('My Error')


try:
    raise_error()
except MyException as e:
    print(e)
    # My Error


# Raise from
# * Used to set the __cause__ attribute and the message states that the
#   exception was directly caused by. If you omit the from then no __cause__ is
#   set, but the __context__ attribute may be set as well
try:
    raise MyException('My Error') from ValueError('Value error')
except MyException as e:
    print(e.__cause__)
    # Value error


# Try, except with more possible excepts
def raise_some_error(x):
    if x == 1:
        raise ArithmeticError('First error')
    else:
        raise StopIteration('Second error')


x = 2
try:
    raise_some_error(x)
except ArithmeticError as e:
    print(e)
except StopIteration as e:
    print(e)
    # Second error


# Try, except and finally
# * Finally is used to execute a code block idependent if some exception raised
#   or not
x = 10
try:
    y = x / 0
except ZeroDivisionError as e:
    print(e)
    # division by zero
finally:
    x = 0
print(x)
# 0


# Try except else
x = 10
try:
    y = x / 0
except ZeroDivisionError as e:
    print(e)
else:
    x = 0  # Execute just if no raise ocurred
print(x)
# 10
