"""
Classes and Constructors

* Classes provide a means of bundling data and functionality together
* Constructors are special methods that are called when an object is created
* Creating a new class creates a new type of object, allowing new instances of
  this type to be made
* A class is like a template that can be used to create objects.
* Class is a collection of related attributes and methods that try to
  represent a real-world situation. This idea of putting data and functions
  together in a class is central to the concept of object-oriented
  programming (OOP)
* NOTE: Take a look at _class_template.py file to see a template for a class
* To create a class, use the keyword class.
* Syntaxes to define classes:
###############################################################################
Syntax                           Description
###############################################################################
class <name>:                    Define a class
class <name>():                  Define a class
class <name>(<bases>)            Define a child class
class <name>(metaclass=<meta>):  Define a class with other metaclass
###############################################################################
* NOTE: for child and metaclass documentation, take a look at _inheritance.py
  and _metaclass.py files
"""


###############################################################################
# Defining Classes
###############################################################################


# Defining a class
# * To define some class, the "class" keyword can be used
# * The class below is empty, i.e., it does not have any attribute or method
class Person:
    pass


# Creating an instance of the class
# * To create an instance of the class, we can just call the class
# * By calling the class, a new object will be created
x = Person()
print('Type:', type(x))
print('Address:', id(x))
# Type: <class '__main__.Person'>
# Address: 2885317808016


# Creating other instance of the class
# * The same way as above can be used to create other instances of the class
# * Each instance will be a different object, with different memory address
y = Person()
print('Type:', type(y))
print('Address:', id(y))
# Type: <class '__main__.Person'>
# Address: 2137523800272


###############################################################################
# Class Constructor
###############################################################################


# Defining a class with an empty constructor
# * To define a class with constructor, the "__init__" method can be used. This
#   method will be called when the class is instantiated
# * The constructor method is used to define the the data that will be used by
#   the instance
# * In the example below, the class has an empty constructor, so that no
#   arguments are necessary to create an instance of this class
# * The "self" parameter is used to reference the instance itself
class Person:

    def __init__(self):
        ...


# Defining a class with a constructor
# * Now, the class below requires some data (name) to create a new instance
# * When creating a new instance of Person, the name must be set and this name
#   will be attached to the instance
class Person:

    def __init__(self, name):
        self.name = name


# Creating an instance of the class
# * To create an instance of the class with a constructor, we can just call the
#   class with the required data
x = Person('John')
print(x.name)
# John
