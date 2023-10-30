"""
Flyweight design pattern

* Book: GOF
* Flyweight is a structural design pattern that lets you fit more objects into
  the available amount of RAM by sharing common parts of state between multiple
  objects instead of keeping all of the data in each object
* For more convenient access to various flyweights, you can create a factory
  method that manages a pool of existing flyweight objects
"""
from abc import ABC, abstractmethod


# Sprite class
class Sprite():
    def __init__(self, name, data):
        self.name = name
        self.data = data


# Flyweight factory
class SpriteFactory():
    cache = []

    @classmethod
    def get_sprite(cls, name, data):
        for cached in cls.cache:
            if cached.name == name:
                print(f'[From cache] {cached.name}', end=' ')
                return cached
        print(f'[Stored] {name}')
        sprite = Sprite(name, data)
        cls.cache.append(sprite)
        return sprite


# Algorithm
tree = SpriteFactory.get_sprite('tree', '892732713')   # [Stored] tree
car = SpriteFactory.get_sprite('car', '593895832')     # [Stored] car
tree2 = SpriteFactory.get_sprite('tree', '892732713')  # [From cache] tree
