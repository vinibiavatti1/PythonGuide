"""
Singleton

* The Singleton pattern ensures that a class has only one instance and provides
  a global point of access to it.
* This is useful when exactly one object is needed to coordinate actions across
  the system.
* In Python, we can implement it using metaclasses or decorators.
"""


###############################################################################
# Singleton (Metaclass)
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from typing import Any
from functools import wraps


# Singleton Metaclass
# * We will create a metaclass that overrides the `__call__` method to manage
#   instance creation and ensure only one instance exists.
class SingletonMeta(type):
    instances: dict[type, Any] = {}
    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


# Service Manager
# * Now, we will create a class that must be singleton.
# * To enable this behavior, we will set the metaclass to `SingletonMeta`.
class ServiceManager(metaclass=SingletonMeta):
    ...


# Testing
# * Since the ServiceManager is a singleton, all calls to it will return the
#   same instance.
service_1 = ServiceManager()
service_2 = ServiceManager()
print(id(service_1) == id(service_2))
# True


###############################################################################
# Singleton (Decorator)
###############################################################################


# Singleton Decorator
# * We can also use a decorator to handle singleton classes.
# * The decorator will set the instance to the target class if it doesn't
#   exist.
def singleton(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not hasattr(cls, '__instance__'):
            setattr(cls, '__instance__', cls(*args, **kwargs))
        return getattr(cls, '__instance__')
    return wrapper


# Service Manager
# * Now, we will create a class that must be singleton.
# * To enable this behavior, we will decorate this class with the singleton
#   decorator.
@singleton
class ServiceManager:
    ...


# Testing
# * Since the ServiceManager is a singleton, all calls to it will return the
#   same instance.
service_1 = ServiceManager()
service_2 = ServiceManager()
print(id(service_1) == id(service_2))
# True
