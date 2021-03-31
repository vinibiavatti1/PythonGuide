"""
MRO (Method Resolution Ordering)

* MRO is the algorithm to solve the sequence of method resolution in python
  inheritance
* To check the MRO used for some class, you can use the mro() class method
* MRO is used by the super() statement to control the correct inheritance
"""


###############################################################################
# Diamond problem inheritance
# * Diamond problem is said when some class has two base class with the same
#   method, so, the problem is to decide witch method will be used. To solve
#   this, Python has MRO (Method Resolution Ordering)
#
# Simple diamond scheme:
#    A     Base class
#  /   \
# B     C  Intermediary child class
#  \   /
#    D     Final child class
###############################################################################


# Diamond Problem with base calling (NOT SOLVED)
# * In this case, the base class name will be used to call the constructor
# Stack:
# Child         1
# +-- A         2
#     +-- Base  3
# +-- B         4
#     +-- Base  5
class Base(object):
    def __init__(self):
        print('Base')
        object.__init__(self)
        # super().__init__()


class A(Base):
    def __init__(self):
        print('A')
        Base.__init__(self)
        # super().__init__()


class B(Base):
    def __init__(self):
        print('B')
        Base.__init__(self)
        # super().__init__()


class Child(A, B):
    def __init__(self):
        print('Child')
        A.__init__(self)
        B.__init__(self)
        # super().__init__()


Child()
# Child, A, Base, B, Base (MRO Not Resolved, loaded Base twice)
print(Child.mro())  # The MRO was not followed
# [<class '__main__.Child'>, <class '__main__.A'>, <class '__main__.B'>,
# <class '__main__.Base'>, <class 'object'>]


# Diamond Problem with super (SOLVED)
# * In this case, the super() will be used to call the constructor
# Stack:
# Child         1
# +-- A         2
# +-- B         3
#     +-- Base  4
class Base2(object):
    def __init__(self):
        print('Base')
        # object.__init__(self)
        super().__init__()


class A2(Base2):
    def __init__(self):
        print('A')
        # Base.__init__(self)
        super().__init__()


class B2(Base2):
    def __init__(self):
        print('B')
        # Base.__init__(self)
        super().__init__()


class Child2(A2, B2):
    def __init__(self):
        print('Child')
        # A.__init__(self)
        # B.__init__(self)
        super().__init__()


Child2()
# Child, A, B, Base (MRO Resolved)
print(Child2.mro())  # The MRO was followed
# [<class '__main__.Child2'>, <class '__main__.A2'>, <class '__main__.B2'>,
# <class '__main__.Base2'>, <class 'object'>]
