"""
Exceptions

* Used to control the exceptions and create validations
* The keyword used to manipulate exceptions are:
  * try: Define a try-except block
  * except: Handle the error defined in except
  * else: Execute just if no raise ocurred
  * finally: Finally is used to execute a code block idependent if some
             exception raised or not. This is usefull to clean up resources

* Syntax:
    try:
        ...
    except exception1:
        ...
    except exception2 as err:
        ...
    else:
        ...
    finally:
        ...

"""


###############################################################################
# Try, except, else, finally and raise
###############################################################################


# Try, except for all exceptions
# * NOTE: PEP8 NOT RECOMMENDED
try:
    x = 5 / 0
except:
    print('error')
    # error


# Try, except for specific exception without alias (as)
try:
    x = 5 / 0
except ZeroDivisionError:
    print('error')
    # error


# Try, except for specific exception with alias (as)
# * NOTE: In this way, the details for exception can be accessed
try:
    x = 5 / 0
except ZeroDivisionError as err:
    print(err)
    # division by zero


# Try, except chaining exceptions
# * In this example, when some exception happens, a new exception will be
#   raised with the origin exception as __cause__
# * The from keyword specify the __cause__ error for the current exception
try:
    try:
        x = 5 / 0
    except ZeroDivisionError as err:
        raise RuntimeError('You cannot divide') from err
except RuntimeError as err:
    print(err, err.__cause__, sep=', ')
    # You cannot divide, division by zero


# Try, except with more possible excepts
def raise_some_error(x):
    if x == 1:
        raise ArithmeticError('First error')
    else:
        raise StopIteration('Second error')


x = 2
try:
    raise_some_error(x)
except ArithmeticError as err:
    print(err)
except StopIteration as err:
    print(err)
    # Second error


# Try, except, finally
# * Finally is used to execute a code block idependent if some exception raised
#   or not
x = 10
try:
    y = x / 0
except ZeroDivisionError as err:
    print(err)
    # division by zero
finally:
    x = 0
print(x)
# 0


# Try, except, else
x = 10
try:
    y = x / 0
except ZeroDivisionError as err:
    print(err)
else:
    x = 0  # Execute just if no raise ocurred
print(x)
# 10


# Try, except, else, finally
x = 10
y = 2  # <- Change to zero to check the result!
try:
    z = x / y
except ZeroDivisionError as err:
    print('exception')  # Execute if some raise ocurred
else:
    print('else')       # Execute just if no raise ocurred
finally:
    print('finally')    # Execute always
# else
# finally


###############################################################################
# Create custom exception
###############################################################################


# Create exception class
class MyException(Exception):
    pass


# try, except, raise with exception created
def raise_error():
    raise MyException('My Error')


try:
    raise_error()
except MyException as err:
    print(err)
    # My Error


###############################################################################
# Raise, From
###############################################################################


# raise, from
# * Used to set the __cause__ attribute and the message states that the
#   exception was directly caused by. If you omit the from then no __cause__ is
#   set, but the __context__ attribute may be set as well
try:
    raise MyException('My Error') from ValueError('Value error')
except MyException as err:
    print(err)            # My Error
    print(err.__cause__)  # Value error