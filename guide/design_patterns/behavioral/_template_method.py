"""
Template Method design pattern

* Book: GOF
* Template Method is a behavioral design pattern that defines the skeleton of
  an algorithm in the superclass but lets subclasses override specific steps of
  the algorithm without changing its structure.
* The Template Method pattern suggests that you break down an algorithm into a
  series of steps, turn these steps into methods, and put a series of calls to
  these methods inside a single template method
"""
from abc import ABC, abstractmethod


# Game AI ABC
class GameAI(ABC):
    def execute(self):  # <- Template Method
        self.collect_resources()
        self.build()
        self.attack()

    def collect_resources(self):
        print('Collect resources')

    def build(self):
        print('Build')

    def attack(self):
        print('Attack!')


# Ally AI
class AllyAI(GameAI):
    def attack(self):
        print('Not Attack!')


# Enemy AI
class EnemyAI(GameAI):
    pass


# Gaia AI
class GaiaAI(GameAI):
    def collect_resources(self):
        print('Nothing')

    def build(self):
        print('Nothing')

    def attack(self):
        print('Nothing')


# Algorithm
ally_ai = AllyAI()
enemy_ai = EnemyAI()
gaia_ai = GaiaAI()

ally_ai.execute()
# Collect resources
# Build
# Not Attack!

enemy_ai.execute()
# Collect resources
# Build
# Attack!

gaia_ai.execute()
# Nothing
# Nothing
# Nothing
