"""
Metaclasses

* Metaclasses are a deep and powerful feature of Python that allow you to
  customize class creation and behavior at a fundamental level.
* They are often described as "classes of classes," meaning they define how
  classes themselves behave, rather than instances of those classes.
* In Python, everything is an object, including classes. Classes are instances
  of metaclasses, and the default metaclass in Python is `type`.
* Metaclasses can be used to modify class attributes, enforce coding standards,
  or even implement design patterns like singletons or factories.
* They are defined by inheriting from `type` and overriding methods like
  `__new__` or `__init__`.

* The table below shows the methods that can be overridden in a metaclass:
###############################################################################
Method       Description
###############################################################################
__prepare__  Called to prepare the class namespace (rarely used)
__new__      Called to create a new class object
__init__     Called to initialize the class object
__call__     Called when an instance of the class is created
###############################################################################

* The table below shows the parameters that are used by most of the methods:
###############################################################################
Parameter  Type              Description
###############################################################################
cls        Self              The metaclass itself
name       str               The name of the class being created
bases      tuple[type, ...]  The base classes that the class will inherit from
attrs      dict[str, Any]    A dict of attributes and methods
###############################################################################

* Class creation Lifecycle (call order):
  1. Metaclass.__prepare__
  2. Metaclass.__new__
  3. Metaclass.__init__
* Instance creation Lifecycle:
  1. Metaclass.__call__
  2. Class.__new__
  3. Class.__init__
"""


###############################################################################
# Signature
###############################################################################


# Importing necessary modules
# * Since we will be using type hints to clearify the metaclass signature,
#   we need to import some types from the typing module.
from typing import Any, Self


# Defining a standard metaclass signature
# * A metaclass is defined by inheriting from `type` and overriding the
#   `__new__`, `__init__` and/or `__call__` methods.
# * Usually, the metaclass has the "Meta" suffix in its name.
# * Below we will define a metaclass to show the signature.
class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type, ...],
                    **kwds: Any) -> dict[str, Any]:
        ...

    def __new__(cls, name: str, bases: tuple[type, ...],
                attrs: dict[str, Any]) -> Self:
        ...

    def __init__(cls, name: str, bases: tuple[type, ...],
                 attrs: dict[str, Any]) -> None:
        ...

    def __call__(cls, *args, **kwargs) -> Any:
        ...


###############################################################################
# Methods
###############################################################################


# Defining a metaclass
# * We will define a metaclass called `MyMeta` that inherits from `type`.
# * This metaclass will override all the methods to demonstrate how they
#   are called during the class/instance creation process.
class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        print('Method __prepare__ called')
        return super().__prepare__(name, bases, **kwds)

    def __new__(cls, name, bases, attrs):
        print('Method __new__ called')
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('Method __init__ called')
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print('Method __call__ called')
        return super().__call__(*args, **kwargs)


# Methods calls
# * These methods are called when a new class object is created.
# * The parameters are:
#   * cls: the metaclass itself (usually `MyMeta`).
#   * name: the name of the class being created.
#   * bases: a tuple of base classes that the new class will inherit from.
#   * attrs: a dictionary of attributes and methods defined in the class.
# * Note that the print message in both methods will be executed when
#   the class is defined, not when an instance of the class is created.
# * NOTE: The main difference between `__new__` and `__init__` in a metaclass
#   is that `__new__` is responsible for creating the class object itself,
#   while `__init__` is responsible for initializing the class object after it
#   has been created. After the class object is created by `__new__`,
#   `__init__` cannot change the class object itself, but it can modify its
#   attributes or perform other initialization tasks.
class MyClass(metaclass=MyMeta):
    ...
# Method __prepare__ called
# Method __new__ called
# Method __init__ called


# The __call__ method
# * This method is called when an instance of the class is created.
# * The parameters are:
#   * cls: the metaclass itself (usually `MyMeta`).
#   * *args: positional arguments passed to the class constructor
#   * **kwargs: keyword arguments passed to the class constructor
# * Note that the print message in this method will be executed when
#   an instance of the class is created, not when the class is defined.
x = MyClass()
# Method __call__ called


###############################################################################
# Plugin Registration Example
###############################################################################


# Plugin Registration Example
# * This example shows how to use a metaclass to register plugins in a system.
# * The metaclass will automatically register any class that inherits from it
class PluginMeta(type):
    plugins = []
    def __new__(cls, name, bases, attrs):
        x = super().__new__(cls, name, bases, attrs)
        cls.plugins.append(x)
        return x


# Defining a plugin using the metaclass
# * This class will be automatically registered in the `PluginMeta.plugins`
#   list when it is defined.
class MyPlugin(metaclass=PluginMeta):
    ...


# Check the registered plugins
# * The `MyPlugin` class will be automatically registered in the
#   `PluginMeta.plugins` list when it is defined.
print(PluginMeta.plugins)
# [<class '__main__.MyPlugin'>]


###############################################################################
# Singleton Example
###############################################################################


# Singleton Example
# * This example shows how to use a metaclass to implement the Singleton
#   design pattern, which ensures that a class has only one instance.
# * The metaclass will override the `__call__` method to control the instance
#   creation process and ensure that only one instance is created.
# * Note that the implementation is simplified for demonstration purposes. It
#   will not work as intended for multiple classes using the same metaclass.
class SingletonMeta(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


# Defining a singleton class using the metaclass
# * This class will use the `SingletonMeta` metaclass to ensure that only one
#   instance is created.
class SingletonClass(metaclass=SingletonMeta):
    ...


# Check the singleton behavior
# * Both instances will be the same, demonstrating that only one instance is
#   created.
x = SingletonClass()
y = SingletonClass()
print(id(x) == id(y))
# True
