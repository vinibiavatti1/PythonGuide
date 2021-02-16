"""
Class properties examples

* There are 3 ways to create get and set methods in classes
  * Property methods defined with decorators @property (RECOMENDED)
  * Property methods as normal methods ()
  * Property methods defined with property() function

* There are 3 property methods to manipulate a property
  * Set (Set the value)
  * Get (Get the value)
  * Del (Delete the property)
"""
# Property
class Client1:
    def __init__(self, name):
        self._name = name # property (With '_' to define it as a private property)

# Property methods defined with decorators @property (RECOMENDED)
class Client2:
    def __init__(self, name): # Init method
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @name.deleter
    def name(self):
        del self._name
client = Client2('Vini') # Constructor
print(client.name)       # Get > Vini
client.name = 'Truta'    # Set
print(client.name)       # Get > Truta
del client.name          # Delete
# print(client.name)     # AttributeError

# Property methods as normal methods
class Client3:
    def __init__(self, name): # Init method
        self._name = name
    def get_name(self):       # Get method
        return self._name
    def set_name(self, name): # Set method
        self._name = name
    def del_name(self):       # Del method
        del self._name
client = Client3('Vini')   # Constructor
print(client.get_name())   # Get > Vini
client.set_name('Truta')   # Set
print(client.get_name())   # Get > Truta
client.del_name()          # Delete
# print(client.get_name()) # AttributeError

# Property methods defined with property() function
class Client4:
    def __init__(self, name): # Init method
        self._name = name
    def get_name(self):       # Get method
        return self._name
    def set_name(self, name): # Set method
        self._name = name
    def del_name(self):       # Del method
        del self._name
    name = property(get_name, set_name, del_name, 'Name of client') # Property function (get, set, del, doc)
client = Client4('Vini')   # Constructor
print(client.name)         # Get > Vini
client.name = 'Truta'      # Set
print(client.name)         # Get > Truta
del client.name            # Delete
# print(client.name)       # AttributeError