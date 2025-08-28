"""
Check Button (TTK)

* This is the TTK (Themed Tkinter) version of the Checkbutton widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
* The Checkbutton widget is used to create a checkbox that can be toggled on
  or off.
* It allows the user to select one or more options from a set of choices.
* The state of the check button can be controlled using a variable.
* It is commonly used in forms and settings dialogs.
* In other libraries, it may be referred to as a checkbox.
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
root = tk.Tk()
check = ttk.Checkbutton(
    master=root,
    text='Check it!'
)
check.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
check = ttk.Checkbutton()
[print(k) for k in check.keys()]
"""
variable
onvalue
offvalue
command
takefocus
text
textvariable
underline
width
image
compound
padding
state
cursor
style
class
"""


# Methods
# * The common methods for the widget are:
"""
deselect()
flash()
invoke()
select()
toggle()
"""
