"""
Raw string

* The 'r' char defines the string is a raw string, so scape chars will be
  ignored
* It is commonly used to define regex patterns
"""


###############################################################################
# Raw string
###############################################################################


# Define Raw string
# * The scape char will not be processed
raw = r'Hello \n World'
print(raw)
# Hello \n World


# Define a regex
# * Raw string is commonly used to define regex patterns
regex = r'\$\s[0-9,]+'
print(regex)
# \$\s[0-9,]+
