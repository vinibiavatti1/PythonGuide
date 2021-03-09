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
* The bits used to separete or targe some bit sequence is called as bit mask

###############################################################################
Operator    Example     Description
###############################################################################
&	        a & b	    Bitwise AND
|	        a | b	    Bitwise OR
^	        a ^ b	    Bitwise XOR (exclusive OR)
~	        ~a	        Bitwise NOT
<<	        a << n	    Bitwise left shift
>>	        a >> n	    Bitwise right shift
###############################################################################
"""


###############################################################################
# Bitwise operators
###############################################################################


# AND (& (ampersand))
# 0 0 = 0
# 0 1 = 0
# 1 0 = 0
# 1 1 = 1
x = 156       # 10011100 (156)
y = 52        # 00110100 (52)
print(x & y)  # 00010100 (20)


# OR (| (bar))
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 1
x = 156       # 10011100 (156)
y = 52        # 00110100 (52)
print(x | y)  # 10111100 (188)


# XOR (^ (caret))
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 0
x = 156       # 10011100 (156)
y = 52        # 00110100 (52)
print(x ^ y)  # 10101000 (168)


# NOT (~ (tilde))
# 0 = 1
# 1 = 0
x = 156       # 10011100 (156)
print(~x)     # 01100011 (-157)


# Left shift (<<)
y = 52         # 00110100 (52)
print(y << 1)  # 01101000 (104)
print(y << 2)  # 11010000 (208)


# Right shift (>>)
y = 52         # 00110100 (52)
print(y >> 1)  # 00011010 (26)
print(y >> 2)  # 00001101 (13)


###############################################################################
# Assignment bitwise operators
###############################################################################


# AND (&=)
x = 156
x &= 52
print(x)
# 20


# OR (|=)
x = 156
x |= 52
print(x)
# 188


# XOR (^=)
x = 156
x ^= 52
print(x)
# 168


# Left shift (<<=)
x = 32
x <<= 2
print(x)
# 128


# Right shift (>>=)
x = 128
x >>= 2
print(x)
# 32
