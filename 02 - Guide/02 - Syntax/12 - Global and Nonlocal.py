"""
Global and NonLocal

Global
* The "global" instruction is used to indicate that some variable is global in
  a function scope, i.e. the variable is from the root context (outside the
  function)
* When a variable is identified as global in a function, a direct reference to
  this variable will be defined
* If the global variable is defined in a function, the value of the global
  variable can be change inside the function, and the variable will be updated
* It is generally recommended to avoid changing global variables within
  functions, as it can make the code harder to understand and maintain

NonLocal
* The "nonlocal" instruction is used to indicate that some variable is not
  local relative to the current scope, i.e. the variable is from other scope,
  but still not global
* When a variable is identified as nonlocal in a function, a direct reference
  to this variable will be defined
* If the nonlocal variable is defined in a function, the value of the nonlocal
  variable can be change inside the function, and the variable will be updated

Global vs NonLocal
* Global: Give access to a global variable from the root scope
* NonLocal: Give access to a variable outside of current context

globals() and locals()
* The functions "globals()" and "locals()" are used to return the variables of
  the specified context
* The result will be a dictionary containing the resources of the scope
* These functions can be used for code analysis, type checkers and code
  documentation
"""


###############################################################################
# Global
###############################################################################


# Declare a global variable
# * We will define a global variable to be used for a function
x = 5


# Declare a function that changes the global variable
# * The function below access the global variable directly due to the "global"
#   statement
# * If the "global" keyword was not used, the "x" variable inside the function
#   would not be related to the global "x" variable
def change_global_variable():
    global x
    x = 10


# Call the function and check the global variable value
# * After call the function, the "x" variable will be updated since it was
#   referenced directly inside the function
change_global_variable()
print(x)
# 10


###############################################################################
# NonLocal
###############################################################################


# Declare a function that changes the a nonlocal variable
# * For this example, we must use two function to create two different scopes
# * The function has a internal function that access the variable from the
#   parent function, and changes its value
def parent():
    x = 5
    def change_nonlocal_variable():
        nonlocal x
        x = 10
    change_nonlocal_variable()
    return x


# Call a function that changes a nonlocal variable
# * After call the function, the "x" variable will be modified by the internal
#   function since it has a direct access to this variable
result = parent()
print(result)
# 10


###############################################################################
# Global Resources (globals())
###############################################################################


# Get global resources
# * To return the global resources, we can use the "globals()" function
result = globals()
print(result)
# {'__name__': '__main__', '__doc__': '...', '__annotations__': {} ...


###############################################################################
# Locals Resources (locals())
###############################################################################


# Declare a function to define a scope
# * We must create a scope to use the "locals()" function, and check if the
#   function will return only the local resources
# * The variable "text" is considered local because it is encapsulated inside
#   the function
def get_locals():
    text = 'Hello World'
    return locals()


# Get the local resources
# * The result of the function above will be the local resources as a
#   dictionary
# * The "text" variable will be present in the returned dictionary since it is
#   a local variable
result = get_locals()
print(result)
# {'text': 'Hello World'}


###############################################################################
# Global vs Local Resources in Global Context
###############################################################################


# Check the global and local resources in the global context
# * If we check the local resources "locals()" of the global context, it will
#   be the same of the global resources, cause we will be checking the global
#   context
# * The code below compare the values from "globals()" and "locals()" in a
#   global context, and shows that the result is the same
result = locals() == globals()
print(result)
# True
