"""
Typing Module

* The `typing` module provides runtime support for type hints as specified by
  PEP 484, PEP 526, PEP 544, PEP 586, PEP 589, and PEP 591
* The most fundamental support consists of the types Any, Union, Tuple,
  Callable, TypeVar, and Generic
* The native types `int`, `str`, `float`, `complex`, `bool`, `range`, `bytes`,
  `bytearray`, and `memoryview` can be used as type hints without importing the
  `typing` module
"""


###############################################################################
# Custom Type
###############################################################################


# Type Var
# * The TypeVar type is used to create a custom type variable
# * A new type can have multiple types (union type)
# * Syntax: TypeVar('TypeVarName', Type1, Type2, ...)
from typing import TypeVar
T = TypeVar('T', int, str)
x: T = 5
y: T = 'Hello'


# Type Alias
# * The TypeAlias type is used to create an alias for any type
# * Note that in the example below, we set the new type with other type, not
#   a value
# * On this case, `Vector` is a shorthand for `tuple[float, float, float]`
from typing import TypeAlias
Vector: TypeAlias = tuple[float, float, float]
x: Vector = [1.0, 2.0, 3.0]
print(x)
# [1.0, 2.0, 3.0]


# New Type
# * The NewType type is used to create a distinct type with a distinct name
# * It is used to create a new type that is a subclass of the original type
# * Syntax: NewType('NewTypeName', OriginalType)
from typing import NewType
Id = NewType('Id', int)
x: Id = Id(123)
y: int = 123
print(type(x), type(y))
# <class 'int'> <class 'int'>


###############################################################################
# Special Types
###############################################################################


# Any
# * The Any type is used to specify that the variable can be any type of value
#   (int, str, float, etc.)
from typing import Any
x: Any = 'Hello World'
y: Any = 3.14


# AnyStr
# * The AnyStr type is used to specify that the variable can be a string or a
#   bytes object
from typing import AnyStr
x: AnyStr = 'Hello World'
y: AnyStr = b'Hello World'


# Text
# * The Text type is an alias for str, used to provide a forward-compatible
#   path for Python 2 code
from typing import Text
x: Text = 'Hello World'


# Literal String
# * The Literal String type is used to define a variable that can only have a
#   literal value. In other words, the variable can only have a value which
#   is not variable
# * It can be used for database queries to avoid SQL injection
# * In the example below, if we want to concatenate the `x` variable with
#   a variable value, it will raise a type error, since the variable should
#   be literal, and not variable
from typing import LiteralString
x: LiteralString = 'Hello World'


# Never or NoReturn
# * The Never type is used to specify that the function never returns, i.e.
#   it either raises an exception or stays in a loop forever
# * Note that when using None, the function can return None, but it still
#   returns
# * NoReturn is a synonym for Never. The Never type is preferred.
from typing import Never
def loop() -> Never:
    while True:
        pass


# Self
# * The Self type is used to specify the type of the class itself
# * For example, if we want to specify that a method returns an instance of
#   the class it belongs to, we can use the Self type
from typing import Self
class CustomClass:
    def get_instance(self) -> Self:
        return self


# Union or '|'
# * The Union type is used to specify that the variable can be of any of the
#   specified types
# * It is used to indicate that a variable can have multiple types
# * The `|` operator can be used as a shorthand for Union (preferred)
from typing import Union
x: Union[int, str] = 1
y: int | str = 1


# Optional or '| None'
# * The Optional type is used to specify that the variable can be of the
#   specified type or None
# * It is used to indicate that a variable is optional
# * The `|` operator can be used as a shorthand for Union (preferred)
from typing import Optional
x: Optional[int] = None
y: int | None = None


# Literal
# * The Literal type is used to indicate that the variable has a value
#   equivalent to the provided literal
# * It is used to restrict the possible values of a variable
# * In the example below, the `x` variable can only have the values 'a' or 'b'
from typing import Literal
x: Literal['a', 'b'] = 'a'


# Class Variable
# * The ClassVar type is used to mark class variables
# * A class variable is a variable that is shared by all instances of a class
from typing import ClassVar
class CustomClass:
    x: ClassVar[int] = 5


# Final
# * The Final type is used to indicate to type checkers that a name cannot be
#   re-assigned or overridden
# * It is used to declare constants
# * The variable below cannot be changed anymore
from typing import Final
X: Final[int] = 123


