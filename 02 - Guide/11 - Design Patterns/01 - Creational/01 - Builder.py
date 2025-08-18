"""
Builder

* The Builder pattern is a creational design pattern that allows for the
  step-by-step construction of complex objects.
* It separates the construction of a complex object from its representation,
  allowing the same construction process to create different representations.
"""


###############################################################################
# Builder
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from typing import Self


# Model
# * The model is the object that will be built by the builder.
# * The class below represents a simple object with some attributes.
class Person:
    def __init__(self, key: int, name: str) -> None:
        self.key = key
        self.name = name


# Builder
# * The builder is responsible for constructing the object.
# * It provides the methods implementation for constructing the object step by
#   step.
class PersonBuilder:
    def __init__(self):
        self.person = Person(0, "")

    def with_key(self, key: int) -> Self:
        self.person.key = key
        return self

    def with_name(self, name: str) -> Self:
        self.person.name = name
        return self

    def build(self) -> Person:
        return self.person


# Director
# * The director is responsible for managing the construction process.
# * It uses a builder to construct the object step by step.
# * The director implements the build function to construct a person object.
# * Usually, the director is not necessary, but it can be useful when we need
#   to have different representations of the same object.
class PersonDirector:
    def __init__(self, builder: PersonBuilder) -> None:
        self.builder = builder

    def build(self, key: int, name: str) -> Person:
        self.builder \
            .with_key(key) \
            .with_name(name)
        return self.builder.build()


# Testing
# * Now, we will demonstrate the usage of the builder and director.
builder = PersonBuilder()
director = PersonDirector(builder)
person = director.build(1, "John")
print(person.key, person.name)
# 1 John
