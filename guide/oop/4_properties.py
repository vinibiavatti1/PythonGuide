"""
Properties

* Properties are special kind of attributes which have getter, setter and
  delete methods
* They are used to control the access to the attributes, and offer a controlled
  way to access and mutate them
* The property methods are not called directly, they are triggered in specific
  cases
* Properties are created by using the `@property` decorator

There are 3 methods that a property can have:
###############################################################################
Method   Description           Trigger
###############################################################################
Setter   Sets the value        obj.prop = val
Getter   Gets the value        obj.prop
Deleter  Deletes the property  del obj.prop
###############################################################################
"""


###############################################################################
# Defining Properties
###############################################################################


# Defining a class with a property (getter)
# * To define an attribute as a property, we need to use the `@property`
#   decorator
# * The property decorator will transform the attribute into a property
# * The decorator will create a getter method for the attribute
# * The setter and deleter methods are optional
# * NOTE: We are using the dunder (double underscore) syntax "__" as prefix to
#   the attribute to make it private (take a look at _access_modifiers.py for
#   more details)
class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('Getter method called')
        return self.__name


# Using the getter method
# * Now, when the attribute is accessed, the getter method will be called
# * Note that the text 'Getter method called' will be printed proving that the
#   getter method was called instead of the attribute
# * We first need to create some instances of the class to access the attribute
#   and see it in action
x = Person('John')
x.name
# Getter method called


# Defining a class with a property (getter, setter and deleter)
# * To create the setter and the deleter, we must use the syntax as a
#   decorator: `@<property_name>.setter` and `@<property_name>.deleter`
# * The setter method is called when the attribute is set (mutated)
# * The deleter method is called when the attribute is deleted by the `del`
# * The getter method is required to allow the setter and deleter methods to be
#   created
class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print('Setter method called')
        self.__name = name

    @name.deleter
    def name(self):
        print('Deleter method called')
        del self.__name


# Using the setter method
# * Now, when the attribute is set, the setter method will be called
# * Note that the text 'Setter method called' will be printed proving that the
#   setter method was called instead of the attribute
x = Person('')
x.name = 'John'
del x.name
# Setter method called
# Deleter method called


# Defining setter and deleter without getter
# * Since the getter is required to create the setter and deleter, we cannot
#   define them without the getter
# * To avoid this, we can simply return "None" in the getter method to disable
#   getting the attribute value
class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return None  # Returning None

    @name.setter
    def name(self, name):
        self.__name = name


###############################################################################
# Use Case
###############################################################################


# Defining a class with properties
# * In this example, we will create a class with properties to control the
#   attributes
# * The properties now have validations to control the attribute values
class Product:

    def __init__(self, name, price, stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            price = 0.00
        self.__price = price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            stock = 0
        self.__stock = stock

    @stock.deleter
    def stock(self):
        self.__stock = 0


# Creating some products
# * We will create a product and manipulate it using the properties
product = Product('Pencil', 1.99, 10)
product.price = -10
del product.stock
print(product.name, product.price, product.stock, sep=', ')
# Pencil, 0.0, 0
