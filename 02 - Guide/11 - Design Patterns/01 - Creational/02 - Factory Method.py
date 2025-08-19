"""
Factory Method

* The Factory Method pattern defines an interface for creating an object, but
  lets subclasses alter the type of objects that will be created.
* A class will delegate the responsibility of instantiating objects to the
  subclasses.
"""


###############################################################################
# Factory Method
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Button
# * The model below is a class that represents a Button.
# * It contains a Markup field that represents the button's markup.
# * This button can have different styles, such as flat or rounded.
class Button:
    def __init__(self, markup: str) -> None:
        self.markup = markup


# Frame
# * The abstract class below defines what consists of a form.
# * It looks similar to the abstract factory, but it is a component itself,
#   not a factory.
# * The `create_button` method is called "Factory Method".
class Frame(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self) -> None:
        button_element = self.create_button()
        print(f"Button: {button_element.markup}")


# Flat Frame
# * The class below is a concrete form that implements the Frame interface.
# * Note that the factory method is implemented with different logic for each
#   form.
class FlatFrame(Frame):
    def create_button(self) -> Button:
        return Button('[Button]' )


# Rounded Frame
# * The class below is another concrete form that implements the Frame
#   interface.
# * Note that the factory method is implemented with different logic for each
#   form.
class RoundedFrame(Frame):
    def create_button(self) -> Button:
        return Button('(Button)')


# Testing
# * Now, we will test the forms. Note that the output will vary depending on
#   the form used.
frame_1 = FlatFrame()
frame_2 = RoundedFrame()
frame_1.render()
frame_2.render()
# Button: [Button]
# Button: (Button)
