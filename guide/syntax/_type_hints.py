"""
Type Hints

* New feature provided by PEP 484
* The PEP 484 aims to provide a standard syntax for type annotations, opening
  up Python code to easier static analysis and refactoring, potential runtime
  type checking, and (perhaps, in some contexts) code generation utilizing type
  information
"""


###############################################################################
# Function arguments
###############################################################################


# Define function specifing the type for parameter and return
# * It is allowed to specify the type annotation for a parameter or return
# * NOTE: The Python runtime does not enforce function and variable type
#   annotations, it is just a hint during the development
# * Syntax: Parameter: (arg: type) / Return: def fn() -> type:
def type_hint(x: int, y: float, z: list[str]) -> bool:
    return True


# Call function with typing
# * We use the same way to call any function, but for this function, if you
#   provide wrong datatype, the IDE can warn about it
result = type_hint(9, 3.5, ['a', 'b', 'c'])
print(result)
# True


###############################################################################
# Type Alias
###############################################################################


# Define type alias
# * The types can be stored into a variable and used as an alias
Vector = list[float]


# Define function using type alias
# * You can use the type alias as type hint
def render(position: Vector):
    ...
