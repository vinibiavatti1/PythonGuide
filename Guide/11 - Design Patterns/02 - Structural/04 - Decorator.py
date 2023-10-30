"""
Decorator design pattern

* Book: GOF
* Decorator is a structural design pattern that lets you attach new behaviors
  to objects by placing these objects inside special wrapper objects that
  contain the behaviors
* 'Wrapper' is the alternative nickname for the Decorator pattern that clearly
  expresses the main idea of the pattern
"""
import base64
from abc import ABC, abstractmethod


# Abstract data writer
class AbstractDataWriter(ABC):

    @abstractmethod
    def write(self, data):
        pass


# Concrete data writer
class DataWriter(AbstractDataWriter):

    def write(self, data):
        print(data)


# Decorator to change data
class Base64Decorator(AbstractDataWriter):

    def __init__(self, data_writer):
        self._data_writer = data_writer

    def write(self, data):
        bin_data = data.encode('ascii')
        encoded = base64.b64encode(bin_data)
        self._data_writer.write(encoded)


# Algorithm
data_writer = DataWriter()
data_writer = Base64Decorator(data_writer)
data_writer.write('test')
# b'dGVzdA=='
