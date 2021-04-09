"""
Try, except, finally

* Used to control the exceptions and create validations
* The keyword used to manipulate exceptions are:
  * try: Define a try-except block
  * except: Handle the error defined in except
  * else: Execute just if no raise ocurred
  * finally: Finally is used to execute a code block idependent if some
             exception raised or not. This is usefull to clean up resources

* Try, except, else, finnaly syntax:
    try:
        ...
    except exception1:
        ...
    except exception2 as err:
        ...
    except (exception3, exception4) as err:
        ...
    else:
        ...
    finally:
        ...

* Raise syntax:
    raise exception(message)
    raise exception(message) from cause
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


# Try, except for specific exception
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


# Try, except with more possible excepts
x = 0  # <- Change it to a string to check the execution of TypeError block
try:
    y = 10 / x
except ZeroDivisionError as err:
    print(err)
    # division by zero
except TypeError as err:
    print(err)
    # unsupported operand type(s) for /: 'int' and 'str'


# Try, except with more exception in the same except block
x = 0  # <- Change it to a string to check the execution of TypeError block
try:
    y = 10 / x
except (ZeroDivisionError, TypeError) as err:
    print(err)
    # division by zero
    # unsupported operand type(s) for /: 'int' and 'str'


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


# Raise from (Set __cause__)
# * Used to set the __cause__ attribute and the message states that the
#   exception was directly caused by. If you omit the from then no __cause__ is
#   set, but the __context__ attribute may be set as well
# * The "from" keyword specify the __cause__ error for the current exception
try:
    try:
        x = 5 / 0
    except ZeroDivisionError as err:
        raise RuntimeError('You cannot divide') from err
except RuntimeError as err:
    print(err, err.__cause__, sep=', ')
    # You cannot divide, division by zero


###############################################################################
# Create user-defined exception
###############################################################################


# Create exception class
class MyException(Exception):
    pass


try:
    raise MyException('My Error')
except MyException as err:
    print(err)
    # My Error
