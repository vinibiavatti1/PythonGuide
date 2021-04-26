"""
Walrus operator

* This operator assigns values to variables as part of a larger expression. It
  is affectionately known as |the walrus operator| due to its resemblance to
  the eyes and tusks of a walrus
* It can be used to define and return a value in the same time to some variable
* Can be used inside if, while, etc statements
* Syntax: :=
"""


###############################################################################
# Walrus operator
###############################################################################


# Define and return
# * The definition and the return occurs in the same time
print('1.', text := 'Hello World')
print('2.', text)
# 1. Hello World
# 2. Hello World


# If statement
# * The walrus operator define and return the value of length, used in
#   condition
txt = 'Hello world'
if (size := len(txt)) > 5:
    print('The size of txt is:', size)
# The size of txt is: 11


# While statement
# * It can be used in while loops too
txt = 'Hello world'
idx = 0
while (char := txt[idx]) != ' ':
    print(char, end='')
    idx += 1
print()
# Hello
