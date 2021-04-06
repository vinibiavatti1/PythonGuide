"""
Template

* Tiis is the template for class construction
"""


# Class template
class Template(object, metaclass=type):

    # Class constant
    VERSION: 1

    # Class attribute
    number: 1

    # Init (Constructor) (Magic method)
    def __init__(self, name, surname):
        self.name = name          # public attribute
        self.__surname = surname  # private attribute

    # Properties
    @property
    def surname(self):  # Getter
        return self.__surname

    @surname.setter
    def surname(self, surname):  # Setter
        self.__surname = surname

    @surname.deleter
    def surname(self):  # Deleter
        del self.surname

    # Public method
    def get_full_name(self):
        return f'{self.name}: {Template.number}'

    # Private method
    def __erase_name(self):
        self.name = ''

    # Class methods
    @classmethod
    def from_dict(cls, dct):
        return cls(**dct)

    # Static methods
    @staticmethod
    def is_valid_version(version):
        return True
