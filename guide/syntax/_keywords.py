"""
Keywords

* This page lists all the keywords present in Python language
* Each keyword has an example to show a case of usage of it
* The keywords cannot be used as identifiers, otherwise, a syntax exception
  will be raised
* Below there is a list containing all the keywords in Python
* NOTE: Soft keyword means that the keyword is threat as keyword only in
  specific cases
###############################################################################
Keyword                 Description
###############################################################################
and                     AND operator
as                      Defines aliases to resources
assert                  asserts a boolean expression
async                   Declares asynchronous resources
await                   Awaits asynchronous executions
break                   Breaks a loop
case                    Used inside match block (Soft keyword)
class                   Declares a class
continue                Skips loop block
def                     Declares a function
del                     Delete resource
elif                    Used in if blocks
else                    Used in if blocks
except                  Used in try blocks
False                   Reference to False boolean value
finally                 Used in try blocks
for                     Defines a loop with a sequence
from                    Used with import, yield and raise instructions
global                  References a global resource
if                      Conditional instruction
import                  Imports Python modules
in                      Membership operator
is                      Identity operator
lambda                  Declares a anonymous function
match                   Structural match pattern instruction (Soft keyword)
None                    Defines a null pointer
nonlocal                References a non-local resource
not                     NOT operator
or                      OR operator
pass                    Defines an empty block
raise                   Raises an exception
return                  Defines the return data of a function
True                    Reference to True boolean value
try                     Defines a try block for exception handling
while                   Defines a conditional loop
with                    Creates a context to a resource
yield                   Defines the generator return data
###############################################################################
"""


###############################################################################
# Keywords
###############################################################################


# and
# * Logical AND operator that can be used in expressions
# * It is considered a binary operator since it must be used with two
#   values/expressions
x = True
y = False
result = x and y
print(result)
# False


# as
# * Defines an alias to a resource
# * It can be used in some cases:
#   * With the import statement to declares an alias to the imported resource
#   * With the except instruction to give an alias to the exception
#   * With the "with" instruction to give an alias to the resource
import threading as thread

try:
    result = 1 / 0
except ArithmeticError as err:
    pass

with thread.Lock() as file:
    pass


# assert
# * the "assert" keyword is used for debugging purposes
# * While programming, sometimes we wish to know the internal state or check if
#   our assumptions are true
# * It helps to find bugs more conveniently
# * It is followed by a condition and a optional message
assert 1 == 1
assert 1 == 1, 'An error ocurred'


# async
# * The "async" keyword is provided by the asyncio library in Python
# * They are used to write concurrent code
# * NOTE: Check _asyncio.py for more details
async def async_function():
    pass


# await
# * The "await" keyword is provided by the asyncio library in Python
# * They are used to invoke an asynchronous operation
# * NOTE: Check _asyncio.py for more details
async def other_async_function():
    await async_function()


# break
# * The "break" keyword is used to stops a loop
# * When the cursor reaches a break instruction inside a loop, the cursor will
#   automatically jump out of the loop
# * It works for "while" and "for" loops
for val in range(10):
    print(val, end=' ')
    if val == 5:
        break
print()
# 0 1 2 3 4 5


# case
# * The "case" keyword is used to define pattern cases inside the "match"
#   instruction block
# * Multiple cases can be defined inside the block
# * This is a soft keyword, i.e. this keyword is considered a keyword only in
#   a specific context. In this case, only inside the "match" block
x = 200
match x:
    case 200:
        print('Success')
    case 500:
        print('Error')
# Success


# class
# * The "class" keyword is used to declare a class
# * A class in Python is a custom datatype that can have specific behaviors and
#   attributes
class MyClass:
    pass


# continue
# * Like the "break" keyword, the "continue" keyword skips the current loop
#   execution
# * When the pointer reaches the "continue" instruction, the cursor will be
#   send to the next loop iteration automatically
for val in [1, 2, 3, 4, 5]:
    if val == 3:
        continue
    print(val, end=' ')
print()
# 1 2 4 5


