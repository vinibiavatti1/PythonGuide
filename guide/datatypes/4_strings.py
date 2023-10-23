"""
Strings

* Python strings are char arrays
* They are immutable, which means that changing the value of a string requires
  creating a new string
* Since everything in Python is an object, strings are actually objects too
  with methods that are used to perform operations on strings
"""


###############################################################################
# Creating a String
###############################################################################


# Creating a single-line String
# * The quotes or double quotes can be used to create a string
# * As convention, the single quotes are preferred
x = 'Hello World'


# Creating a multi-line String
# * To create a multi-line string, triple quotes can be used (''' or """)
# * As convention, the single quotes are preferred
# * Note that the line breaks are included in the string
x = '''First Line
Second Line
Third Line'''
print(x)
# First Line
# Second Line
# Third Line


###############################################################################
# Scape Characters
###############################################################################


# Scape characters
# * Since the single quotes are used to create a string, they can't be used
#   normally as part of the string, otherwise it will be interpreted as the end
#   of the string. For this situation, we can use scape characters
# * The char '\' is used to scape the next character to change the normal
#   behavior of it
# * below there is a list containing common scape characters in Python:
"""
###############################################################################
Scape       Description             Acronym
###############################################################################
\'          Single Quote
\"          Double Quote
\\          Backslash
\n          New Line                LF
\r          Carriage Return         CR
\t          Tabular                 TAB
\b          Backspace               BS
\f          Form Feed (new page)    FF
\123        Octal value
\x12        Hex value
###############################################################################
"""


# Using single quote scape character
# * In the example below, we will use the single quote as part of the string
#   and print the result
x = '\'Hello World\''
print(x)
# 'Hello World'


# Using new line scape character
# * In this case, the \n will break the line and print the next text in a new
#   line
# * NOTE: "\n" is the POSIX style to define a new line, but in Windows, it is
#   necessary to use "\r\n" (Carriage Return + New Line (CRLF))
x = 'Hello\r\nWorld'
print(x)
# Hello
# World


# Using octal value scape character
# * We can use the octal value to print a character by its ASCII code
# * Note that for octal values, we must use the scape character '\' with the
#   number
x = '\110\145\154\154\157'
print(x)
# Hello


# Using hex value scape character
# * The same result as above can be reached using the hex value too
# * Note that for hexadecimal values, we must use the scape character '\x' with
#   the number
x = '\x48\x65\x6c\x6c\x6f'
print(x)
# Hello


###############################################################################
# String Length
###############################################################################


# Obtaining the length of a string
# * To get the length of a string, we can use the len() function
x = 'Hello World'
y = len(x)
print(y)
# 11


###############################################################################
# Iterate through a String
###############################################################################


# Accessing a character in a position
# * To access a single character in a string, we can use the index operator:
#   x[n]
# * The index operator will return the character in the position n
# * A Python loop can be used to access all characters in a string and
#   evaluate it individually
"""
[6]
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   |  ^|   |   |   |   |
"""
x = 'Hello World'
print(x[6])
# W


# Accessing a character in a position (negative index)
# * When using a negative index, the negative index sequence will be used to
#   access the string (from end to start)
# * Take a look at the table below to see the position of the negative numbers
"""
[-5]
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   |  ^|   |   |   |   |
"""
x = 'Hello World'
print(x[-5])
# W


# Iterating through a string (while loop)
# * We can use a loop to iterate through a string and print each character
# * In this example, we will use a while loop, but it can be done with a for
#   that is the recommended way
x = 'Hello World'
i = 0
while i < len(x):
    print(x[i], end='')
    i += 1
print()
# Hello World


# Iterating through a string (for loop)
# * Using a for-each loop is less verbose than the while loop
# * In this way, we don't need to use the index operator to access the string
#   characters, since the for-each loop will do it automatically
x = 'Hello World'
for c in x:
    print(c, end='')
print()
# Hello World


###############################################################################
# String Slicing
###############################################################################


# Obtaining a slice of a string [start:end]
# * We can use the [start:end] syntax to obtain a slice of a string
# * The start index will determine the beginning of the slice, and the end
#   index will determine the end of the slice
# * NOTE: The end index is not included in the slice (exclusive)
"""
[6:11] (equivalent to [6:11:1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   | 1º| 2º| 3º| 4º| 5º|
"""
x = 'Hello World'
print(x[6:11])
# World


