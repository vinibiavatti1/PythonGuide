"""
Combo Box (TTK)

* The Combobox widget is used to create a drop-down list of options from
  which the user can select one.
* It combines the functionality of an entry field and a drop-down menu.
* The state of the Combobox can be controlled using a variable.
* In other libraries, it is often referred to as a combo box or drop-down
  list.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
# * Note that the Options Menu constructor is different, and accepts positional
#   arguments for the options.
root = tk.Tk()
options = 'Option 1', 'Option 2', 'Option 3'
var = tk.StringVar(value='Option 1')
option_menu = ttk.Combobox(
    root,
    textvariable=var,
    values=options
)
option_menu.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
option_menu = ttk.Combobox()
[print(k) for k in option_menu.keys()]
"""
height
postcommand
values
exportselection
font
invalidcommand
justify
show
state
textvariable
validate
validatecommand
width
xscrollcommand
foreground
background
takefocus
cursor
style
class
"""


# Methods
# * The common methods for the widget are:
"""
get()
"""
