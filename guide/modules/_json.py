"""
Json module

* JSON (JavaScript Object Notation) is a popular data format used for
  representing structured data. It's common to transmit and receive data
  between a server and web application in JSON format
* To work with JSON (string, or file containing JSON object), you can use
  Python's json module
* NOTE: 's' functions like (loads and dumps) work with in memory data
* NOTE: 'not s' functions like (load and dump) work with stored data (files)

Python objects and their equivalent conversion to JSON:
-------------------------------------------------------------------------------
Python	                JSON Equivalent
-------------------------------------------------------------------------------
dict	                object
list, tuple	            array
str	                    string
int, float, int	        number
True	                true
False	                false
None	                null
-------------------------------------------------------------------------------
"""
import json
import os
import sys
current_path = sys.path[0]


# Parse JSON (JSON > dict)
jsn = '{"name": "Vini", "age": 26}'
parsed = json.loads(jsn)
print(parsed)        # {'name': 'Vini', 'age': 26}
print(type(parsed))  # <class 'dict'>


# Convert JSON (dict > JSON)
dct = {'name': 'Vini', 'age': 26}
dumped = json.dumps(dct)
print(dumped)        # {"name": "Vini", "age": 26}
print(type(dumped))  # <class 'str'>


# Parse JSON File (JSON File > dict)
file_path = os.path.join(current_path, '../../resources/file_json.json')
with open(file_path) as f:
    parsed = json.load(f)
print(parsed)
# {'name': 'Vini', 'age': 26}


# Convert JSON File (dict > JSON File)
dct = {'name': 'Vini', 'age': 26}
file_path = os.path.join(current_path, '../../resources/file_json.json')
with open(file_path, 'w') as f:
    json.dump(dct, f)
# File content: {"name": "Vini", "age": 26}
