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
    TypedDict,
    Generic,
    KT,
    VT,
    TypeVar,
    Callable,
    NoReturn
)


###############################################################################
# Datatypes
###############################################################################


# List
# * Define the variable type as list
lst: List[str] = ['John']


# Tuple
# * Define the variable type as tuple
tpl: Tuple[str] = ('John')


# Dict
# * Define the variable type as dict
dct: Dict[str, int] = {'age': 26}


# Set
# * Define the variable type as set
st: Set[str] = {'John'}


# Frozenset
# * Define the variable type as frozenset
fst: FrozenSet[str] = frozenset({'John'})


# Any
# * Define the variable type as any (Can has any value)
val: Any = 'Hello'


# Callable
# * Define the variable type as callable (Any resource that can be called)
fn: Callable = lambda x: x


###############################################################################
# Enum types
###############################################################################


# Literal
# * A type that can be used to indicate to type checkers that the corresponding
#   variable or function parameter has a value equivalent to the provided
#   literal (or one of several literals)
# * In the example, the literal indicates the only possible values that the
#   function can return
def send_mail(_from: str, _to: str, /) -> Literal['success', 'error']:
    ...


# Union
# * Used to define more than on possible type for some resource
# * In the example, the function can receive the value as integer or string
def double(value: Union[int, str]):
    ...


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
class HashMap(Generic[KT, VT]):
    ELEMENTS: dict[KT, VT] = {}


# NoReturn
# * Specifies that the function has no return
def msg() -> NoReturn:
    ...


# Text
# * Text is an alias for str. It is provided to supply a forward compatible
#   path for Python 2 code
txt: Text = 'Hello'


###############################################################################
# Custom type
###############################################################################


# TypeVar
# * Create a custom type variable
# * In the example, the KEY type can be str or int
KEY = TypeVar('KEY', str, int)
key_1: KEY = 1
key_2: KEY = '2'
