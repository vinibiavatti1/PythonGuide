"""
Descriptors

* Python descriptors are objects that implement a method of the descriptor
  protocol, giving them special behavior when they are accessed as attributes
  of other objects.
* They act like a proxy, controlling and intercepting get, set, and delete
  operations.

* The methods of the descriptor protocol are:
###############################################################################
Method                           Description
###############################################################################
__set_name__(self, owner, name)  Used to set the name of the attribute
__get__(self, instance, owner)   Called for attribute access
__set__(self, instance, value)   Called for attribute assignment
__delete__(self, instance)       Called for attribute deletion.
###############################################################################

* The `__set_name__` method is used to set the name of the attribute being
  managed by the descriptor. Without this method, the descriptor would not
  know which attribute it is managing. The "name" parameter is the name of
  the attribute as it appears in the owner class.
* If a descriptor implements just `__get__()`, it's a non-data descriptor. If
  it implements `__set__()` or `__delete__()`, it's a data descriptor.
* Common examples include `@property`, `@staticmethod`, and `@classmethod`.
"""


###############################################################################
# Signature
###############################################################################


# Importing necessary modules
# * Since we will be using type hints to clearify the descriptors signature,
#   we need to import some types from the typing module.
from typing import Any, Self


# Defining a standard descriptor signature
# * This is a standard descriptor class that implements the descriptor protocol
class Descriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        ...

    def __get__(self, instance: Self, owner: type) -> Any:
        ...

    def __set__(self, instance: Self, value: Any) -> None:
        ...

    def __delete__(self, instance: Self) -> None:
        ...


###############################################################################
# Implementation
###############################################################################


# Defining a descriptor
# * Descriptors are created using classes that implement one or more methods of
#   the descriptor protocol.
# * Descriptors can be used to manage attribute access, validation, and
#   transformation.
# * They can be used to create properties, manage access control, or implement
#   caching mechanisms.
# * Note that we have to define the `__set_name__` method to set the name of
#   the attribute being managed. We need to use a prefix to avoid name clashes
#   and infinite recursion.
class Descriptor:
    def __set_name__(self, owner, name):
        print(f'Name: {name}')
        self.name = f'_{name}'

    def __get__(self, instance, owner) -> Any:
        print('Method __get__ called')
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print('Method __set__ called')
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        print('Method __delete__ called')
        delattr(instance, self.name)


# Using the descriptor
# * Now, we can use the descriptor in a class to manage attribute access
# * The descriptor will be used to control access to the 'name' attribute
# * Note that we must set the name attribute as a class variable to define
#   the descriptor. When the instance is created, the descriptor will be
#   used to manage access to the 'name' attribute.
class Person:
    name = Descriptor()

    def __init__(self, name):
        self.name = name


# Testing the descriptor
# * Now, when managing the 'name' attribute, the descriptor will be used
# * Note below that the descriptor will print messages
person = Person('John Doe')
person.name = 'John'
person.name
del person.name
# Name: name
# Method __set__ called
# Method __get__ called
# Method __delete__ called
