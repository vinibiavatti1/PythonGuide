"""
Variables examples
"""
# Declare
x = 1 # Integer
y = 'Hello world' # String
avg = 3.5 # Float
lst = [1, 2, 3] # List
tpl = (1, 2, 3) # Tuple

# Multiple variables in same line
x, y, z = 1, 2, 3
print(x, y, z, sep='\n')

# One value for multiple variables
x = y = z = 'Orange'
print(x, y, z, sep='\n')

# Unpack a Collection
lst = [1, 2, 3]
x, y, z = lst
print(x, y, z, sep='\n')

# Concat
x, y = 'Hello ', 'world'
print(x + y)

x, y = 'The ', 7
print(x + str(y)) # It needs to be cast otherwise compiler will raise an error

# Global Variables
x = 1 # Global
def func():
  x = 2 # Not global
  print("Python is " + x) # 2
func()
print("Python is " + x) # 1

# Global keyword
x = 1
def func2():
    global x
    x = 2
    print(x) # 2
func2()
print(x) # 2

