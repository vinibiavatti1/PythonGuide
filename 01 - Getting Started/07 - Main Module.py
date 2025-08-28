"""
Main Module

* Different from other languages, Python doesn't require a main function to
  run.
* Instead, the code at the top level of a module is executed when the module is
  run as a script.
* This means you can write scripts without explicitly defining a main function.
* However, it's still a good practice to define an entry point module for your
  application.
* The `if __name__ == "__main__":` construct is used to determine if a module
  is being run as the main program or if it is being imported into another
  module. This can be used to control the execution of code blocks based on
  the module's context.
"""


###############################################################################
# Main Module
###############################################################################


# Defining the Main Module
# * The main module is the entry point of your application.
# * Usually, the main module is called `main.py`.
# * It will be present in the `app` directory.
"""
###############################################################################
Structure             Description
###############################################################################
project               Project root folder
|- .venv              Virtual environment folder
|- app                Sources folder
   |- main.py         Main module (entry point)
###############################################################################
"""


# Main Construct
# * The difference of this module to others, is that it will contain the
#   main logic of your application, typically under the
#   `if __name__ == "__main__":` construct.
# * The condition above allows you to write code that can be used both as a
#   standalone script and as an importable module.
if __name__ == "__main__":
    print("This is the main module.")


# Running the Main Module
# * Since we have the instruction above on this module, we can run it directly.
# * When executed, it will print "This is the main module."
# * In case this module is imported into another module, the code block under
#   `if __name__ == "__main__":` will not be executed.
# * Run this module and check the output.
""" This is the main module. """