# def
# * The "def" keyword is used to declare functions and methods
# * It can be used inside and outside a class. When used inside a class, the
#   "def" will declare a method, when outside, the "def" will declare a
#   function
def function():
    pass


# del
# * The "del" keyword is used to delete a resource reference
# * Since Python has a Garbage Collector, the "del" is used only for special
#   cases
# * Examples: Delete an item from a list, delete a key from a dictionary, etc.
collection = ['A', 'B', 'C']
del collection[1]
print(collection)
# ['A', 'C']


# elif
# * The "elif" instruction is used together with the "if" statement
# * It defines a "else if" condition, that will be evaluated when the above
#   condition(s) evaluates to False
x = 2
if x == 1:
    print('one')
elif x == 2:
    print('two')
# two


# else
# * The "else" statement is usually used together with the "if" statement
# * It defines a "else" block, that will be performed when the above
#   condition(s) evaluates to False
# * It can also be used with the "for", "while" and "try" instructions
x = 2
if x == 1:
    print('one')
else:
    print('two')
# two


# except
# * The "except" keyword is used with the "try" block, to specify a block that
#   will watch one or multiple exceptions, and when some of the exceptions are
#   raised inside the "try" block, the "except" block is performed
try:
    result = 1 / 0
except ArithmeticError as err:
    print(err)
# division by zero


# False
# * The "False" keyword is used to reference the false boolean value
# * NOTE: Since Python is case sensitive, this keyword will only be interpreted
#   if capitalized, otherwise, the word will be unrecognized
x = False


# finally
# * The "finally" keyword is used with the "try" block to define a code block
#   that will be performed independent if some exception is raised or not by
#   the "try" block
try:
    result = 1 / 0
except ArithmeticError as err:
    print(err)
finally:
    print('end')
# division by zero
# end


# for
# * The "for" instruction is used to create a iteration loop
# * Since the "while" loop works by a condition, the "for" loop works to
#   iterate a collection
# * The "for" loop requires a iterable object to be used to create the loop
for val in range(5):
    print(val, end=' ')
print()
# 0 1 2 3 4


# from
# * The "from" keyword is used in three different contexts:
#   * 1. With the "import" to specify the path to the module
#   * 2. With the "raise" to specify a exception cause to the inner exception
#   * 3. With the "yield" to yields a generator value inside other generator
from typing import Any

try:
    try:
        result = 1 / 0
    except ArithmeticError as err:
        raise ValueError('Value error') from err
except ValueError as err:
    print(err.__cause__)

def generator():
    yield 1
def other_generator():
    yield from generator()

print(next(other_generator()))
# division by zero
# 1


# global
# * The "global" keyword is used to specify a reference to a global variable
#   inside a context
# * For example, when there is a global variable outside a function, we this
#   variable should be managed inside the function, we can specify this
#   variable with a global keyword inside the function to have access to this
#   outside variable
x = 1
def function():
    global x
    x = 2
function()
print(x)
# 2


# if
# * The "if" keyword is used to define a condition. If the condition evaluates
#   to True, the "if" block will be performed, otherwise, the "if" block will
#   be ignored
# * The "else" and "elif" keywords can be used together with the "if" to define
#   multiple conditional blocks
x = 1
if x == 1:
    print('one')
# one


# import
# * The "import" statement is used to import some Python module
# * Is considered a Python module any file with the ".py" extension
# * The "from" keyword can be used with the "import" to specify the location of
#   the Python module
import threading


# in
# * The "in" operator is used to check if a value is member of a collection
# * It is considered a membership operator in Python
collection = ['A', 'B', 'C']
if 'B' in collection:
    print('B is present inside the collection')
# B is present inside the collection


# is
# * The "is" operator is used to check the identity of some object in Python
# * It is considered a identity operator in Python
# * NOTE: To validate if some object is "None", the is operator is used instead
#   of the "==" operator, because the "is" will check the reference that is
#   used in memory directly, and the equals operator will evaluates a method to
#   check if the object is the same
collection = [1, 2, 3]
other_collection = collection
if collection is other_collection:
    print('It is the same object')
# It is the same object


