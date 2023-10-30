"""
Visitor design pattern

* Book: GOF
* Visitor is a behavioral design pattern that lets you separate algorithms from
  the objects on which they operate.
* The Visitor pattern suggests that you place the new behavior into a separate
  class called visitor, instead of trying to integrate it into existing classes
"""
from abc import ABC, abstractmethod


# Person ABC with visitor accept
class Person(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Customer class
class Customer(Person):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def accept(self, visitor):
        visitor.visit_customer(self)


# Employee class
class Employee(Person):
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def accept(self, visitor):
        visitor.visit_person(self)


# Visitor ABC
class Visitor(ABC):
    @abstractmethod
    def visit_customer(self, customer):
        pass

    @abstractmethod
    def visit_person(self, person):
        pass


# Visitor implementation
class XMLExportVisitor(Visitor):
    def visit_customer(self, customer):
        print(f'{customer.name} exported')

    def visit_person(self, person):
        print(f'{person.name} exported')


# Algorithm
lst = [
    Customer('Customer', 'Due'),
    Employee('Employee', 'IT'),
]
visitor = XMLExportVisitor()
for person in lst:
    person.accept(visitor)
# Customer exported
# Employee exported
