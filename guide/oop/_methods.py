"""
Methods

* Methods are functions inside some class
* There are four kinds of methods:
  * 1. Instance methods (self)
  * 2. Class methods (cls)
  * 3. Static methods
  * 4. Magic methods (dunder)
"""


###############################################################################
# Instance methods
###############################################################################


# Define instance method
# * Instace methods are called by the instance (object) created from the class
# * This kind of method has as the first parameter the self (instance)
# * NOTE: Private methods have as prefix the dunder "__" signature
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def price(self, discount=0):  # public method
        return self.__price - discount

    def __reset_price(self):  # private method
        self.__price = 0


# Access instance methods
# * The public method is allowed to be accessed
# * The private method is not allowed (Just with name mangling)
product = Product('pencil', 7.99)
print(product.price(1))  # 6.99
# product.__reset_price()  Attribute error
product._Product__reset_price()  # Name mangling (Access not recommended)


###############################################################################
# Class methods
###############################################################################


# Define class method
# * Class methods are called by the class
# * It needs to be decorated with @classmethod decorator
# * This kind of method has as the first parameter the cls (class)
# * Class methods are usually used to create other constructors for the class,
#   methods that use the class attributes, etc...
class Math:
    pi = 3.1415  # class attribute

    @classmethod
    def get_pi(cls):  # class method
        return cls.pi


# Access class methods
# * The class methods must be accessed by the class, not the instance
print(Math.pi)
# 3.1415


###############################################################################
# Static methods
###############################################################################


# Define static method
# * Static methods are called by the class
# * It needs to be decorated with @staticmethod decorator
# * This kind of method has no pre-established first parameter
# * Static methods are usually used to create utility methods
class Calculator:
    @staticmethod
    def sum(x, y):  # static method
        return x + y


# Access static methods
# * The static methods must be accessed by the class, not the instance
print(Calculator.sum(4, 9))
# 13


###############################################################################
# Magic methods
###############################################################################


# Define magic method
# * Magic methods are a special kind of methods that is called by some specific
#   situation
# * It needs to start and and with dunder "__"
# * It is no recommended to create a inexistent magic method, just use the
#   already defined in Python
# * NOTE: Check _magic_methods.py for more details
class Magic:
    def __init__(self, value):  # Magic method to construct the object
        self.value = value

    def __gt__(self, other):  # Magic method to work with > operator
        return self.value > other

    def __repr__(self):  # Magic method to work with repr() function
        return f'Value is: {self.value}'


# Access magic methods
# * The magic methods are called by some specific situation
magic = Magic(5)
print(magic > 10, magic > 3, repr(magic), sep=', ')
# False, True, Value is: 5
