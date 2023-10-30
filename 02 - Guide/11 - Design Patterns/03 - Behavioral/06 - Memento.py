"""
Memento design pattern

* Book: GOF
* Memento is a behavioral design pattern that lets you save and restore the
  previous state of an object without revealing the details of its
  implementation
* The Memento pattern delegates creating the state snapshots to the actual
  owner of that state, the originator object
"""
from abc import ABC, abstractmethod


# Recover ABC
class Recoverable(ABC):
    def backup(self):
        pass

    def restore(self, memento):
        pass


# Memento ABC
class Memento(ABC):
    def __init__(self, data):
        self.data = data

    def get_data(self):
        pass


# Text editor
class TextEditor(Recoverable):
    def __init__(self):
        self.text = ''

    def write(self, text):
        self.text += text

    def backup(self):
        return TextEditorMemento(self.text)

    def restore(self, memento):
        if not memento:
            return
        self.text = memento.get_data()


# Text editor memento data
class TextEditorMemento(Memento):
    def __init__(self, data):
        super().__init__(data)

    def get_data(self):
        return self.data


# Backup manager
class CareTaker:
    def __init__(self):
        self.mementos = []

    def add(self, memento):
        self.mementos.append(memento)

    def undo(self):
        if not self.mementos:
            return None
        return self.mementos.pop()


# Algorithm
text_editor = TextEditor()
care_taker = CareTaker()

text_editor.write('Hello ')
care_taker.add(text_editor.backup())

text_editor.write('World ')
care_taker.add(text_editor.backup())

text_editor.write('Python')
print(text_editor.text)
# Hello World Python

text_editor.restore(care_taker.undo())
print(text_editor.text)
# Hello World

text_editor.restore(care_taker.undo())
print(text_editor.text)
# Hello
