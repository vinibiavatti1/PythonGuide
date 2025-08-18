"""
Abstract Factory

* Abstract Factory is a creational design pattern that lets you produce
  families of related objects without specifying their concrete classes.
* A class will delegate the responsibility of instantiating objects to a
  factory.
"""


###############################################################################
# Abstract Factory
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


# Component Factory
# * The abstract class below defines a factory for creating UI components.
# * In our case, we will only define a method for creating buttons.
class ComponentFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass


# Flat Component Factory
# * The class below is a concrete factory that implements the ComponentFactory
#   interface.
# * It creates a flat components.
class FlatComponentFactory(ComponentFactory):
    def create_button(self) -> Button:
        return Button("(Button)")


# Rounded Component Factory
# * The class below is another concrete factory that implements the
#   ComponentFactory interface.
# * It creates a rounded components.
class RoundedComponentFactory(ComponentFactory):
    def create_button(self) -> Button:
        return Button("(Button)")


# Frame
# * The abstract class below defines a frame for the UI components.
# * It contains a factory for creating the components, and a method for
#   rendering them.
class Frame(ABC):
    def __init__(self, factory: ComponentFactory) -> None:
        self.factory = factory

    def render(self) -> None:
        button_element = self.factory.create_button()
        print(f"Button: {button_element.markup}")


# Flat Frame
# * The class below is a concrete class that implements the Frame interface.
class FlatFrame(Frame):
    def __init__(self) -> None:
        super().__init__(FlatComponentFactory())


# Rounded Frame
# * The class below is a concrete class that implements the Frame interface.
class RoundedFrame(Frame):
    def __init__(self) -> None:
        super().__init__(RoundedComponentFactory())


# Testing
# * Now, we will test the frames. Note that the output will vary depending on
#   the factory used.
x = FlatFrame()
y = RoundedFrame()
x.render()
y.render()
# Button: (Button)
# Button: (Button)
