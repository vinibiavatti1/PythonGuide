"""
Methods

* Methods are functions inside a class
* There are four kinds of methods:
  * 1. Instance methods (self)
  * 2. Class methods (cls)
  * 3. Static methods
  * 4. Magic methods (dunder)
* The instance methods always have as the first parameter the self (instance)
* The class methods always have as the first parameter the cls (class)
* The static methods have no pre-established first parameter
* The magic methods are a special kind of methods called in a specific
  situation or methods that belongs to some protocol
"""


###############################################################################
# Instance Methods
###############################################################################


# Defining an instance method
# * Methods are used to define behaviors for the class objects, and to access
#   and manipulate object attributes
# * Since we are talking about methods, we need to define them inside a class
# * The instance methods are called by the instance (object) created from the
#   class
# * This kind of method has as the first parameter the self (instance)
# * NOTE: Take a look at _access_methods.py to check how to define the
#   accessibility of methods
class Person:

    def __init__(self, name):
        self.name = name

    def say(self, word):
        print(f'{self.name} says {word}')


# Calling an instance method
# * To call an instance method, we first need to create an instance (object) of
#   the class, and call the method from the instance
x = Person('John')
x.say('hello')
# John says hello


###############################################################################
# Class Methods
###############################################################################


# Defining a class method
# * To define a class method, we need to use the `@classmethod` decorator
# * This kind of method has as the first parameter the cls (class)
# * Class methods are usually used to create other constructors for the class,
#   methods that use the class attributes, etc...
# * In the example below, we are creating a class method that will be used as a
#   alternative constructor
class Person:

    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls):
        return cls('Unknown')


# Calling a class method
# * We will create two instances of the Person class, one using the default
#   constructor, and another using the class method
# * NOTE: In this example, we are using the class method as an alternative
#   constructor, however class methods can be used for other purposes too
x = Person('John')
y = Person.create()
print(x.name, y.name)
# John Unknown


###############################################################################
# Static Methods
###############################################################################


# Defining a static method
# * To define a static method, we need to use the `@staticmethod` decorator
# * This kind of method has no pre-established first parameter
# * Static methods are usually used to create utility methods. They are similar
#   to class methods, the unique difference is that static methods don't have
#   the cls parameter
class Math:

    @staticmethod
    def sum(x, y):
        return x + y


# Calling a static method
# * We will call the static method from the class, not from the instance
print(Math.sum(4, 9))
# 13


###############################################################################
# Magic Methods
###############################################################################


# Defining some magic methods
# * Magic methods are a special kind of methods that is called by some specific
#   situation
# * It uses the dunder (double underscore) syntax "__" as prefix and suffix
# * It is not recommended to create normal methods with dunder syntax, since
#   this pattern is used for magic methods
# * NOTE: Check _magic_methods.py for more details
class Unit:

    def __init__(self, value):  # Magic method (constructor)
        self.value = value

    def __gt__(self, other):  # Magic method (greater than ">")
        return self.value > other

    def __repr__(self):  # Magic method (representation string)
        return f'Value is: {self.value}'


# Calling some magic methods
# * The magic methods are called by some specific situation, not directly
# * For the example above, the magic methods are called by the following cases:
#   * __init__(): When the object is created
#   * __gt__(): When the object is compared with the greater than operator ">"
#   * __repr__(): When the object is called by the repr() function
x = Unit(5)
print(x > 10, x > 3, repr(x), sep=', ')
# False, True, Value is: 5


###############################################################################
# Use Case
###############################################################################


# Defining a class with different methods
# * In this case, we are going to define a class with different methods in a
#   real use case
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def create_on_sale(cls, name, price, discount):
        new_price = cls.calc_sale_price(price, discount)
        return cls(name, new_price)

    @staticmethod
    def calc_sale_price(price, discount):
        return price - discount

    def increase_price(self, amount):
        self.price += amount

    def __repr__(self):
        return f'Product: {self.name}, Price: {self.price}'


# Creating some products
# * We will create some products using the constructors, and we will manipulate
#   these products using the methods
# * NOTE: Note that we didn't need to use the `repr()` function to use the
#   result of the magic method since the print() function already does that
product_1 = Product('Pencil', 1.99)
product_1.increase_price(0.50)
product_2 = Product.create_on_sale('Pen', 3.99, 1.00)
print(product_1, product_2, sep='\n')
# Product: Pencil, Price: 2.49
# Product: Pen, Price: 2.99
