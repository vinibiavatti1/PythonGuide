"""
Radio Button

* The radio button widget is used to create a set of options from which the
  user can select only one.
* It consists of a circular indicator and a label.
* The state of the radio button can be controlled using a variable.
* In other libraries, it is often referred to as a radio button or option
  button.
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
var = tk.IntVar(value=1)
radio1 = tk.Radiobutton(
    master=root,
    variable=var,
    value=1,
    text='Option 1'
)
radio2 = tk.Radiobutton(
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
widget = tk.Radiobutton()
[print(k) for k in widget.keys()]
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
value
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
"""
