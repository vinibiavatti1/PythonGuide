"""
Mixins

* Mixins are classes with shared functionalities that can be inherited by other
  classes
* Mixin classes commonly dont have properties, or have only private properties
  without a constructor
* The main difference of interface (or ABC) is that mixins have the methods
  already implemented
"""


###############################################################################
# Defining a mixin class
###############################################################################


# Defining a Mixin class
# * In the example below, we will create a mixin class with JSON
#   functionalities
# * The class below can be inherited by other classes to add these JSON
#   functions
# * By convention, mixin classes have the "Mixin" suffix in the name
class JSONMixin:

    def to_json(self):
        import json
        return json.dumps(self.__dict__)


# Defining a child class
# * Now we are going to define another class only to use multiple inheritance
#   for the next examples
class Person:

    def __init__(self, name):
        self.name = name


# Defining a class that inherits the mixin class
# * Now we are going to define a class that will inherit the mixin class
# * NOTE: The mixin base classes must be set in front of the other classes that
#   the child class will inherit, to ensure the correct MRO (Method Resolution
#   Order)
class Employee(JSONMixin, Person):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company


# Calling the mixin method
# * A new instance of Employee class will be created and the mixin method will
#   be called to transform the object into a JSON string
x = Employee('John', 'Google')
print(x.to_json())
# {"name": "John", "company": "Google"}