###############################################################################
# Casting Type
###############################################################################


# Castint type
# * The `cast` function can be used to cast a variable to a specific type, so
#   that the type checker understands that the variable is of that type
from typing import cast
x = '5'
y = cast(int, x)
print(y)
# 5


###############################################################################
# Typed Dictionary
###############################################################################


# Typed Dictionary
# * The TypeDict type is used to specify the type of the keys and values of a
#   dictionary
# * We can create a class that extends TypedDict. The attributes of the class
#   are the keys of the dictionary
from typing import TypedDict
class CustomDict(TypedDict):
    name: str
    value: int


# Required
# * The Required type is used to indicate that a TypedDict key is required
from typing import Required
class CustomDict(TypedDict):
    name: Required[str]
    value: int


# Not Required
# * The NotRequired type is used to indicate that a TypedDict key is not
#   required
from typing import NotRequired
class CustomDict(TypedDict):
    name: Required[str]
    value: NotRequired[int]


# Creating an instance of a TypedDict
# * We can create an instance of a TypedDict by passing the keys and values
#   as arguments
x: CustomDict = dict(name='John', value=5)
y: CustomDict = {'name': 'John', 'value': 5}


###############################################################################
# Named Tuple
###############################################################################


# Named Tuple
# * The NamedTuple type is used to create a new tuple type with named fields
# * This is an alternative way of creating a type using the
#   `collections.namedtuple()` function
from typing import NamedTuple
class Customer(NamedTuple):
    name: str
    id: int


# Named Tuple (with collections.namedtuple())
# * The example above is equivalent to the example below
# * Note that both examples return a `Customer` type with the same
#   caracteristics
from collections import namedtuple
Customer = namedtuple('Customer', ['name', 'id'])


###############################################################################
# Callable
###############################################################################


# Callable
# * The Callable type is used to specify that the variable is a callable
#   (function, method, etc.)
# * Syntax: Callable[[Arg1Type, Arg2Type, ...], ReturnType]
from typing import Callable
x: Callable[[int, int], int] = lambda x, y: x + y


# Callable (...)
# * The `...` syntax can be used to specify that the variable is a callable
#   with any number of arguments
x: Callable[..., Any] = lambda x: x
y: Callable[..., Any] = lambda x, y: x + y


###############################################################################
# Generic
###############################################################################


# Generic
# * The Generic type is used to specify that the class has a generic type
# * A generic type is a type that can be parameterized in a class to define
#  that the class can work with a specific variable type
# * Note that we don't need to import the Generic class from the typing module
#   since Python 3.7 (PEP 560) introduced a new feature that allows us to
#   define a generic type with the '[]' syntax
# * In the example below, the `T` is a generic type
class CustomList[T]:
    def add(self, x: T) -> None:
        ...


###############################################################################
# Protocols
###############################################################################


# Reversible
# * The Reversible type is used to specify that the object supports the
#   `reversed` function
from typing import Reversible
x: Reversible = [1, 2, 3]
y = reversed(x)
print(list(y))
# [3, 2, 1]


# SupportsAbs
# * The SupportsAbs type is used to specify that the object supports the
#   `abs` function
from typing import SupportsAbs
x: SupportsAbs = -5
y = abs(x)
print(y)
# 5


# SupportsBytes
# * The SupportsBytes type is used to specify that the object supports the
#   `bytes` function
from typing import SupportsBytes
x: SupportsBytes = 'Hello'
y = bytes(x, 'utf-8')
print(y)
# b'Hello'


# SupportsComplex
# * The SupportsComplex type is used to specify that the object supports the
#   `complex` function
from typing import SupportsComplex
x: SupportsComplex = 5
y = complex(x)
print(y)
# (5+0j)


# SupportsFloat
# * The SupportsFloat type is used to specify that the object supports the
#   `float` function
from typing import SupportsFloat
x: SupportsFloat = 5
y = float(x)
print(y)
# 5.0


# SupportsIndex
# * The SupportsIndex type is used to specify that the object supports the
#   indexing operation `x[n]`
from typing import SupportsIndex
x: SupportsIndex = [1, 2, 3]
y = x[0]
print(y)
# 1


# SupportsInt
# * The SupportsInt type is used to specify that the object supports the
#   `int` function
from typing import SupportsInt
x: SupportsInt = 5.5
y = int(x)
print(y)
# 5


