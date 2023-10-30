"""
Spinbox widget

* The Spinbox widget allows the user to select values from a given set. The
  values may be a range of numbers, or a fixed set of strings
* On the screen, a Spinbox has an area for displaying the current values, and a
  pair of arrowheads
  * The user can click the upward-pointing arrowhead to advance the value to
    the next higher value in sequence. If the value is already at maximum, you
    can set up the widget, if you wish, so that the new value will wrap around
    to the lowest value
  * The user can click the downward-pointing arrowhead to advance the value to
    the next lower value in sequence. This arrow may also be configured to wrap
    around, so that if the current value is the lowest, clicking on the
    down-arrow will display the highest value
  * The user can also enter values directly, treating the widget as if it were
    an Entry. The user can move the focus to the widget, either by clicking on
    it or by using tab or shift-tab, and then edit the displayed value
* Syntax:
  * tk.Spinbox(parent, option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = tk.Spinbox(master=window).keys()
[print(k) for k in keys]
window.destroy()
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


###############################################################################
# Methods
###############################################################################


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


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.StringVar(master=window)
variable.set('5.0')
widget = tk.Spinbox(
    master=window,
    from_=0,
    to=10,
    increment=.1,
    textvariable=variable
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
