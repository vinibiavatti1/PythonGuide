"""
Strategy

* The Strategy pattern defines a family of algorithms, encapsulates each one,
  and makes them interchangeable.
* Strategy lets the algorithm vary independently from clients that use it.
* It is a behavioral design pattern that enables selecting an algorithm's
  behavior at runtime.
"""


###############################################################################
# Strategy
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Strategy
# * The Strategy interface declares a method for executing a strategy.
# * The Context uses this interface to call the algorithm defined by Concrete
#   Strategies.
class EvenCheckerStrategy(ABC):
    @abstractmethod
    def is_even(self, number):
        pass


# Arithmetic Strategy
# * The class below is a concrete strategy that implements the strategy
#   interface.
# * This class uses a arithmetic approach to determine if a number is even.
class ArithmeticStrategy(EvenCheckerStrategy):
    def is_even(self, number):
        return number % 2 == 0


# Byte Strategy
# * The class below is a concrete strategy that implements the strategy
#   interface.
# * This class uses a bitwise approach to determine if a number is even.
class ByteStrategy(EvenCheckerStrategy):
    def is_even(self, number):
        return (number & 1) == 0


# Even Checker
# * The class below represents the context that uses the strategy.
# * The algorithm used to determine if a number is even can be changed at
#   runtime.
class EvenChecker:
    def __init__(self, strategy: EvenCheckerStrategy) -> None:
        self.strategy = strategy

    def is_even(self, number: int) -> bool:
        return self.strategy.is_even(number)


# Testing
# * Now, note that we can vary the strategy at runtime.
# * The first strategy that will be used is the arithmetic strategy. Then, we
#   change it to use the byte strategy algorithm.
even_checker = EvenChecker(ArithmeticStrategy())
print(even_checker.is_even(10))  # True
print(even_checker.is_even(11))  # False
even_checker.strategy = ByteStrategy()
print(even_checker.is_even(10))  # True
print(even_checker.is_even(11))  # False
