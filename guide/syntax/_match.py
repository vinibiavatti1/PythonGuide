"""
Match

* The "match" instruction was added in Python 3.10 version
* This statement is used to verify pattern cases of a value. It is a better and
  richer way to validate data without using the "if elif" syntax
* This concept of the "match" instruction is called "Structural Pattern
  Matching"
* The case statements are use to validate the "pattern" and the input value
* It is similar to the "switch" instruction for some other languages, like Java
  and C#, but it works different. While in "switch" statement the value will be
  checked with conditions, for "match" a pattern will be verified
* More content in: https://www.python.org/dev/peps/pep-0636
* NOTE: For this page, I used the concept of HTTP request status to make the
  examples more real and easy to understand.
* Syntax:

match <target>:
    case <pattern>:
    case <pattern>, <pattern>:
    case <pattern> if <condition>:
"""


###############################################################################
# Pattern Matching (Single Value)
###############################################################################


# Match a value that corresponds to a pattern
# * The "match" instruction works like the "if elif" syntax, but allow to
#   define patterns to validate the input
# * The patterns are set in "case" clauses, and each case will be verified to
#   check if the input value corresponds with the pattern
# * In the example below, a single value will be validated
http_status = 200
match http_status:
    case 200:
        print('success')
    case 500:
        print('fail')
# success


# Match a value that doesn't corresponds to any pattern
# * If no pattern corresponds with the input value, no "case" block is
#   performed
# * In the example below, there is no pattern for the "x" value
http_status = 300
match http_status:
    case 200:
        print('success')
    case 500:
        print('fail')
# (nothing printed)


# Match a value that corresponds to the "anyone" case
# * We can define a "any" value for when no pattern is match with the input
# * To define the "any" value, we can specify the pattern with a non-literal
#   value, i.e. with a variable name
# * For this example, the default variable name is a wildcard "_" since we will
#   not use the value
# * The wildcard works as a "any" value for the "case" instructions
http_status = 300
match http_status:
    case 200:
        print('success')
    case 500:
        print('fail')
    case _:
        print('unknown')
# unknown


# Match a value that corresponds to the "anyone" case and print the value
# * Like the example above, the variable didn't match the "case" values, and
#   the last "case" scenario was performed. This "case" had a wildcard since we
#   didn't use the value, but for the example below, we will need to know what
#   is the value that didn't match with any pattern
# * Instead using the wildcard "_", we defined a variable name that will
#   receive the input value
http_status = 300
match http_status:
    case 200:
        print('success')
    case 500:
        print('fail')
    case x:
        print(f'unknown status: {x}')
# unknown status: 300


###############################################################################
# Pattern Matching (Multiple Values)
###############################################################################


# Match a tuple that corresponds to a pattern (value)
# * Collections can be accepted into a "match" instruction
# * There is two ways to work with the patterns: value and structural
#   * Value: The pattern is defined with values, and the collection values will
#     be verified
#   * Structural: The pattern is defined with variables, and the collection
#     structure will be verified
# * In this example, the values of the tuple will be verified
collection = (200, 201, 202)
match collection:
    case (200, 201):
        print('one')
    case (200, 201, 202):
        print('two')
    case (200, 300, 500):
        print('three')
# two


# Match a tuple that corresponds to a pattern (structural)
# * In the structural pattern matching, the structure of the collection will be
#   verified
# * If the structure corresponds with the pattern, the case will be performed
collection = ('Maria', 'Rose', 'Sina')
match collection:
    case (x, y):
        print('one')
    case (x, y, z):
        print('two')
    case (x, y, z, w):
        print('three')
# two


# Match a tuple that corresponds to a pattern (value and structural)
# * The both concepts can be used together to check a pattern that match with
#   the input value
# * In this case, we will use literal values and variable names
collection = (1, 2, 3)
match collection:
    case (2, y, z):
        print('one')
    case (x, 2, z):
        print('two')
    case (x, y, 2):
        print('three')
# two


