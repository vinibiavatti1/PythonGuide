"""
Functions

* In Python, a named function is defined using the "def" keyword
* A "parameter" is the variable listed inside the parentheses in the function
  definition.
* An "argument" is the value that is sent to the function when it is called
* Functions are used to decompose problems
* When pass arguments to a function that doesn't have parameters, it will raise
  a TypeError
* Python has two kinds of functions:
  * Named functions: Functions with name, that can be defined using "def"
  * Anonymous functions: Lambda functions that can be defined usign "lambda"
    (Check _lambda.py for more details)
* For parameters, check _parameters.py file
"""


###############################################################################
# Functions
###############################################################################


# Define an empty named function
# * To define a named function, the keyword "def" need to be used
# * You can use the pass keyword to create empty resources
def my_function():
    pass


# Define a named function with some execution
# * Some logic can be inside a function
def show_message():
    print('Function!')


# Call a named function
# * To call the function, just call the name of the function using parenthesis
show_message()
# Function!


# Define a function with parameters
# * Parameters are data that functions need to be executed
# * The values passed to a function are called as arguments
def show_text(txt, amount):
    print(txt * amount)


# Call a parameters function passing arguments
# * To call a function containing parameters to be set, you must put the
#   arguments inside the parenthesis
show_text('abc', 2)
# abcabc


# Define a function with return
# * Functions can return a result after execution. The "result" keyword is used
#   to do this
def sum_values(x, y):
    return x + y


# Call a function with return
# * The returned data can be stored in a variable and used as well
result = sum_values(5, 5)
print(result)
# 10


# Define a function with return for specific cases
# * You can create a function that return values just for specific cases
# * NOTE: This is not a good practice (avoid)
def return_when_true(arg):
    if arg:
        return 'Thats it!'


# Call a function that returns for specific cases
# * The default value for functions that does not return any data is None
result1 = return_when_true(True)
result2 = return_when_true(False)
print(result1, result2, sep=', ')
# Thats it!, None


# Define a function that returns more then one element
# * Functions can return more then on element
# * NOTE: In this case, the elements will be returned as a tuple
# * NOTE: Check _tuple.py file for more details
def return_sum_and_sub(x, y):
    r1 = x + y
    r2 = x - y
    return r1, r2  # NOTE: This is an implicit tuple (same of (r1, r2))


# Call a function that returns more then one element
# * The function that return more elements return a tuple actually
# * You can use the umpack syntax to get these values, or process the values
#   as a tuple
r1, r2 = return_sum_and_sub(7, 3)
print(r1, r2, sep=', ')
# 10, 4


# Define a nested function (inner function)
# * A function inside a function is called by inner function or nested function
def root():
    def nested():  # Nested function
        pass
    nested()  # Call nested function inside the root function


###############################################################################
# Recursive Function
###############################################################################


# Define a recursive function
# * A recursive function is a function that call themselves from within their
#   own code, to solve some problem
# * To define a recursive function, you must call this function inside itself
def recursive(n):
    if n > 0:
        print(n, end='')
        recursive(n - 1)
    else:
        print()


# Call a recursive function
# * To call a recursive function you just use the same method to call a common
#   functions
recursive(5)
# 54321


# Define a recursive function with return
# * To define a recursive function with return you must know how the call stack
#   of the programming language works.
# * You can return the call of the function to return the value by the call
#   chain
def recursive_with_return(n):
    if n > 0:
        return n + recursive_with_return(n - 1)
    else:
        return n


# Call a recursive function with return
# * This function can be called the same way of the recursive function
result = recursive_with_return(5)
print(result)
# 15


###############################################################################
# Shadowing
###############################################################################


# Define function with parameter containing the same name of variable
# * The Python has a mechanism called by shadowing that make the parameters be
#   different of the variables, even if the parameter and the variable have the
#   same identifier (name)
def shadowing(name):
    return name


# Call function with parameters having the same name of variable
# * The mechanism will consists this to prevent conflicts
name = 'Outside function'
result = shadowing('From function')
print(name, result, sep=', ')
# Outside function, From function


###############################################################################
# Function reference
###############################################################################


# Get the reference of the function
# * You can use the reference of the function as arguments, to declare some
#   variable, etc.
# * To get the reference you must need to point to the name of the function,
#   without defining the parenthesis ()
my_show_message = show_message
my_show_message()
# Function!


# Define a function that accepts function as parameter
# * You can pass a function as parameters to other function using the reference
#   of it
def execute_function(fn):
    fn()


# Call the function passing a function as argument
# * To call, you have to passe the function without parenthesis, to don't
#   execute it, but passing the reference
execute_function(show_message)
# Function!


# Define a function inside a dictionary
# * You can put some function reference inside a dictionary
dct = {'sum': sum_values}
result = dct['sum'](6, 4)
print(result)
# 10


###############################################################################
# Typing
###############################################################################


# Define function specifing the type for parameter and return
# * It is allowed to specify the type annotation for a parameter or return
# * NOTE: The Python runtime does not enforce function and variable type
#   annotations
# * Syntax: Parameter: (arg: type) / Return: def fn() -> type:
def integer_sum(x: int, y: int) -> int:
    return x + y


# Call function with typing
# * We use the same way to call any function, but for this function, if you
#   provide wrong datatype, the IDE can warn about it
result = integer_sum(9, 3)
print(result)
# 12
