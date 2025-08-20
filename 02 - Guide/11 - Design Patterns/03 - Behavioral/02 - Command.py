"""
Command

* The Command pattern is a behavioral design pattern that turns a request into
  a stand-alone object.
* The pattern encapsulates a request as an object, thereby allowing for
  parameterization of clients with queues, requests, and operations.
* It also provides support for undoable operations.
"""


###############################################################################
# Command
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Command
# * Abstract base class for all commands
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Text Editor
# * Receiver class that performs the actual operations.
# * The receiver is the class that contains the business logic.
class TextEditor:
    def open_file(self) -> None:
        print(f"File opened")

    def save_file(self) -> None:
        print(f"File saved")

    def close_file(self) -> None:
        print("File closed")


# Open Command
# * Command to open a file.
class OpenCommand(Command):
    def __init__(self, editor: TextEditor) -> None:
        self.editor = editor

    def execute(self) -> None:
        self.editor.open_file()


# Save Command
# * Command to save a file.
class SaveCommand(Command):
    def __init__(self, editor: TextEditor) -> None:
        self.editor = editor

    def execute(self) -> None:
        self.editor.save_file()


# Close Command
# * Command to close a file.
class CloseCommand(Command):
    def __init__(self, editor: TextEditor) -> None:
        self.editor = editor

    def execute(self) -> None:
        self.editor.close_file()


# Toolbar
# * Invoker class that triggers the commands.
# * The invoker holds the command objects and invokes them.
class Toolbar:
    def __init__(self, editor: TextEditor) -> None:
        self.open = OpenCommand(editor)
        self.save = SaveCommand(editor)
        self.close = CloseCommand(editor)

    def open_file(self) -> None:
        self.open.execute()

    def save_file(self) -> None:
        self.save.execute()

    def close_file(self) -> None:
        self.close.execute()


# Testing
# * Now, note that the commands are decoupled from the invoker.
editor = TextEditor()
toolbar = Toolbar(editor)
toolbar.open_file()
toolbar.save_file()
toolbar.close_file()
# File opened
# File saved
# File closed
