"""
Exec

* The `exec()` function in Python is used to execute dynamically generated
  Python code.
* It can execute multi-line code and statements, unlike `eval()`, which is
  limited to expressions.
* `exec()` can also be dangerous if used with untrusted input, as it can
  execute arbitrary code.
* Syntax:
  * exec(object, globals = None, locals = None)
"""


###############################################################################
# Exec Code
###############################################################################


# Executing code
# * While eval can only evaluate expressions, exec can execute statements and
#   code blocks.
# * The example below demonstrates the use of `exec()` to set a variable
x = 10
y = 5
z = None
exec('z = x + y')
print(z)
# 15


# Executing complex code
# * The exec can be use to define functions dynamically, or perform any
#   Python code.
# * The example below demonstrates the use of `exec()` to define a function and
#   then call it.
x = '''
def add(a, b):
    return a + b
y = add(5, 3)
'''
y = None
exec(x)
print(y)
# 8


# Globals
# * The globals parameter allows to specify a dictionary of global variables
#   that will be available to the exec code.
# * Normally, we use the `globals()` function to get the current global context
#   and share it with the `exec()` function.
# * NOTE: When a context is defined, the executed code will not reflect changes
#   to the original variables outside the context.
global_context = {
    'x': 5,
    'y': 5,
    'z': 0
}
x = 'z = x + y'
exec(x, global_context)
print(global_context['z'])
# 10


# Locals
# * The locals parameter allows to specify a dictionary of local variables
#   that will be available to the exec code.
# * Normally, we use the `locals()` function to get the current local context
#   and share it with the `exec()` function.
# * The difference between globals and locals is that globals are accessible
#   from anywhere in the code, while locals are only accessible within the
#   current function or block. Inside the evaluation expression, local
#   variables take precedence over global variables.
# * NOTE: When a context is defined, the executed code will not reflect changes
#   to the original variables outside the context.
global_context = {
    'x': 2,
    'y': 2,
    'z': 0
}
local_context = {
    'x': 3,
    'y': 3,
    'z': 0
}
x = 'z = x + y'
z = None
exec(x, global_context, local_context)
print(global_context['z'], local_context['z'])
# 0 6
