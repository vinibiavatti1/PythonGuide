"""
Module Template

* This is the template for module construction
"""
from typing import (
    Any,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    pass  # Type hint importations


###############################################################################
# Module Constants
###############################################################################


PUBLIC_CONST = 1      # public
__PRIVATE_CONST = 2   # private


###############################################################################
# Module Variables
###############################################################################


public_var = 1      # public
__private_var = 2   # private


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


if __name__ == '__main__':
    main()
