"""
Typing module

* This module provides runtime support for type hints as specified by PEP 484,
  PEP 526, PEP 544, PEP 586, PEP 589, and PEP 591
* The most fundamental support consists of the types Any, Union, Tuple,
  Callable, TypeVar, and Generic
* Reference: https://docs.python.org/3/library/collections.abc.html
"""
from typing import (
    Any,
    AnyStr,
    Text,
    Awaitable,
    Concatenate,
    Iterable,
    Iterator,
    ParamSpec,
    Literal,
    Union,
    Final,
    TypedDict,
    Generic,
    NewType,
    TypeAlias,
    Type,
    Protocol,
    TypeVar,
    Callable,
    NoReturn,
    Optional,
    TypeGuard,
    Coroutine,
    ClassVar,
    Generator,
    NamedTuple,
    final,
    TYPE_CHECKING
)


###############################################################################
# Data types
###############################################################################


# Data Types
# * The python datatypes can be used to define the type hint for the variables,
#   return type and etc.
x: int = 1
x: str = 'hello world'
x: float = 1.5
x: complex = 1j
x: bool = True
x: range = range(1, 5)
x: bytes = b'Hello World'
x: bytearray = bytearray(5)
x: memoryview = memoryview(bytes(5))


###############################################################################
# Collection Types
###############################################################################


# Collection Types
# * Define the variable type as builtin collection.
# * For the tuple, the type specify the data type of the exact position in the
#   tuple.
# * NOTE: The typing module collection data types, like List, Tuple, Set, etc..
#   are deprecated. The builtin collection data types can now be used for
#   type hints.
x: tuple[str, int, bool] = ('John', 26, True)
x: list[str] = ['John']
x: set[str] = {'John', 'Doe'}
x: frozenset[str] = frozenset({'John', 'Doe'})
x: dict[str, int] = {'age': 26}


###############################################################################
# Special Types
###############################################################################


# None
# * Specifies that the function returns None (common return type)
def action() -> None: ...


# Any
# * Define the variable type as any (It can be any type of value)
x: Any = 'Hello'


# AnyStr
# * AnyStr is a type variable defined as AnyStr = TypeVar('AnyStr', str, bytes)
# * Used to accept strings and string as bytes
# * The same kind of arguments is required. Cannot accept mix types like:
#   WRONG:   method(b'hi', u'hi', 'hi')
#   CORRENT: method(b'hi', b'hi', b'hi')
def method(arg1: AnyStr, arg2: AnyStr) -> None: ...  # Accepts '', b'' and u''


# Text
# * Text is an alias for str. It is provided to supply a forward compatible
#   path for Python 2 code
txt: Text = 'Hello'


# NoReturn
# * Specifies that the function never returns (the function will raise an
#   exception, or will stay in a loop forever)
def forever() -> NoReturn: ...


# TypeAlias
# * Special annotation for explicitly declaring a type alias.
Vector: TypeAlias = list[float]


###############################################################################
# Special Forms
###############################################################################


# Final
# * A special typing construct to indicate to type checkers that a name cannot
#   be re-assigned or overridden.
# * Can be used to declare constants.
X: Final[int] = 1234  # Cannot be changed anymore


# ClassVar
# * Special type construct to mark class variables.
# * The variable cannot be used in the instance context.
class SomeClass:
    class_variable: ClassVar[int] = 5  # Class Variable


# Union
# * Used to define more than on possible type for some resource
# * Since Python 3.10, you can use the pipe char (|) for union
# * In the example, the function can receive the value as integer or string
def double(value: Union[int, str]) -> Union[int, str, None]: ...


# Union Pipe (|)
# * You can define union types using the pipe char- In this way, the
#   declaration is less verboose
# * Available in 3.10 version
def triple(value: int | str) -> int | str | None: ...


# Optional
# * The optional is used as a annotation in a context which the value can be
#   the specified type or None
def get_idx(index: int) -> Optional[str]: ...


# Optional Pipe (|)
# * The same result can be made using the pipe (|) char and None
# * Available in 3.10 version
def get_the(index: int) -> str | None: ...


# Type
# * Accept classes and subclasses of the typed class
class User:
    ...


class BasicUser(User):
    ...


def create_user(user: Type[User]): ...  # Accepts User and BasicUser as arg


# Literal
# * A type that can be used to indicate to type checkers that the corresponding
#   variable or function parameter has a value equivalent to the provided
#   literal (or one of several literals)
# * In the example, the literal indicates the only possible values that the
#   function can return
def send_mail(_from: str, _to: str, /) -> Literal['success', 'error']: ...


# TypeGuard
# * Ensure the type specified into TypeGuard is that type if the function
#   returns True
# * Using -> TypeGuard[...] tells the static type checker that for a given
#   function:
#   1. The return value is a boolean.
#   2. If the return value is True, the type of its argument is the type inside
#      TypeGuard.
# * Available in 3.10 version
def is_str_list(lst: list[object]) -> TypeGuard[list[str]]: ...


###############################################################################
# Callable
###############################################################################


# Callable
# * Define the variable type as callable (Any resource that can be called)
# * Template: Callable[[Arg1Type, Arg2Type, ...], ReturnType]
x: Callable[[str], str] = lambda x: x


# Callable Ellipsis
# * Use ellipsis to define any amount of parameters
x: Callable[..., Any] = lambda x, y, z: x


###############################################################################
# Custom type
###############################################################################


