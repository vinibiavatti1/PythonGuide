"""
Bool examples
"""
# Syntax
# The bool values always have the first letter capitalized
x = True
b = False


# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# Below are the false values
bool(False)  # False
bool(None)   # False
bool(0)      # False
bool("")     # False
bool(())     # False
bool([])     # False
bool({})     # False


# For objects, it will be Flase if this is None or if the __len__ method
# was implemented to return 0
class Client():
    def __len__(self):
        return 0


obj = Client()
print(bool(obj))  # False
