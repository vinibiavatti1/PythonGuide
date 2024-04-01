"""
RE module

* RE module is a module to work with regular expressions
* A Regular Expression (RegEx) is a sequence of characters that defines a
  search pattern
* NOTE: The raw string is recommended to be used to define regex expressions
"""
import re


###############################################################################
# Regular expressions
###############################################################################


# Raw string (Scape chars not work)
pattern = r'\$\s[0-9,]+'
print(pattern)
# \$\s[0-9,]+


# Find all
# * Find all occurrences
text = 'At 7:50:41 pm happened something'
pattern = r'\d+'
result = re.findall(pattern, text)
print(result)
# ['7', '50', '41']


# Split
# * Sprit string by regex pattern
text = 'dog 1 cat 2 bird'
pattern = r'\d+'
result = re.split(pattern, text)
print(result)
# ['dog ', ' cat ', ' bird']


# Sub
# * Replace matches with some content
text = 'dog 1 cat 2 bird'
pattern = r'\d+'
result = re.sub(pattern, ',', text)
print(result)
# dog , cat , bird


# Subn
# * Similar to Sub
# * Returns a tuple of 2 items containing the new string and the number of
#   substitutions made
text = 'dog 1 cat 2 bird'
pattern = r'\d+'
result = re.subn(pattern, ',', text)
print(result)
# ('dog , cat , bird', 2)


# Search
# * The method looks for the first location where the RegEx pattern produces a
#   match with the string
# * If the search is successful, re.search() returns a match object, if not, it
#   returns None
text = 'The price is $ 123,45 and the tax is $ 1,23'
pattern = r'\$\s[0-9,]+'
match = re.search(pattern, text)
print(True if match else False)
# True


###############################################################################
# Match
# * RE object that is returned from search method
###############################################################################


# Group and Groups
# * Returns the part of the string where there is a match
# * Use parentheses to make the groups
text = 'The price is $12 !'
pattern = r'(\$)(\d{2})'
match = re.search(pattern, text)
print(match.group(1))  # $
print(match.group(2))  # 12
print(match.groups())  # ('$', '12')


# Start, end and span
# * start() returns the start index of the matched substring
# * end() returns the end index of the matched substring
# * span() return a tuple with start and end indexes
text = 'The price is $12 !'
pattern = r'(\$)(\d{2})'
match = re.search(pattern, text)
print(match.start())  # 13
print(match.end())    # 16
print(match.span())   # (13, 16)


# Re and string
# * re returns the pattern
# * string returns the text
text = 'The price is $12 !'
pattern = r'(\$)(\d{2})'
match = re.search(pattern, text)
print(match.re)      # re.compile('(\\$)(\\d{2})')
print(match.string)  # The price is $12 !
