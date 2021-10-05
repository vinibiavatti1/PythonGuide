"""
Match (PEP 636)

* Python 3.10 introduced the "match" statement that works like a if elif,
  comparing the input value and calling the corresponding execution block
* This concept is called Structural Pattern Matching
* The case statements are use to validate the "pattern" and the input value
* It is the same of "switch" for some other languages, like Java and C#
* More content in: https://www.python.org/dev/peps/pep-0636
"""


###############################################################################
# Match
###############################################################################


# Match
# * The match statement need a input (variable or constant) to be checked to
#   call the corresponding pattern (case)
http_status = 200
match http_status:
    case 200:
        print('Success')
    case 500:
        print('Internal server error')
    case 418:
        print('I\'m a teapot')
# Success


###############################################################################
# Wildcard
###############################################################################


# Wildcard
# * The match uses the "_" wildcard to define when no pattern was matched
http_status = 400
match http_status:
    case 200:
        print('Success')
    case 500:
        print('Internal server error')
    case _:
        print('Other error')
# Other error


# Collection example
name_and_age = ('Vini', 27)
match name_and_age:
    case 'Ana', 23:
        print('Vini')
    case 'John', 27:
        print('John')
    case 'Vini', _:  # The wildcard was used only for the "age" value
        print('Vini')
# Vini


###############################################################################
# Or Patterns and Sub Patterns
###############################################################################


# Or Patterns
# * The case can contains more patterns available to be used in the comparing
#   process. The pipe (|) char is used as the or operator
http_status = 400
match http_status:
    case 200 | 201 | 202:  # when http_status is 200 or 201 or 202
        print('Success')
    case 400 | 401 | 403:  # when http_status is 400 or 401 or 403
        print('No permisson')
# No permission


# Sub Patterns
# * The or patterns can also be used inside collections as sub patterns
err_and_code = ('Error', 2)
match err_and_code:
    case 'Error', 1 | 2 | 3:  # when err is "Error" and code is 1 or 2 or 3
        print('Common Error')
    case _:
        print('Strange Error')
# Common Error


###############################################################################
# Guards
###############################################################################


# Guard
# * Guards consist of the if keyword followed by any expression, to evaluate
#   that pattern only if the condition is True
login = True
error = 401
match error:
    case 401 if login:  # when err is 401 if login (guard)
        print('Contact support')
    case 401:           # when err is 401
        print('Please, do login')
# Contact support
