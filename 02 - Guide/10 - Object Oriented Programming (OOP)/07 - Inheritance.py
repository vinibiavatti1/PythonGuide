"""
Inheritance

* Inheritance allows us to define a class that inherits all the methods and
  properties from another class.
* It is used to reuse code, following the DRY principle (Don't Repeat Yourself)
* In inheritance, the classes are organized in a hierarchy, having the concepts
  below:
  * Base class (aka. parent or super class): the class being inherited from
  * Child class (aka. derived class): the class that inherits from other class
* When a class inherits from another class, it inherits all the properties and
  methods of the base class, including the constructor
* Python allows multi inheritance, i.e., a class can inherit from multiple base
  classes
* Syntaxes:
###############################################################################
Syntax                  Description
###############################################################################
class <name>:           Define a class
class <name>(<bases>):  Define a child class (bases are the base classes)
###############################################################################
"""


###############################################################################
# Defining a Base Class
###############################################################################


# Defining a base class
# * In the example below, we will create a simple base class that will be used
#   as the base class for the other classes
# * When a class does not specify a base class, the "object" class will be set
#   as the base class for this class implicitly
# * NOTE: The "_type" argument contains a underscore because "type" is a
#   built-in function in Python
class Animal:

    def __init__(self, name, _type):
        self.name = name
        self.type = _type


###############################################################################
# Defining Child Classes
###############################################################################


# Defining a child class
# * Now, we are going to define a child class that will inherit from the base
#   class (Animal)
# * In this case, the Dog class will contain the same attributes and methods of
#   Animal class
class Dog(Animal):
    ...


# Defining another child class
# * We can define other child classes that will inherit from the base class
# * In this case, the Cat class will contain the same attributes and methods of
#   Animal class
class Cat(Animal):
    ...


###############################################################################
# Creating Instances of Child Classes
###############################################################################


# Creating an instance of the child classes
# * We have two child classes now, so that lets create instances of each one
# * Note that the base class has a constructor with two arguments. By knowing
#   that the child classes inherit from the base class, we can assume that the
#   child classes will have the same constructor
x = Dog('Rex', 'dog')
y = Cat('Tom', 'cat')
print(x.name, x.type)
print(y.name, y.type)
# Rex dog
# Tom cat


###############################################################################
# Overriding the Constructor
###############################################################################


# Importing Override Decorator
# * To mark a method as overrided, we can use the `@override` decorator from
#   the `typing` module
from typing import override


# Overriding the constructor (Dog)
# * See that in the example above, we must set the "_type" argument which means
#   the type of the animal. This argument is necessary because the base class
#   contains it in the constructor. However, we always know that the Dog will
#   have the type "dog", and the Cat will have the type "cat", so that, we can
#   override the constructor in the child classes
# * The override concept is used to change the behavior of the base class
#   method
# * Since we are working in two contexts (child class and base class), we can
#   access the base class resources using the "super()" function. In the case
#   below, we will use the "super()" function to call the base class
#   constructor
class Dog(Animal):

    @override
    def __init__(self, name):
        super().__init__(name, 'dog')


# Overriding the constructor (Cat)
# * Here we will override the constructor of the Cat class as well
class Cat(Animal):

    @override
    def __init__(self, name):
        super().__init__(name, 'cat')


# Creating instances of the child classes
# * Now, we can create instances of the child classes without passing the _type
#   argument
# * The "_type" argument is required by the base class constructor, however, we
#   override that constructor with new ones
x = Dog('Rex')
y = Cat('Tom')
print(x.name, x.type)
print(y.name, y.type)
# Rex dog
# Tom cat


###############################################################################
# Overriding Methods
###############################################################################


# Defining a base class with methods
# * In the example below, we will define a base class with a method that will
#   be shared between the child classes
# * WE are using the
class Animal:

    @override
    def say(self):
        print('???')


# Overriding the base class methods (Dog)
# * We can override the methods of the base class like we did with the
#   constructor
# * In this case, we will override the "say" method with other behavior in our
#   Dog class
class Dog(Animal):

    @override
    def say(self):
        print('Woof!')


# Overriding the base class methods (Cat)
# * We will do the same thing for the Cat class, with even other behavior
class Cat(Animal):

    @override
    def say(self):
        print('Meow!')


# Calling the methods
# * We must create instances of each class to call the methods
# * Note that the "say" method is different for each class (has a different
#   behavior)
x = Animal()
y = Dog()
z = Cat()
x.say()
y.say()
z.say()
# ???
# Woof!
# Meow!


# Extending the base class methods (Animal)
# * We are still able to use the base class methods even when we override them
# * For this, we can call the base class method using the "super()" function
class Pug(Dog):

    @override
    def say(self):
        super().say()  # Before
        print('Yap!')
        super().say()  # After


# Calling the extended methods
# * Now, we can call the extended methods to see that both operations will be
#   performed
x = Pug()
x.say()
# Woof!
# Yap!
# Woof!


###############################################################################
# Abstract Base Class (ABC)
###############################################################################


# Importing the ABC module
# * Look that we are instantiating the Animal class in the previous example,
#   which has the `say` method that returns '???', since we don't know the
#   animal it is yet. To avoid this, we can set the Animal class as an abstract
#   class
# * Abstract classes are classes that cannot be instantiated, and are used only
#   as base classes
# * To set a class as an abstract class, we must inherit the ABC class from the
#   abc module
# * To define an abstract method inside an abstract class, we need to import
#   the `abstractmethod` as well
# * The `abstractmethod` decorator is used to define abstract methods, i.e.
#   methods that must be implemented by the child class
# * NOTE: Take a look at _abc.py file for more details about Abstract Base
#   Class
from abc import ABC, abstractmethod


# Defining an abstract base class
# * Now, we can define the Animal class as an abstract class
# * The method `say` will be set as an abstract method, so that, the child
#   classes must implement it
class Animal(ABC):

    def __init__(self, name, _type):
        self.name = name
        self.type = _type

    @abstractmethod
    def say(self):
        pass


# Defining a child class
# * The example below shows the Dog class that will inherit the Animal class,
#   and implement the `say` method
class Dog(Animal):

    @override
    def __init__(self, name):
        super().__init__(name, 'dog')

    @override
    def say(self):
        print('Woof!')


# Instantiating the child class
# * Now we can instantiate the child class to test it
x = Dog('Rex')
print(x.name, x.type)
x.say()
# Rex dog
# Woof!


###############################################################################
# Final Classes/Methods
###############################################################################


# Importing final decorator
# * The `final` decorator is used to prevent the class or method from being
#   overridden
from typing import final


# Defining a final class
# * When a class is marked as final, it cannot be inherited, i.e., it cannot
#   be used as a base class for any other class
@final
class CustomClass:
    ...


# Defining a final method
# * When a method is marked as final, it cannot be overridden by the child
#   classes
class CustomClass:

    @final
    def process(self):
        ...
