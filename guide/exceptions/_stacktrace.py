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
  * Line content: note: IDLE’s editor window doesn’t show line numbers, but it
    displays the current cursor location at the bottom-right corner; use it to
    locate the erroneous line in a long source code
  * Error's name: the name of the error and a short explanation.
"""


# Run the code to raise an error
x = 1 / 0
# Traceback (most recent call last):
#   File "c:\git\PythonGuide\guide\exceptions\_stacktrace.py", line 21, in
#   <module>
#     1 / 0
# ZeroDivisionError: division by zero


# Stack with function chain
def c():
    return 1 / 0


def b():
    return c()


def a():
    return b()


a()
# Traceback (most recent call last):
#   File "c:\git\PythonGuide\guide\exceptions\_stacktrace.py", line 42, in
#   <module>
#     a()
#   File "c:\git\PythonGuide\guide\exceptions\_stacktrace.py", line 39, in a
#     return b()
#   File "c:\git\PythonGuide\guide\exceptions\_stacktrace.py", line 35, in b
#     return c()
#   File "c:\git\PythonGuide\guide\exceptions\_stacktrace.py", line 31, in c
#     return 1 / 0
# ZeroDivisionError: division by zero