# Match a tuple that corresponds to multiple patterns
# * If multiple patterns match with the input value, the first will be
#   performed
# * In this example, there are more then only one "case" that matches with the
#   input value
collection = (1, 2, 3)
match collection:
    case (1, y, z):
        print('one')
    case (x, 2, z):
        print('two')
    case (x, y, 3):
        print('three')
# one


###############################################################################
# OR Cases (|)
###############################################################################


# Match a value that corresponds to a pattern with OR
# * We can use the OR (|) operand in a "case" statement to avoid code
#   repetition
# * The same "case" can be used for different matches
# * The example below shows the second "case" that corresponds to: B or C or D
http_status = 401
match x:
    case 200 | 201 | 202:
        print('success')
    case 400 | 401 | 403:
        print('unauthorized')
    case _:
        print('unknown')
# unauthorized


# Match a list that corresponds to a pattern with OR
# * With collections we can use the same behavior. For a collection element, we
#   will define a "case" with ORs that checks if the element matches with the
#   pattern
# * This concepts is called "sub pattern"
# * Note that the last case is impossible to be matched since the superior case
#   has the same rule
collection = ['net', 403]
match collection:
    case 'net', 200:
        print('net success')
    case 'net', (400 | 401 | 403):
        print('net unauthorized')
    case 'lan', 200:
        print('lan success')
    case 'lan', (400 | 401 | 403):
        print('lan unauthorized')
# net unauthorized


###############################################################################
# Guards (if)
###############################################################################


# Match a value that corresponds to a pattern with a guard
# * Guards are conditions that can be added to the "case" statement that will
#   be checked when the pattern is matched
# * Even if the pattern is matched, if the guard returns False, the "case"
#   block will not be performed
# * In the example below, we use a guard to the first case. The guard will
#   check other variable value to evaluate the condition
authenticated = True
http_status = 401
match http_status:
    case 401 if authenticated:
        print('forbidden')
    case 401:
        print('unauthorized')
# forbidden


# Match a value that doesn't corresponds to a pattern with a guard
# * The example below uses the same example of above, but the guard will be
#   evaluated to False
authenticated = False
http_status = 401
match http_status:
    case 401 if authenticated:
        print('forbidden')
    case 401:
        print('unauthorized')
# unauthorized


###############################################################################
# Matching Objects
###############################################################################


# Declare the objects
# * To use objects into a "match" instruction, we have to declare the class
#   first
# * We will use "named tuples" to facilitate the class definition
# * Take a look at the collections reference for more details
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Vector = namedtuple('Vector', ['x', 'y', 'z'])


# Match an object that corresponds to a pattern
# * We can use instances of the Point class, or even other classes into the
#   "case" statements to validate the pattern
# * If the instance is not equivalent with the input instance, it will not be
#   matched, and no error will happen
point = Point(2, 3)
match point:
    case Point(1, 3):
        print('one')
    case Point(2, 3):
        print('two')
    case other:
        print('three')
# two


# Match an object that corresponds to a pattern with a variable
# * We can use the variables into the constructor of the object to be the
#   "anyone" value
# * In this example, the same match of the above example was used, but the
#   third case uses a "anyone" variable in the pattern
point = Point(2, 5)
match point:
    case Point(1, 3):
        print('one')
    case Point(2, _):
        print('two')
    case other:
        print('three')
# two


# Match an object that corresponds to a pattern with named params
# * Named parameters are also allowed to be used into the object constructors
# * The example below is the same of the above one, but uses keyword arguments
point = Point(2, 5)
match point:
    case Point(x=1, y=3):
        print('one')
    case Point(x=2, y=_):
        print('two')
    case other:
        print('three')
# two


# Match an object that corresponds to a None pattern
# * The value None can be checked too in a "case" statement
# * Note that other object types are used to this example, and no error
#   happens, because match handles it by using the "isinstance()" function
point = Point(2, 3)
match point:
    case Vector(2, 3, 4):
        print('one')
    case Point(1, 3):
        print('two')
    case None:
        print('none')
# none
