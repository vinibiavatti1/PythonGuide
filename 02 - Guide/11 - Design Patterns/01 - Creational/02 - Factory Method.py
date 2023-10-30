"""
Factory Method design pattern

* Book: GOF
* Factory Method is a creational design pattern that provides an interface for
  creating objects in a superclass, but allows subclasses to alter the type of
  objects that will be created
* he Factory Method pattern suggests that you replace direct object
  construction calls (using the new operator) with calls to a special factory
  method. Don't worry: the objects are still created via the new operator, but
  it's being called from within the factory method. Objects returned by a
  factory method are often referred to as products
"""
from abc import ABC, abstractmethod


# Click interface
class Clickable(ABC):
    @abstractmethod
    def click(self):
        pass


# Windows Button
class WinButton(Clickable):
    def click(self):
        print('Win Button')


# Mac button
class MacButton(Clickable):
    def click(self):
        print('Mac button')


# Dialog interface with factory method
class Dialog(ABC):

    @abstractmethod
    def create_button(self):
        pass


# Windows dialog
class WinDialog(Dialog):

    def create_button(self):
        return WinButton()


# Mac dialog
class MacDialog(Dialog):

    def create_button(self):
        return MacButton()


# Algorithm
os = 'Windows'
dialog = None
if os == 'Windows':
    dialog = WinDialog()
else:
    dialog = MacDialog()
btn = dialog.create_button()
btn.click()
# Windows btn
