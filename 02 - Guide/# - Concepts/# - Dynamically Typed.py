"""
Dynamically Typed

* Python is a dynamically-typed language, which means that the type of the
  variable is inferred at runtime
* The variable type is determined by the value assigned to it
* Python can change variable types at runtime
"""


###############################################################################
# Dynamically Typed
###############################################################################


# Changing a variable type at runtime
# * The same variable will be changed to different types at runtime
x = 8       # int
x = x / 2   # float
x = x // 2  # int
x = x == 2  # bool
print(x)
# True
