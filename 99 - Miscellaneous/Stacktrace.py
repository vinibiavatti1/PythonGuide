"""
Stacktrace

* The stacktrace happens when some error ocurred
* The stacktrace is formed with:
  * Traceback: which is the path that the code traverses through different
    parts of the program - you can ignore it for now, as it is empty in such a
    simple code
  * Location: the name of the file containing the error, line number and module
    name)
    NOTE: the number may be misleading, as Python usually shows the place where
    it first notices the effects of the error, not necessarily the error itself
  * Line content: note: IDLE's editor window doesn't show line numbers, but it
    displays the current cursor location at the bottom-right corner; use it to
    locate the erroneous line in a long source code
  * Error's name: the name of the error and a short explanation.
"""


# Stack with a single expression
# * The error below will be raised and generate the stacktrace with only one
#   call since it is a single expression at module level
x = 1 / 0
"""
Traceback (most recent call last):
  File "c:/.../_stacktrace.py", line 21, in <module>
    x = 1 / 0
        ~~^~~
ZeroDivisionError: division by zero
"""


# Stack with multiple functions
# * The error below will be raised and generate the stacktrace with multiple
#   calls since the error ocurred inside the function that was called by
#   other functions
def c():
    return 1 / 0


def b():
    return c()


def a():
    return b()


a()
"""
Traceback (most recent call last):
  File "c:/.../_stacktrace.py", line 44, in <module>
    a()
  File "c:/.../_stacktrace.py", line 41, in a
    return b()
           ^^^
  File "c:/.../_stacktrace.py", line 37, in b
    return c()
           ^^^
  File "c:/.../_stacktrace.py", line 33, in c
    return 1 / 0
           ~~^~~
ZeroDivisionError: division by zero
"""
