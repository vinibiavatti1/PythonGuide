"""
MRO (Method Resolution Ordering)

* MRO is the algorithm to solve the sequence of method resolution in python
  inheritance
* To check the MRO used for some class, you can use the mro() class method, or
  check the help of the class
* MRO is also used by the super() statement to control the correct inheritance,
  and prevent diamond problems
* If you are using the super class to call the methods, without use super(),
  the MRO will not be followed
"""


###############################################################################
# MRO (Method Resolution Ordering)
###############################################################################


# Define a super class
# * This is the root class of the hierarchy
class Animal:
    def say(self):
        print('Animal')


class Aquatic(Animal):
    def say(self):
        print('Aquatic')


class Terrestrial(Animal):
    def say(self):
        print('Terrestrial')


class Turtle(Aquatic, Terrestrial):
    pass


# Check the MRO (Method resolution order)
# * The MRO will bring the sequence that will be used to call the methods in
#   order in the hierarchy
# * NOTE: The order of the definition of the base classes in the child class
#   changes the order of MRO
# * In the result, the sequence will be:
#   1. Turtle
#   2. Aquatic
#   3. Terrestrial
#   4. Animal
#   5. object
print(Turtle.mro())
"""
<class '__main__.Turtle'>,
<class '__main__.Aquatic'>,
<class '__main__.Terrestrial'>,
<class '__main__.Animal'>,
<class 'object'>
"""

# Call the inherited method using MRO
# * The MRO will be followed until find the first ocurrence of the say() method
# * In the result, the sequence will be:
#   1. Turtle    # not contains say method
#   2. Aquartic  # contains say method
turtle = Turtle()
turtle.say()
# Aquatic


###############################################################################
# Diamond problem inheritance
# * Diamond problem is said when some class has two base class with the same
#   method, so, the problem is to decide which method will be used. To solve
#   this, Python uses MRO in super() statement (Method Resolution Ordering)
#
# Simple diamond scheme:
#    A     Base class
#  /   \
# B     C  Intermediary class
#  \   /
#    D     Sub class
###############################################################################


# Define multi Inheritance without super()
# * In this case, the base class name will be used to call the constructor
# * The super() function will not be used
class Base:
    def __init__(self):
        print('Base')


class IntermediaryA(Base):
    def __init__(self):
        print('Intermediary A')
        Base.__init__(self)


class IntermediaryB(Base):
    def __init__(self):
        print('Intermediary B')
        Base.__init__(self)


class Sub(IntermediaryA, IntermediaryB):
    def __init__(self):
        print('Sub')
        IntermediaryA.__init__(self)
        IntermediaryB.__init__(self)


# Check the MRO (Method resolution order)
# * The MRO jumps from the Intermediary A to Intermediary B to fix the diamond
#   problem
# * The super() function will follow the MRO stack, but for the example, the
#   base class is used to call the __init__, ignoring the MRO sequence
print(Sub.mro())
"""
<class '__main__.Sub'>,
<class '__main__.IntermediaryA'>,
<class '__main__.IntermediaryB'>,
<class '__main__.Base'>,
<class 'object'>]
"""


# Create instance from multi inheritance without super()
# * The super() was not used, so, the result of the creation will be wrong
# * The Base class is present between the intermediary classes. this shows that
#   the MRO sequence was not used
Sub()
"""
Sub
Intermediary A
Base
Intermediary B
Base
"""


# Define multi Inheritance with super()
# * In this case, the super() function will be used to call the constructor
# * The super() guarantees that the MRO will be used
class _Base:
    def __init__(self):
        print('Base')


class _IntermediaryA(_Base):
    def __init__(self):
        print('Intermediary A')
        super().__init__()


class _IntermediaryB(_Base):
    def __init__(self):
        print('Intermediary B')
        super().__init__()


class _Sub(_IntermediaryA, _IntermediaryB):
    def __init__(self):
        print('Sub')
        super().__init__()


# Check the MRO (Method resolution order)
# * The super() will follow the MRO stack
print(_Sub.mro())
"""
<class '__main__.Sub'>,
<class '__main__.IntermediaryA'>,
<class '__main__.IntermediaryB'>,
<class '__main__.Base'>,
<class 'object'>]
"""


# Create instance from multi inheritance with super()
# * The super() is used, so, the result of the creation will be right
# * The Base class now is not present between the intermediary classes. this
#   shows that the MRO sequence was used correctly
_Sub()
"""
Sub
Intermediary A
Intermediary B
Base
"""
