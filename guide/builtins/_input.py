"""
Input

* The input() function allows user input
* The input() always return a string type
* NOTE: VS CODE does not allow to interact with OUTPUT, use TERMINAL instead

Syntax: input(prompt)
"""


# Define a variable with input value
x = input('Type the value:')
print(x)


# Input without text
print('Type the value:')
x = input()
print(x)


# Input cast
x = int(input('Type the value'))
print(x * 2)
