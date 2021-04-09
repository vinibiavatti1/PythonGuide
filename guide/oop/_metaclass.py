"""
Metaclass

* The class of a class. Class definitions create a class name, a class
  dictionary, and a list of base classes. The metaclass is responsible for
  taking those three arguments and creating the class. Most object oriented
  programming languages provide a default implementation. What makes Python
  special is that it is possible to create custom metaclasses. Most users never
  need this tool, but when the need arises, metaclasses can provide powerful,
  elegant solutions. They have been used for logging attribute access, adding
  thread-safety, tracking object creation, implementing singletons, and many
  other tasks
* By default, classes are constructed using type(). The class body is executed
  in a new namespace and the class name is bound locally to the result of
  type(name, bases, namespace)
* The class creation process can be customized by passing the metaclass keyword
  argument in the class definition line, or by inheriting from an existing
  class that included such an argument
"""
from datetime import datetime


###############################################################################
# Metaclass
###############################################################################


# Default metaclass
# * By default, classes are constructed using type()
class People(metaclass=type):
    pass


# Create metaclass
# * To create a metaclass, you just need to create a class, and inherits the
#   type metaclass
class Meta(type):
    pass


###############################################################################
# Metaclass examples
###############################################################################


# Creating a metaclass
# * This class will be used as an intermediary class to change some default
#   actions in the class creation process
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances[cls]
        else:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return instance


class DBConnection(metaclass=Singleton):
    pass


# Check the work of the metaclass
# * Both instances will be the same
db1 = DBConnection()
db2 = DBConnection()
print(id(db1) == id(db2))
# True


# Datetime creation metaclass
# * This is an example to create a metaclass that provides the datetime that
#   the class was created
class RegisterTimeType(type):
    def __new__(cls, name, bases, attrs):
        instance = super().__new__(cls, name, bases, attrs)
        instance._creation_time = datetime.now()
        return instance


class Transaction(metaclass=RegisterTimeType):
    pass


# Check the work of the metaclass
# * The class will always has the _creation_time variable
transaction = Transaction()
print(getattr(transaction, '_creation_time'))
# 2021-03-17 20:37:21.760565
