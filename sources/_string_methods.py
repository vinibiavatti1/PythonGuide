"""
String methods
"""


# upper() and lower()
# * Uppercase and lowercase
text = 'HELLO world'
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world


# swapcase()
# * Swaps cases, lower case becomes upper case and vice versa
t1 = 'SWAP'
t2 = 'swap'
t3 = 'SwAp'
print(t1.swapcase())  # swap
print(t2.swapcase())  # SWAP
print(t3.swapcase())  # sWaP


# strip([chars])
# * Returns a trimmed version of the string
t1 = '  Hello world  '
t2 = 'AAHello worldAA'
print(t1.strip())     # Hello world
print(t2.strip('A'))  # Hello world


# lstrip([chars])
# * Returns a left trim version of the string
t1 = '  Hello world  '
print(t1.lstrip())
# Hello world  (EOF)


# rstrip([chars])
# * Returns a right trim version of the string from right
t1 = '  Hello world  '
print(t1.rstrip())
#   Hello world


# replace(old, new, [count])
# * Replace content of string
t1 = 'Hello world'
t2 = "AAAAAA"
print(t1.replace('Hello', 'Hi'))  # Hi world
print(t2.replace('A', 'B', 3))    # BBBAAA


# split(str, [maxsplit])
# * Returns a list where the text between the specified separator
text = 'Orange, Apple, Pineaple'
print(text.split(', '))     # ['Orange', 'Apple', 'Pineaple']
print(text.split(', ', 1))  # ['Orange', 'Apple, Pineaple']


# rsplit(str, [maxsplit])
# * Returns a list where the text between the specified separator from right
text = 'Orange, Apple, Pineaple'
print(text.rsplit(', '))     # ['Orange', 'Apple', 'Pineaple']
print(text.rsplit(', ', 1))  # ['Orange, Apple', 'Pineaple']


# format(str)
# * Fomart some string with the values
age = 26
text = 'He is {} years old'
print(text.format(age))  # He is 26 years old


# Format in order
name = 'Vini'
age = 26
text = '{1} is {0} years old'
print(text.format(age, name))  # Vini is 26 years old


# Format with named Indexes
name = 'Vini'
age = 26
text = '{name} is {age} years old'
print(text.format(name=name, age=age))  # Vini is 26 years old


# format_map(map)
# * Formats specified values in a string by dict
fmt = {'age': 26}
text = 'Vini is {age} years old'
text.format_map(fmt)  # Vini is 26 years old


# capitalize()
# * Upper the first letter of the string
text = 'vini'
print(text.capitalize())  # Vini


# center()
# * Returns a centered string
title = 'title'
content = 'content'
footer = 'footer'
print(title.center(10))    #   title
print(content.center(10))  #  content
print(footer.center(10))   #   footer


# rjust(width, [fillchar])
# * Returns a right justified version of the string
t1 = 'Hello World'
t2 = 'This is a text'
print(t1.rjust(20))       #          Hello World
print(t2.rjust(20, '.'))  # ......This is a text


# count(str, [start], [end])
# * Returns the number of times a specified value occurs in a string
text = 'Hello world'
print(text.count('l'))        # 3
print(text.count('l', 0, 5))  # 2


# encode([encoding], [errors])
# * Returns an encoded version of the string
text = '字符'
print(text.encode())
print(text.encode('utf-8'))


# startswith(prefix, [start], [end]) and
# * Returns true if the string starts with with the specified value
text = 'Hello world'
print(text.startswith('Hello'))      # True
print(text.startswith('world', 6))   # True
print(text.startswith('wor', 6, 9))  # True


# endswith(prefix, [start], [end])
# * Returns true if the string ends with with the specified value
text = 'Hello world'
print(text.endswith('world'))     # True
print(text.endswith('rld', 8))    # True
print(text.endswith('or', 6, 9))  # True


# expandtabs(tabsize)
# * Sets the tab size of the string
text = 'Hello\tworld'
print(text.expandtabs(10))
# Hello     world


# find(sub, start, end)
# * Searches the string for a specified value and returns the position of where
#   it was found -1 when not found
text = 'Hello world'
print(text.find('world'))        # 6
print(text.find('world', 5))     # 6
print(text.find('world', 1, 3))  # -1


# index(sub, start, end)
# * Searches the string for a specified value and returns the position of where
#   it was found
# * This is similar to find(), but when the string is not found, it will raise
#   an error
text = 'Hello world'
print(text.index('world'))          # 6
print(text.index('world', 5))       # 6
# print(text.index('world', 1, 3))  # ValueError: substring not found


