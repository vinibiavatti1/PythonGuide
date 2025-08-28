"""
Code Order

* Python interpreter reads the code from the top to bottom, each line from
  left to right
* NOTE: You have to declare the function, class, variable, etc... before the
  usage of it in a Python module (Inside the class this rule is not applied)
"""


###############################################################################
# Define Function Before Calling (OK)
###############################################################################


# Define function before calling it
# * In this example, the function is defined before the call
def add(x, y):
    return x + y


# Call the function after definition
# * Now, the function will be called after the definition
add(2, 3)
# 5


###############################################################################
# Define Function After Calling (ERROR)
###############################################################################


# Call the function before definition
# * In the example below, the function will be called before the definition,
#   and an error will be raised
# * NOTE: The example is commented to prevent runtime errors
"""
add(2, 3)


def add(x, y):
    return x + y


# NameError: name 'add' is not defined.
"""


###############################################################################
# Define Method After Calling (OK)
###############################################################################


# Call the method before method signature
# * Since the class will be always processed and stored in memory, all the
#   methods will be already defined before the calls. In this case, the order
#   will not matter
class CodeOrderExample:

    def __init__(self):
        add(2, 3)  # Works

    def add(x, y):
        return x + y
