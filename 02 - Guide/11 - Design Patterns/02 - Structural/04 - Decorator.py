"""
Decorator

* The Decorator pattern is a structural pattern that allows behavior to be
  added to individual objects, either statically or dynamically, without
  affecting the behavior of other objects from the same class.
* It is a flexible alternative to subclassing for extending functionality.
"""


###############################################################################
# Decorator
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Writer
# * Abstract base class for all writers.
class Writer(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        pass


# Text Writer
# * Concrete implementation of the Writer interface for plain text.
class TextWriter(Writer):
    def write(self, data: str) -> None:
        print(data)


# HTML Writer Decorator
# * This is a decorator that adds HTML tags to the output of the writer.
# * Note that it serves as a wrapper around the existing writer.
class HTMLWriterDecorator(Writer):
    def __init__(self, writer: Writer) -> None:
        self.writer = writer

    def write(self, data: str) -> None:
        html_data = f"<p>{data}</p>"
        self.writer.write(html_data)


# Testing
# * We will test the decorator by using it to wrap a text writer.
# * Note that we can "decorate" the text writer with the html writer, to
#   enhance the output data
text_writer = TextWriter()
html_writer = HTMLWriterDecorator(text_writer)
html_writer.write("Hello, World!")
# <p>Hello, World!</p>
