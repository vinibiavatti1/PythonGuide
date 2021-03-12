"""
Chain of Responsibility design pattern

* Book: GOF
* Chain of Responsibility is a behavioral design pattern that lets you pass
  requests along a chain of handlers. Upon receiving a request, each handler
  decides either to process the request or to pass it to the next handler in
  the chain
* Like many other behavioral design patterns, the Chain of Responsibility
  relies on transforming particular behaviors into stand-alone objects called
  handlers. In our case, each check should be extracted to its own class with a
  single method that performs the check. The request, along with its data, is
  passed to this method as an argument
"""
from abc import ABC, abstractmethod


# Processor ABC
class Processor(ABC):
    @abstractmethod
    def process(self, data):
        pass


# Root processor
class NumberProcessor:
    def __init__(self):
        self.next_processor = NegativeProcessor()

    def process(self, data):
        if self.next_processor is not None:
            self.next_processor.process(data)


# Negative number processor
class NegativeProcessor(NumberProcessor):
    def __init__(self):
        self.next_processor = ZeroProcessor()

    def process(self, data):
        if data < 0:
            print('[NegativeProcessor] Number processed!')
        elif self.next_processor is not None:
            self.next_processor.process(data)


# Zero number processor
class ZeroProcessor(NumberProcessor):
    def __init__(self):
        self.next_processor = PositiveProcessor()

    def process(self, data):
        if data == 0:
            print('[ZeroProcessor] Number processed!')
        elif self.next_processor is not None:
            self.next_processor.process(data)


# Positive number processor
class PositiveProcessor(NumberProcessor):
    def __init__(self):
        self.next_processor = None

    def process(self, data):
        if data > 0:
            print('[PositiveProcessor] Number processed!')
        elif self.next_processor is not None:
            self.next_processor.process(data)


# Algorithm
processor = NumberProcessor()
processor.process(-1)  # [NegativeProcessor] Number processed!
processor.process(0)   # [ZeroProcessor] Number processed!
processor.process(1)   # [PositiveProcessor] Number processed!
