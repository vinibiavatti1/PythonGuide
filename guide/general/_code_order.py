"""
Code Order

* Python interpreter reads the code from the top to bottom, each line from the
  left to right
* NOTE: You cannot define some function or class after the usage of it
* Inside class this rule is not applied
"""


###############################################################################
# Define Function Before Call (OK)
###############################################################################


# Define function before calling
def sum_(x, y):
    return x + y


sum_(2, 3)
# 5


###############################################################################
# Define Function Before Call (ERROR)
###############################################################################


# Call the function before definition
"""
sum_(2, 3)
def sum_(x, y):
    return x + y
# NameError: name 'sum_' is not defined.
"""


###############################################################################
# Inside Class Works Anyway
###############################################################################


# Call the method before method signature
class CodeOrderExample:

    def __init__(self):
        sum_(2, 3)  # Works

    def sum_(x, y):
        return x + y
