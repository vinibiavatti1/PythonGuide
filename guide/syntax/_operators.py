"""
Operators

The list below contains the operators present in Python:
* Arithmetic Operators
* Assignment Arithmetic Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Bitwise Operators
* Assignment Bitwise Operators

###############################################################################
Operator        Example         Representation
###############################################################################
Arithmetic operators:
+   	        x + y           Addition
-		        x - y           Subtraction
*		        x * y           Multiplication
/		        x / y           Division
//		        x // y          Floor division
%		        x % y           Modulo
**		        x ** y          Exponentiation
@               x @ y           Matrix Multiplication

Assignment operators:
=	            x = y	        x = y
+=	            x += y	        x = x + y
-=	            x -= y	        x = x - y
*=	            x *= y	        x = x * y
/=	            x /= y	        x = x / y
//=	            x //= y	        x = x // y
%=	            x %= y	        x = x % y
**=	            x **= y	        x = x ** y
@=              x @= y          x = x @ y

Comparison operators:
==	    	    x == y          Equal
!=	    	    x != y          Not equal
>	    	    x > y           Greater than
<	    	    x < y           Less than
>=	    	    x >= y          Greater than or equal to
<=	    	    x <= y          Less than or equal to

Logical operators:
and 	        x and y         Returns True if both statements are true
or	            x or y          Returns True if one of the statements is true
not	            not x           Returns the inverse result

Identity operators:
is 	            x is y          Returns True if both variables are the same
is not	        x is not y      Returns False if both variables are the same

Membership operators:
in 	            x in y          Returns True if element is present in iterable
not in	        x not in y      Returns False if element is present in iterable
###############################################################################

Bitwise Operators

* Low level operators
* Bitwise operators let you manipulate those individual bits of data at the
  most granular level
* You can use bitwise operators to implement algorithms such as compression,
  encryption, and error detection
* Python has no unsigned right shift operator (>>>), because integers in Python
  works different of other langs. Integers are unlimited, so, the sign bit
  doesn't have a fixed position
* The bits used to separate or target some bit sequence is called "bit mask"

###############################################################################
Operator        Example         Representation
###############################################################################
Bitwise Operators:
& 	            x & y	        AND
|		        x | y           OR
^		        x ^ y           XOR (exclusive OR)
~ 		        ~x              NOT
<<		        x << y          Shift to left
>>		        x >> y          Shift to right

Assignment Bitwise Operators:
&=	            x &= 3	        x = x & 3
|=	            x |= 3	        x = x | 3
^=	            x ^= 3	        x = x ^ 3
>>=	            x >>= 3	        x = x >> 3
<<=	            x <<= 3	        x = x << 3
###############################################################################
"""


###############################################################################
# Arithmetic Operators
###############################################################################


# Addition (+)
x = 5 + 5
print(x)
# 10


# Subtraction (-)
x = 5 - 5
print(x)
# 0


# Multiplication (*)
x = 5 * 5
print(x)
# 25


# Division (/)
# NOTE: / by 0 (zero) raises ZeroDivisionError
x = 25 / 5
y = 4. / 2
z = -6 / 4
print(x)
print(y)
print(z)
# 5.0
# 2.0
# -1.5


# Floor division or Integer division (//) (Used to divide integers)
# * The result value is rounding always going to the LESSER int (1.9 -> 1)
# * Using a decimal value to floor division always result in a decimal
#   result
# NOTE: // by 0 (zero) raises ZeroDivisionError
x = 15 // 2
y = 8. // 5
z = -6 // 4.
print(x)
print(y)
print(z)
# 7
# 1.0
# -2.0


# Modulo (%)
# NOTE: % by 0 (zero) raises ZeroDivisionError
x = 20 % 7
print(x)
# 6


# Exponentiation (**)
# NOTE: The ** operator uses Right-sided binding (right to left ordering)
x = 5 ** 2
print(x)
# 25


# Matrix Multiplication (@)
# * NOTE: There is no builtin type that implements the Matrix Multiplication
#   methods. Check _matrix_multiplication.py for more details


###############################################################################
# Assignment Arithmetic Operators
###############################################################################


# Addition and Assignment (+=)
# * Same as (x = x + y)
x = 4
x += 3
print(x)
# 7


# Subtraction and Assignment (-=)
# * Same as (x = x - y)
x = 4
x -= 3
print(x)
# 1


