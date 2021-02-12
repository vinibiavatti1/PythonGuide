"""
Pass examples

"pass" is a null operation. When it is executed, nothing happens. It is useful 
as a placeholder when a statement is required syntactically, but no code needs 
to be executed.

Empty instructions without pass will raise an error
if 1 == 1: 
    # nothing
print('end if')

IndentationError: expected an indented block
"""
# If
if 1 == 1:
    pass
else:
    pass

# While
while False:
    pass

# For
for i in range(5):
    pass

# Function
def sum(x, y):
    pass

# Class
class Client():
    pass

# try except
try:
    pass
except:
    pass