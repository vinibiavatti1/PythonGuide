"""
Assert

* The assert keyword lets you test if a condition in your code returns True, if
  not, the program will raise an AssertionError
* It can be used to test some module, or to debug the code
* You can specify a message to the assert expression
* NOTE: If the Python program is running with '-O' argument, the assertions
  will be ignored!
* Syntax:
  * assert <expression>
  * assert <expression>, <message>
"""


# Assert expression
lst = [1, 2, 3]
assert len(lst) == 3
assert len(lst) == 999  # AssertionError


# Assert expression with message
lst = [1, 2, 3]
assert len(lst) == 3
assert len(lst) == 999, 'Invalid length'  # AssertionError: Invalid length
