"""
Compile

* The compile() method returns a Python code object from the source (normal
  string, a byte string, or an AST object)
* The object generated can be executed with exec() and eval()
* Parameters
  * source: a normal string, a byte string, or an AST object
  * filename: file from which the code was read. If it wasn't read from a file,
              you can give a name yourself
  * mode: Either exec or eval or single
  * eval: accepts only a single expression
  * exec: It can take a code block that has Python statements, class and
          functions, and so on
  * single: if it consists of a single interactive statement
  * flags (optional) and dont_inherit (optional): controls which future
          statements affect the compilation of the source. Default Value: 0
  * optimize (optional): optimization level of the compiler. Default value:1
* Syntax
  * compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
"""


# Exec
exp = 'result = (2 ** 8) / 64\nprint(result)'
obj = compile(exp, 'source_1', 'exec')
exec(obj)
# 4.0


# Eval
exp = '(2 ** 8) / 64'
obj = compile(exp, 'source_2', 'eval')
result = eval(obj)
print(result)
# 4.0
