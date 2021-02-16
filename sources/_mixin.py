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


# MixIn
class JSONParseMixIn:
    def toJSON(self):
        return json.dumps(self.__dict__)

    def fromJSON(self, json_object):
        return json.loads(json_object)


# Base Class
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


# Child Class with MixIn
# NOTE: MixIn classes have to be in the front to guarantee the correct MRO
# processing
class CustomerData(JSONParseMixIn, Customer):
    def __init__(self, name, company):
        super().__init__(name, company)


customerData = CustomerData('Vini', 'ABC S/A')
print(customerData.toJSON())
# {"_name": "Vini", "_company": "ABC S/A"}
jsonData = {"name": "Vini", "company": "ABC S/A"}
print(customerData.fromJSON(jsonData))
# {'name': 'Vini', 'company': 'ABC S/A'}
