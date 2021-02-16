"""
PEP (Python Enhancement Proposals)

* PEP8 is a documentation to describe the good practices for Python
* This is allowed in https://www.python.org/dev/peps/
* The idea is to describe the way to type code using 'Pythonic' way
"""
# [Easter egg] Manifest (By Tim Peters)
import this
# The Zen of Python, by Tim Peters
# 
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# Naming Convension
#
# 1. General
# Avoid using names that are too general or too wordy. Strike a good balance between the two.
# Bad: data_structure, my_list, info_map, dictionary_for_the_purpose_of_storing_data_representing_word_definitions
# Good: user_profile, menu_options, word_definitions
# Don’t be a jackass and name things “O”, “l”, or “I”
# When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)
# Never use special symbols like !, @, #, $, %, etc.
data_structure = 1         # Bad
def my_function(): pass    # Bad
class IMyInterface(): pass # Bad
class HttpServer(): pass   # Bad

customer_count = 1         # Good
def render_bitmap(): pass  # Good
class Animal(): pass       # Good
class HTTPServer(): pass   # Good

# 2. Packages
# Package names should be all lower case
# When multiple words are needed, an underscore should separate them
# It is usually preferable to stick to 1 word names
# Ex: my_package

# 3. Modules
# Module names should be all lower case
# When multiple words are needed, an underscore should separate them
# It is usually preferable to stick to 1 word names
# Ex: my_module

# 4. Classes
# Class names should follow the UpperCaseCamelCase convention
# Python’s built-in classes, however are typically lowercase words
# Exception classes should end in “Error”
class SecuredCustomer(): pass
class Client(): pass
class ClientMustBeGoodError(): pass # Exception example

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
class Client1():
    customer_count = 1
    _company_name = "Hello world" # Non-public
client = Client()

# 7. Methods
# Method names should be all lower case
# Words in an method name should be separated by an underscore
# Non-public method should begin with a single underscore
# If a method name needs to be mangled, two underscores may begin its name
class Client2():
    def get_name(self): pass
    def _change_surname(self): pass # Non-public method

# 8. Method Arguments
# Instance methods should have their first argument named ‘self’.
# Class methods should have their first argument named ‘cls’
class Client3():
    def set_name(self, name): pass # Instance mathod

    @classmethod
    def new_instance(cls, name): pass # Class method

# 9. Functions
# Function names should be all lower case
# Words in a function name should be separated by an underscore
def calc_sum(x, y): pass

# 10. Constants
# Constant names must be fully capitalized
# Words in a constant name should be separated by an underscore
PI = 3.14

# Strings
# There is no differece for use " (double quotes) or ' (single quotes)
# The ' (single quotes) is a best practice
text = "Hello" # Bad
text = 'Hello' # Good