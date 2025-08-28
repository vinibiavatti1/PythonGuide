"""
Option Menu

* The option menu widget is used to create a drop-down menu for selecting
  one option from a list.
* It is similar to the Combobox widget but is more limited in functionality.
* The state of the OptionMenu can be controlled using a variable.
* In other libraries, it is often referred to as a drop-down menu or combo box.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


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
option_menu = tk.OptionMenu(
    root,
    var,
    *options
)
option_menu.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
option_menu = tk.OptionMenu(master=None, variable=None, value=None)
[print(k) for k in option_menu.keys()]
"""
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
cursor
direction
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
indicatoron
justify
menu
padx
pady
relief
compound
state
takefocus
text
textvariable
underline
width
wraplength
"""


# Methods
# * The common methods for the widget are:
"""
get()
"""
