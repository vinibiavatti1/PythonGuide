"""
Template

* Tiis is the template for class construction
"""


# Class template
class Template(object, metaclass=type):

    # Class constant
    VERSION: 1

    # Class variable
    number: 1

    # Init (Constructor) (Magic method)
    def __init__(self, name):
        self.name = name  # Attribute

    # Properties
    @property
    def name(self):  # Getter
        return self.name

    @name.setter
    def name(self, name):  # Setter
        self.name = name

    @name.deleter
    def name(self):  # Deleter
        del self.name

    # Method
    def get_full_name(self):
        return f'{self.name}: {Template.version}'

    # Class methods
    @classmethod
    def fromJSON(cls, json_object):
        return cls(json_object)

    # Static methods
    @staticmethod
    def is_valid_version(version):
        return True
