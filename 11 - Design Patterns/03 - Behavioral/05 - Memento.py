"""
Memento

* The Memento pattern is a behavioral design pattern that allows an object to
  capture its internal state and save it externally, so that it can be restored
  later without violating encapsulation.
* The Memento pattern is often used to implement undo functionality in
  applications, allowing users to revert to a previous state of an object
  without exposing its internal structure.
"""


###############################################################################
# Memento
###############################################################################


# Document
# * The class below represents our model that will be saved and restored.
class Document:
    def __init__(self, content: str) -> None:
        self.content = content


# Document Snapshot
# * The class below is the memento class that stores the document's state.
class DocumentSnapshot:
    def __init__(self, content: str) -> None:
        self.content = content


# Editor
# * The class below is the caretaker that manages the document and its
#   snapshots.
# * Note that it stores a history of the document's states.
class Editor:
    def __init__(self) -> None:
        self.document = Document('')
        self.snapshots: list[DocumentSnapshot] = []

    def save_snapshot(self) -> None:
        self.snapshots.append(DocumentSnapshot(self.document.content))

    def undo(self) -> None:
        if self.snapshots:
            snapshot = self.snapshots.pop()
            self.document.content = snapshot.content


# Testing
# * Now, we will create a document, make some changes and then, we will undo
#   those changes.
editor = Editor()
editor.document.content = "Lorem ipsum"
editor.save_snapshot()
editor.document.content = "dolor sit amet"
editor.save_snapshot()
editor.document.content = "consectetur adipiscing"
print(editor.document.content)
editor.undo()
print(editor.document.content)
editor.undo()
print(editor.document.content)
# consectetur adipiscing
# dolor sit amet
# Lorem ipsum
