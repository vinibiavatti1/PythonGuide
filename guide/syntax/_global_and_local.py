"""
Global and Local (Context)

global and nonlocal
* Used to manipulate a global or local variable inside a scoped block

globals() and locals()
* Used to return the global and local accessible variables as a dict in current
  scope
* Syntax
  * globals()
  * locals()
"""


# Use global variable inside a function
x = 1  # Global


def func1():
    global x
    x = 2


func1()
print(x)
# 2


# Dont use global Variables inside a function
x = 1  # Global


def func2():
    x = 2  # Local variable
    print(x)


func2()
# 1


# Using outside variables inside two or more functions
def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2

    inner()
    print(x)


outer()
# 2


# Get global context
print(globals())
# {'__name__': '__main__', '__doc__': ... }


# Get local context
def local():
    z = 1
    print(locals())


local()
# {'z': 1}
