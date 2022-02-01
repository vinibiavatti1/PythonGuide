"""
Operators

* There are 7 operator types in Python:
  * Aritmetic operators
  * Assignment operators
  * Comparison operators
  * Logical operators
  * Identity operators
  * Membership operators
  * Bitwise operators

###############################################################################
Operator        Example                 Representation
###############################################################################
Aritmetic operators:
+   	        x + y                   Addition
-		        x - y                   Subtraction
*		        x * y                   Multiplication
/		        x / y                   Division
//		        x // y                  Floor division
%		        x % y                   Modulo
**		        x ** y                  Exponentiation
@               x @ y                   Matrix Multiplication
NOTE: The ** operator uses Right-sided binding (right to left ordering)

Assignment operators:
=	            x = 5	                x = 5
+=	            x += 3	                x = x + 3
-=	            x -= 3	                x = x - 3
*=	            x *= 3	                x = x * 3
/=	            x /= 3	                x = x / 3
%=	            x %= 3	                x = x % 3
//=	            x //= 3	                x = x // 3
**=	            x **= 3	                x = x ** 3
&=	            x &= 3	                x = x & 3
|=	            x |= 3	                x = x | 3
^=	            x ^= 3	                x = x ^ 3
>>=	            x >>= 3	                x = x >> 3
<<=	            x <<= 3	                x = x << 3

Comparison operators:
==	    	    x == y                  Equal
!=	    	    x != y                  Not equal
>	    	    x > y                   Greater than
<	    	    x < y                   Less than
>=	    	    x >= y                  Greater than or equal to
<=	    	    x <= y                  Less than or equal to

Logical operators:
and 	        x < 5 and x < 10        Returns True if both statements are
                                        true
or	            x < 5 or x < 4          Returns True if one of the statements
                                        is true
not	            not(x < 5 and x < 10)   Reverse the result

Identity operators:
is 	            x is y                  Returns True if both variables are the
                                        same object
is not	        x is not y              Returns True if both variables are not
                                        the same object

Membership operators:
in 	            x in y                  Returns True if a sequence with the
                                        specified value isbpresent in the
                                        object
not in	        x not in y              Returns True if a sequence with the
                                        specified value is not present in the
                                        object

Bitwise operators:
& 	            8 & 16	        AND
|		        8 | 16          OR
^		        8 ^ 16          XOR
~ 		        ~8              NOT
<<		        8 << 2          Shift left
>>		        8 >> 2          Shift right
###############################################################################
"""


###############################################################################
# Aritmetic operators
###############################################################################


# Addition (+)
print(5 + 5)
# 10


# Subtraction (-)
print(5 - 5)
# 0


# Multiplication (*)
print(5 * 5)
# 25


# Division (/)
# NOTE: / by 0 (zero) raises ZeroDivisionError
print(25 / 5)  # 5.0
print(4. / 2)  # 2.0
print(-6 / 4)  # -1.5


# Floor division or Integer division (//) (Used to divide integers)
# NOTE: The result value is rounding always goes to the LESSER int (1.9 -> 1)
# NOTE: // by 0 (zero) raises ZeroDivisionError
print(15 // 2)  # 7 (in normal division, it would be 7.5)
print(8. // 5)  # 1.0
print(-6 // 4)  # -2


# Modulo (%)
# NOTE: % by 0 (zero) raises ZeroDivisionError
print(20 % 7)
# 6


# Exponentiation (**)
print(5 ** 2)
# 25


# Matrix Multiplication (@)
# * NOTE: There is no builtin type that implements the Matrix Multiplication
#   methods. Check _matrix_multiplication.py for more details


###############################################################################
# Casting
###############################################################################


# When some float number is present in expression, the result will become a
# float too
print(3 ** 2 + 5 * 1.)  # 14.0
print(5. + 5)           # 10.0
print(5 + 5.)           # 10.0


###############################################################################
# Identity operators
###############################################################################


# is
x = [1, 2]
y = [1, 2]
print(x is x)      # True
print(x is y)      # False
print(x is not y)  # True


###############################################################################
# Membership operators
###############################################################################


# in
lst = [1, 2, 3, 4, 5]
print(3 in lst)      # True
print(6 in lst)      # False
print(6 not in lst)  # True


###############################################################################
# Logical operators
###############################################################################


# and
if True and True:
    print(True)
# True


# or
if False or True:
    print(True)
# True


# not
if not(False and True):
    print(True)
# True


###############################################################################
# Bitwise operators
# * NOTE: check _bitwise.py
###############################################################################
