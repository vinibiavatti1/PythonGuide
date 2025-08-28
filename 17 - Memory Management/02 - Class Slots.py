"""
Class Slots

* Slots are used to restrict the attributes that can be assigned to an object
* It is used to optimize memory usage and performance
* When you define slots in a class, only the attributes defined in the slots
  can be assigned to the object, and the `__dict__` attribute is not created
* Slots are defined by setting the `__slots__` attribute in the class. The
  value of the attribute can be a string, a list of strings, or a tuple of
  strings
* Syntax:
  * class <name>: __slots__ = 'attr1', 'attr2', ...
"""


###############################################################################
# Class Slots
###############################################################################


# Define a class with slots
# * To define slots, we must set the `__slots__` attribute in the class with
#   the attributes that can be assigned to the object
# * When the `__slots__` attribute is defined, the `__dict__` attribute is not
#   created in the object
class Person:
    __slots__ = 'name', 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Assigning a new attribute
# * Since the class uses slots, and the `__dict__` attribute is not created in
#   the object, we cannot assign a new attribute to the object
# * In this examle, we tried to assign a new attribute `profession` to the
#   object, but it raised an AttributeError
"""
x = Person('John', 30)
x.profession = 'Developer'

AttributeError: 'Person' object has no attribute 'profession' and no __dict__
for setting new attributes
"""


# Acessing the __dict__ attribute
# * Since the class uses slots, the `__dict__` attribute is not created in the
#   object
x = Person('John', 30)
print(hasattr(x, '__dict__'))
# False


###############################################################################
# Weak References
###############################################################################


# Importing weakref module
# * For the next examples, we have to import the `weakref` module to create
#   weak references to objects
import weakref


# Enabling weak references
# * To enable weak references in a class which uses slots, we must set the
#   `__weakref__` attribute in the slots, otherwise, the module will not be
#   able to create weak references to the object
class Person:
    __slots__ = 'name', 'age', '__weakref__'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating a weak reference
# * Now that the `__weakref__` attribute is set in the slots, the routine will
#   be able to define the `__weakref__` attribute in the object
x = Person('John', 30)
y = weakref.ref(x)
print(y)
# <weakref at 0x7f8c5c2b4a70; to 'Person' at 0x7f8c5c2b4b90>
