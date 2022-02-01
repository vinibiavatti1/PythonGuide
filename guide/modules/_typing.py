"""
Typing module

* This module provides runtime support for type hints as specified by PEP 484,
  PEP 526, PEP 544, PEP 586, PEP 589, and PEP 591
* The most fundamental support consists of the types Any, Union, Tuple,
  Callable, TypeVar, and Generic
"""
from typing import (
    List,
    Dict,
    Tuple,
    Set,
    FrozenSet,
    Any,
    Text,
    Literal,
    Union,
    Final,
    final,
    TypedDict,
    Generic,
    KT,
    VT,
    TypeVar,
    Callable,
    NoReturn,
    Optional
)
import typing


###############################################################################
# Datatypes
###############################################################################


# List
# * Define the variable type as list
# * The same for using list[]
lst: List[str] = ['John']


# Tuple
# * Define the variable type as tuple
# * The same for using list[]
tpl: Tuple[str] = ('John')


# Dict
# * Define the variable type as dict
# * The same for using dict[]
dct: Dict[str, int] = {'age': 26}


# Set
# * Define the variable type as set
# * The same for using set[]
st: Set[str] = {'John'}


# Frozenset
# * Define the variable type as frozenset
# * The same for using frozenset[]
fst: FrozenSet[str] = frozenset({'John'})


# Any
# * Define the variable type as any (Can has any type of value)
val: Any = 'Hello'


# Callable
# * Define the variable type as callable (Any resource that can be called)
fn: Callable = lambda x: x


###############################################################################
# Literal type
###############################################################################


# Literal
# * A type that can be used to indicate to type checkers that the corresponding
#   variable or function parameter has a value equivalent to the provided
#   literal (or one of several literals)
# * In the example, the literal indicates the only possible values that the
#   function can return
def send_mail(_from: str, _to: str, /) -> Literal['success', 'error']:
    ...


###############################################################################
# Union type (|)
###############################################################################


# Union
# * Used to define more than on possible type for some resource
# * Since Python 3.10, you can use the pipe char (|) for union
# * In the example, the function can receive the value as integer or string
def double(value: Union[int, str]) -> Union[int, str]:
    ...


# Union Pipe
# * You can define union types using the pipe char- In this way, the
#   declaration is less verboose
def triple(value: int | str) -> int | str:
    pass


###############################################################################
# Optional
###############################################################################


# Optional
# * The optional is used as a annotation in a context which the value can be
#   the specified type or None
def get_idx(index: int) -> Optional[str]:
    pass


# Optional Pipe
# * The same result can be made using the pipe (|) char and None
def get_the(index: int) -> str | None:
    pass


###############################################################################
# Special types
###############################################################################


# Final
# * A special typing construct to indicate to type checkers that a name cannot
#   be re-assigned or overridden
VALUE: Final[int] = 1234  # Cannot be changed anymore


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


# Generic
# * A generic type is typically declared by inheriting from an instantiation of
#   this class with one or more type variables
# * There are commonly generics types already defined in typing module:
#   * KT: Key type
#   * VT: Value type
KT = TypeVar('KT')
VT = TypeVar('VT')


class HashMap(Generic[KT, VT]):
    ELEMENTS: dict[KT, VT] = {}


# NoReturn
# * Specifies that the function never returns (the function will raise an
#   exception, or will stay in a loop forever)
def msg() -> NoReturn:
    ...


# None
# * Specifies that the function returns None (common return type)
def action() -> None:
    ...


# Text
# * Text is an alias for str. It is provided to supply a forward compatible
#   path for Python 2 code
txt: Text = 'Hello'


# final decorator
# * Decorator to indicate to type checkers that the decorated method cannot be
#   overridden, and decorated class cannot be subclassed
@final
class Animal:  # Cannot be used as super class
    @final  # Cannot be overrided
    def eat(self):
        ...


###############################################################################
# Custom type
###############################################################################


# TypeVar
# * Create a custom type variable
# * In the example, the KEY type can be str or int
KEY = TypeVar('KEY', str, int)
key_1: KEY = 1
key_2: KEY = '2'


###############################################################################
# Cyclic importations
###############################################################################


# Type Checking Flag
# * To handle with cyclic importantions, the typing.TYPE_CHECKING flag can be
#   used to import the object just for type checking
if typing.TYPE_CHECKING:
    from abc import ABC  # ABC will just be used for type hints
