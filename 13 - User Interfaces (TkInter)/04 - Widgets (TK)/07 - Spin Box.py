"""
Spin Box

* The spin box widget is used to select a value from a fixed set of values or a
  range of values.
* It displays the current value and provides buttons to increment or decrement
  the value.
* The state of the spin box can be controlled using a variable.
* Users can also enter values directly into the spin box.
* It is commonly used for numeric input, such as selecting a quantity or a
  range of values.
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
var = tk.StringVar(value='5.0')
spinbox = tk.Spinbox(
    master=root,
    from_=0,
    to=10,
    increment=.1,
    textvariable=var
)
spinbox.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
spinbox = tk.Spinbox()
[print(k) for k in spinbox.keys()]
"""
activebackground
background
bd
bg
borderwidth
buttonbackground
buttoncursor
buttondownrelief
buttonuprelief
command
cursor
disabledbackground
disabledforeground
exportselection
fg
font
foreground
format
from
highlightbackground
highlightcolor
highlightthickness
increment
insertbackground
insertborderwidth
insertofftime
insertontime
insertwidth
invalidcommand
invcmd
justify
relief
readonlybackground
repeatdelay
repeatinterval
selectbackground
selectborderwidth
selectforeground
state
takefocus
textvariable
to
validate
validatecommand
values
vcmd
width
wrap
xscrollcommand
"""


# Methods
# * The common methods for the widget are:
"""
bbox(index)
delete(first, last=None)
get()
icursor(index)
identify(x, y)
index(i)
insert(index, text)
invoke(element)
scan_dragto(x)
scan_mark(x)
selection('from', index)
selection('to', index)
selection('range', start, end)
selection_clear()
selection_get()
"""
