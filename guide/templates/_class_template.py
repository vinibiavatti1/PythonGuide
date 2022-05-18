"""
Class Template

* This is the template for class construction
"""
from abc import ABC, abstractmethod
from typing import (
    Any,
    Final,
    ClassVar,
    TYPE_CHECKING
)
if TYPE_CHECKING:
    pass  # Type hint imports


class ClassTemplate(ABC):
    """
    Summary of the class.

    Some description here.
    """

    ###########################################################################
    # Class Constants
    ###########################################################################

    PUBLIC_CONST: Final[int] = 1      # public
    _PROTECTED_CONST: Final[int] = 2  # protected
    __PRIVATE_CONST: Final[int] = 3   # private

    ###########################################################################
    # Class Variables
    ###########################################################################

    public_attr: ClassVar[int] = 1      # public
    _protected_attr: ClassVar[int] = 2  # protected
    __private_attr: ClassVar[int] = 3   # private

    ###########################################################################
    # Static Methods
    ###########################################################################

    @staticmethod
    def static_method(parameter: Any) -> None:
        """
        Static method.
        """

    ###########################################################################
    # Class Methods
    ###########################################################################

    @classmethod
    def class_method(cls, parameter: Any) -> None:
        """
        Class method.
        """

    ###########################################################################
    # Magic Methods
    ###########################################################################

    def __init__(self, name: str, surname: str, age: int) -> None:
        """
        Constructor.
        """
        self.name = name         # public attribute
        self._surname = surname  # protected attribute
        self.__age = age         # private attribute

    ###########################################################################
    # Abstract Methods
    ###########################################################################

    @abstractmethod
    def abstract_method(self, parameter: Any) -> None:
        """
        Abstract method.
        """

    ###########################################################################
    # Public Methods
    ###########################################################################

    def public_method(self, parameter: Any) -> None:
        """
        Public method.
        """

    ###########################################################################
    # Protected Methods
    ###########################################################################

    def _protected_method(self, parameter: Any) -> None:
        """
        Protected method.
        """

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __private_method(self, parameter: Any) -> None:
        """
        Private method.
        """

    ###########################################################################
    # Properties
    ###########################################################################

    @property
    def age(self) -> int:
        """Age getter."""
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        """Age setter."""
        self.__age = age

    @age.deleter
    def age(self) -> None:
        """Age deleter."""
        del self.__age
