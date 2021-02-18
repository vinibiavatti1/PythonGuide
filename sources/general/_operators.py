"""
Operators

Aritmetic operators:
+   Addition	    x + y
-	Subtraction	    x - y
*	Multiplication	x * y
/	Division	    x / y
%	Modulus	        x % y
**	Exponentiation	x ** y
//	Floor division	x // y

Assignment operators:
=	    x = 5	    x = 5
+=	    x += 3	    x = x + 3
-=	    x -= 3	    x = x - 3
*=	    x *= 3	    x = x * 3
/=	    x /= 3	    x = x / 3
%=	    x %= 3	    x = x % 3
//=	    x //= 3	    x = x // 3
**=	    x **= 3	    x = x ** 3
&=	    x &= 3	    x = x & 3
|=	    x |= 3	    x = x | 3
^=	    x ^= 3	    x = x ^ 3
>>=	    x >>= 3	    x = x >> 3
<<=	    x <<= 3	    x = x << 3

Comparison operators:
==	    Equal	                    x == y
!=	    Not equal	                x != y
>	    Greater than	            x > y
<	    Less than	                x < y
>=	    Greater than or equal to	x >= y
<=	    Less than or equal to	    x <= y

Logical operators:
and 	x < 5 and  x < 10       Returns True if both statements are true
or	    x < 5 or x < 4          Returns True if one of the statements is true
not	    not(x < 5 and x < 10)   Reverse the result, returns False if the result
                                is true

Identity operators:
is 	    x is y      Returns True if both variables are the same object
is not	x is not y  Returns True if both variables are not the same object

Membership operators:
in 	    x in y      Returns True if a sequence with the specified value is
                    present in the object
not in	x not in y  Returns True if a sequence with the specified value is not
                    present in the object

Bitwise operators:
& 	AND	                        Sets each bit to 1 if both bits are 1
|	OR	                        Sets each bit to 1 if one of two bits is 1
^	XOR	                        Sets each bit to 1 if only one of two bits is 1
~ 	NOT	                        Inverts all the bits
<<	Zero fill left shift	    Shift left by pushing zeros in from the right
                                and let the leftmost bits fall off
>>	Signed right shift	        Shift right by pushing copies of the leftmost
                                bit in from the left, and let the rightmost
                                bits fall off
"""


# Aritmetic examples
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
print(25 / 5)
# 5.0


# Modulus (%)
print(20 % 7)
# 6


# Exponentiation (**)
print(5 ** 2)
# 25


# Floor division (//)
print(15 // 2)
# 7 (in normal division, it would be 7.5)


# Identity operators
x = [1, 2]
y = [1, 2]
print(x is x)      # True
print(x is y)      # False
print(x is not y)  # True


# Membership operators
lst = [1, 2, 3, 4, 5]
print(3 in lst)      # True
print(6 in lst)      # False
print(6 not in lst)  # True
