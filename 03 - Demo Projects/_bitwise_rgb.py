"""
Bitwise RGB

* Conversor decimal to binary for RGB

RGB Pattern
R        G        B
00000000 00000000 00000000 (binary)
"""


# Decimal to binary
# 214      217      163
# 11010110 11011001 10100011
rgb_decimal = 14080419
r = rgb_decimal >> 16
g = rgb_decimal >> 8 & 255
b = rgb_decimal & 255
print(r, g, b, sep=', ')
# 214, 217, 163


# Binary to decimal
rgb_decimal = (r << 16) | (g << 8) | b
print(rgb_decimal)
# 14080419


# Example:
# Operation to get green value
# 11010110 11011001 10100011 >> 8
# 00000000 11010110 11011001 &  00000000 00000000 11111111 (255)
# 00000000 00000000 11011001
