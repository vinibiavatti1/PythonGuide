"""
Annotations (Type Hints)

* New feature provided by PEP 484
* The PEP 484 aims to provide a standard syntax for type annotations, opening
  up Python code to easier static analysis and refactoring, potential runtime
  type checking, and (perhaps, in some contexts) code generation utilizing type
  information
"""


###############################################################################
# Function and Variable annotations
###############################################################################


# Define function specifing the type for parameter and return
# * It is allowed to specify the type annotation for a parameter or return
# * NOTE: The Python runtime does not enforce function and variable type
#   annotations, it is just a hint during the development
# * Syntax: Parameter: (arg: type) / Return: def fn() -> type:
def fn(x: int, y: float, z: list[str]) -> bool:
    return True


# Call function with typing
# * We use the same way to call any function, but for this function, if you
#   provide wrong datatype, the IDE can warn about it
result = fn(9, 3.5, ['a', 'b', 'c'])
print(result)
# True


# Check the annotations of a function
# * The annotations of the function are stored in the __annotations__ attribute
print(fn.__annotations__)
# {'x': <class 'int'>, 'y': <class 'float'>, 'z': list[str], 'return':
# <class 'bool'>}


# Define variable with annotation
# * The varaible can be defined specifing a type
ratio: float = 5.7


###############################################################################
# Annotation as commentaries
###############################################################################


# Type comments
# * The type of the data can be defined as commentary too
# * Syntax: # type: (<arg types>) -> <return type>
def calc(x, y, z):
    # type: (int, float, list[str]) -> bool
    return True


# Type comments in variables
# * Variables can has the type defined too
weight = 70.5  # type: float


###############################################################################
# Annotation alias
###############################################################################


# Define annotation alias
# * The types can be stored into a variable and used as an alias
Vector = list[float]


# Define function using type alias
# * You can use the type alias as type hint
def render(position: Vector):
    ...
