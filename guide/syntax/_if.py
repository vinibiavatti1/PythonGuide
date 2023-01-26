"""
If (condition)

* The if instruction is used to create conditions
* Python supports the usual logical conditions from mathematics:
  * Equals: a == b
  * Not Equals: a != b
  * Less than: a < b
  * Less than or equal to: a <= b
  * Greater than: a > b
  * Greater than or equal to: a >= b
* Python supports chained conditions too:
  * Example: y1 < x < y2
* Syntax:
  * if <condition>:
  * if (<conditions):
"""


###############################################################################
# If Conditions
###############################################################################


# Create a condition using if (true)
# * The example below shows how to create a simple condition using if
# * This condition will always compute true
if 1 == 1:
    print('equal')
# equal


# Create a condition using if (false)
# * The example below shows how to create a simple condition using if
# * This condition will always compute false
if 1 == 2:
    print('equal')
# (nothing printed)


###############################################################################
# If Conditions (Comparison Operators)
###############################################################################


# Create a condition (Equal)
# * The below condition uses the operator == (equal)
x = 1
y = 1
if x == y:
    print('equal')
# equal


# Create a condition (Not Equal)
# * The below condition uses the operator != (not equal)
x = 1
y = 2
if x != y:
    print('not equal')
# not equal


# Create a condition (Greater Than)
# * The below condition uses the operator > (greater than)
x = 2
y = 1
if x > y:
    print('greater')
# greater


# Create a condition (Less Than)
# * The below condition uses the operator < (less than)
x = 1
y = 2
if x < y:
    print('less')
# less


# Create a condition (Greater Than or Equal To)
# * The below condition uses the operator >= (greater than or equal to)
x = 1
y = 1
if x >= y:
    print('greater or equal')
# greater or equal


# Create a condition (Less Than or Equal To)
# * The below condition uses the operator <= (less than or equal to)
x = 0
y = 1
if x >= y:
    print('less or equal')
# less or equal


###############################################################################
# If Conditions (Logical Operators)
###############################################################################


# Create a multiple conditions (and)
# * We can use logical operators to create multiples conditions to an if
x = 1
y = 1
if x == 1 and y == 1:
    print('equal')
# equal


# Create a multiple conditions (or)
# * The below condition uses the OR operator
x = 2
y = 1
if x == 1 or y == 2:
    print('equal')
# equal


# Create a inverse condition (not)
# * The not operator invert the result of the condition
x = 2
y = 1
if not x == y:
    print('not equal')
# not equal


# Create multiple conditions with multiple logical operators
# * We can use any unlimited operators to a if instruction
x = 1
y = 2
z = 3
if (x == 1 and y == 3) or not(z < 2):
    print('true')
# true


###############################################################################
# If Conditions (Identity Operators)
###############################################################################


# Create a condition to validate identity (is)
# * The is operator can be used to validate the identity of the object
x = [1, 2, 3]
y = x
if x is y:
    print('equal')
# equal


# Create a condition to validate identity (is not)
# * The not operator can be used to inverse the result
# * NOTE: Both variables contains the same value data, but the object is
#   different. X contains a list, and Y contains another list
x = [1, 2, 3]
y = [1, 2, 3]
if x is not y:
    print('not equal')
# not equal


# Create a condition to validate None
# * The below condition checks if the object is None
# * NOTE: To check if an object is None, the identity operator should be used
#   to ensure the object type will be validated without using the return of
#   the __eq__ magic method
x = None
if x is None:
    print('is none')
# is none


# Create a condition to validate a boolean value
# * The below condition checks if the object is True or False
# * NOTE: To check if an object is True or False, the identity operator should
#   be used to ensure the object type will be validated without using the
#   return of the __eq__ magic method
# * The condition can be simplified if you are going to validate if the value
#   is True or False (boolean)
x = True
if x is True:
    print('is true')
# is true


###############################################################################
# If Conditions (Membership Operators)
###############################################################################


# Create a condition to if x is present in collection (in)
# * The "in" operator can be used to validate if "x" is a member of "y"
x = 2
y = [1, 2, 3]
if x in y:
    print('x is member')
# x is member


# Create a condition to if x is not present in collection (not in)
# * To invert the result, we can use the not syntax
x = 7
y = [1, 2, 3]
if x not in y:
    print('x is not member')
# x is not member


###############################################################################
# Chained Comparison (a <= x <= b)
###############################################################################


# Create a condition using chained comparison (a <= x <= b)
# * The chained comparison is a valid syntax to Python
# * It is used to validate value ranges
# * Syntax: <condition> x <condition>
# * The example below is equivalent to: (if x >= 0 and x <= 10:)
x = 5
if 0 <= x <= 10:
    print('x is between')
# x is between


###############################################################################
# If Conditions (Check Implicit True Values)
###############################################################################


# Create a condition to validate an implicit true value (without operators)
# * The condition below does not use any operator. It will check if the value
#   is an implicit true or not (check the Python true rule table to see what
#   is considered True or False).
x = True
y = 1
z = [1, 2, 3]
if x:
    print('1. is true')
if y:
    print('2. is true')
if z:
    print('3. is true')
# 1. is true
# 2. is true
# 3. is true


###############################################################################
# If Else
###############################################################################


# Create a condition with else block
# * The condition can contain a else block that will be performed if the
#   condition evaluates to False
x = 1
if x is None:
    print('is none')
else:
    print('is not none')
# is not none


###############################################################################
# If Elif
###############################################################################


# Create multiple case conditions (if elif)
# * The "elif" instruction can be used to add a condition to an existent "if"
# * It is similar to the "match" syntax
x = 1
if x == 0:
    print('is 0')
elif x == 1:
    print('is 1')
elif x is None:
    print('is none')
# is 1


###############################################################################
# If Elif Else
###############################################################################


# Create multiple case conditions with else (if elif else)
# * The "else" can be used into a "if elif" clause to add a logic that will be
#   executed if any of the conditions are match
x = 'A'
if x == 0:
    print('is 0')
elif x == 1:
    print('is 1')
elif x is None:
    print('is none')
else:
    print('is other thing')
# is other thing


###############################################################################
# Ternary Condition
###############################################################################


# Create an inline condition (ternary if)
# * The ternary condition (ternary if) is used to create an inline condition
# * Syntax: <true result> if <condition> else <false result>
# * NOTE: the else block is always required for ternary conditions, otherwise,
#   a syntax error will be raised
x = 2
result = True if x == 1 else False
print(result)
# False


###############################################################################
# Ternary Condition With Tuple (Not Recommended)
###############################################################################


# Create an inline condition (ternary if using a tuple)
# * The ternary condition can be created using a tuple too
# * Syntax: (<false result>,<true result>)[<condition>]
# * NOTE: This is not recommended since it is hard to read
x = True
result = (1, 2)[x]
print(result)
# 2