# SupportsRound
# * The SupportsRound type is used to specify that the object supports the
#   `round` function
from typing import SupportsRound
x: SupportsRound = 5.5
y = round(x)
print(y)
# 6


###############################################################################
# Custom Protocol
###############################################################################


# Creating a new Protocol
# * The Protocol type is used as a base class for defining protocols classes
# * A protocol class is a class that defines a set of methods that a class must
#   implement to support a particular interface
from typing import Protocol
class CustomProtocol(Protocol):
    def __method__(self) -> int:
        ...


# Implementing class with Protocol
# * Now, we will create a class that implements the protocol
# * Since Python uses duck typing, the class does not need to explicitly
#   implement the protocol, but it must have the required methods
class CustomClass:
    def __method__(self) -> int:
        return 5


# Ensuring that the object implements the Protocol
# * To ensure that some argument or variable implements the protocol, we can
#   use the custom protocol as the type hint
x: CustomProtocol = CustomClass()
print(x.__method__())
# 5


###############################################################################
# Type Var Tuple
###############################################################################


# Type Var Tuple
# * The TypeVarTuple type is used to create a custom type variable tuple
# * Syntax: TypeVarTuple('TypeVarTupleName')
from typing import TypeVarTuple
T = TypeVarTuple('T')


# Unpack or '*'
# * The Unpack type is used to specify that the variable is a tuple with the
#   specified elements unpacked
# * The '*' operator can be used as a shorthand for Unpack (preferred)
from typing import Unpack
T = TypeVarTuple('T')
x: tuple[Unpack[T]] = 1, 2, 3


###############################################################################
# Param Spec
###############################################################################


# Create ParamSpec
# * The ParamSpec type is used to forward the parameter types of one callable
#   to another callable
# * Commonly found in higher order functions and decorators
# * In the example below, we will create a ParamSpec
from typing import ParamSpec
P = ParamSpec('P')


# Using ParamSpec in a decorator
# * The P is used and linked to inner function
# * The P.args and P.kwargs are allowed to be used to link the parameters
#   between the functions
def decorator(fn: Callable[P, Any]) -> Callable[P, Any]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
        ...
    return wrapper


###############################################################################
# Concatenate
###############################################################################


# Create ParamSpec for Concatenate
# * Used with Callable and ParamSpec to type annotate a higher order callable
#   which adds, removes, or transforms parameters of another callable
# * A ParamSpec must be created to be used with Concatenate
from typing import Concatenate
P = ParamSpec('P')


# Using Concatenate in a decorator
# * The Concatenate says that the Callable object will be modified with the
#   concatenate arguments.
# * Commonly found in higher order functions and decorators.
def decorator(fn: Callable[Concatenate[str, P], Any]) -> Callable[P, Any]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
        fn('something', *args, **kwargs)
    return wrapper


###############################################################################
# Other Types
###############################################################################


# Type Guard
# * The TypeGuard type is used to ensure that the type specified is the type
#   of the argument if the function returns True
# * The TypeGuard tells to the static type checker that for a given function:
#   1. The return value is a boolean
#   2. If the return value is True, the type of its argument is the type inside
#      TypeGuard
# * For example, when we want to validate the type of a data, we can use the
#   TypeGuard type as the return type of the function to ensure that the data
#   is of the specified type
from typing import TypeGuard
def is_str_list(x: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(el, str) for el in x)


# Annotated
# * The Annotated type is used to attach metadata to a type hint
# * It is used to provide additional information about the resource
# * In the example below, we created a new int type, but with some additional
#   metadata
from typing import Annotated
T = Annotated[int, 'metadata']
print(T.__metadata__)
# metadata


###############################################################################
# Override
###############################################################################


# Importing Override
# * The Override type is used to indicate that some method is overriding a
#   method from a super class
from typing import override


# Defining a super class
# * We must define a super class with a method that will be overrided
class SuperClass:
    def process(self) -> None:
        ...


# Defining a sub class with overrided method
# * Note that the `process` method was overrided and contains the `override`
#   decorator to indicate it for the type checker
class SubClass(SuperClass):
    @override
    def process(self) -> None:
        ...


###############################################################################
# Overload
###############################################################################


