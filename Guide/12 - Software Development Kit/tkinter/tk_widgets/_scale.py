"""
Scale widget

* The purpose of a scale widget is to allow the user to set some int or float
  value within a specified range. Here are two scale widgets, one horizontal
  and one vertical
* Each scale displays a slider that the user can drag along a trough to change
  the value
  * You can drag the slider to a new value with mouse button 1
  * If you click button 1 in the trough, the slider will move one increment in
    that direction per click. Holding down button 1 in the trough will, after a
    delay, start to auto-repeat its function
  * If the scale has keyboard focus, left arrow and up arrow keystrokes will
    move the slider up (for vertical scales) or left (for horizontal scales).
    Right arrow and down arrow keystrokes will move the slider down or to the
    right
* Syntax:
  * tk.Scale(parent, option, ...)
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
keys = tk.Scale(master=window).keys()
[print(k) for k in keys]
window.destroy()
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


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
coords(value=None)
get()
identify(x, y)
set(value)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.DoubleVar()
variable.set(5.)
widget = tk.Scale(
    master=window,
    variable=variable,
    from_=0,
    to=10
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
