"""
Function vs Method

* Function doesn't belong to any data
* Methods change the state of a selected entity
* A method is owned by the data it works for, while a function is owned by the
  whole code
"""


# Function
def sum(x, y):
    return x + y


# Method
class Person:
    def get_name(self):
        return 'Vini'


# Calling function
x = sum(5, 5)
print(x)
# 10


# Calling method
person = Person()
x = person.get_name()
print(x)
# Vini
