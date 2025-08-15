"""
Module Template
"""
from typing import Final, TYPE_CHECKING
if TYPE_CHECKING:
    ...  # Type checking imports


PUBLIC_CONST: Final[int] = 1
__PRIVATE_CONST: Final[int] = 2


public_var: int = 1
__private_var: int = 2


class PublicClass:
    ...


class __PrivateClass:
    ...


def public_function() -> None:
    ...


def __private_function() -> None:
    ...


def main() -> None:
    ...


if __name__ == '__main__':
    main()
