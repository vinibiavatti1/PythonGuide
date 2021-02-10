"""
PEP (Python Enhancement Proposals)

PEP is a documentation to describe the good practices for Python
This is allowed in https://www.python.org/dev/peps/
"""
# Naming Convension
#
# 1. General
# Avoid using names that are too general or too wordy. Strike a good balance between the two.
# Bad: data_structure, my_list, info_map, dictionary_for_the_purpose_of_storing_data_representing_word_definitions
# Good: user_profile, menu_options, word_definitions
# Don’t be a jackass and name things “O”, “l”, or “I”
# When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)
# Never use special symbols like !, @, #, $, %, etc.
data_structure = 1  # Bad
def my_function():  # Bad
class IMyInterface(): # Bad
class HttpServer():   # Bad

customer_count = 1  # Good
def render_bitmap()  # Good
class Animal():     # Good
class HTTPServer():   # Good

# 2. Packages
# Package names should be all lower case
# When multiple words are needed, an underscore should separate them
# It is usually preferable to stick to 1 word names
my_package

# 3. Modules
# Module names should be all lower case
# When multiple words are needed, an underscore should separate them
# It is usually preferable to stick to 1 word names
my_module

# 4. Classes
# Class names should follow the UpperCaseCamelCase convention
# Python’s built-in classes, however are typically lowercase words
# Exception classes should end in “Error”
class SecuredCustomer():
class Client():
class ClientMustBeGoodError(): # Exception example

# 5. Global (module-level) Variables
# Global variables should be all lowercase
# Words in a global variable name should be separated by an underscore
customer_count = 1
company_name = "Hello world"

# 6. Instance Variables
# Instance variable names should be all lower case
# Words in an instance variable name should be separated by an underscore
# Non-public instance variables should begin with a single underscore
# If an instance name needs to be mangled, two underscores may begin its name
class Client():
    customer_count = 1
    _company_name = "Hello world" # Non-public
client = Client()

# 7. Methods
# Method names should be all lower case
# Words in an method name should be separated by an underscore
# Non-public method should begin with a single underscore
# If a method name needs to be mangled, two underscores may begin its name
class Client():
    def get_name(self):
    def _change_surname(self): # Non-public method

# 8. Method Arguments
# Instance methods should have their first argument named ‘self’.
# Class methods should have their first argument named ‘cls’
class Client():
    def set_name(self, name): # Instance mathod

    @classmethod
    def new_instance(cls, name): # Class method

# 9. Functions
# Function names should be all lower case
# Words in a function name should be separated by an underscore
def calc_sum(x, y):

# 10. Constants
# Constant names must be fully capitalized
# Words in a constant name should be separated by an underscore
PI = 3.14

# Strings
# There is no differece for use " (double quotes) or ' (single quotes)
# The ' (single quotes) is a best practice
text = "Hello" # Bad
text = 'Hello' # Good