# Multiplication and Assignment (*=)
# * Same as (x = x * y)
x = 4
x *= 3
print(x)
# 12


# Division and Assignment (/=)
# * Same as (x = x / y)
x = 5
x /= 2
print(x)
# 2.5


# Floor Division and Assignment (//=)
# * Same as (x = x // y)
x = 4
x //= 3
print(x)
# 7


# Modulo and Assignment (%=)
# * Same as (x = x % y)
x = 4
x %= 3
print(x)
# 1


# Exponentiation and Assignment (**=)
# * Same as (x = x ** y)
x = 4
x **= 2
print(x)
# 16


# Matrix Multiplication and Assignment (@=)
# * NOTE: There is no builtin type that implements the Matrix Multiplication
#   methods. Check _matrix_multiplication.py for more details


###############################################################################
# Casting
###############################################################################


# Automatic Float Casting
# * When some float number is present in expression, the result will become a
#   float too
x = 3 ** 2 + 5 * 1.
y = 5. + 5
z = 5 + 5.
print(x)
print(y)
print(z)
# 14.0
# 10.0
# 10.0


###############################################################################
# Identity Operators
###############################################################################


# is
# * Used for reference equality
# * It's used to check if two references refer (or point) to the same object
x = [1, 2]
y = [1, 2]
print(x is x)
print(x is y)
# True
# False


# is not
# * Same as "is" but return the inverse boolean
x = [1, 2]
y = [1, 2]
print(x is not x)
print(x is not y)
# False
# True


# is None / is not None
# * To check None values we must use the "is" identity operator
# * Using "is" ensures that the reference of the object will be checked,
#   instead of the result of __eq__ magic method
x = None
print(x is None)
print(x is not None)
# True
# False


###############################################################################
# Membership Operators
###############################################################################


# in
# * Used to validate if the element is present in some iterable object
lst = [1, 2, 3, 4, 5]
print(3 in lst)
print(6 in lst)
# True
# False


# not in
# * Same as "in" but return the inverse boolean value
lst = [1, 2, 3, 4, 5]
print(3 not in lst)
print(6 not in lst)
# False
# True


###############################################################################
# Logical Operators
###############################################################################


# and
# * Use to compare two values based on the AND truth table:
# 0 0 = 0
# 0 1 = 0
# 1 0 = 0
# 1 1 = 1
if True and True:
    print(True)
# True


# or
# * Use to compare two values based on the OR truth table:
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 1
if False or True:
    print(True)
# True


# not
# * Used to negate the boolean value (inverse)
# 0 = 1
# 1 = 0
if not (False and True):
    print(True)
# True


###############################################################################
# Bitwise Operators
###############################################################################


# AND (& - ampersand) (x & y)
# 0 0 = 0
# 0 1 = 0
# 1 0 = 0
# 1 1 = 1
x = 156        # 10011100 (156)
y = 52         # 00110100 (52)
print(x & y)   # 00010100 (20)


# OR (| - bar) (x | y)
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 1
x = 156        # 10011100 (156)
y = 52         # 00110100 (52)
print(x | y)   # 10111100 (188)


# XOR (^ - caret) (x ^ y)
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 0
x = 156        # 10011100 (156)
y = 52         # 00110100 (52)
print(x ^ y)   # 10101000 (168)


# NOT (~ - tilde) (~x)
# 0 = 1
# 1 = 0
x = 156        # 10011100 (156)
print(~x)      # 01100011 (-157)


# Left shift (<<) (x << y)
x = 52         # 00110100 (52)
print(x << 1)  # 01101000 (104)
print(x << 2)  # 11010000 (208)


# Right shift (>>) (x >> y)
x = 52         # 00110100 (52)
print(x >> 1)  # 00011010 (26)
print(x >> 2)  # 00001101 (13)


###############################################################################
# Assignment Bitwise Operators
###############################################################################


# AND (&=)
# * Same as: (x = x & y)
x = 156
x &= 52
print(x)
# 20


# OR (|=)
# * Same as: (x = x | y)
x = 156
x |= 52
print(x)
# 188


# XOR (^=)
# * Same as: (x = x ^ y)
x = 156
x ^= 52
print(x)
# 168


# Left shift (<<=)
# * Same as: (x = x << y)
x = 32
x <<= 2
print(x)
# 128


# Right shift (>>=)
# * Same as: (x = x >> y)
x = 128
x >>= 2
print(x)
# 32
