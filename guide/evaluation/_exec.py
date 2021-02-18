"""
Exec function

* This function supports dynamic execution of Python code
* The code argument is parsed and evaluated as a Python expression using the
  globals and locals dictionaries as global and local namespace
* The arguments are a string and optional globals and locals. If provided,
  globals must be a dictionary. If provided, locals can be any mapping object
* Syntax
  * exec(expression[, globals[, locals]])
"""


# Exec expression
# * Same of exec(expression, globals(), locals())
x = 10
y = 5
result = None
exp = 'result = (x * y + (x - y)) / 2'
exec(exp)
print(result)
# 27.5


# Eval expression with globals
global_context = {'y': 10}
exec('y = y * 3', global_context)
print(global_context['y'])
# 30


# Eval expression with globals and locals
global_context = {'y': 13}
local_context = {'z': 7}
exec('x = y + z', global_context, local_context)
print(local_context['x'])
# 20
