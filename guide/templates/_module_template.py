"""
Module Template

* This is a template for module construction
"""
from typing import (
    Any,
    Final,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    ...  # Type checking imports


###############################################################################
# Module Constants
###############################################################################


PUBLIC_CONST: Final[int] = 1
__PRIVATE_CONST: Final[int] = 2


###############################################################################
# Module Variables
###############################################################################


public_var: int = 1
__private_var: int = 2


###############################################################################
# Public/Private Classes
###############################################################################


class PublicClass:
    """
    Public Class.
    """


class __PrivateClass:
    """
    Private Class.
    """


###############################################################################
# Public/Private Functions
###############################################################################


def public_function(param1: Any) -> None:
    """
    Public function.
    """


def __private_function(param1: Any) -> None:
    """
    Private function.
    """


###############################################################################
# Main
###############################################################################


def main() -> None:
    """
    Main function.
    """


# Initialization
if __name__ == '__main__':
    main()
