"""
Input

* The input() function can be used to get input from the user in the terminal.
* It always return a string data type.
* The `prompt` parameter is optional and represents the message that will be 
  displayed to the user.
* Syntax: input(prompt)
"""


###############################################################################
# Input
###############################################################################


# Input
# * In the example below, the main thread will wait for the user to type a 
#   value. This value will be returned as a string by the `input` function.
x = input()
print(x)
# ...


# Input (with prompt)
x = print('Type a value: ')
print(x)
# ...


# Input (with validation)
# * In the case below, we want only a number as input. To ensure that, we can
#   use the `int` function to convert the input to an integer. If the input is
#   not a number, a ValueError will be raised.
x = input('Type a number: ')
if not x.isdecimal():
    raise ValueError('Invalid input.')
x = int(x)
print(x)