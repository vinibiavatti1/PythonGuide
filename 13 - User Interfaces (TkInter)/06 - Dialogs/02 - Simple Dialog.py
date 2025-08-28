"""
Simple Dialog

* The tkinter.simpledialog module provides a way to create simple dialog boxes
  for user input.
* It includes functions to prompt the user for a string, integer, or float.
* The dialogs are modal, meaning they block input to other windows until
  closed.
* The user can cancel the dialog, which will return None.
* If the user input is invalid (e.g., not a number for integer/float dialogs),
  an error message will be shown.
* The dialogs can be customized with additional options, such as default values
  and validation functions.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
from tkinter import simpledialog


###############################################################################
# Inputs
###############################################################################


# String Input
# * The `askstring` function is used to prompt the user for a string input.
# * If the user cancels the dialog, it returns None.
x = simpledialog.askstring('Dialog', 'What is your name?')
print(x)
# John Doe


# Integer Input
# * The `askinteger` function is used to prompt the user for an integer input.
# * If the user cancels the dialog, it returns None.
x = simpledialog.askinteger('Dialog', 'What is your age?')
print(x)
# 30


# Float Input
# * The `askfloat` function is used to prompt the user for a float input.
# * If the user cancels the dialog, it returns None.
x = simpledialog.askfloat('Dialog', 'What is your height?')
print(x)
# 5.9


###############################################################################
# Initial Value
###############################################################################


# Initial Value
# * The initial value can be set using the `initialvalue` parameter.
x = simpledialog.askstring(
    'Dialog', 'What is your name?', initialvalue='John Doe'
)
print(x)
# John Doe