# lambda
# * The "lambda" keyword is used to declare an anonymous function in Python
# * Since Python was not made to follow Functional Programming concepts, this
#   keyword is available anyway
# * It can be used with the function programming built-in functions, like:
#   map(), filter(), sorted(), ...
collection = [1, 2, 3, 4]
collection_filtered = filter(lambda val: val > 2, collection)
print(list(collection_filtered))
# [3, 4]


# match
# * The "match" keyword is used to define a Structural Pattern Matching
#   instruction
# * The purpose of this concept is to provide a organized way to validate
#   structural or value patterns of a Python resource
# * Since it is similar with the "switch" statement in other programming
#   languages, it works different
# * The "case" keyword is used together with the "match" statement to define
#   the pattern case blocks
collection = (1, 2, 3)
match collection:
    case (1, 2):
        print('one')
    case (1, 2, z):
        print('two')
    case _:
        print('three')
# two


# None
# * The "None" keyword is used to specify a reference to a null pointer
# * NOTE: Since Python is case sensitive, this keyword will only be interpreted
#   if capitalized, otherwise, the word will be unrecognized
x = None


# nonlocal
# * The "nonlocal" keyword is used to set a reference to a variable outside the
#   current context, but still not global
# * It is similar with the "global" keyword, but works for non-global variables
def function():
    x = 1
    def inner_function():
        nonlocal x
        x = 2
    inner_function()
    return x
print(function())
# 2


# not
# * Logical "NOT" operator that can be used in expressions
# * It is considered an unary operator since it works only for one
#   value/expression
x = False
result = not x
print(result)
# True


# or
# * Logical OR operator that can be used in expressions
# * It is considered a binary operator since it must be used with two
#   values/expressions
x = True
y = False
result = x or y
print(result)
# True


# pass
# * The "pass" keyword is used to define an empty block in Python
# * Since Python indentation is mandatory to define blocks, the "pass" keyword
#   helps to define an empty block for some case that an indentation is
#   required
# * The ellipsis "..." works as the same way
def empty_function():
    pass


# raise
# * The "raise" keyword is used to raise an exception
# * The "from" keyword can be used together with the raise to identify a parent
#   exception as the cause of the inner exception, when available
try:
    raise ValueError('Raise example')
except ValueError as err:
    print(err)
# Raise example


# return
# * The "return" keyword is used to return a value from a function
# * A function without "return" always returns the value None
def my_sum(x, y):
    return x + y
print(my_sum(7, 3))
# 10


# True
# * The "True" keyword is used to reference the true boolean value
# * NOTE: Since Python is case sensitive, this keyword will only be interpreted
#   if capitalized, otherwise, the word will be unrecognized
x = True


# try
# * The "try" keyword is used to specify a block that will be watched for
#   exception raises
# * When an exception is raised inside the "try" block, the "except" block that
#   is set to handle the exception that was raised will be evaluated
# * The keywords "except", "finally" and "else" can be used with the "try"
#   block
try:
    result = 1 / 0
except ArithmeticError as err:
    print(err)
# division by zero


# while
# * The "while" keyword is used to define a conditional loop
# * While the condition evaluates to True, the loop block will be performed
x = 0
while x < 5:
    print(x, end=' ')
    x += 1
print()
# 0 1 2 3 4


# with
# * The "with" statement is used as a context manager to an object in Python
#   that implements the Context Manager protocol
# * When the cursor enters in a "with" block, the "__enter__" method from the
#   context manager protocol will be triggered
# * When the cursor jumps out of the "with" block, the "__exit__" method from
#   the context manager protocol will be triggered
# * It is usually used to handle database connections, to perform thread
#   operations with a Lock(), to read a file and ensure that the file is closed
#   after usage, etc.
with threading.Lock():
    print('Sync operation')
# Sync operation


# yield
# * The "yield" keyword is used to declare a generator, and to specify what
#   this generator will returns
# * The "from" keyword can be used together with the "yield" when a generator
#   is called inside other generator
def generator():
    yield 1
    yield 2
generator_iter = generator()
print(next(generator_iter))
print(next(generator_iter))
# 1
# 2
