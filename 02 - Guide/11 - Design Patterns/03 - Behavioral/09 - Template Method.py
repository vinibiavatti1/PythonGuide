"""
Template Method

* The Template Method is a behaviora pattern that defines the skeleton of an
  algorithm in a method, deferring some steps to subclasses.
* It lets subclasses redefine certain steps of an algorithm without changing
  the algorithm's structure.
"""


###############################################################################
# Template Method
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Enemy AI
# * The interface defines the skeleton of an algorithm, allowing subclasses to
#   override specific steps without changing the overall structure.
class EnemyAI(ABC):
    @abstractmethod
    def turn(self) -> None:
        pass

    @abstractmethod
    def build_structure(self) -> None:
        pass

    @abstractmethod
    def build_unit(self) -> None:
        pass

    @abstractmethod
    def collect_resource(self) -> None:
        pass


# Base Enemy AI
# * The base class implements the template method and provides default
#   implementations for some steps of the algorithm.
class BaseEnemyAI(EnemyAI):
    def turn(self) -> None:
        self.collect_resource()
        self.build_structure()
        self.build_unit()

    def build_structure(self) -> None:
        print("Structure Built!")

    def build_unit(self) -> None:
        print("Unit Built!")

    def collect_resource(self) -> None:
        print("Gold Collected!")


# Orcs AI
# * The subclasses override the methods to provide their own implementations of
#   the steps in the algorithm.
# * Note that some steps are not overridden, so the base class's implementation
#   will be used.
class OrcsAI(BaseEnemyAI):
    def build_structure(self) -> None:
        print("Orc Structure Built!")

    def build_unit(self) -> None:
        print("Orc Unit Built!")


# Humans AI
# * The human subclass also overrides the methods to provide their own
#   implementations of the steps in the algorithm.
class HumansAI(BaseEnemyAI):
    def build_structure(self) -> None:
        print("Human Structure Built!")

    def collect_resource(self) -> None:
        print("Food Collected!")


# Testing
# * Now, note that the output will vary based on the subclass implementation.
orcs_ai = OrcsAI()
humans_ai = HumansAI()
orcs_ai.turn()
humans_ai.turn()
# Output (Orcs):
# Gold Collected!
# Orc Structure Built!
# Orc Unit Built!
#
# Output (Humans):
# Food Collected!
# Human Structure Built!
# Unit Built!
