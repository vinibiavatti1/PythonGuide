"""
Ord (Ordinal) and Chr (Character)

* The `ord()` and `chr()` functions are used to convert characters to their
  unicode code points and vice versa.
* The `ord()` function returns an integer representing the unicode code point
  of the character.
* The `chr()` function returns an character related to the unicode code point.
* Syntax:
    * ord(char)
    * chr(integer)
* Reference: https://en.wikipedia.org/wiki/List_of_Unicode_characters
"""


###############################################################################
# Ord (Ordinal)
###############################################################################


# Getting the code point (integer) related to a character
# * We can use `ord()` to get the code point (integer) of a character
x = 'A'
y = ord(x)
print(y)
# 65


###############################################################################
# Chr (Character)
###############################################################################


# Getting the character related to a code point (integer)
# * We can use `chr()` to get the character related to a code point (integer)
x = 65
y = chr(x)
print(y)
# A
