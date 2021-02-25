"""
Slicing

* It is a notation to select, update or delete elements in collections by some
  range
* The values needs to be integers or None, or an object with the __index__
  method implemented
* NOTE: Slicing selects left-to-right elements when step is positive
* NOTE: Slicing dont accept reverse lists
* Syntax
  * [start:stop:step]
"""


# Normal values
lst = [1, 2, 3, 4, 5, 6]
print(lst[0:6])  # [1, 2, 3, 4, 5, 6]
print(lst[2:4])  # [3, 4]
print(lst[1:5])  # [2, 3, 4, 5]


# Negative values
# * Access the index from the right to the left
print(lst[-6:-2])  # [1, 2, 3, 4]
print(lst[-2:-1])  # [5]
print(lst[-3:-5])  # []  NOTE: Cannot select right-to-left!


# Mixing values
print(lst[1:-1])  # [2, 3, 4, 5]
print(lst[-5:5])  # [2, 3, 4, 5]
print(lst[-1:2])  # []
print(lst[-4:0])  # []
print(lst[0:-3])  # [1, 2, 3]


# Blank values
print(lst[:])   # [1, 2, 3, 4, 5, 6]
print(lst[:2])  # [1, 2]
print(lst[2:])  # [3, 4, 5, 6]


# Step
print(lst[::2])    # [1, 3, 5]
print(lst[2:5:2])  # [3, 5]
print(lst[:4:3])   # [1, 4]
print(lst[0:3:3])  # [1]


# Step with negative values (invese)
print(lst[::-1])      # [6, 5, 4, 3, 2, 1]
print(lst[1:6:-1])    # []
print(lst[::-2])      # [6, 4, 2]
print(lst[-1:-5:-1])  # [6, 5, 4, 3]
# print(lst[:::])     Invalid Syntax


# None
print(lst[None:None])       # [1, 2, 3, 4, 5, 6]
print(lst[0:None])          # [1, 2, 3, 4, 5, 6]
print(lst[None:5])          # [1, 2, 3, 4, 5]
print(lst[None:])           # [1, 2, 3, 4, 5, 6]
print(lst[:None])           # [1, 2, 3, 4, 5, 6]
print(lst[None:None:None])  # [1, 2, 3, 4, 5, 6]


# Class with __index__
class MagicValue:
    def __index__(self):
        return 4


print(lst[:MagicValue()])
# [1, 2, 3, 4]
