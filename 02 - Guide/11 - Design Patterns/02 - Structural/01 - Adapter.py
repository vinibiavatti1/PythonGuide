"""
Adapter

* The adapter is a structural design pattern that allows incompatible
  interfaces to work together.
* It acts as a bridge between two incompatible interfaces, allowing them to
  communicate.
"""


###############################################################################
# Adapter
###############################################################################


# Text Writer
# * This class is responsible for writing text data.
# * Since this writer doesn't support byte data, we need an adapter.
class TextWriter:
    def write_text(self, data: str) -> None:
        print(data)


# Adapter
# * The adapter allows the TextWriter to accept byte data.
# * Then, it converts the byte data to text before passing it to the
#   TextWriter.
class ByteToTextWriterAdapter:
    def __init__(self, adaptee: TextWriter) -> None:
        self.adaptee = adaptee

    def write_bytes(self, data: bytes) -> None:
        self.adaptee.write_text(data.decode('utf-8'))


# Testing
# * We will create instances of the TextWriter and the adapter, then test the
#   adapter.
# * Note that the adapter allows us to use the TextWriter with byte data.
text_writer = TextWriter()
byte_adapter = ByteToTextWriterAdapter(text_writer)
byte_adapter.write_bytes(b"Hello, World!")
# Hello, World!