# Obtaining a slice of a string [start:end:step]
# * In this case, we will define the step to be used to obtain the slice
# * The step determines the number of characters to be skipped
"""
[6:11:2]
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   | 1º|   | 2º|   | 3º|
"""
x = 'Hello World'
print(x[6:11:2])
# Wrd


# Obtaining a slice of a string [start:]
# * We can omit the end index to get a slice from the start index to the end of
#   the string
# * This way is useful since we don't need to work with the length of the
#   string
"""
[6:] (equivalent to [6:11:1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   | 1º| 2º| 3º| 4º| 5º|
"""
x = 'Hello World'
print(x[6:])
# World


# Obtaining a slice of a string [:end]
# * Like the previous example, we can omit the start index to get a slice from
#   the beginning of the string to the end index
"""
[:5] (equivalent to [0:5:1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
| 1º| 2º| 3º| 4º| 5º|   |   |   |   |   |   |
"""
x = 'Hello World'
print(x[:5])
# Hello


# Obtaining a slice of a string [:] or [::]
# * We can omit both start and end indexes to get a slice from the beginning of
#   the string to the end of the string
# * In this case, since a string is immutable, it will works the same way as
#   declaring a new variable pointing to the same string (it will use the same
#   memory address)
"""
[:] or [::] (equivalent to [0:11:1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
| 1º| 2º| 3º| 4º| 5º| 6º| 7º| 8º| 9º|10º|11º|
"""
x = 'Hello World'
y = x[:]
z = x[::]
print(x, y, z, sep='\n')
# Hello World
# Hello World
# Hello World


# Obtaining a slice of a string [-start:-end]
# * When using negative numbers, the index will follow the opposite direction
#   of the string
# * Look at the table below to see the position of the negative numbers
# * Have in mind that in this example, the step is still positive, so, the
#   slice will be get from the start to the end (left to right)
"""
[-11:-6] (equivalent to [-11:-6:1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
| 1º| 2º| 3º| 4º| 5º|   |   |   |   |   |   |
"""
x = 'Hello World'
print(x[-11:-6])
# Hello


# Obtaining a slice of a string [start:end:-step]
# * When using a negative step, the index will follow the opposite direction of
#   the string (right to left)
"""
[10:5:-1]
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   | 5º| 4º| 3º| 2º| 1º|
"""
x = 'Hello World'
print(x[10:5:-1])
# dlroW


# Obtaining a slice of a string [::-step]
# * On this way, the same string will be returned, but inverted
"""
[::-1] (equivalent to [0:11:-1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|11º|10º| 9º| 8º| 7º| 6º| 5º| 4º| 3º| 2º| 1º|
"""
x = 'Hello World'
print(x[::-1])
# dlroW olleH


# Obtaining a slice of a string (invalid range)
# * When using an invalid range, the result string will be empty
"""
[7:3:] (equivalent to [7:3:1])
|-11|-10|-09|-08|-07|-06|-05|-04|-03|-02|-01|
| 00| 01| 02| 03| 04| 05| 06| 07| 08| 09| 10|
|  H|  e|  l|  l|  o|   |  W|  o|  r|  l|  d|
|   |   |   |   |   |   |   |   |   |   |   |
"""
x = 'Hello World'
print(x[7:3])
# (empty)


###############################################################################
# Concatenating
###############################################################################


# Concatenating strings
# * To concatenate strings, we can use the '+' operator
# * Since strings are immutable, the '+' operator will create a new string
x = 'Hello' + ' ' + 'World'
print(x)
# Hello World


# Concatenating other types
# * When other object type (int, float, etc.) is concatenated with a string,
#   it must be converted to string first
# * If the value is not converted, a TypeError will be raised
x = 'The number is: ' + str(5)
print(x)
# The number is: 5


###############################################################################
# Multiplying Strings
###############################################################################


# Multiplying strings
# * When multiplying a string, the string will be repeated the number of times
#   defined by the number
x = 'Hi!'
y = x * 3
print(y)
# Hi!Hi!Hi!


# Multiplying strings (zero or negative)
# * When using a number less than or equal to zero, the result will be an empty
#   string
x = 'Hi!'
y = x * 0
z = x * -3
print(y, z)
# (empty)


