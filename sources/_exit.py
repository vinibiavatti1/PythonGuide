"""
Exit examples
exit(): Stops the application
quit(): Synonym to exit
sys.exit(arg): Stops the application with status 
"""
import sys

print("Exiting...")
exit() # or quit()
print("This can be printed")

# sys needs to be imported to call the exit function
sys.exit("Some error ocurred!")