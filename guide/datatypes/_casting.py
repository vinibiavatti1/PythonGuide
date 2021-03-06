"""
Casting
"""


###############################################################################
# Variables
###############################################################################


# Variables conversion
x = str(3)      # '3'
x = int(3)      # 3
x = float(3)    # 3.0
x = int('1')    # 1
# x = int('a')  # ValueError


# Coercion
# * Cast by interpreter before execute
x = 3.5 + 10  # Equivalent to x = 3.5 + float(10)


###############################################################################
# Collections
###############################################################################


# Tuple to list
tpl = (1, 2, 3)
lst_cast = list(tpl)  # [1, 2, 3]

# Set to tuple
st = {1, 2, 3}
tpl_cast = tuple(st)  # (1, 2, 3)

# List to set
lst = [1, 2, 3]
st_cast = set(lst)    # {1, 2, 3}


###############################################################################
# Int builtin function to cast
###############################################################################


# The int base parameters
# * Base can be from 2 to 36 only
# * On the high end, 36 is chosen arbitrarily because we use symbols from
#   "0123456789abcdefghijklmnopqrstuvwxyz" (10 digits + 26 characters)
# Syntax: int(x, base=10)
i1 = int('9', base=10)
i2 = int('a', base=36)
i3 = int('z', base=36)
print(i1, i2, i3, sep=', ')
# 9, 10, 35
