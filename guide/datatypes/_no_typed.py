"""
No Typed

* Python is a dynamically-typed language, so, it is no strongly typed
* Don't need to declare variables specifying the type
* Dynamically typed: Python data can change their types in lifecicle
"""


# No typed
x = 8  # int
y = 4  # int
print(type(x / y))
# <class 'float'>


# Dynamically typed
x = 5
y = 5.0
print(x == y)  # Changed the y to float to compare
# True
