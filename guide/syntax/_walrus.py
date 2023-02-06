"""
Walrus Operator

* The walrus operator ":=" is used to assign variables in a expression that
  will be evaluated.
* It permits to assign variables in the if condition, while condition, in
  arguments, etc.
* Syntax:
  * <variable> := <value>
"""


###############################################################################
# Walrus in Arguments
###############################################################################


# Use the walrus operator in a argument
# * The walrus operator allows us to set a variable while this variable is used
#   in expression that is being evaluated
# * In arguments for example, the walrus will set the value to a variable and
#   this value will be used as the argument
# * In this example, the second variable will be set using the walrus operator,
#   and the value of this variable will be set and sent as an argument at the
#   same time
print('1.', text := 'Hello World')
print('2.', text)
# 1. Hello World
# 2. Hello World


###############################################################################
# Walrus in Conditions
###############################################################################


# Use the walrus operator in a "if" condition
# * Like in arguments, the walrus operator can be used inside expressions
# * In this example, the variable will be declared and used to evaluate the
#   condition at the same time, and the variable will be allowed to be used
#   inside the "if" block
collection = [1, 2, 3]
if (size := len(collection)) > 0:
    print(f'The collection has {size} elements')
# The collection has 3 elements


# Use the walrus operator in a "while" condition
# * Like the example above, the "walrus" operator can be used in a "while" loop
#   too
# * In this case, the variable will be updated for each iteration, and will be
#   used to evaluate the condition
sentence = 'Hello World.'
index = 0
while (char := sentence[index]) != '.':
    print(char, end='')
    index += 1
print()
# Hello World


###############################################################################
# Example
###############################################################################


# Use the walrus operator to read a file content
# * An good example of the usage of the walrus is for reading non-deterministic
#   contents
# * The example below simulates a file stream. Each line of the file will be
#   read inside the loop. The "walrus" will declare the "line" variable with
#   the file content, and evaluate the expression to check if the line is not
#   empty
from io import StringIO
file_content = StringIO('This is\na walrus\nexample')
while (line := file_content.read()) != '':
    print(line)
# This is
# a walrus
# example
