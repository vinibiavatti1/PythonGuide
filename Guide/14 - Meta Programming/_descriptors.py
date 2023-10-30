"""
Descriptors

* Descriptors are Python objects that implement a method of the descriptor
  protocol, which gives you the ability to create objects that have special
  behavior when they're accessed as attributes of other objects
* The methods of the descriptor protocol are:
  * __get__(self, obj, type=None) -> object
  * __set__(self, obj, value) -> None
  * __delete__(self, obj) -> None
* If your descriptor implements just .__get__(), then it's said to be a
  non-data descriptor. If it implements .__set__() or .__delete__(), then
  it's said to be a data descriptor
* The descriptor works like a Proxy, controlling the resource that it is
  attached on
* Reference:
  * https://realpython.com/python-descriptors/
"""
import time


###############################################################################
# Create a descriptor
###############################################################################


# Define descriptor
# * The descriptor will be create as a class
# * The parameters of the descriptor methods are:
#   * self: is the instance of the descriptor you're writing.
#   * obj: is the instance of the object your descriptor is attached to
#   * type: is the type of the object the descriptor is attached to
class Descriptor:
    def __init__(self):
        self.value = 10

    def __get__(self, obj, type=None):
        print('Descriptor: get')
        return self.value

    def __set__(self, obj, value):
        print('Descriptor: set')
        self.value = value

    def __delete__(self, obj):
        print('Descriptor: delete')
        del self.value


# Attach descriptor
# * The descriptor will be used in the attributes of some class, to control the
#   access and to print the information
# * NOTE: The descriptor must be set as class variable to the variable, to
#   define to the access of the class that this will be used by a descriptor
class Person:
    name = Descriptor()

    def __init__(self):
        pass


# Test descriptor
# * Now, we can check that the descriptor will control the object it is
#   attached
person = Person()
person.name = 'Vini'
person.name
del person.name
# Descriptor: set_name
# Descriptor: set
# Descriptor: get
# Descriptor: delete


###############################################################################
# Create a descriptor as decorator
###############################################################################


# Define descriptor decorator
# * The magic that transforms your obj.method(*args) call into
#   method(obj, *args) is inside a __get__() implementation of the function
#   object that is a non-data descriptor
# * So, we can create an object that implements the __get__() method and use it
#   as a decorator
# * NOTE: The function will be set in constructor
class MyProperty:
    def __init__(self, function):
        self.function = function

    def __get__(self, obj, type=None):
        print('Getting the property')
        return self.function(obj)


# Decorate method
# * The decorator will be used to decorate some method as a property
class People:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @MyProperty
    def full_name(self):
        return self._name + ' ' + self._surname


# Test decorator
# * The class will be instantiated and the method will be call as attribute
#   access
people = People('Vini', 'Biavatti')
print(people.full_name)
# Getting the property
# Vini Biavatti


###############################################################################
# Examples
###############################################################################


# Lazy property
# * Some properties can take a long time to be processed, so, with descriptors
#   we can store the result and keep the result of the processed function
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.value = None

    def __get__(self, obj, type=None):
        if self.value is None:
            self.value = self.function(obj)
        return self.value


# Decorate with lazy property decorator
# * The method will be decorated with the @LazyProperty
class Customer:
    @LazyProperty
    def data(self):
        time.sleep(1)
        return 'data'


# Call method
# * The descriptor will be called first and check if the data variable is
#   already defined inside descriptor
customer = Customer()
print(customer.data)  # Take time
print(customer.data)  # Fast
print(customer.data)  # Fast


# Private attribute
# * The descriptor can be used to set some attribute as private also
class Private:
    def __init__(self):
        self.value = None

    def __get__(self, obj, type=None):
        raise AttributeError('Private access to attribute')

    def __set__(self, obj, value):
        self.value = value


# Create class with private attribute
# * The private descriptor will be used to block the access to the attribute
# * The descriptor could be created as decorator too
class Bank:
    master_password = Private()

    def __init__(self):
        self.master_password = '12345'


# Try to access the attribute
# * Now, we will try to access that attribute
"""
bank = Bank()
print(bank.master_password)

AttributeError: Private access to attribute
"""
