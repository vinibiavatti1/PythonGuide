"""
Eval

* The `eval()` function in Python is used to evaluate a string as a Python
  expression.
* It can be used to dynamically execute Python code stored in strings.
* To run a code that is not an expression, you can use the `exec()` function.
* `eval()` can be dangerous if used with untrusted input, as it can execute
  arbitrary code.
* Syntax:
  * eval(expression, globals = None, locals = None)
"""


###############################################################################
# Eval Expression
###############################################################################


# Evaluating expression
# * An expression is a piece of code that produces a value.
# * Expressions can be as simple as a single value or variable, or more complex
#   involving operators and function calls.
# * The code below demonstrates evaluating a simple arithmetic expression.
x = '5 + 5'
y = eval(x)
print(y)
# 10


# Evaluating complex expression
# * We can evaluate a more complex expression involving multiple operators and
#   function calls.
x = 'max(5, 10) + min(3, 8)'
y = eval(x)
print(y)
# 13


# Globals
# * The globals parameter allows to specify a dictionary of global variables
#   that will be available to the evaluated expression.
# * Normally, we use the `globals()` function to get the current global context
#   and share it with the `eval()` function.
global_context = {
    'x': 5,
    'y': 5
}
x = 'x + y'
y = eval(x, global_context)
print(y)
# 10


# Locals
# * The locals parameter allows to specify a dictionary of local variables
#   that will be available to the evaluated expression.
# * Normally, we use the `locals()` function to get the current local context
#   and share it with the `eval()` function.
# * The difference between globals and locals is that globals are accessible
#   from anywhere in the code, while locals are only accessible within the
#   current function or block. Inside the evaluation expression, local
#   variables take precedence over global variables.
global_context = {
    'x': 5,
    'y': 5
}
local_context = {
    'x': 10
}
x = 'x + y'
y = eval(x, global_context, local_context)
print(y)
# 15
