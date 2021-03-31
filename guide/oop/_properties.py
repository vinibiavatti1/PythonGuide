"""
Properties

* Properties are special kind of attributes which have getter, setter and
  delete methods
* There are 3 ways to create property methods in classes
  * Property methods defined with decorators @property (RECOMMENDED)
  * Property methods as normal methods ()
  * Property methods defined with property() function
* The underscore as prefix of some attribute indicates that this attribute is
  private (Example: _name), and can have property methods to manipulate its val

There are 3 property methods to manipulate a property:
###############################################################################
Method              Description             Trigger
###############################################################################
Setter              Sets the value          obj.prop = val
Getter              Gets the value          obj.prop
Deleter             Deletes the property    del obj.prop
###############################################################################
"""


###############################################################################
# Property
###############################################################################


# Define a property
# * Properties are defined inside the __init__ method (constructor)
# * NOTE: To make a property being private, you can use dunder "__"
# * NOTE: Private properties have the name changed with the class name as
#   prefix to avoid access to this.
class Person:
    def __init__(self, name, age):
        self.__name = name  # private
        self.age = age      # public


###############################################################################
# Property methods
###############################################################################


# Define property methods (with decorator @) (Recommended)
# * To define property methods it is recommended to use the decorators:
#   @property, @setter, @deleter
class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


# Manipulate properties in instance
# * The access to the properties will be handled by the property methods, not
#   directly to property itself
client = Client('Vini')  # Constructor
print(client.name)       # Call getter
client.name = 'John'     # Call setter
del client.name          # Call deleter
# client.__name          # raise AttributeError


# Define property methods (with property fn) (Old way)
# * To define property methods in a old way you can use the property function,
#   passing as argument the getter, setter and deleater methods
class Customer:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def del_name(self):
        del self.__name

    # Property function (get, set, del, doc)
    name = property(get_name, set_name, del_name, 'Name of client')


# Manipulate properties in instance
# * The access to the properties will be handled by the property methods, not
#   directly to property itself
customer = Customer('Vini')  # Constructor
print(customer.name)         # Call getter
customer.name = 'John'       # Call setter
del customer.name            # Call deleter
# customer.__name            # raise AttributeError