# isalnum()
# * Returns True if all characters in the string are alphanumeric
t1 = 'abc'
t2 = 'a b c'
print(t1.isalnum())  # True
print(t2.isalnum())  # False


# isalpha()
# * Returns True if all characters in the string are in the alphabet
t1 = 'abc'
t2 = '123'
print(t1.isalpha())  # True
print(t2.isalpha())  # False


# isdecimal()
# * Returns True if all characters in the string are decimals
t1 = '3'
t2 = '3.5'
print(t1.isdecimal())  # True
print(t2.isdecimal())  # False


# isdigit()
# * Returns True if all characters in the string are digits
t1 = '123'
t2 = 'abc'
print(t1.isdigit())  # True
print(t2.isdigit())  # False


# isidentifier()
# * Returns True if the string is a valid identifier in Python. If not, it
#   returns False
t1 = 'my_var'
t2 = 'my-var'
print(t1.isidentifier())  # True
print(t2.isidentifier())  # False


# islower()
# * Returns True if all characters in the string are lower case
t1 = 'hello world'
t2 = 'Hello World'
print(t1.islower())  # True
print(t2.islower())  # False


# isupper()
# * Returns True if all characters in the string are lower case
t1 = 'HELLO WORLD'
t2 = 'hello world'
print(t1.isupper())  # True
print(t2.isupper())  # False


# isnumeric()
# * Returns True if all characters in the string are numeric
t1 = '3'
t2 = 'abc'
t3 = '3.5'
print(t1.isnumeric())  # True
print(t2.isnumeric())  # False
print(t3.isnumeric())  # False


# isprintable()
# * Returns True if all characters in the string are printable
t1 = 'hello world'
t2 = 'Hello\tWorld'
print(t1.isprintable())  # True
print(t2.isprintable())  # False


# isspace()
# * Returns True if all characters in the string are whitespaces
t1 = '   '
t2 = ''
t3 = 'abc'
print(t1.isspace())  # True
print(t2.isspace())  # False
print(t3.isspace())  # False


# istitle()
# * Returns True if the string follows the rules of a title
t1 = 'Hello World'
t2 = 'Hello world'
print(t1.istitle())  # True
print(t2.istitle())  # False


# join(iterable)
# * Joins the elements of an iterable to the end of the string
fruits = ('Apple', 'Orange', 'Pineaple')
comma = ', '
print(comma.join(fruits))
# Apple, Orange, Pineaple


# ljust(width, [fillchar])
# * Returns a left justified version of the string
text = 'Hello'
print(text.ljust(10, 'o'))
# Helloooooo


# maketrans(x)
# * Returns a mapping table for translation usable for translate() method
text = 'welcome'
dictionary = {
    'w': 'h',
    'c': 'l',
    'm': 'o'
}
trans = text.maketrans(dictionary)
print(text.translate(trans))  # hellooe
print(trans)                  # {119: 'h', 99: 'l', 109: 'o'}


# partition(sep)
# * Returns a tuple where the string is parted into three parts
text = 'Hello my World'
print(text.partition('my'))  # ('Hello ', 'my', ' World')


# rpartition(sep)
# * Returns a tuple where the string is parted into three parts
text = 'Hello my World my Hello'
print(text.rpartition('my'))  # ('Hello my World ', 'my', ' Hello')

# rfind(sub, [start], [end])
# * Searches the string for a specified value and returns the last position of
#   where it was found
text = 'Mi casa, su casa'
print(text.rfind('casa'))
# 12


# rindex(sub, [start], [end])
# * Searches the string from right for a specified value and returns the last
#   position of where it was found
# * This is similar to rfind(), but when the string is not found, it will raise
#   an error
text = 'Mi casa, su casa'
print(text.rindex('casa'))  # 12
# print(text.rindex('abc')) # ValueError


# splitlines(keepends)
# * Splits the string at line breaks and returns a list
text = 'This is\na big\ntext'
print(text.splitlines())      # ['This is', 'a big', 'text']
print(text.splitlines(True))  # ['This is\n', 'a big\n', 'text']


# title()
# * Converts the first character of each word to upper case
text = 'the da vinci code'
print(text.title())
# The Da Vinci Code


# translate(table)
# * Returns a translated string
# * The method maketrans() can be used to generate a dictionary
text = 'welcome'
dictionary = {
    119: 'h',
    99: 'l',
    109: 'o'
}
print(text.translate(dictionary))
# hellooe


# zfill(width)
# * Fills the string with a specified number of 0 values at the beginning
hour = '3'
minute = '45'
second = '7'
print(hour.zfill(2), minute.zfill(2), second.zfill(2), sep=':')
# 03:45:07
