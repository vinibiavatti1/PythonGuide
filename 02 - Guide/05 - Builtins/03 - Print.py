"""
Print

* Prints the given object to the standard output device (screen) or to the text
  stream file.
* Syntax: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""


###############################################################################
# Print
###############################################################################


# Print
# * Below we can find a simple example of how to print a string into the 
#   terminal
print('Hello World')
# Hello World


# Print (with multiple arguments)
# * If multiple arguments are given, they will be printed separated with a 
#   space by default
print('Hello', 'World')
# Hello World


# Print (with a custom separator)
# * A custom separator can be defined using the `sep` parameter. In this case,
#   when multiple arguments are given, they will be printed separated with the
#   defined separator.
print('A', 'B', 'C', sep=', ')
# A, B, C


# Print (with a custom end character)
# * The `end` parameter defines the character that will be printed at the end 
#   of the line. By default, it is a newline character ('\n').
print('Hello', 'World', end='!\n')
# Hello World!


# Print (with a custom output location)
# * The `file` parameter defines the output stream where the message will be
#   printed. By default, it is the standard output stream (sys.stdout).
# * In the example below, we used a StringIO object to store the output message
#   simulating a in-memory file.
from io import StringIO
output = StringIO()
print('Hello World', file=output)
print(output.getvalue())
# Hello World


# Print (with flush set to True)
# * The `flush` parameter defines if the output stream will be flushed after
#   the message is printed. By default, it is False.
# * By default, the output stream is flushed only when a newline character is 
#   found. If the `flush` parameter is set as True, the output stream will be
#   flushed after the message is printed (regardless of whether the character 
#   is a newline or not).
#   In the example below, the `end` parameter is set as an empty string, so the
#   end character will not represent a new line.
output = StringIO()
print('Hello World', end='', file=output, flush=True)
print(output.getvalue())
# Hello World