###############################################################################
# String Templates
###############################################################################


# Importing the string module
# * To use string templates, we must import the string module first
import string


# Define a string template
# * The Template class can be used to create string template instances
# * A template has placeholders ($name) that will be replaced by the values
# * To replace the placeholders, we can use the substitute() method
x = string.Template('Best language: $lang')
y = x.substitute(lang='Python')
print(y)
# Best language: Python


###############################################################################
# String Methods
###############################################################################


# upper()
# * Returns the string as uppercase
x = 'HELLO world'
print(x.upper())
# HELLO WORLD


# lower()
# * Returns the string as lowercase
x = 'HELLO world'
print(x.lower())
# hello world


# swapcase()
# * Returns a string where all uppercase characters are converted to lowercase
#   and vice versa
x = 'HELLO world'
print(x.swapcase())
# hello WORLD


# strip(__chars = None)
# * Equivalent to the trim() method in other languages
# * Returns a trimmed version of the string
# * When a char is not specified, the default is to remove whitespaces
x = ' Hello World '
print(x.strip())
# Hello World


# lstrip(__chars = None)
# * Same as strip() method but applied only to the left side
x = '_Hello world_'
print(x.lstrip('_'))
# Hello world_


# rstrip(__chars = None)
# * Same as strip() method but applied only to the right side
x = '_Hello world_'
print(x.rstrip('_'))
# _Hello world


# replace(__old, __new, __count = -1)
# * Replaces the "__old" occurrences with the "__new" content in a string
# * The count parameter defines the number of occurrences to be replaced
x = 'AAA'
y1 = x.replace('A', 'B')
y2 = x.replace('A', 'B', 1)
print(y1, y2, sep='\n')
# BBB
# BAA


# split(__sep = None, maxsplit = -1)
# * Divides the string in chunks separated by the specified separator
# * The maxsplit parameter defines the number of splits to be done
# * The default separator is the whitespace
x = 'Apple, Orange, Pineapple'
y1 = x.split()
y2 = x.split(', ')
y3 = x.split(', ', 1)
print(y1, y2, y3, sep='\n')
# ['Apple,', 'Orange,', 'Pineapple']
# ['Apple', 'Orange', 'Pineapple']
# ['Apple', 'Orange, Pineapple']


# rsplit(__sep = None, maxsplit = -1)
# * Sames as split() method but applied from right to left
x = 'Apple, Orange, Pineapple'
y1 = x.rsplit()
y2 = x.rsplit(', ')
y3 = x.rsplit(', ', 1)
print(y1, y2, y3, sep='\n')
# ['Apple,', 'Orange,', 'Pineapple']
# ['Apple', 'Orange', 'Pineapple']
# ['Apple, Orange', 'Pineapple']


# format(*args, **kwargs) (empty braces)
# * Replace braces "{}" in a string with the given values
# * In this case, the parameters order will determine the order of the values
#   that will be replaced
x = 'The best {} is {}'
y = x.format('language', 'Python')
print(y)
# The best language is Python


# format(*args, **kwargs) (braces with indexes)
# * A index can be given to a brace to determinate the order of the values that
#   will be replaced
x = 'The best {1} is {0}'
y = x.format('Python', 'language')
print(y)
# The best language is Python


# format(*args, **kwargs) (named braces)
# * Names can be given to the braces to replace the values by using keywords
#   arguments
x = 'The best {x1} is {x2}'
y = x.format(x1='language', x2='Python')
print(y)
# The best language is Python


# format_map(map)
# * Works the same way as format() method, but the values are given by a
#   dictionary
x = 'The best {x1} is {x2}'
replaces = {
    "x1": "language",
    "x2": "Python",
}
print(x.format_map(replaces))
# The best language is Python


# capitalize()
# * Converts the first character to upper case
# * Note that the second word has not been converted
x = 'hello world'
print(x.capitalize())
# Hello world


# center(__width, __fillchar = ' ')
# * Centers the string in a specified width using the specified fill character
# * The default fill character is the whitespace
x = 'header'
y = 'body'
z = 'footer'
print(x.center(10, '_'))
print(y.center(10, '_'))
print(z.center(10, '_'))
# __header__
# ___body___
# __footer__


