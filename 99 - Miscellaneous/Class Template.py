"""
Class Template
"""
from abc import ABC, abstractmethod
from typing import Any, Final, ClassVar, TYPE_CHECKING
if TYPE_CHECKING:
    ...  # Type checking imports


class ClassTemplate(ABC):
    # Constants
    PUBLIC_CONST: Final[int] = 1
    _PROTECTED_CONST: Final[int] = 2
    __PRIVATE_CONST: Final[int] = 3

    # Class Variables
    public_var: ClassVar[int] = 1
    _protected_var: ClassVar[int] = 2
    __private_var: ClassVar[int] = 3

    # Static Methods
    @staticmethod
    def static_method() -> None:
        ...

    # Class Methods
    @classmethod
    def class_method(cls) -> None:
        ...

    # Constructor
    def __init__(self) -> None:
        ...

    # Magic Methods
    def __repr__(self) -> None:
        ...

    # Abstract Methods & Properties
    @abstractmethod
    def abstract_method(self, parameter: Any) -> None:
        pass

    # Public Methods & Properties
    def public_method(self, parameter: Any) -> None:
        ...

    # Protected Methods & Properties
    def _protected_method(self, parameter: Any) -> None:
        ...

    # Private Methods & Properties
    def __private_method(self, parameter: Any) -> None:
        ...
