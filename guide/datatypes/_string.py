"""
String
"""
# -----------------------------------------------------------------------------
# Intro


# Create string
text = 'Hello world'


# Create multiline string
text = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit. In sem
justo, tincidunt vel faucibus at,
tempus commodo.'''
print(text)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit. In sem
# justo, tincidunt vel faucibus at,
# tempus commodo.


# -----------------------------------------------------------------------------
# Iterate with string


# Strings are lists
text = 'Hello'
print(text[0])
# H


# Iterate through string with foreach
for c in 'Hello World':
    print(c, end="")
    # Hello World
print()


# len()
# Length of string
text = 'Hello'
print(len(text))
# 5


# -----------------------------------------------------------------------------
# Select content
# [start,end,step]


# Contains
# Check if some text is present in string
text = 'Hello World'
print('World' in text)      # True
print('World' not in text)  # False


# Slice range
text = 'Hello World'
print(text[1:8])
# ello Wo


# Slice from start
text = 'Hello World'
print(text[:8])
# Hello Wo


# Slice to end
text = 'Hello World'
print(text[3:])
# lo World


# Slice with negative numbers
# * Used to reverse the index
text = 'Hello World'
print(text[-5:])
# World


# Step Odd
# * Using step to get odd values
text = 'Hello World'
print(text[::2])
# HloWrd


# Step Invert
# * Using step to invert string
text = 'Hello World'
print(text[::-1])
# dlroW olleH


# -----------------------------------------------------------------------------
# Concatenation and multiplying


# Concatenation
# The '+' operator can be used to concat strings
print('Hello ' + 'world')  # Hello world
# print('Hello ' + 1)      # Error


# Multiplying
# The '*' operator can be used to multiply strings
# NOTE: A number less than or equal to zero produces an empty string
print('Hi' * 3)   # HiHiHi
print('Hi' * 0)   # (empty)
print('Hi' * -3)  # (empty)

# -----------------------------------------------------------------------------
# Interpolation


# Interpolation (MODERN STYLE)
name = 'Vini'
age = 26
text = f'{name} is {age} years old'
print(text)
# Vini is 26 years old


# Interpolation with % (OLD STYLE)
name = 'Vini'
age = 26
print('%s is %s years old' % (name, age))
# Vini is 26 years old


# -----------------------------------------------------------------------------
# Scape


# The char '/' is used to scape
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

text = 'The movie \'Back to the future\' is cool'
print(text)
# The movie 'Back to the future' is cool


# Print unicode char
print('\U00000040')
# @
