"""
Multiple Inheritance

* Multiple inheritance is a feature that allows a class to inherit attributes
  and methods from multiple base classes
* This feature can be dangerous, so it must be used with caution to avoid
  problems like the "diamond problem"
"""


###############################################################################
# Multiple Inheritance
###############################################################################


# Defining a base class
# * Python allows us to inherit from multiple base classes
# * Now we are going to create a base class that will be used as the base class
#   for the next examples
# * NOTE: Multiple inheritance can be dangerous, so that, it must be used with
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
# Overriding the Constructor
###############################################################################


# Overriding the constructor
# * To override the constructor in a multi-inheritance context, we cannot use
#   the `super()` function, since it will call the constructor of the first
#   base class only
# * We can access the resources of the base classes using the base class name
# * In the example below, we will override the constructor of the first base
#   class (Person) and call the constructor of both base classes
# * NOTE: We must pass the `self` argument when using this way
from typing import override
class Programmer(Person, Employee):

    @override
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
# * By knowing that Python allows multi-inheritance, we can have some
#   additional problems with this concept
# * The diamond problem is an ambiguity that occurs when a class (D) inherits
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
# * To simulate a -inheritance call problem, we are going to design the
#   diamond architecture
# * In the example below, we are defining the classes that will be the root
#   class
# * We will also define the `say` method that will be used by the child classes
# * NOTE: We are not using the `super()` function to call the base class method
#   to demonstrate the multiple inheritance call problem
class A:

    def say(self):
        print('A (Base)')


class B(A):

    @override
    def say(self):
        print('B (Intermediary)')
        A.say(self)


class C(A):

    @override
    def say(self):
        print('C (Intermediary)')
        A.say(self)


class D(B, C):

    @override
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

    @override
    def say(self):
        print('B (Intermediary)')
        super().say()


class C(A):

    @override
    def say(self):
        print('C (Intermediary)')
        super().say()


class D(B, C):

    @override
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
