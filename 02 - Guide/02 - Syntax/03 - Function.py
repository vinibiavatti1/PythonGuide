"""
Function

* In Python, a named function is defined using the "def" keyword
* A "parameter" is the variable listed inside the parentheses in the function
  definition.
* An "argument" is the value that is sent to the function when it is called
* Functions are used to decompose problems
* When pass arguments to a function that doesn't have parameters, it will raise
  a TypeError
* Python has two kinds of functions:
  * Named functions: Functions with name, that can be defined using "def"
  * Anonymous functions: Lambda functions that can be defined using "lambda"
    (Check _lambda.py for more details)
* NOTE: For parameters, check _parameters.py file
* NOTE: For type hints, check _type_hints.py file
"""


###############################################################################
# Functions
###############################################################################


# Define a function
# * To define a named function, the keyword "def" must be used
# * NOTE: You can use the pass keyword to create empty expressions
def my_function():
    pass


# Define a function with execution
# * The function can contain some logic inside
def show_message():
    print('Function!')


# Call a function
# * To call the function, just call the name of the function using parenthesis
#   as the suffix
# * The parenthesis is used for the function arguments
show_message()
# Function!


###############################################################################
# Functions Parameters
###############################################################################


# Define a function with parameters
# * Parameters are data that functions require to be executed
# * The values passed to the function parameters are called arguments
def show_text(txt):
    print(txt)


# Call function with arguments
# * To call a function containing parameters to be set, you must provide the
#   required parameters
show_text('abc')
# abc


###############################################################################
# Functions Return
###############################################################################


# Define a function with return
# * Functions can return a result after execution.
# * Usually, the returned value is the result of the operation that was
#   executed.
def sum_values(x, y):
    return x + y


# Call a function with return
# * The returned data can be stored in a variable and used as well
result = sum_values(5, 5)
print(result)
# 10


# Define a function with optional return
# * You can create a function that return values just in specific cases
# * The default return data for a function is None
# * NOTE: Python allows a function to return in specific situations, however,
#   this is not a good practice. A function that returns something should
#   present the return expression for any way that the function can perform
def return_when_true(ret):
    if ret:
        return 'Thats it!'


# Call a function with optional return
# * The default value for functions that does not return any data is None
result1 = return_when_true(True)
result2 = return_when_true(False)
print(result1)
print(result2)
# Thats it!
# None


# Define a function with multiple return data
# * We can use tuples to return more then one data in a function
# * NOTE: Check _tuple.py file for more details
def return_sum_and_sub(x, y):
    r1 = x + y
    r2 = x - y
    return r1, r2  # Same of: return (r1, r2)


# Call a function with multiple return data
# * The function that return more elements usually return a tuple
# * You can use the unpack syntax to get these values, or process the values
#   as a tuple
r1, r2 = return_sum_and_sub(7, 3)   # Unpack Tuple
results = return_sum_and_sub(7, 3)  # Tuple
print(r1, r2, sep=', ')
print(results[0], results[1], sep=', ')
# 10, 4
# 10, 4


# Define a function with empty return
# * The return keyword can be used in a function that does't return anything to
#   terminate the function execution
def is_correct(correct):
    if not correct:
        return
    print('It is correct')


# Call a function with empty return
# * When the empty return is reached, it will stop the function execution
is_correct(False)
# (Nothing was printed because the empty return was reached)


# Define a nested function (inner function)
# * The function can be defined inside another function
# * A function inside a function is called "inner function" or "nested
#   function"
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
# * It is considered hard to read and can be simplified by using collections
def recursive(n):
    if n > 0:
        print(n, end=', ')
        recursive(n - 1)  # Call itself
    else:
        print()


# Call a recursive function
# * To call a recursive function you just use the same method to call a common
#   functions
recursive(5)
# 5, 4, 3, 2, 1,


# Define a recursive function with return
# * To define a recursive function with return you must know how the call stack
#   of the programming language works
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
# * The Python has a mechanism called shadowing that makes the parameters be
#   different of the variables, even if the parameter and the variable have the
#   same identifier (name)
# * You don't need to worry about naming parameters since they will not
#   conflict with the function outside data
def shadowing(name):
    return name


# Call function with parameters having the same name of variable
# * The mechanism will consists this to prevent conflicts
name = 'Name: Outside'
result = shadowing('Name: Inside')
print(name, result, sep=', ')
# Name: Outside, Name: Inside


###############################################################################
# Function Reference
###############################################################################


# Get the reference of the function
# * To get the reference you must need to point to the name of the function,
#   without defining the parenthesis ()
# * You can use the reference for some dynamic logic, reflection or to operate
#   with high order functions
my_show_message = show_message
my_show_message()
# Function!


# Require function as function parameter
# * You can pass a function as parameters to other function using the reference
#   of it
def execute_function(fn):
    fn()


# Call the function passing a function as argument
# * To call the example function, you must pass the function reference as
#   argument
execute_function(show_message)
# Function!


# Working with function references
# * You can work with function reference as any datatype
# * You can add the function to collections, store to a variable, etc.
lst = [sum_values]
dct = {'sum': sum_values}
print(lst[0](6, 4))
print(dct['sum'](6, 4))
# 10
# 10
