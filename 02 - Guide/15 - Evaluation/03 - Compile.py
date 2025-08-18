"""
Compile

* The compile() function is used to compile source code into a code object.
* Different from `eval()` and `exec()`, which evaluate expressions and execute
  code blocks respectively, `compile()` is specifically designed for the
  compilation of source code into a code object that can be executed later.

* The table below describes all parameters of the compile() function:
###############################################################################
Parameter    Description
###############################################################################
source       The source code to compile (string, bytes, or AST object)
filename     The filename from which the code was read (string)
mode         The mode in which to compile the code (exec, eval, or single)
flags        Controls which future statements affect the compilation
dont_inherit Future statements from the module will not be inherited
optimize     Optimization level of the compiler
###############################################################################

* The list below shows the possible modes for the compile() function:
  * exec: for executing a block of code
  * eval: for evaluating a single expression
  * single: for a single interactive statement (like when using Python REPL)

* Syntax:
  * compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
"""


###############################################################################
# Compile Code
###############################################################################


# Compiling an expression
# * Like `eval()`, we can use `compile()` to compile a single expression.
# * In this case, the `compile()` function will return a code object that can
#   be executed later, instead of immediately.
# * The `filename` is mandatory. This is useful for error messages and
#   debugging.
x = '5 + 5'
y = compile(x, 'compile.py', 'eval')
z = eval(y)
print(z)
# 10


# Compiling a code block
# * Similar to `exec()`, we can use `compile()` to compile a block of code.
# * The example below demonstrates the use of `compile()` to define a function
#   and then call it.
# * Different from `exec()`, the `compile()` function returns a code object
#   that can be executed later.
x = '''
def add(a, b):
    return a + b
z = add(5, 10)
'''
z = None
y = compile(x, 'compile.py', 'exec')
exec(y)
print(z)
# 15
