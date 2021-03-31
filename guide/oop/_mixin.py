"""
MixIn

* Is an interface that you don't have to actually implement because it's
  already implemented
* Mixins commonly dont have properties, or just have private properties without
  constructor
* The main difference of interface (or ABC) is that mixins have the methods
  already implemented
* NOTE: The recommended for OOP programing is to use ABC classes, without the
  implementantion for the most of cases
"""
import json


# Define a MixIn class
# * The MixIn class must have the MixIn suffix in the name
class JSONParseMixIn:
    def toJSON(self):
        return json.dumps(self.__dict__)

    def fromJSON(self, json_object):
        return json.loads(json_object)


# Define a base class
# * This class will be used as the base class
class Customer:
    def __init__(self, name, company):
        self._name = name
        self._company = company

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company


# Define the child class with MixIn
# * NOTE: MixIn classes have to be set in the front to guarantee the correct
#   MRO (Method Resolution Order) processing
class CustomerData(JSONParseMixIn, Customer):
    def __init__(self, name, company):
        super().__init__(name, company)


# Call MixIn methods
# * The MixIn methods will be available in the class that inherites it
customerData = CustomerData('Vini', 'ABC S/A')
jsonData = {"name": "Vini", "company": "ABC S/A"}
print(customerData.toJSON())
print(customerData.fromJSON(jsonData))
# {"_name": "Vini", "_company": "ABC S/A"}
# {'name': 'Vini', 'company': 'ABC S/A'}
