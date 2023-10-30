"""
Ord and Chr functions

Ord
* Given a string representing one Unicode character, return an integer
  representing the Unicode code point of that character
* Syntax
  * ord(c)

Chr
* Return the string representing a character whose Unicode code point is the
  integer i
* Syntax
  * chr(i)
"""


# String > Integer
char_str = 'A'
print(ord(char_str))
# 65


# Integer > String
char_code = 65
print(chr(char_code))
# A
