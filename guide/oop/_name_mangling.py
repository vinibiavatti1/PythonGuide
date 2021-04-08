"""
Name Mangling

* This concept is used for private attributes and methods inside a class, to
  change the name of these resources automatically
* It is used to prevent easy access to private resources
* For any resource inside a class that uses the "__" dunder as prefix, Python
  will change this char to "_<class>__"
* NOTE: Calling private resources with Name Mangling is not recommended. The
  access needs to be done by properties
"""


###############################################################################
# Name mangling
###############################################################################


# Define private attribute and method inside a class
# * To define these resources as private, we have to use the "__" dunder
# * NOTE: Any resource with "__" as prefix will be replaces with the name class
class Client:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def __full_name(self):
        return f'{self.__name} {self.__surname}'


# Check the real name of these resources
# * To check the available resources in the class, we can use the dir()
#   function
# * All of the private resources was replaced with the name class as prefix
# * NOTE: It can be accessed by name mangling, but it is not recommended!
client = Client('Vini', 'Biavatti')
print(dir(client))
# ['_Client__full_name', '_Client__name', '_Client__surname', ...]


# Check the Python replacement inside a class
# * To check the real call in Python call, we can generate Attribute error
#   inside a class
class Customer:
    def __init__(self, name):
        self.__name = name
        del self.__name     # Removed the attribute
        print(self.__name)  # Will generate AttributeError


# Call the class to check the AttributeError
# * We will instantiate the class to check the real call of the attribute
# * The name for the attribute will contains the name of the class
"""
customer = Customer('Vini')

AttributeError: 'Customer' object has no attribute '_Customer__name'
"""


# Define the private resource of other class inside a class
# * To check the name mangling happening again, we can try to access some
#   private resource of some class inside in other class
# * NOTE: The name mangling will put the class name of the current class,
#   independent if the object is from other class
class Car:
    def set_proprietary(self, client):
        print(client.__name)


# Access the private resource of other class inside a class
# * In this situation, the AttributeError will be generated because the dunder
#   will be replaced with the current class name "Car", not the real class of
#   the object "Client"
"""
car = Car()
car.set_proprietary(client)

'Client' object has no attribute '_Car__name'
"""
