"""
Pickle module

* Pickle is used to persist python data into files (Serialization) as binary
  data, and used to read the binary data back to a python
* Can be used to store some object states, python data, etc.
* The name of this process is Serialization
* NOTE: 's' functions like (loads and dumps) work with in memory data
* NOTE: 'not s' functions like (load and dump) work with stored data (files)
"""
import os
import sys
import pickle


###############################################################################
# File Paths
###############################################################################
DAT_FILE = os.path.join(sys.path[0], '../../resources/python_data.dat')


###############################################################################
# Write
###############################################################################


# Define a class to persist
# * Any Python data can be stored by pickle
# * A collection with objects can be persisted, but for this example, just
#   one object will be persisted
# * This example uses objects created from a class to be stored
# * NOTE: The open() functions needs to be set to write as binary because
#   pickle stores data as binary
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'{self.name}: hi!')


# Persist the object (Serialization)
# * The object will be persisted as binary data into the file
# * The file will contains binary data that cannot be read easily
person = Person('Vini', 28)
with open(DAT_FILE, 'wb') as f:
    pickle.dump(person, f)
# File content:
# <binary_content>


###############################################################################
# Read
###############################################################################


# Read the object
# * The object will be read from the binary data of the file
person = None
with open(DAT_FILE, 'rb') as f:
    person = pickle.load(f)
    person.say()
    print(person.name, person.age, sep=', ')
# Vini: hi!
# Vini, 28
