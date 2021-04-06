"""
Attributes

* Attributes are data (information) present inside the class or the object
* There are two kinds of attributes for a Python class:
  * 1. Class Attributes: Are attributes which are owned by the class
  * 2. Instance Attributes: Are attributes which are owned by the object
"""


###############################################################################
# Instance attributes
###############################################################################


# Define the instance attributes
# * To define this kind of attributes, you must define it inside a class
#   method, usually inside the constructor (__init__)
# * This kind of attribute will have the value defined by the object, not the
#   class (each object will have a different value for the attribute)
# * NOTE: To make a attribute being private, you can use dunder "__"
# * NOTE: Private attributes have the name changed with the class name as
#   prefix to avoid access to this (Name mangling)
# * NOTE: To access the private attribute, the best way is to define this
#   attribute as a property (check _properties.py file)
class Client:
    def __init__(self, name, surname):
        self.name = name          # public
        self.__surname = surname  # private


# Access the instance attributes
# * To access the public attribute, you can just access it
# * To access the private attribute, you can define this attribute as a
#   property, or access by name mangling (not recommended)
client1 = Client('Vini', 'Biavatti')
client2 = Client('Ana', 'Almeida')
print(client1.name, client2.name)  # Vini Ana
# print(client1.surname)           # raise Attribute error


###############################################################################
# Class attributes
###############################################################################


# Define the class attributes
# * To define this kind of attributes, you must define it inside the class only
# * This kind of attribute will have the value defined by the class, not the
#   object (every object will have the same value for this attribute)
# * NOTE: You cannot make a class attribute as private
# * NOTE. In other programming languages, this kind of attribute is called by
#   static attribute
class Product:
    tax = 0.05

    def __init__(self, name, value):
        self.name = name
        self.value = value + (value * Product.tax)


# Access the class attributes
# * To access the public attribute, you can just access it
# * To access the private attribute, you can define this attribute as a
#   property, or access by name mangling (not recommended)
product1 = Product('Book', 50)
print(product1.name, product1.value, Product.tax, sep=', ')
# Book, 52.5, 0.05 (Access by the class)
