"""
Prototype

* The Prototype pattern is a creational design pattern that allows you to
  create new objects by copying an existing object, known as the prototype.
* This pattern is useful when the cost of creating a new object is more
  expensive than copying an existing one.
* Usually, to implement the Prototype pattern, we need to implement a clone
  method. In Python, we can use the `copy` module to create shallow copies
  of objects.
"""


###############################################################################
# Prototype
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from typing import Self
from copy import copy


# Button
# * The model below is a class that represents a Button.
# * It will override the `__copy__` method to create a copy of the button.
# * Note that the `__copy__` method is called when the `copy` function is used.
#   It belongs to the copy protocol.
# * Since the copy already knows how to copy a simple object, the
#   implementation below is not necessary. We will implement it anyway for
#   demonstration purposes.
class Button:
    def __init__(self, label: str) -> None:
        self.label = label

    def __copy__(self) -> Self:
        return Button(self.label)


# Testing
# * Now, we will create a clone of the button, using the button itself as a
#   prototype.
button_1 = Button("First Name")
button_2 = copy(button_1)
button_2.label = "Last Name"
print(button_1.label)
print(button_2.label)
# First Name
# Last Name
