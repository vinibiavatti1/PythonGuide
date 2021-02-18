"""
Print

* Prints the given object to the standard output device (screen) or to the text
  stream file
* Syntax
  * print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""


# Print
print('Hello World')
# Hello World


# Print *args
print('A', 'B', 'C')
# A B C


# Print with separator
print(1, '2', sep=',')
# 1,2


# Print with end parameter
print('Same', end=" ")
print('line')
# Same line
