"""
Class template example
"""
# Template
class Template:

    # Class variables (static)
    version: 1

    # Class methods (static)
    @classmethod
    def add_version(cls):
        Template.version += 1

    # Init (Constructor)
    def __init__(self, name): 
        self.name = name

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