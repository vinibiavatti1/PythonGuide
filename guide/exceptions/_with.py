"""
With

* With statement in Python is used in exception handling to make the code
  cleaner and much more readable
* It simplifies the management of common resources like file streams
* With already call the close() method of resources
"""
import os
import sys
current_path = sys.path[0]


# With
file_path = os.path.join(current_path, '../../resources/file_read.txt')
with open(file_path) as f:
    print(f.read())
# Lorem ipsum dolor sit amet...


# Try with error
try:
    f = open(file_path)
except FileNotFoundError as e:
    print(e)
else:
    with f:
        print(f.read())
        # Lorem ipsum dolor sit amet...


# Create class to support with
class MyReader:
    def __init__(self):
        self.open = False

    def __enter__(self):
        self.open = True
        return self

    def __exit__(self, exc, val, trace):
        self.open = False
        return self


reader = MyReader()
with reader:
    print(reader.open)  # True
print(reader.open)  # False