# ljust(__width, __fillchar = ' ')
# * Returns the string left justified in a specified width using the specified
#   fill character
x = 'header'
y = 'body'
z = 'footer'
print(x.ljust(10, '_'))
print(y.ljust(10, '_'))
print(z.ljust(10, '_'))
# header____
# body______
# footer____


# rjust(__width, __fillchar = ' ')
# * Returns the string right justified in a specified width using the specified
#   fill character
x = 'header'
y = 'body'
z = 'footer'
print(x.rjust(10, '_'))
print(y.rjust(10, '_'))
print(z.rjust(10, '_'))
# ____header
# ______body
# ____footer


# count(x, start = None, end = None)
# * Returns the number of times a specified value occurs in a string
# * The start and end parameters can be used to specify a range to count
x = 'Hello world'
y1 = x.count('l')
y2 = x.count('l', 0, 5)
print(y1, y2, sep='\n')
# 3
# 2


# encode(encoding = 'utf-8', errors = 'strict')
# * Returns an encoded version of the string as a bytes object
# * The errors parameter determines how the errors in the string will be
#   evaluated. The default is 'strict' meaning that encoding errors raise a
#   UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
#   'xmlcharrefreplace' as well as any other name registered with
#   codecs.register_error that can handle UnicodeEncodeErrors
x = '字符'
y1 = x.encode()
y2 = x.encode('ascii', 'ignore')
print(y1, y2, sep='\n')
# b'\xe5\xad\x97\xe7\xac\xa6'
# b''


# startswith(__prefix, __start = None, __end = None)
# * Returns true if the string starts with the specified value
# * The "__prefix" parameter can be a tuple of values to be checked
# * The "__start" and "__end" parameters can be used to specify a range to
#   check
x = 'Hello world'
y1 = x.startswith('Hello')
y2 = x.startswith('Hello', 3)
y3 = x.startswith(('Hi', 'Hello'))
print(y1, y2, y3, sep='\n')
# True
# False
# True


# endswith(__suffix, __start = None, __end = None)
# * Returns true if the string ends with the specified value
# * The "__suffix" parameter can be a tuple of values to be checked
# * The "__start" and "__end" parameters can be used to specify a range to
#   check
x = 'Hello world'
y1 = x.endswith('world')
y2 = x.endswith('world', 7)
y3 = x.endswith(('Hi', 'world'))
print(y1, y2, y3, sep='\n')
# True
# False
# True


# expandtabs(tabsize = 8)
# * Return a copy of the string where all tab characters are expanded using
#   spaces
# * This method preserves the tabular formatting of the text
x = 'Col1\tCol2\tCol3\nA\tB\tC'
y = x.expandtabs(10)
print(y)
# Col1      Col2      Col3
# A         B         C


# find(__sub, __start = None, __end = None)
# * Search the string for a specified value and returns the index of where it
#   was found
# * The "__start" and "__end" parameters can be used to specify a range to
#   search
x = 'A B C B A'
y1 = x.find('A')
y2 = x.find('A', 5)
y3 = x.find('C', 1, 2)
y4 = x.find('B C B')
y5 = x.find('D')
print(y1, y2, y3, y4, y5, sep='\n')
# 0
# 8
# -1 (not found)
# 2
# -1 (not found)


# rfind(__sub, __start = None, __end = None)
# * Same as above, but starts the search from the right to the left
x = 'A B C B A'
y1 = x.rfind('A')
y2 = x.rfind('A', 5)
y3 = x.rfind('C', 1, 2)
y4 = x.rfind('B C B')
y5 = x.rfind('D')
print(y1, y2, y3, y4, y5, sep='\n')
# 8
# 8
# -1 (not found)
# 2
# -1 (not found)


# index(__sub, __start = None, __end = None)
# * Searches the string for a specified value and returns the position of where
#   it was found
# * This is similar to find(), but when the string is not found, it will raise
#   an exception
# * The code is commented to avoid the error being raised
"""
x = 'Hello world'
y = x.index('abc')

ValueError: substring not found
"""


# rindex(__sub, __start = None, __end = None)
# * Same as above but from right to left
"""
x = 'Hello world'
y = x.rindex('abc')

ValueError: substring not found
"""


