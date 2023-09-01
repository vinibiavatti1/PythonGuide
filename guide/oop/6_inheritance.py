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

    def __init__(self, name):
        super().__init__(name, 'dog')


# Overriding the constructor (Cat)
# * Here we will override the constructor of the Cat class as well
class Cat(Animal):

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

    def say(self):
        print('???')


# Overriding the base class methods (Dog)
# * We can override the methods of the base class like we did with the
#   constructor
# * In this case, we will override the "say" method with other behavior in our
#   Dog class
class Dog(Animal):

    def say(self):
        print('Woof!')


# Overriding the base class methods (Cat)
# * We will do the same thing for the Cat class, with even other behavior
class Cat(Animal):

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

    def __init__(self, name):
        super().__init__(name, 'dog')

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
# Multi Inheritance
###############################################################################


# Defining a base class
# * Python allows us to inherit from multiple base classes
# * Now we are going to create a base class that will be used as the base class
#   for the next examples
# * NOTE: Multi inheritance can be dangerous, so that, it must be used with
#   precaution. Thats is the reason why some languages do not allow multi
#   inheritance
class Person:

    def __init__(self, name) -> None:
        self.name = name


# Defining other base class
# * Other base class will be defined to be used in the next examples
class Employee:

    def __init__(self, company) -> None:
        self.company = company


# Defining a child class with multiple inheritance
# * In the next example, both classes (Person and Employee) will be inherited
#   by the Worker class

class Programmer(Person, Employee):
    ...


# Creating an instance of the child class with multiple inheritance
# * Since we are inheriting from multiple base classes, both base classes have
#   a constructor. In this case, the constructor of the first inherited class
#   will be used
# * Note that the company attribute was not created into the child class. If we
#   change the order of the inheritance, the company attribute will be created
#   instead
x = Programmer('John')
print(x.name, hasattr(x, 'company'))
# John False


###############################################################################
# Overriding the Constructor (Multi Inheritance)
###############################################################################


# Overriding the constructor (Multi Inheritance)
# * To override the constructor in a multi inheritance context, we cannot use
#   the `super()` function, since it will call the constructor of the first
#   base class only
# * We can access the resources of the base classes using the base class name
# * In the example below, we will override the constructor of the first base
#   class (Person) and call the constructor of both base classes
# * NOTE: We must pass the `self` argument when using this way
class Programmer(Person, Employee):

    def __init__(self, name, company):
        Person.__init__(self, name)
        Employee.__init__(self, company)


# Creating an instance of the child class with multiple inheritance
# * Now, we can create an instance of the child class passing all the
#   information to the constructor
x = Programmer('John', 'Google')
print(x.name, x.company)
# John Google


###############################################################################
# MRO (Method Resolution Order)
###############################################################################


# Diamond problem
# * Sometimes referred to as the "Deadly Diamond of Death"
# * By knowing that Python allows multi inheritance, we can have some
#   additional problems with this concept
# * The diamond problem in an ambiguity that occurs when a class (D) inherits
#   from two other classes (B, C) that has the same class as base (A). If the
#   base class (A) has a method that the child classes (B, C) override but the
#   child class (D) does not, then, which method will be used?
# * In this case, Python follows the order of the base classes to decide which
#   will be prioritized, but this still can bring call problems
# * Take a look at the diagram below to understand better the inheritance that
#   generates the diamond problem
r"""
   A     Base class
 /   \
B     C  Intermediary class
 \   /
   D     Sub class
"""


# Defining the diamond problem architecture (without MRO)
# * To simulate a multi inheritance call problem, we are going to design the
#   diamond architecture
# * In the example below, we are defining the classes that will be the root
#   class
# * We will also define the `say` method that will be used by the child classes
# * NOTE: We are not using the `super()` function to call the base class method
#   to demonstrate the multi inheritance call problem
class A:

    def say(self):
        print('A (Base)')


class B(A):

    def say(self):
        print('B (Intermediary)')
        A.say(self)


class C(A):

    def say(self):
        print('C (Intermediary)')
        A.say(self)


class D(B, C):

    def say(self):
        print('D (Child)')
        B.say(self)
        C.say(self)


# Creating an instance of the child class (D)
# * Finally, we can create an instance of the child class (D) to test the
#   result of the say method
# * Note that "Base" will be printed twice, since the `say` method of the base
#   class (A) was called twice. This happens because we are not using the
#   Method Resolution Order (MRO) algorithm to prevent this problem
x = D()
x.say()
"""
D (Child)
B (Intermediary)
A (Base)
C (Intermediary)
A (Base)
"""


# Defining the diamond problem architecture (with MRO)
# * Now, we are going to create the same architecture above, but using the
#   Method Resolution Order (MRO) algorithm
# * To use the MRO algorithm, we must use the `super()` function to call the
#   parent class resources
class A:

    def say(self):
        print('A (Base)')


class B(A):

    def say(self):
        print('B (Intermediary)')
        super().say()


class C(A):

    def say(self):
        print('C (Intermediary)')
        super().say()


class D(B, C):

    def say(self):
        print('D (Child)')
        super().say()


# Creating an instance of the child class (D)
# * We will create an instance of the child class (D) to test the result
# * Note that the `say` method was called only once, since the MRO algorithm
#   was used by the `super()` function
x = D()
x.say()
"""
D (Child)
B (Intermediary)
C (Intermediary)
A (Base)
"""


# Checking the Method Resolution Order (MRO)
# * To see the MRO algorithm in action, we can print the `__mro__` attribute of
#   the class, or use the `mro()` method
# * This will return a collection with the order of the classes that will be
#   considered when calling the `super()` function
# * Note that there is no A class after the B class
print(D.mro())
"""
<class '__main__.D'>,
<class '__main__.B'>
<class '__main__.C'>
<class '__main__.A'>
<class 'object'>
"""
