"""
Assert

* The assert keyword lets you test if a condition in your code returns True, if
  not, the program will raise an AssertionError
* It can be used to test some module, or to debug the code
* You can specify a message to the assert expression
* NOTE: If the Python program is running with '-O' argument, the assertions
  will be disabled
  * Ex: $ python -O main.py
* Syntax:
  * assert <expression>
  * assert <expression>, <message>
"""


###############################################################################
# Assert
###############################################################################


# Use the assert instruction
# * The assert instruction can be used to validate an expression
lst = [1, 2, 3]
assert len(lst) == 3
assert len(lst) == 999
# AssertionError


# Use the assert instruction with a custom message
# * We can set a custom message to the assert instruction to be used when the
#   assert fails
lst = [1, 2, 3]
assert len(lst) == 3
assert len(lst) == 999, 'Invalid length'
# AssertionError: Invalid length
