"""
Function vs Method

* Function doesn't belong to any data
* Methods change the state of a selected entity
* A method is owned by the data it works for, while a function is owned by the
  whole code
"""


###############################################################################
# Function
###############################################################################


# Function
# * The function is defined using the "def" keyword
# * Functions are at module level
def add(x, y):
    return x + y


# Call a function
# * The function is called by its name
# * If the function is located in another module, it must be imported
x = add(5, 5)
print(x)
# 10


###############################################################################
# Method
###############################################################################


# Method
# * A method is a function present inside a class
# * Methods are at class level
class Person:
    def get_name(self):
        return 'John'


# Call a method
# * To call a method, it is necessary to create an instance of the class
person = Person()
x = person.get_name()
print(x)
# John