# Use TypeVar to create custom types
# * Create a custom type variable
# * In the example, the KEY type can be str or int
CustomType = TypeVar('CustomType', str, int)
key_1: CustomType = 1
key_2: CustomType = '2'


###############################################################################
# Generic
###############################################################################


# Set generic variables
# * A generic type is typically declared by inheriting from an instantiation of
#   this class with one or more type variables.
KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


# Create generic class
# * The class musc extends the Generic class to use generic data
class HashMap(Generic[KeyType, ValType]):
    ELEMENTS: dict[KeyType, ValType] = {}


# Create instance of generic class
# * To create an instance, just add the type into []
hash_map = HashMap[int, str]()


###############################################################################
# Protocol
###############################################################################


# Defining a Protocol
# * Protocol is a class with a specific structure (group of methods).
# * IT uses the concept of "duck-typing".
class Proto(Protocol):
    def __my_method__(self) -> None:
        ...


# Protocol Type Hint
# * The protocol class can be used as typehint to ensure the resource has the
#   structure of the protocol.
def process(arg1: Proto) -> None: ...  # The arg1 must implement __my_method__


###############################################################################
# ParamSpec
###############################################################################


# Create ParamSpec
# * Used to forward the parameter types of one callable to another callable.
# * Commonly found in higher order functions and decorators.
Param = ParamSpec('Param')


# Using ParamSpec in decorator
# * The param is used and linked to inner function
# * The ParamSpec.args and ParamSpec.kwargs are allowed to be used to link the
#   parameters.
def decorator(fn: Callable[Param, Any]) -> Callable[Param, Any]:
    def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> Any:
        ...
    return wrapper


###############################################################################
# Concatenate
###############################################################################


# Create ParamSpec for Concatenate
# * Used with Callable and ParamSpec to type annotate a higher order callable
#   which adds, removes, or transforms parameters of another callable.
# * A ParamSpec must be created to be used with Concatenate.
Arg = ParamSpec('Arg')


# Using Concatenate in decorator
# * The Concatenate says that the Callable object will be modified with the
#   concatenate arguments.
# * Commonly found in higher order functions and decorators.
def add_str(fn: Callable[Concatenate[str, Arg], Any]) -> Callable[Arg, Any]:
    def wrapper(*args: Arg.args, **kwargs: Arg.kwargs) -> Any:
        fn('added str', *args, **kwargs)
    return wrapper


###############################################################################
# Generator, Iterable and Iterator
###############################################################################


# Generator
# * A generator can be annotated by the generic type Generator
# * If your generator will only yield values, set the SendType and ReturnType
#   to None
# * Alternatively, annotate your generator as having a return type of either
#   Iterable[YieldType] or Iterator[YieldType]
# * Template: Generator[YieldType, SendType, ReturnType]
# * NOTE: SendType is a feature introduced way back in Python 2.5 as part
#   of PEP 342, which extended generators to work as coroutines.
def generator() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'


# Iterable
# * Classes that provide the __iter__() method.
def other_generator() -> Iterable[int]:
    yield 0


# Iterator
# * ABC for classes that provide the __iter__() and __next__() methods
def another_generator() -> Iterator[int]:
    yield 0


###############################################################################
# Asynchronous Programming
###############################################################################


# Asyncio Coroutines Typehints
# * Used to define async function types.
# * The variance and order of type variables correspond to those of Generator.
# * Template (Similar to Generator): Generator[YieldType, SendType, ReturnType]
def run_async_fn(fn: Coroutine[int, float, str]) -> Any: ...


# Awaitable
# * ABC for awaitable objects, which can be used in await expressions.
# * Custom implementations must provide the __await__() method.
async def async_fn(val: int) -> str:
    return 'text'


fn: Callable[[int], Awaitable[str]] = async_fn


# Async Generators
# * AsyncIterable, AsyncIterator and AsyncGenerator can be used for async
#   generators to coroutines.


###############################################################################
# Other Special Directives
###############################################################################


# NamedTuple
# * Type version for collections.namedtuple()
# * The example is equivalent to:
#   collections.namedtuple('Employee', ['name', 'id'])
class Employee(NamedTuple):
    name: str
    id: int


# TypedDict
# * TypedDict declares a dictionary type that expects all of its instances to
#   have a certain set of keys, where each key is associated with a value of a
#   consistent type
# * This expectation is not checked at runtime but is only enforced by type
#   checkers
class Point(TypedDict):
    x: int
    y: int


point: Point = dict(x=5, y=4)  # Ok
point: Point = dict(x=4)  # Fails type check


# NewType
# * Use the NewType helper class to create distinct types.
# * If the argument asks for a distict type, this type must be respected.
UserId = NewType('UserId', int)
some_id = UserId(123)
other_id = 456  # NOTE: Is not accepted as an UserId type!


###############################################################################
# Cyclic importations
###############################################################################


# Type Checking Flag
# * To handle with cyclic importantions, the typing.TYPE_CHECKING flag can be
#   used to import the object just for type checking
if TYPE_CHECKING:
    from abc import ABC  # ABC will just be used for type hints


###############################################################################
# Decorators
###############################################################################


# final decorator
# * Decorator to indicate to type checkers that the decorated method cannot be
#   overridden, and decorated class cannot be subclassed
@final
class Animal:  # Cannot be used as super class
    @final  # Cannot be overrided
    def eat(self):
        ...
