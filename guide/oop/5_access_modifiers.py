"""
Access Modifiers

* Python doesn't enforce strict access modifiers, it relies on naming
  conventions to suggest the intended visibility and access level of class
  attributes and methods
* There are three types of access modifiers (public, protected and private):
###############################################################################
Access Modifier  Accessibility                     Prefix
###############################################################################
Public           internal, external and inherited  attr, method
Protected        internal and inherited            _attr, _method
Private          internal only                     __attr, __method
###############################################################################
"""


###############################################################################
# Access Modifiers
###############################################################################


# Defining a class with instance attributes
# * Here we are defining a class with three instance attributes with different
#   access modifiers
# * The `x` attribute is public, the `_y` attribute is protected and the `__z`
#   attribute is private
class MyClass:

    def __init__(self, x, y, z) -> None:
        self.x = x  # public
        self._y = y  # protected
        self.__z = z  # private


# Defining a class with class attributes
# * Same as the previous example, but now we are defining class attributes
class MyClass:

    x = 1  # public
    _y = 2  # protected
    __z = 3  # private


# Defining a class with instance methods
# * Same as the previous example, but now we are defining instance methods
class MyClass:

    def x(self):
        """public"""

    def _y(self):
        """protected"""

    def __z(self):
        """private"""


# Defining a class with class methods
# * Same as the previous example, but now we are defining class methods
class MyClass:

    @classmethod
    def x(cls):
        """public"""

    @classmethod
    def _y(cls):
        """protected"""

    @classmethod
    def __z(cls):
        """private"""


# Defining a class with static methods
# * Same as the previous example, but now we are defining static methods
class MyClass:

    @staticmethod
    def x():
        """public"""

    @staticmethod
    def _y():
        """protected"""

    @staticmethod
    def __z():
        """private"""


###############################################################################
# Name Mangling
###############################################################################


# Defining private attributes and methods inside a class
# * Name Mangling is the name of the concept used for private attributes, on
#   which Python changes the name of these resources automatically to prevent
#   easy access to private resources
# * NOTE: Python doesn't remove the direct access to private resources, it only
#   changes the name of these resources to make it harder to access them
# * For any resource inside a class that uses the "__" dunder as prefix, Python
#   will change this char to "_<class>__<resource>"
# * In the example below, we are going to define a new class with private
#   resources, to show the name mangling in action
class Person:

    __legal_age = 18  # private class attribute

    def __init__(self, name):
        self.__name = name  # private instance attribute

    def __say(self):  # private instance method
        print('Hi!')


# Checking the real name of these resources
# * Below we are checking the real name of the private resources
# * The dir() function will return a list with all the resources available in
#   the object
x = Person('John')
print(dir(x))
# ['_Person__legal_age', '_Person__name', '_Person__say', ...]


# Accessing/Calling private resources
# * We can use the real name to access/call the private resources
# * The access to these resources is not recommended since they are private in
#   concept, but it is still possible using the correct name
print(Person._Person__legal_age)
print(x._Person__name)
x._Person__say()
# 18
# John
# Hi!
