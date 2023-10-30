"""
Mediator design pattern

* Book: GOF
* Mediator is a behavioral design pattern that lets you reduce chaotic
  dependencies between objects. The pattern restricts direct communications
  between the objects and forces them to collaborate only via a mediator object
* The Mediator pattern suggests that you should cease all direct communication
  between the components which you want to make independent of each other.
  Instead, these components must collaborate indirectly, by calling a special
  mediator object that redirects the calls to appropriate components
"""
from abc import ABC, abstractmethod


# Mediator ABC
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


# Root frame
class Frame(Mediator):
    def __init__(self):
        self.components = []

    def notify(self, sender, event):
        if event == 'click':
            print('Btn click')
        elif event == 'close':
            print('Frame close')

    def add_component(self, component):
        self.components.append(component)


# Button component
class Button:
    def __init__(self, frame):
        self.frame = frame

    def click(self):
        self.frame.notify(self, 'click')


# Close button component
class CloseButton:
    def __init__(self, frame):
        self.frame = frame

    def click(self):
        self.frame.notify(self, 'close')


# Algorithm
frame = Frame()

button = Button(frame)
close = CloseButton(frame)

frame.add_component(button)
frame.add_component(close)

button.click()  # Btn click
close.click()   # Frame close
