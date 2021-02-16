"""
Class template example
"""
# Template
class Template:

    # Class variables
    version: 1

    # Init (Constructor)
    def __init__(self, name): 
        self.name = name

    # Class methods
    @classmethod
    def fromJSON(cls, json_object):
        return cls(json_object)
    
    # Static methods
    @staticmethod
    def is_valid_version(version):
        return True

    # Properties
    @property
    def name(self):       # Getter
        return self.name
    @name.setter
    def name(self, name): # Setter
        self.name = name
    @name.deleter
    def name(self):       # Deleter
        del self.name

    # Methods
    def get_full_name(self):
        return f'{self.name}: {Template.version}'