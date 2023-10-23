"""
Booleans

* Booleans (bool) is a datatype that stores True or False values only
* The name comes from George Boole (1815-1864), the author of the fundamental
  work, The Laws of Thought, which contains the definition of Boolean algebra
* The bool class is a subclass of the integer (int) class
* Casting some value to bool will perform the "Truth testing procedure", which
  means that the value will be evaluated to True or False depending the bool
  rule
"""


###############################################################################
# Syntax
###############################################################################


# Defining bool variables
# * To define a variable as bool, just assign a (True or False) value to it
# * The bool values always have the first letter capitalized
x = True
y = False
print(x, y)
# True False


###############################################################################
# Casting (Values)
###############################################################################


# Casting values to bool
# * The "truth testing procedure" is the process of evaluating a value to True
#   or False
# * Almost any value is evaluated to True if it has some sort of content
# * Any string is True, except empty strings
# * Any number is True, except 0
# * Any list, tuple, set, and dictionary are True, except empty ones
# * Below are the False values:
bool(False)  # False
bool(None)   # False
bool(0)      # False
bool('')     # False
bool(())     # False
bool([])     # False
bool({})     # False


###############################################################################
# Casting (Class Objects)
###############################################################################


# Defining a class with `__bool__` method
# * For class objects, the bool value will be determined by the __bool__ method
# * If the `__bool__` method is not implemented, then the __len__ method will
#   be used instead
# * In the example below, the `__bool__` method will be implemented
class Unit:

    def __bool__(self):
        return True


# Casting a class object with `__bool__` method to bool
# * The bool value will be determined by the __bool__ method when casting the
#   object
x = Unit()
y = bool(x)
print(y)
# True


# Defining a class with `__len__` method
# * If the `__bool__` method is not implemented, then the __len__ method will
#   be used instead
# * If the `__len__` method returns 0, then the bool value will be False,
#   otherwise the bool value will be True
class Unit:

    def __len__(self):
        return 1


# Casting a class object with `__len__` method to bool
# * Since the `__bool__` method is not implemented, then the __len__ method
#   will be used instead
x = Unit()
y = bool(x)
print(y)
# True


###############################################################################
# Comparing Bool Values
###############################################################################


# Comparing bool values
# * Since bool is a subclass of int, then it can be compared
# * The True value represents 1 and False represents 0
print(True > False, True < False)
# True False