# Importing Overload
# * The Overload type is used to indicate that a method has multiple
#   implementations with different signatures for the type checker
# * The overloaded methods cannot be implemented, they are just for the type
#   checker to know that the method has multiple implementations
# * NOTE: The method that contains the implementation cannot be marked as
#   overload
from typing import overload


# Defining a class with overloaded methods
# * The class below contains some overloaded methods
# * Note that the `process` method has multiple implementations with different
#   signatures, but the last implementation is the actual implementation. The
#   other implementations are just for the type checker
class CustomClass:
    @overload
    def process(self, x: int) -> int: ...
    @overload
    def process(self, x: str) -> str: ...
    def process(self, x):
        ...


# Get overloads
# * The `get_overloads` function can be used to retrieve the overloads of a
#   method or function as a list
from typing import get_overloads
x = get_overloads(CustomClass.process)
print(x)
# [<function CustomClass.process at ..>, <function CustomClass.process at ..>]


# Clear overloads
# * Clear all registered overloads in the internal registry
# * This can be used to reclaim the memory used by the registry
from typing import clear_overloads
clear_overloads()
# Clear all overloads in the internal registry


###############################################################################
# Final
###############################################################################


# Final
# * Decorator to indicate to type checkers that the decorated method cannot be
#   overridden, and decorated class cannot be subclassed
# * In the example below, the `CustomClass` cannot be subclassed, and the
#   `process` method cannot be overridden
from typing import final
@final
class CustomClass:
    @final
    def process(self):
        ...


###############################################################################
# Other Functions
###############################################################################


# Assert Type
# * Used to assert that the type of the variable is the specified type
# * At runtime this method does nothing, but it is useful for type checkers
from typing import assert_type
x = 'abc'
assert_type(x, int)
# Nothing happens, but the type checker will warn that the type is wrong


# Assert Never
# * Used to assert that some case is never reached
# * If the case is reached, it will raise an AssertionError
from typing import assert_never
if True is False:
    assert_never('This case should never be reached')
# AssertionError: This case should never be reached


# Get Type Hints
# * Return a dictionary containing type hints for a function, method, module or
#   class object
from typing import get_type_hints
def fn(x: int) -> str: ...
x = get_type_hints(fn)
print(x)
# {'x': <class 'int'>, 'return': <class 'str'>}


# Get Origin
# * Get the unsubscripted version of a type, i.e. the origin of a type
# * For example, if the type is `list[int]`, the origin is `list`
from typing import get_origin
x = get_origin(list[int])
print(x)
# <class 'list'>


# Is Typed Dict
# * Check if the type is a TypedDict
from typing import is_typeddict
x = is_typeddict(CustomDict)
print(x)
# True


# Reveal Type
# * Ask a static type checker to reveal the inferred type of an expression
from typing import reveal_type
x: int = 5
reveal_type(x)
# Runtime type is 'int'


###############################################################################
# Other Decorators
###############################################################################


# Dataclass Transform
# * Decorator to mark an object as providing dataclass-like behaviour
# * A class marked with this decorator will be viwed as a dataclass by the
#   type checker
# * Can be applied to a functions, classes, or metaclasses
from typing import dataclass_transform
@dataclass_transform()
class CustomClass:
    ...


# No Type Check
# * Decorator to indicate that annotations are not type hints
# * The argument must be a class or function; if it is a class, it applies
#   recursively to all methods and classes defined in that class (but not to
#   methods defined in its superclasses or subclasses)
from typing import no_type_check
@no_type_check
class CustomClass:
    ...


# No Type Check Decorator
# * Decorator to give another decorator the @no_type_check effect
# * Used to create decorators with the no_type_check effect
from typing import no_type_check_decorator
@no_type_check_decorator
def decorator(fn):
    ...


# Type Check Only
# * Decorator to mark a class or function as unavailable at runtime, only
#   available for type checkers
from typing import type_check_only
@type_check_only
class NewType:
    ...


# Runtime Checkable
# * Mark a protocol class as a runtime protocol
# * Used to ensure that the type checker should check if the protocol is
#   implemented at runtime
from typing import runtime_checkable
@runtime_checkable
class CustomProtocol(Protocol):
    ...


###############################################################################
# Constants
###############################################################################


# Type Checking Flag
# * To handle with cyclic importantions, the typing.TYPE_CHECKING flag can be
#   used to import the object just for type checking
# * In the example below, the ABC module will just be used for type checkers,
#   and it will not be imported at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from abc import ABC
