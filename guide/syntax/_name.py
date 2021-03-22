"""
Name

* When the interpreter run Python files, it does two things:
  * it sets a few special variables like __name__
  * it executes all of the code found in the file
* The __name__ variable is set when Python run the source code
* This variable can be used to check if the code is running by itself, or if
  the python file is importing from other .py file
* When the .py file is running by main (python foo.py), the __name__ variable
  will be set with '__main__' value
* When the .py file is importing by other file, the __name__ variable will
  receive the name of its module with the extension (.py)
"""


# Using __name__ to control the execution/importation of the file
if __name__ == '__main__':
    print('This file is being executing as main file')
    # This file is being executing as main file
else:
    print('This file is being imported')
    # (Just execute if the file is imported from another)
    # __name__ will be '_name' (name of this file)
