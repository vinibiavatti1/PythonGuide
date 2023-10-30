"""
Strategy design pattern

* Strategy is a behavioral design pattern that lets you define a family of
  algorithms, put each of them into a separate class, and make their objects
  interchangeable
* The Strategy pattern suggests that you take a class that does something
  specific in a lot of different ways and extract all of these algorithms into
  separate classes called strategies
"""
from abc import ABC, abstractmethod


# Strategy ABC
class MathOperationStrategy(ABC):
    @abstractmethod
    def evaluate(self, x, y):
        pass


# Concrete Sum Strategy
class SumStrategy(MathOperationStrategy):
    def evaluate(self, x, y):
        return x + y


# Concrete Sub Strategy
class SubStrategy(MathOperationStrategy):
    def evaluate(self, x, y):
        return x - y


# Math operation (contains strategy)
class MathOperation():
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, x, y):
        return self.strategy.evaluate(x, y)


# Algorithm
sum_operation = MathOperation(SumStrategy())
sub_operation = MathOperation(SubStrategy())
print(sum_operation.execute(6, 4))  # 10
print(sub_operation.execute(6, 4))  # 2