# isalnum()
# * Returns True if all characters in the string are alpha-numeric, False
#   otherwise
x1 = 'abc'.isalnum()
x2 = 'a b c'.isalnum()
print(x1, x2, sep='\n')
# True
# False


# isalpha()
# * Returns True if all characters in the string are in the alphabet, False
#   otherwise
x1 = 'abc'.isalpha()
x2 = 'a b c'.isalpha()
print(x1, x2, sep='\n')
# True
# False


# isdecimal()
# * Returns True if all characters in the string are decimals, False otherwise
x1 = '1'.isdecimal()
x2 = '1.5'.isdecimal()
print(x1, x2, sep='\n')
# True
# False


# isdigit()
# * Returns True if all characters in the string are digits, false otherwise
x1 = '1'.isdecimal()
x2 = '1.5'.isdecimal()
print(x1, x2, sep='\n')
# True
# False


# isidentifier()
# * Returns True if the string is a valid identifier in Python, False otherwise
x1 = 'my_var'.isidentifier()
x2 = 'my-var'.isidentifier()
print(x1, x2, sep='\n')
# True
# False


# islower()
# * Returns True if all characters in the string are in lowercase
x1 = 'hello world'.islower()
x2 = 'Hello World'.islower()
print(x1, x2, sep='\n')
# True
# False


# isupper()
# * Returns True if all characters in the string are in uppercase
x1 = 'HELLO WORLD'.isupper()
x2 = 'Hello World'.isupper()
print(x1, x2, sep='\n')
# True
# False


# isnumeric()
# * Returns True if all characters in the string are numeric, False otherwise
x1 = '1'.isnumeric()
x2 = '1.5'.isnumeric()
print(x1, x2, sep='\n')
# True
# False


# isprintable()
# * Returns True if all characters in the string are printable
x1 = 'Hello World'.isprintable()
x2 = 'Hello\tWorld'.isprintable()
print(x1, x2, sep='\n')
# True
# False


# isspace()
# * Returns True if all characters in the string are whitespaces
x1 = ' '.isspace()
x2 = ''.isspace()
x3 = 'Hi'.isspace()
print(x1, x2, x3, sep='\n')
# True
# False
# False


# istitle()
# * Return True if the string is a title-cased string, False otherwise
x1 = 'Hello World'.istitle()
x2 = 'Hello world'.istitle()
print(x1, x2, sep='\n')
# True
# False


# join(__iterable)
# * Joins the elements of an iterable to the end of the string
x = ('Apple', 'Orange', 'Pineapple')
print(', '.join(x))
# Apple, Orange, Pineapple


# ljust(__width, __fillchar = ' ')
# * Returns a left justified version of the string
# * The default fill character is the whitespace
x = 'Hello'
y1 = x.ljust(10)
y2 = x.ljust(10, '_')
print(y1, y2, sep='\n')
# Hello
# Hello_____


# maketrans(__x) and translate(__table)
# * maketrans() will return a dictionary with the specified characters to be
#   replaced by the translate() method
x = 'Hi'
rules = {
    'H': 'Y',
    'i': 'a',
}
translation_table = x.maketrans(rules)
x_translated = x.translate(translation_table)
print(x_translated, translation_table, sep='\n')
# Ya
# {72: 'Y', 105: 'a'}


# partition(__sep)
# * Partition the string into three parts using the given separator
x = 'Python is good and is the best language'
y = x.partition('is')
print(y)
# ('Python ', 'is', ' good and is the best language')


# rpartition(sep)
# * Same as above, but it will start looking from the right to the left
x = 'Python is good and is the best language'
y = x.rpartition('is')
print(y)
# ('Python is good and ', 'is', ' the best language')


# splitlines(keepends = False)
# * Split the string by line breaks, and returns a list containing each line
# * The keepends parameter determines if the line breaks will be included in
#   the result
x = 'Hello\nWorld'
y1 = x.splitlines()
y2 = x.splitlines(True)
print(y1, y2, sep='\n')
# ['Hello', 'World']
# ['Hello\n', 'World']


# title()
# * Return a version of the string where each word is title-cased
x = 'hello world'
y = x.title()
print(y)
# Hello World


# zfill(__width)
# * Fills the string with a specified number of 0 values at the beginning
x1 = '4'.zfill(2)
x2 = '25'.zfill(2)
print(x1, x2, sep='\n')
# 04
# 25
