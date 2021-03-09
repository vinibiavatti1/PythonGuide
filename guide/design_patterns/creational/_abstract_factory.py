"""
Abstract Factory design pattern

* Abstract Factory is a creational design pattern that lets you produce
  families of related objects without specifying their concrete classes
* Abstract Factory pattern suggests is to explicitly declare interfaces for
  each distinct product of the product family (e.g., chair, sofa or coffee
  table). Then you can make all variants of products follow those interfaces.
  For example, all chair variants can implement the Chair interface; all coffee
  table variants can implement the CoffeeTable interface, and so on
"""
from abc import ABC, abstractmethod


# Factory interface
class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass


# Windows GUI factory
class WinGuiFactory(GUIFactory):

    def create_button(self):
        print('Windows btn')


# MAC GUI factory
class MacGuiFactory(GUIFactory):

    def create_button(self):
        print('Mac btn')


# Application GUI renderer
class Application:

    def __init__(self, factory):
        self.factory = factory

    def create_ui(self):
        self.factory.create_button()


# Algorithm
os = 'Windows'
factory = None
if os == 'Windows':
    factory = WinGuiFactory()
else:
    factory = MacGuiFactory()
app = Application(factory)
app.create_ui()
# Windows btn
