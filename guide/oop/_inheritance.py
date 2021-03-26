"""
Inheritance

* Inheritance allows us to define a class that inherits all the methods and
  properties from another class.
* Parent class is the class being inherited from, also called base class.
* Child class is the class that inherits from another class, also called
  derived class.
* The base classes are defined in the () togueter the name of the class

Syntax: class Name(base_classes...):

* Caelum: https://www.caelum.com.br/apostila-python-orientacao-a-objetos/
          heranca-multipla-e-interfaces#problema-do-diamante
"""


# Class with just object as the super class
# Client1(object):
class Client1:
    pass


# Class with just object as the super class, other way
# Client1(object):
class Client2():
    pass


# Class with base class and object
class Client3(Client2):
    pass


# Class variables are not shared with child
class Person():
    version: 1


class Client4(Person):
    pass


# print(Client4.version) # AttributeError: type object 'Client4'
# has no attribute 'version'

# Shared properties
class Person1():
    def __init__(self):
        self.name = 'Vini'


class Client5(Person1):
    pass


client = Client5()
print(client.name)  # Vini


# Shared methods
class Person5():
    def action(self):
        print('Hi')


class Client9(Person5):
    pass


client = Client9()
client.action()  # Hi


# Shared init
class Person2():
    def __init__(self, name):
        self.name = name


class Client6(Person2):
    pass


client = Client6('Vini')
print(client.name)  # Vini


# Override init
class Person3():
    def __init__(self, name):
        self.name = name


class Client7(Person3):
    def __init__(self):
        self.name = 'Vini'


client = Client7()
print(client.name)  # Vini


# Call parent class init using super() (RECOMENDED)
class Person4():
    def __init__(self, name):
        self.name = name


class Client8(Person4):
    def __init__(self, name):
        # super without parameters means super(Client8, self)
        super().__init__(name)


client = Client8('Vini')
print(client.name)  # Vini


# Call parent class init using class name
class Person6():
    def __init__(self, name):
        self.name = name


class Client10(Person6):
    def __init__(self, name):
        Person6.__init__(self, name)


client = Client10('Vini')
print(client.name)  # Vini


# Multi inheritance
class Animal():
    def __init__(self):
        self.planet = 'World'


class Flying():
    def __init__(self):
        self.wings = True


class Bird(Animal, Flying):
    pass


bird = Bird()
print(bird.planet)  # World
# print(bird.wings) # Error. Just the first __init__ is called. Use the super
