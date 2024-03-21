"""
Exit and Quit

* The exit and quit functions are used to stop the application. The sys.exit 
  function is used to stop the application with a status.

###############################################################################
Functions       Description
###############################################################################
exit()          Stops the application
quit()          Stops the application
sys.exit(arg)   Stops the application with status
###############################################################################
"""


###############################################################################
# Exit and Quit
###############################################################################


# Exit
# * Stops the application
exit()


# Quit
# * Stops the application (alias for exit)
quit()


###############################################################################
# System Exit
###############################################################################


# Importing sys module
# * To use the `sys.exit()` function, we must import the module first
import sys


# System Exit
# * The function `exit()` accpets an argument that can be the status of the 
#   application, or an error message. If the argument is 0 (zero), it means 
#   that the application was stopped successfully. If it is different from 
#   zero, it means that the application was stopped with an error.
# * The argument can be also a string with an error message that will be 
#   printed into the terminal. On this way, the status will be set as error by
#   default.
sys.exit()                       # Success
sys.exit(0)                      # Success
sys.exit(1)                      # Error
sys.exit('Some error ocurred!')  # Error
