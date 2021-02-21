"""
Bitwise Operators

* Low level operators
* Bitwise operators let you manipulate those individual bits of data at the
  most granular level
* You can use bitwise operators to implement algorithms such as compression,
  encryption, and error detection
* Python has no unsigned right shift operator (>>>), baceuse integers in Python
  works different of other langs. Integeres are unlimited, so, the sign bit
  doesn't have a fixed position

-------------------------------------------------------------------------------
Operator    Example     Description
-------------------------------------------------------------------------------
&	        a & b	    Bitwise AND
|	        a | b	    Bitwise OR
^	        a ^ b	    Bitwise XOR (exclusive OR)
~	        ~a	        Bitwise NOT
<<	        a << n	    Bitwise left shift
>>	        a >> n	    Bitwise right shift
-------------------------------------------------------------------------------
"""


# AND (&)
x = 156       # 10011100 (156)
y = 52        # 00110100 (52)
print(x & y)  # 00010100 (20)


# OR (|)
x = 156       # 10011100 (156)
y = 52        # 00110100 (52)
print(x | y)  # 10111100 (188)


# XOR (^)
x = 156       # 10011100 (156)
y = 52        # 00110100 (52)
print(x ^ y)  # 10101000 (168)


# NOT (~)
x = 156       # 10011100 (156)
print(~x)     # 01100011 (99)


# Left shift (<<)
y = 52         # 00110100 (52)
print(y << 1)  # 01101000 (104)
print(y << 2)  # 11010000 (208)


# Right shift (>>)
y = 52         # 00110100 (52)
print(y >> 1)  # 00011010 (26)
print(y >> 2)  # 00001101 (13)
