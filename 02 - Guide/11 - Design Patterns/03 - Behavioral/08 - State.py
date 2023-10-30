"""
State design pattern

* Book: GOF
* State is a behavioral design pattern that allows an object to change the
  behavior when its internal state changes
* The State pattern suggests that you create new classes for all possible
  states of an object and extract all state-specific behaviors into these
  classes
"""
from abc import ABC, abstractmethod


# State ABC
class State(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass


# Button state A
class ButtonStateA(State):
    def __init__(self, context):
        super().__init__(context)

    def handle(self):
        print('State A')
        self.context.change_state(ButtonStateB(self.context))


# Button state B
class ButtonStateB(State):
    def __init__(self, context):
        super().__init__(context)

    def handle(self):
        print('State B')
        self.context.change_state(ButtonStateA(self.context))


# Button class
class Button():
    def __init__(self):
        self.state = ButtonStateA(self)

    def change_state(self, state):
        self.state = state

    def click(self):
        self.state.handle()


# Algorithm
button = Button()
button.click()  # State A
button.click()  # State B
button.click()  # State A
button.click()  # State B
