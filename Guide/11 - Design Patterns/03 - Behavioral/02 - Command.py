"""
Command design pattern

* Book: GOF
* Command is a behavioral design pattern that turns a request into a
  stand-alone object that contains all information about the request. This
  transformation lets you parameterize methods with different requests, delay
  or queue a request's execution, and support undoable operations
* Good software design is often based on the principle of separation of
  concerns, which usually results in breaking an app into layers
"""
from abc import ABC, abstractmethod


# Command ABC
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Swith to process commands
class Switch:
    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        self.history.append(command)
        command.execute()


# Turn on command
class TurnOnCommand(Command):
    def __init__(self, light):
        self.name = 'Turn ON'
        self.light = light

    def execute(self):
        self.light.turn_on()


# Turn off command
class TurnOffCommand(Command):
    def __init__(self, light):
        self.name = 'Turn OFF'
        self.light = light

    def execute(self):
        self.light.turn_off()


# Light
class Light:
    def __init__(self):
        self.turn_off()

    def turn_on(self):
        self.state = 'ON'

    def turn_off(self):
        self.state = 'OFF'


# Algorithm
lamp = Light()
turn_on_cmd = TurnOnCommand(lamp)
turn_off_cmd = TurnOffCommand(lamp)

switch = Switch()

switch.store_and_execute(turn_on_cmd)
print(lamp.state)  # ON

switch.store_and_execute(turn_off_cmd)
print(lamp.state)  # OFF

# Hisotry
for cmd in switch.history:
    print(cmd.name)
# Turn ON
# Turn OFF
