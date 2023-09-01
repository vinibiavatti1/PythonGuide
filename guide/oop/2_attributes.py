"""
Attributes

* Classes contain attributes, which are variables that hold data (information)
* There are two types of attributes:
  * Class attributes: Are attributes which are owned by the class itself
  * Instance attributes: Are attributes which are owned by the object itself
    (class instance). Each object will have its own instance attributes.
* The instance attributes can be accessed from the `self` parameter inside the
  methods. The `self` parameter is a reference to the current instance of the
  object. In some other languages, this is called by `this` keyword
"""


###############################################################################
# Instance Attributes
###############################################################################


# Defining instance attributes
# * The instance attributes must be defined inside the class methods
# * In the example below, we are defining some attributes inside the __init__
#   method.
# * The __init__ method is a special method, which is called when the object is
#   instantiated. This method is also called by constructor.
# * NOTE: Take a look at _constructor.py for more details about the constructor
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate class objects
# * For the class above, the `name` and `age` attributes are required to create
#   an object of Person
# * Below two instances of Person are created. Each one will store its own
#   attributes values
x = Person('John', 36)
y = Person('Jane', 30)


# Getting instance attributes
# * To access data from some object, we can use the dot notation
print(x.name, x.age)
print(y.name, y.age)
# John 36
# Jane 30


# Setting instance attributes
# * The instance attributes can be modified by using the dot notation as well
# * In the example below, we are modifying the `age` attribute of the `x`
#   object to a new value
# * NOTE: Note that the `y` instance didn't change anything since instance
#   attributes are encapsulated for each object
x.age = 40
print(x.name, x.age)
# John 40


# Deleting instance attributes
# * We can delete an instance attribute by using the Python's `del` keyword
# * This will delete the attribute from the object
# * NOTE: If we try to access the attribute after deleting it, we will get an
#   AttributeError
del x.age


###############################################################################
# Class Attributes
###############################################################################


# Defining class attributes
# * The difference between instance and class attributes is that the class
#   attributes are stored in the class level, and not in the object level
# * All objects of a class will have the same class attributes values
# * Class attributes are used to store data that is shared between all objects,
#   like constants, enumerations, etc
class Person:
    legal_age = 18


# Accessing class attributes
# * To access class attributes, we can use the dot notation like we did with
#   instance attributes, but now, we are going to access it from the class
#   itself, not from the object
print(Person.legal_age)
# 18


# Setting class attributes from objects
# * We can also access class attributes from the object itself
# * If there is an attribute with the same name in the object, the instance
#   attribute will be used prior to the class attribute
x = Person()
print(x.legal_age)
# 18
