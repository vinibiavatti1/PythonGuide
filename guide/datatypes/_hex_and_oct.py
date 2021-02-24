"""
Hex and Oct

Hex (Hexadecimal)
* The number must contain digits taken from the [0..10] and the letters
  A, B, C, D, E and F
* 0xFFF is an hexadecimal number with a (decimal) value equal to 4095
* Syntax
  * 0x<number>
  * 0X<number>

Oct (Octal)
* The number must contain digits taken from the [0..7] range only
* 0o123 is an octal number with a (decimal) value equal to 83
* Syntax
  * 0o<number>
  * 0O<number>
"""


# Hexadecimal
hx = 0x7A3F
print(hx)
# 31295


# Octal
oc = 0o7235
print(oc)
# 3741


# Convert to hexadecimal
hx = hex(31295)
print(hx)
# 0x7a3f


# Convert to octal
oc = oct(3741)
print(oc)
# 0o7235
