"""
Bridge

* The Bridge pattern is a structural design pattern that decouples an
  abstraction from its implementation, allowing the two to vary independently.
* It is useful when you want to avoid a permanent binding between an
  abstraction and its implementation.
"""


###############################################################################
# Bridge
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Content Writer
# * This is an abstract class that defines the interface for content writers.
class ContentWriter(ABC):
    @abstractmethod
    def write_title(self, content: str) -> None:
        pass


# HTML Writer
# * This class will act as a bridge between the File class and the HTML
#   content.
# * Here will be the implementation of the bridge.
class HTMLWriter(ContentWriter):
    def __init__(self) -> None:
        self.content = ""

    def write_title(self, content: str) -> None:
        self.content += f"<h1>{content}</h1>"


# Markdown Writer
# * This class will act as a bridge between the File class and the Markdown
#   content.
# * Here will be the implementation of the bridge.
class MarkdownWriter(ContentWriter):
    def __init__(self) -> None:
        self.content = ""

    def write_title(self, content: str) -> None:
        self.content += f"# {content}\n"


# File
# * This class represents a file with some content.
# * It uses a ContentWriter to write its content.
# * Since the ContentWriter can vary, we can easily switch between different
#   implementations.
class File:
    def __init__(self, writer: ContentWriter) -> None:
        self.writer = writer

    def write_title(self, content: str) -> None:
        self.writer.write_title(content)

    @property
    def content(self) -> str:
        return self.writer.content


# Testing
html_writer = HTMLWriter()
markdown_writer = MarkdownWriter()
file_1 = File(html_writer)
file_2 = File(markdown_writer)
file_1.write_title("Hello, World!")
file_2.write_title("Hello, World!")
print(file_1.content)
print(file_2.content)
# <h1>Hello, World!</h1>
# # Hello, World!
