"""
Scale

* The scale widget is used to select a value from a range of values.
* It displays a slider that can be moved to select the desired value.
* The state of the scale widget can be controlled using a variable.
* Users can also enter values directly into the scale.
* It is commonly used for numeric input, such as selecting a volume level or a
  brightness level.
* In other libraries, it may be referred to as a slider or trackbar.
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
var = tk.IntVar(value=5)
scale = tk.Scale(
    master=root,
    variable=var,
    from_=0,
    to=10,
    orient=tk.HORIZONTAL
)
scale.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
scale = tk.Scale()
[print(k) for k in scale.keys()]
"""
activebackground
background
bigincrement
bd
bg
borderwidth
command
cursor
digits
fg
font
foreground
from
highlightbackground
highlightcolor
highlightthickness
label
length
orient
relief
repeatdelay
repeatinterval
resolution
showvalue
sliderlength
sliderrelief
state
takefocus
tickinterval
to
troughcolor
variable
width
"""


# Methods
# * The common methods for the widget are:
"""
coords(value=None)
get()
identify(x, y)
set(value)
"""
