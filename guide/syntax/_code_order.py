"""
Code order

* Python interpreter reads the code from the top to bottom, each line from the
  left to right
* YOu cannot define some function or class after the usage of it
"""


# Function
# print(sum_vals(5, 5))  # Error (name 'sum_vals' is not defined)


def sum_vals(x, y):
    return x + y


# Class
# car = Car()  # NameError: name 'Car' is not defined


class Car:
    pass
