"""
RE (Regular Expression) Module

* The `re` module provides support for working with regular expressions
* A Regular Expression (RegEx) is a sequence of characters that defines a
  search pattern, mainly for use in pattern matching with strings
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import re


###############################################################################
# Raw String
###############################################################################


# Using raw string to define a pattern
# * Python provides a raw string notation for defining regular expressions
#   patterns
# * On this way, scape characters are not interpreted
# * Note in the example below that the '\' character is not interpreted
#   as a scape character
x = r'\d+'
print(x)
# \d+


###############################################################################
# String Operations
###############################################################################


# Find all
# * Find all occurrences in a string that match the pattern
# * Syntax: findall(pattern, string)
x = 'The time is: 12:34:56'
y = re.findall(r'\d+', x)
print(y)
# ['12', '34', '56']


# Split
# * Split a string by a regular expression pattern
# * Syntax: split(pattern, string)
x = '1, 2, 3'
y = re.split(r',\s', x)
print(y)
# ['1', '2', '3']


# Sub
# * Replace all occurrences of the pattern in the string
# * The first argument is the pattern, the second is the replacement
# * Syntax: sub(pattern, replacement, string)
x = '1, 2, 3'
y = re.sub(r',\s', ' / ', x)
print(y)
# 1 / 2 / 3


# Subn
# * Same as `sub`, but returns a tuple with the new string and the number of
#   substitutions made
# * Syntax: subn(pattern, replacement, string)
x = '1, 2, 3'
y = re.subn(r',\s', ' / ', x)
print(y)
# ('1 / 2 / 3', 2)


# Escape
# * Escape special characters in a string
# * Syntax: escape(string)
x = 'www.example.com'
y = re.escape(x)
print(y)
# www\.example\.com


# Compile
# * Compile a regular expression pattern into a regular expression object
# * Used to avoid recompiling the same pattern multiple times
# * Syntax: compile(pattern)
x = re.compile(r'\d+')
y1 = x.findall('The time is: 12:34:56')
y2 = x.findall('The price is: $123')
print(y1, y2, sep=' / ')
# ['12', '34', '56'] / ['123']


###############################################################################
# Match Operations
###############################################################################


# Search
# * Scan through a string, looking for any location where the pattern matches
#   the string
# * The method returns a match object if there is a match, otherwise, it
#   returns None
# * Syntax: search(pattern, string)
x = 'The time is: 12:34:56'
y = re.search(r'\d+', x)
print(y)
# <re.Match object; span=(12, 14), match='12'>


# Match
# * Determine if the RE matches at the beginning of the string
# * The method returns a match object if there is a match, otherwise, it
#   returns None
# * Note that the validation must be at the beginning of the string
# * Syntax: match(pattern, string)
x = '123 ABC'
y = re.match(r'\d+', x)
print(y)
# <re.Match object; span=(0, 3), match='123'>


# Full Match
# * Determine if the RE matches the entire string
# * The method returns a match object if there is a match, otherwise, it
#   returns None
# * Syntax: fullmatch(pattern, string)
x = '123 ABC'
y = re.fullmatch(r'\d+', x)
print(y)
# None


# Find Iter
# * Find all occurrences in a string that match the pattern
# * The method returns an iterator with the matches
# * Syntax: finditer(pattern, string)
x = 'The time is: 12:34:56'
y = re.finditer(r'\d+', x)
for i in y:
    print(i)
# <re.Match object; span=(12, 14), match='12'>
# <re.Match object; span=(15, 17), match='34'>
# <re.Match object; span=(18, 20), match='56'>


###############################################################################
# Match Object
###############################################################################


# Expand
# * Return the string obtained by doing backslash substitution with the match
#   found in the string
# * A group is defined by parentheses in the pattern
# * The `\g<n>` notation is used to refer to the n-th group
# * Syntax: expand(template)
x = '123 456'
y = re.search(r'(\d+)\s(\d+)', x)
z = y.expand('Numbers: \g<1>, \g<2>')
print(z)
# Numbers: 123, 456


# Group (or __getitem__)
# * Return the part of the string where there is a match
# * If index is 0, return the entire match
# * Syntax: group(index=0) or x[n]
x = '123 456'
y = re.search(r'(\d+)\s(\d+)', x)
print(y[0], y[1], y[2], sep=' / ')
# 123 456 / 123 / 456


# Groups
# * Return a tuple containing all the subgroups of the match
# * Syntax: groups()
x = '123 456'
y = re.search(r'(\d+)\s(\d+)', x)
z = y.groups()
print(z)
# ('123', '456')


# Group Dict
# * Return a dictionary containing all the named subgroups of the match
# * Named groups are defined by the syntax `(?P<name>...)`
# * Syntax: groupdict()
x = '123 456'
y = re.search(r'(?P<first>\d+)\s(?P<second>\d+)', x)
z = y.groupdict()
print(z)
# {'first': '123', 'second': '456'}


# Start
# * Return the start index of the matched substring
# * Syntax: start()
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.start()
print(z)
# 8


# End
# * Return the end index of the matched substring
# * Syntax: end()
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.end()
print(z)
# 11


# Span
# * Return a tuple containing the start and end indexes of the matched
#   substring
# * Syntax: span()
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.span()
print(z)
# (8, 11)


# Pos
# * Return the start index of the search
# * Syntax: pos
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.pos
print(z)
# 0


# End Pos
# * Return the end index of the search
# * Syntax: endpos
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.endpos
print(z)
# 12


# Last Index
# * Return the index of the last matched capturing group
# * Syntax: lastindex
x = '123 456'
y = re.search(r'(\d+)\s(\d+)', x)
z = y.lastindex
print(z)
# 2


# Last Group
# * Return the name of the last matched capturing group
# * Syntax: lastgroup
x = '123 456'
y = re.search(r'(?P<first>\d+)\s(?P<second>\d+)', x)
z = y.lastgroup
print(z)
# second


# Re
# * Return the regular expression object
# * Syntax: re
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.re
print(z)
# re.compile('\\d+')


# String
# * Return the string passed to the search method
# * Syntax: string
x = 'Number: 123'
y = re.search(r'\d+', x)
z = y.string
print(z)
# Number: 123
