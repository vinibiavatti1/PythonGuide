"""
Eval function

* Evaluates some Python expression and return the new context value
* The expression argument is parsed and evaluated as a Python expression using
  the globals and locals dictionaries as global and local namespace
* The arguments are a string and optional globals and locals. If provided,
  globals must be a dictionary. If provided, locals can be any mapping object
* Syntax
  * eval(expression[, globals[, locals]])
"""


# Eval expression
# * Same of eval(expression, globals(), locals())
x = 10
y = 5
exp = '(x * y + (x - y)) / 2'
result = eval(exp)
print(result)
# 27.5


# Eval expression with globals
global_context = {'y': 10}
y = eval('y + 5', global_context)
print(y)
# 15


# Eval expression with globals and locals
global_context = {'y': 13}
local_context = {'z': 7}
result = eval('y + z', global_context, local_context)
print(result)
# 20
