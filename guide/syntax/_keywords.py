"""
Keywords

* Keywords are the reserved words in Python
* NOTE: We cannot use a keyword as a variable name, function name or any other
  identifier

###############################################################################
Keywords in Python
###############################################################################
False	    await	        else	        import	    pass
None	    break	        except	        in	        raise
True	    class	        finally	        is	        return
and	        continue	    for	            lambda	    try
as	        def	            from	        nonlocal	while
assert	    del	            global	        not	        with
async	    elif	        if	            or	        yield
###############################################################################
"""
import asyncio
import threading


# from, import
# * import keyword is used to import modules into the current namespace
# * from, import is used to import specific attributes or functions into the
#   current namespace
import math
from math import cos


# as
# * as is used to create an aliases
# * Can be used while importing a module
# * Can be used to define an alias to exception in try, except block
import math as m  # module alias
try:
    x = 1 / 0
except ZeroDivisionError as error:  # error alias
    print(error)
# division by zero


# True, False
# * True and False are truth values in Python
# * They are the results of comparison operations or logical (Boolean)
#   operations
true = True
false = False
result = 1 == 1
print(true, false, result, sep=', ')
# True, False, True


# None
# * None is a special constant in Python that represents the absence of a value
#   or a null value
# * NOTE: When a function is called and it not returns anything, a None value
#   will be returned
x = None
print(x, x is None, sep=', ')
# None, True


# and, or , not
# * and, or, not are the logical operators in Python
x = True
y = False
print(x and y, x or y, not x, not y, sep=', ')
# False, True, False, True


# assert
# * assert is used for debugging purposes
# * While programming, sometimes we wish to know the internal state or check if
#   our assumptions are true
# * assert helps us do this and find bugs more conveniently
# * assert is followed by a condition and a optional message
x = 5
y = 5
assert x == 5
assert x == 5, 'Error message'
# assert x != 5  Cause AssertionError


# async, await
# * The async and await keywords are provided by the asyncio library in Python
# * They are used to write concurrent code
async def async_function():
    await asyncio.sleep(0.1)
    print('Async')


asyncio.run(async_function())
# Async


# break, continue
# * break and continue are used inside for and while loops to alter their
#   normal behavior
# * break will end the smallest loop it is in and control flows to the
#   statement immediately below the loop
# * continue causes to end the current iteration of the loop, but not the whole
#   loop
x = 0
while x < 5:
    if x == 1:
        x += 1
        continue
    if x == 3:
        break
    print(x, end=', ')
    x += 1
print()
# 0, 2,

for i in range(5):
    if i == 1:
        continue
    if i == 3:
        break
    print(i, end=', ')
print()
# 0, 2,


# class
# * class is used to define a new user-defined class in Python
# * Class is a collection of related attributes and methods that try to
#   represent a real-world situation. This idea of putting data and functions
#   together in a class is central to the concept of object-oriented
#   programming (OOP)
class Client():
    pass


client = Client()
print(type(client))
# <class '__main__.Client'>


# def
# * def is used to define a user-defined function
# * Function is a block of related statements, which together does some
#   specific task. It helps us organize code into manageable chunks and also to
#   do some repetitive task
def my_sum(x, y):
    return x + y


result = my_sum(5, 5)
# 10


# del
# * del is used to delete the reference to an object.
# * Everything is object in Python.
# * We can delete a variable reference using del
dct = dict(name='Vini', age=26)
del dct['age']
print(dct)
# {'name': 'Vini'}


# if, else, elif
# * if, else, elif are used for conditional branching or decision making
# * When we want to test some condition and execute a block only if the
#   condition is true, then we use if and elif
# * elif is short for else if
# * else is the block which is executed if the condition is false
x = 5
if x < 5:
    print(f'{x} < 5')
elif x == 5:
    print(f'{x} == 5')
else:
    print(f'{x} > 5')
# 5 == 5


# try, except, else, finally
# * These keywords are used with exceptions in Python
# * Exceptions are basically errors that suggests something went wrong while
#   executing our program
# * try, except blocks are used to catch exceptions in Python
# Try, except, else, finally
x = 10
y = 2  # <- Change to zero to check the result!
try:
    z = x / y
except ZeroDivisionError as e:
    print('exception')  # Execute if some raise ocurred
else:
    print('else')       # Execute just if no raise ocurred
finally:
    print('finally')    # Execute always
# else
# finally


# for
# * for is used for looping. Generally we use for when we know the number of
#   times we want to loop
for i in range(5):
    print(i, end=', ')
print()
# 0, 1, 2, 3, 4,


# global
# * global is used to declare that a variable inside the function is global
#   (outside the function)
x = 5


def change_x(num):
    global x
    x = num


change_x(10)
print(x)
# 10


# in
# * in is used to test if a sequence (list, tuple, string etc) contains a value
# * The secondary use of in is to traverse through a sequence in a for loop
lst = [1, 2, 3]
dct = dict(name='Vini', age=26)
print(2 in lst)          # True
print(4 in lst)          # False
print('name' in dct)     # True
print('surname' in dct)  # False

for i in range(5):  # Used in for syntax
    pass

# is
# * Is used in Python for testing object identity.
# * While the == operator is used to test if two variables are equal or not,
#   "is" is used to test if the two variables refer to the same object
x = None
lst1 = [1, 2, 3]
lst2 = lst1
del lst1[0]
print(lst1 is lst2)  # True
print(x is None)     # True


# lambda
# * lambda is used to create an anonymous function (function with no name)
# * It is an inline function that does not contain a return statement
# * It consists of an expression that is evaluated and returned
lst = [1, 2, 3, 4]
filtered = list(filter(lambda x: x > 2, lst))
print(filtered)
# [3, 4]


# nonlocal
# * The use of nonlocal keyword is very much similar to the global keyword.
# * nonlocal is used to declare that a variable inside a nested function
#   (function inside a function) is not local
x = 10


def outer_function():
    x = 5

    def inner_function():
        nonlocal x
        x = 7
    inner_function()
    return x


print(x, outer_function(), sep=', ')
# 10, 7


# pass
# * pass is a null statement in Python.
# * Nothing happens when it is executed. It is used as a placeholder
def empty_function():
    pass


# return
# * return statement is used inside a function to exit it and return a value
def my_sub(x, y):
    return x - y


print(my_sub(7, 3))
# 4


# while
# * while is used for looping in Python
x = 0
while x < 5:
    print(x, end=', ')
    x += 1
print()
# 0, 1, 2, 3, 4,


# with
# * with statement is used to wrap the execution of a block of code within
#   methods defined by the context manager
# * Context manager is a class that implements __enter__ and __exit__ methods
# * Use of with statement ensures that the __exit__ method is called at the end
#   of the nested block
lock = threading.Lock()
with lock:
    print('Safe execution')
# Safe execution


# yield
# * yield is used inside a function like a return statement. But yield returns
#   a generator
# * Generator is an iterator that generates one item at a time
def my_range(end):
    x = 0
    while x < end:
        yield x
        x += 1


for i in my_range(5):
    print(i, end=', ')
print()
# 0, 1, 2, 3, 4,
