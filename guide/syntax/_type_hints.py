"""
Type Hints (aka Annotations)

* The Type Hints are described by PEP 484
* They are used to annotate Python resources to specify the datatype
* Python is not a strongly typed language, but the Type Hints provide a way to
  it
* Type checkers can be used as a linter to identify consistences to notify the
  developer to improve the quality of the source code
* For more details, take a look at: _typing.py file
* Syntax:
  * x: <type>
  * def x(argument: <type>) -> <return_type>:
"""


###############################################################################
# Variable Type Hints
###############################################################################


# Annotate numeric variables with a type hint
# * Any variable can have a type hint associated to its declaration
# * Type hints doesn't change the code logic, it is used only for the quality
#   of the code
# * This example shows how to annotate numeric variables with type hints
x: int = 5
x: float = 2.5
x: complex = 2j


# Annotate a text variable with a type hint
# * This example shows how to annotate string variables
x: str = 'Hello World'


# Annotate a range variable with a type hint
# * This example shows how to annotate a range variable
x: range = range(5, 10, 2)


# Annotate a tuple variable with a type hint
# * This example shows how to annotate a tuple
# * For sequences (collections), the annotation can have specific types
#   defined for the content that the collection stores
# * The brackets "[]" are used to set the type of the content of the collection
# * For tuples, each position type of the content must be defined
# * Syntax: <type>[<first_type>, <second_type>, ...]
x: tuple[int, str, bool] = (1, 'Hi', True)


# Annotate list, set and frozenset variables with a type hint
# * For lists, sets, frozensets and dictionaries, only one type is defined for
#   all the data inside the collection
# * Syntax: <type>[<content_type>]
x: list[int] = [1, 2, 3]
x: set[int] = {1, 2, 3}
x: frozenset[int] = frozenset({1, 2, 3})


# Annotate a dictionary variable with a type hint
# * For dicts, the key datatype and the content datatype are specified inside
#   the brackets
# * Syntax: <type>[<key_type>, <content_type>]
x: dict[str, int] = {'Level': 5}


# Annotate boolean variables with a type hint
# * This example shows how to annotate boolean variables
x: bool = False


# Annotate binary variables with a type hint
# * This example shows how to annotate binary variables
x: bytes = b'Hello World'
x: bytearray = bytearray(b'Hello World')
x: memoryview = memoryview(bytearray(b'Hello World'))


###############################################################################
# Special Types Hints
###############################################################################


# Import special type hints
# * The module "typing" has all the special type hints we can use for special
#   cases
# * We must import the special datatypes to be available for usage
# * This page shows only some cases using the special types. Take a loot at:
#   "_typings.py" file for more details and examples
from typing import Any, Final, ClassVar


# Declare a variable with multiple type hints
# * Using the pipe char "|" (OR), we can specify multiple type hints for a
#   variable
# * In this case, the variable will accept all datatypes specified as the type
#   hints
x: int | str | bool = 'Hello World'


# Declare an optional variable
# * An optional variable is a variable that accepts the "None" value as
#   content i.e. the variable can be set with the value, or with the None
# * We can use the pipe char "|" for this
# * Other way to set a variable as optional is by importing the Optional
#   special type from the "typing" module
x: int | None = None


# Declare a variable that accepts any datatype
# * To specify a variable of any type, we can use the "Any" special type from
#   "typing" module
# * This type of variable accepts any datatype
x: Any = True


# Declare a variable as a constant with a type hint
# * Python does not have a special keyword for constants. It can be only
#   specified using a type hint
# * The "typing" module has some features that can be used to define special
#   cases
# * For this case, we can use the "Final" type from the "typing" module
X: Final[int] = 5


# Declare a class variable with a type hint
# * For variables inside a class, we can use the "ClassVar" annotation from
#   the "typing" module
# * The "ClassVar" sets that the specified variable is from the class scope,
#   not from the instance
class MyClass:
    x: ClassVar[int] = 5


# Declare a class variable as constant with a type hint
# * This example shows how to specify a class variable as a constant
# * Note that we didn't use the "ClassVar" keyword for this case
class MyClass:
    x: Final[int] = 5


###############################################################################
# Function Annotations
###############################################################################


# Declare a function with parameter types
# * The parameters of a function can have type hints
# * Each parameter should be annotated like the variables above
def function(x: str, y: int):
    pass


# Declare a function with an optional parameter type
# * Optional parameters can also have type hints
# * In this example, the bool optional parameter is defined with the value set
#   after the type hint
def function(x: bool = True):
    pass


# Declare a function with type hint for arbitrary arguments
# * The example below shows how to annotate arbitrary parameters
# * Since the type is already a collection, the collection type doesn't need to
#   be set, only the content type
def function(*args: int):
    pass


# Declare a function with type hint for arbitrary keyword arguments
# * The example below shows hot to annotate a arbitrary keyword argument
# * In this case, we don't need to specify that the type is a dictionary, only
#   the content of the values of the dictionary
def function(**kwargs: Any):
    pass


# Declare a function with the return type
# * To specify a return datatype of a function, an arrow "->" has to be
#   provided after the function signature
# * After the arrow, the datatype must be set
# * In the example below, the function should return a string type
def function() -> str:
    pass


# Declare a function without return datatype
# * To declare a "void" function (a function that doesn't return data), we can
#   set the None type after the return arrow
# * The example below shows a function that doesn't return any datatype
def function() -> None:
    pass


###############################################################################
# Get Annotations
###############################################################################


# Define a Python resource with type hints
# * The type hints set to a Python resource are stored into the
#   "__annotations__" variable
# * In here, we will declare a function with type hints to be used in the next
#   example
def function(x: str, y: list[int]) -> float | None:
    pass


# Get the annotations of a Python resource
# * To get the annotations of a python resource, we can access them by the
#   "__annotations__" variable
# * The "__annotations__" variable is a dictionary containing a map of all the
#   data of the resource associated to its type hint
print(function.__annotations__)
# {'x': <class 'str'>, 'y': list[int], 'return': float | None}


###############################################################################
# Type Hint Alias
###############################################################################


# Declare a type hint alias
# * We can declare our own type hint alias with a reference to another type
#   hint
# * This can be used to create new specific types
# * In the example below, we created the "Vector3D" type that references to the
#   tuple[float, float, float] type hint
Vector3D = tuple[float, float, float]


# Annotate a resource with the type hint alias
# * Any Python resource can be annotated with the alias
# * In the example below, the type of the "vector" variable is the same of:
#   tuple[float, float, float]
def render(vector: Vector3D) -> None:
    pass
