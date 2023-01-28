"""
Swap

* Swap is a special syntax of Python which permits to move variable data
  between each other without the need to use a temporary variable for it
* The swap syntax uses the same concept of the unpack syntax
* Syntax: x, y = y, x
"""


###############################################################################
# Swap Variable Values
###############################################################################


# Swap variables value
# * To transfer the value of two variables between each other, we can use the
#   syntax below:
x = 1
y = 2
x, y = y, x  # swap
print(x, y)
# 2 1


# Example without swap
# * The example below shows how to create the same behavior without using swap
# * In this example, we must use a temporary variable to store the value of x
x = 1
y = 2
temp = x
x = y
y = temp
print(x, y)
# 2, 1


# Swap variable value (multiple variables)
# * We can use any number of variables to swap
x = 1
y = 2
z = 3
x, y, z = y, z, x
print(x, y, z)
# 2 3 1
