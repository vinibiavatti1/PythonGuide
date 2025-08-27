"""
Radio Button (TTK)

* This is the TTK (Themed Tkinter) version of the Radiobutton widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
* The Radiobutton widget is used to create a set of options from which the
  user can select only one.
* It consists of a circular indicator and a label.
* The state of the Radiobutton can be controlled using a variable.
* In other libraries, it is often referred to as a radio button or option
  button.
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
var = tk.IntVar(value=1)
radio1 = ttk.Radiobutton(
    master=root,
    variable=var,
    value=1,
    text='Option 1'
)
radio2 = ttk.Radiobutton(
    master=root,
    variable=var,
    value=2,
    text='Option 2'
)
radio1.pack(padx=20, pady=20)
radio2.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
widget = ttk.Radiobutton()
[print(k) for k in widget.keys()]
"""
variable
value
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
"""
