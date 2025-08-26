"""
Check Button

* The check button widget is used to create a checkbox that can be toggled on
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


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
check = tk.Checkbutton(
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
check = tk.Checkbutton()
[print(k) for k in check.keys()]
"""
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
command
compound
cursor
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
offrelief
offvalue
onvalue
overrelief
padx
pady
relief
selectcolor
selectimage
state
takefocus
text
textvariable
tristateimage
tristatevalue
underline
variable
width
wraplength
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
