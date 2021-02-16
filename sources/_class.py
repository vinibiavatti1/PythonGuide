"""
Class examples

* Python is an object oriented programming language.
* Almost everything in Python is an object, with its properties and methods.
* A Class is like an object constructor, or a "blueprint" for creating objects.
* To create a class, use the keyword class.
"""
# Define class
class Client1:
    pass
class Client2(): # Used for extensions
    pass

# Create instance
client = Client1() # New object

##############################################
# Class scope (static)                       #
##############################################

# Class variables (static)
class Client3:
    name = 'Vini' # Class variable shared in all instances of the class (static)

# Access class variable
print(Client3.name) # Vini

# Class methods (static)
class Client4:
    @classmethod # Decorator to define this method as class method
    def prt(cls):
        print('Vini')

# Access class methods
print(Client4.prt()) # Vini

##############################################
# Instance scope (object)                    #
##############################################

# Init (Constructor)
class Client5:
    def __init__(self, name): # Called when create new object of this class (aka Contructor)
        self._name = name # Used _ to define it is a private property

# Access init (constructor)
client = Client5('Vini') # Constructor

# Instance variables (properties)
class Client6:
    def __init__(self):
        self._name = 'Vini' # Property. Unique for each instance of the class

# Instance Methods
class Client7:
    def set_name(self, name): # Self as first parameter always for instance methods
        self._name = name
c = Client7()
c.set_name('Vini')

##############################################
# WARNINGS                                   #
##############################################
# CAUTION
# NOTE: If you access the class variable from the instance to set a new value using normal way, 
# the class variable will not be changed, as consequence a new variable will be create for that 
# instance
class Car:
    whells = 4
car1 = Car()
car1.whells = 3 # NOT change the class variable. It created a new variable in instance
print(car1.whells) # 3 (new property)
print(car1.__class__.whells) # 4
print(Car.whells) # 4
